# GTFS Realtime Best Practices

These are recommended practices for describing real-time public transportation services in the [GTFS Realtime Reference](../spec/en/reference.md) format. These complement the explicit recommendations outlined in the GTFS Realtime Reference using the terms “recommend” or “should”. Although not mandatory, following these best practices can significantly improve the quality of the data and the overall experience for riders.
These practices have been synthesized from the experience of the [GTFS Best Practices working group members](https://gtfs.org/schedule/best-practices/#gtfs-best-practices-working-group) and application-specific GTFS practice recommendations. See the [FAQ](https://gtfs.org/schedule/best-practices/#frequently-asked-questions-faq) for more information.

---
⚠️ **NOTE: The GTFS Realtime Best Practices are in the process of being merged into the [GTFS Realtime Reference](../spec/en/reference.md) (see [issue #396](https://github.com/google/transit/issues/396) and [issue #451](https://github.com/google/transit/issues/451) for more information).**
**New Best Practices will be added directly to the GTFS Realtime Reference. If you'd like to suggest a new Best practice, you can:**
- **look at the existing [list of outstanding issues and PRs](https://github.com/google/transit/issues/421). If your new Best Practice idea is referenced on this list, comment on the issue**
- **[open a new issue](https://github.com/google/transit/issues/new/choose)**
- **open a Pull Request following the [GTFS Realtime Amendment Process](https://gtfs.org/realtime/process/).**
---

## Documentation Structure

The GTFS Realtime Best Practices are written in Markdown and are organized by Message and by use case.

* `field_name`: The name of the GTFS Realtime field being described
* `recommendations`: An array of the recommendations provided for each field_name
