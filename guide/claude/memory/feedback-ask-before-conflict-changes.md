---
name: feedback-ask-before-conflict-changes
description: "Drone dashboard: record every change in report/ files; delete what the user named; ask before any change/deletion forced by a conflict"
metadata:
  node_type: memory
  type: feedback
  originSessionId: 87f6917f-8b99-4854-81f1-7fe4443564b0
  modified: 2026-09-30T07:05:49.906Z
---

For the whole drone career dashboard project (main/):
- Record every implementation in the report folder (revision_requests.md for the request list/decisions, report.md, worklog.md).
- Items the user explicitly says to delete may be deleted directly.
- When a conflict with other features would require changing or deleting something the user did not name, stop and ask first (list what, why, options, recommendation). Never change it silently.

**Why:** User said (2026-09-30) to prevent healthy features from being removed and to keep full traceability; applies for the entire project.
**How to apply:** Before each revision batch, write the request list to report/revision_requests.md; implement named items; collect conflict-driven changes into a question list. Related: [[project-drone-career-main]]
