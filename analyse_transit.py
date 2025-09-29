import streamlit as st
import pandas as pd
import os

# --- Step 1: Data Loading ---

# Base path to the cleaned data folder
BASE_PATH = os.path.join('data', 'cleaned-data')

# Dictionary of files for easy loading
FILES_TO_LOAD = {
    "issues": "issues_fixed.json",
    "issues_comments": "issues_comments_fixed.json",
    "pulls": "pulls_fixed.json",
    "pr_comments": "pr_comments_fixed.json",
}

@st.cache_data
def load_all_data():
    """Loads all JSON files into pandas DataFrames. Using cache for performance."""
    dataframes = {}
    for key, file_name in FILES_TO_LOAD.items():
        path = os.path.join(BASE_PATH, file_name)
        try:
            dataframes[key] = pd.read_json(path)
        except FileNotFoundError:
            st.error(f"File not found: {path}. Please check your folder structure.")
            return None
        except Exception as e:
            st.error(f"An error occurred while loading {file_name}: {e}")
            return None
    return dataframes

# Load all data
all_data = load_all_data()

# We only proceed if the main data files are loaded
if all_data and "issues" in all_data and "issues_comments" in all_data and "pr_comments" in all_data:
    issues_df = all_data["issues"]
    issues_comments_df = all_data["issues_comments"]
    pr_comments_df = all_data["pr_comments"]

    # --- Step 2: Data Preparation and Cleaning ---

    # Convert date columns
    for col in ['created_at', 'updated_at', 'closed_at']:
        if col in issues_df.columns:
            issues_df[col] = pd.to_datetime(issues_df[col], errors='coerce')

    # Extract username from the user dictionary
    if 'user' in issues_df.columns:
        issues_df['username'] = issues_df['user'].apply(lambda user: user.get('login') if isinstance(user, dict) else None)
    
    # Prepare comments data for search (handle missing text)
    issues_comments_df['body'] = issues_comments_df['body'].fillna('')
    pr_comments_df['body'] = pr_comments_df['body'].fillna('')


    # --- Step 3: Interactive Dashboard Creation ---

    st.title("Google Transit - Contribution Analyzer")

    st.header("Explore Issues and Pull Requests")
    st.info("Use the filters in the sidebar to refine your search.")
    
    # --- Sidebar for Filters ---
    st.sidebar.header("Filters")

    # Filter by user
    if 'username' in issues_df.columns:
        users = sorted(issues_df['username'].dropna().unique())
        selected_users = st.sidebar.multiselect("Filter by user", users)
    else:
        selected_users = []

    # Filter by date range
    min_date = issues_df['created_at'].min().to_pydatetime()
    max_date = issues_df['created_at'].max().to_pydatetime()
    selected_dates = st.sidebar.date_input(
        "Filter by creation date",
        value=(min_date, max_date),
        min_value=min_date,
        max_value=max_date
    )
    
    # Filter by keyword in title or comments
    search_term = st.sidebar.text_input("Search keyword in title or comments")

    # --- Filtering Logic ---
    
    # Start with a copy to avoid modifying the original dataframe
    filtered_issues = issues_df.copy()

    if selected_users:
        filtered_issues = filtered_issues[filtered_issues['username'].isin(selected_users)]

    if len(selected_dates) == 2:
        start_date, end_date = pd.to_datetime(selected_dates[0]), pd.to_datetime(selected_dates[1])
        filtered_issues = filtered_issues[
            (filtered_issues['created_at'].dt.date >= start_date.date()) &
            (filtered_issues['created_at'].dt.date <= end_date.date())
        ]

    if search_term:
        # 1. Find issues with matching titles
        title_mask = filtered_issues['title'].str.contains(search_term, case=False, na=False)

        # 2. Find issue numbers from matching comments
        matching_issue_comments = issues_comments_df[issues_comments_df['body'].str.contains(search_term, case=False)]
        issue_numbers_from_comments = matching_issue_comments['issue_url'].str.split('/').str[-1].astype(int).unique()

        # 3. Find PR numbers from matching comments
        matching_pr_comments = pr_comments_df[pr_comments_df['body'].str.contains(search_term, case=False)]
        pr_numbers_from_comments = matching_pr_comments['pull_request_url'].str.split('/').str[-1].astype(int).unique()
        
        # Combine all numbers from comments
        all_comment_numbers = set(issue_numbers_from_comments) | set(pr_numbers_from_comments)

        # 4. Create a mask for issues that have matching comments
        comment_mask = filtered_issues['number'].isin(all_comment_numbers)

        # An issue is included if its title OR its comments match
        filtered_issues = filtered_issues[title_mask | comment_mask]


# --- Display Results ---

    st.header(f"Results: {len(filtered_issues)} items found")
    st.dataframe(filtered_issues[['number', 'title', 'username', 'state', 'created_at']])

    # --- Show matching comments if a search term is used ---
    if search_term and not filtered_issues.empty:
        st.subheader("Matching Comments")

        # Filtrer les commentaires des issues
        matching_issue_comments = issues_comments_df[
            (issues_comments_df['body'].str.contains(search_term, case=False, na=False)) &
            (issues_comments_df['issue_url'].str.split('/').str[-1].astype(int)
                 .isin(filtered_issues['number']))
        ]

        # Filtrer les commentaires des PR
        matching_pr_comments = pr_comments_df[
            (pr_comments_df['body'].str.contains(search_term, case=False, na=False)) &
            (pr_comments_df['pull_request_url'].str.split('/').str[-1].astype(int)
                 .isin(filtered_issues['number']))
        ]

        # Concaténer
        combined_comments = pd.concat([
            matching_issue_comments[['issue_url', 'user', 'body', 'created_at']],
            matching_pr_comments[['pull_request_url', 'user', 'body', 'created_at']]
        ], ignore_index=True)

        if not combined_comments.empty:
            # Extraire le login utilisateur
            combined_comments['username'] = combined_comments['user'].apply(
                lambda u: u.get('login') if isinstance(u, dict) else None
            )
            st.dataframe(combined_comments[['username', 'body', 'created_at']])
        else:
            st.info("No comments matched the search term in the selected issues/PRs.")

    # --- Visualizations ---
    st.header("Statistics for the current selection")

    if not filtered_issues.empty:
        col1, col2 = st.columns(2)

        with col1:
            st.subheader("Top Contributors")
            # Display top 10 for readability
            st.bar_chart(filtered_issues['username'].value_counts().head(10))

        with col2:
            st.subheader("Status of Issues/PRs")
            st.bar_chart(filtered_issues['state'].value_counts())
    else:
        st.warning("No data to display for the current selection.")