import streamlit as st
import pandas as pd
import os
from datetime import datetime, timedelta

# --- Load Data Function ---
BASE_PATH = os.path.join('data', 'cleaned-data')

FILES_TO_LOAD = {
    "issues": "issues_fixed.json",
    "issues_comments": "issues_comments_fixed.json",
    "pulls": "pulls_fixed.json",
    "pr_comments": "pr_comments_fixed.json",
}

@st.cache_data
def load_all_data():
    dataframes = {}
    for key, file_name in FILES_TO_LOAD.items():
        path = os.path.join(BASE_PATH, file_name)
        try:
            dataframes[key] = pd.read_json(path)
        except FileNotFoundError:
            st.error(f"File not found: {path}. Please check your folder structure.")
            return None
        except Exception as e:
            st.error(f"Error loading {file_name}: {e}")
            return None
    return dataframes

# --- Load Data ---
all_data = load_all_data()
if all_data is None:
    st.stop()

issues_df = all_data["issues"]
pulls_df = all_data["pulls"]
pr_comments_df = all_data["pr_comments"]

# --- Normalize datetime columns ---
for df, col in [(issues_df, 'created_at'), (pulls_df, 'created_at'), (pr_comments_df, 'created_at')]:
    df[col] = pd.to_datetime(df[col]).dt.tz_localize(None)

# --- Sidebar: Month & Year Selector ---
st.sidebar.header("Select Month")
available_years = sorted(issues_df['created_at'].dt.year.unique(), reverse=True)
selected_year = st.sidebar.selectbox("Year", available_years)

available_months = list(range(1, 13))
selected_month = st.sidebar.selectbox("Month", available_months, format_func=lambda x: datetime(2000, x, 1).strftime('%B'))

# --- Compute first and last day of selected month ---
first_day = datetime(selected_year, selected_month, 1)
last_day = (first_day + pd.offsets.MonthEnd(1)).to_pydatetime()

month_name = first_day.strftime("%B %Y")
st.title(f"📊 {month_name} – Monthly GTFS Community Report")

# --- Filter data for selected month ---
mask_issues = (issues_df['created_at'] >= first_day) & (issues_df['created_at'] <= last_day)
issues_last_month = issues_df[mask_issues]

mask_pulls = (pulls_df['created_at'] >= first_day) & (pulls_df['created_at'] <= last_day)
pulls_last_month = pulls_df[mask_pulls]

mask_pr_comments = (pr_comments_df['created_at'] >= first_day) & (pr_comments_df['created_at'] <= last_day)
pr_comments_last_month = pr_comments_df[mask_pr_comments]

# --- Narrative Section ---
st.header(f"{month_name} – Highlights")
st.markdown(
    f"This month, the GTFS community discussed and voted on several proposals.\n\nHere’s an overview of key activities from **{month_name}**."
)

# --- Contributor Shoutouts ---
st.subheader("🏅 Contributor Shoutouts")
top_contributors = pr_comments_last_month['user'].apply(
    lambda u: u.get('login') if isinstance(u, dict) else None
).value_counts().head(10)

if not top_contributors.empty:
    st.write("Top contributors this month:")
    st.table(top_contributors.rename_axis("Username").reset_index().rename(columns={'index': 'Username', 'user': 'Contributions'}))
else:
    st.write("No contributions found for this month.")

# --- Voting and Recently Adopted Proposals ---
st.subheader("🗳️ Recently Adopted")
adopted_pulls = pulls_last_month[pulls_last_month['state'] == 'closed']  # assume closed = adopted

if not adopted_pulls.empty:
    # Show only user login, not full dict
    adopted_pulls_display = adopted_pulls.copy()
    adopted_pulls_display['user'] = adopted_pulls_display['user'].apply(lambda u: u.get('login') if isinstance(u, dict) else None)
    st.table(adopted_pulls_display[['number', 'title', 'user', 'closed_at']])
else:
    st.write("No proposals were adopted last month.")

# --- Active Discussions ---
st.subheader("🐙 Most Active Conversations")
if not issues_last_month.empty:
    active_issues = issues_last_month.sort_values(by='comments', ascending=False).head(5)
    # Show only username
    active_issues_display = active_issues.copy()
    active_issues_display['user'] = active_issues_display['user'].apply(lambda u: u.get('login') if isinstance(u, dict) else None)
    st.table(active_issues_display[['number', 'title', 'user', 'comments']])
else:
    st.write("No active issues found last month.")
