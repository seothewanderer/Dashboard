# CLAUDE.md

Behavioral guidelines to reduce common LLM coding mistakes. Merge with project-specific instructions as needed.

**Tradeoff:** These guidelines bias toward caution over speed. For trivial tasks, use judgment.

## 1. Think Before Coding

**Don't assume. Don't hide confusion. Surface tradeoffs.**

Before implementing:
- State your assumptions explicitly. If uncertain, ask.
- If multiple interpretations exist, present them - don't pick silently.
- If a simpler approach exists, say so. Push back when warranted.
- If something is unclear, stop. Name what's confusing. Ask.

## 2. Simplicity First

**Minimum code that solves the problem. Nothing speculative.**

- No features beyond what was asked.
- No abstractions for single-use code.
- No "flexibility" or "configurability" that wasn't requested.
- No error handling for impossible scenarios.
- If you write 200 lines and it could be 50, rewrite it.

Ask yourself: "Would a senior engineer say this is overcomplicated?" If yes, simplify.

## 3. Surgical Changes

**Touch only what you must. Clean up only your own mess.**

When editing existing code:
- Don't "improve" adjacent code, comments, or formatting.
- Don't refactor things that aren't broken.
- Match existing style, even if you'd do it differently.
- If you notice unrelated dead code, mention it - don't delete it.

When your changes create orphans:
- Remove imports/variables/functions that YOUR changes made unused.
- Don't remove pre-existing dead code unless asked.

The test: Every changed line should trace directly to the user's request.

## 4. Goal-Driven Execution

**Define success criteria. Loop until verified.**

Transform tasks into verifiable goals:
- "Add validation" → "Write tests for invalid inputs, then make them pass"
- "Fix the bug" → "Write a test that reproduces it, then make it pass"
- "Refactor X" → "Ensure tests pass before and after"

For multi-step tasks, state a brief plan:
```
1. [Step] → verify: [check]
2. [Step] → verify: [check]
3. [Step] → verify: [check]
```

Strong success criteria let you loop independently. Weak criteria ("make it work") require constant clarification.

---

**These guidelines are working if:** fewer unnecessary changes in diffs, fewer rewrites due to overcomplication, and clarifying questions come before implementation rather than after mistakes.

---

## Project References

| File | Purpose |
|---|---|
| `plan.md` | What to build: features, pages, data, priorities, progress |
| `design/DESIGN.md` | How it looks and behaves: tokens, components, interactions, theming |
| `report/report.md` | Change log: what was changed, why, and which files were affected |

### Workflow
- Before starting any task, read `plan.md` and confirm which item you are working on.
- Before any UI work (layout, charts, cards, styling, interactions), read the relevant sections of `design/DESIGN.md`.
- Follow `design/DESIGN.md` strictly: use defined tokens only; never hardcode colors, fonts, or spacing.
- If a task needs something not defined in these files, ask before implementing. Do not invent new design rules or features.

### Precedence
- For visual and interaction decisions, `design/DESIGN.md` takes precedence.
- For scope and features, `plan.md` takes precedence.
- If the two conflict, stop and ask me.

## Documentation Updates

Keep the reference files in sync with the code. After each approved change, update the matching files:

| Type of change | Update |
|---|---|
| Dashboard features, pages, data, or scope (added, modified, removed) | `plan.md` + `report/report.md` |
| Design system additions or changes (tokens, components, theming, interactions) | `design/DESIGN.md` + `report/report.md` |
| Detailed design settings (per-chart or per-component specs) | `design/DESIGN.md` + `report/report.md` |

- Update `design/DESIGN.md` only for design changes I have approved. Add new rules to the matching section, keep existing rules unless I ask to change them, and mark values not in the original design system as "Proposed (not in source)".
- In `plan.md`, update the status of completed tasks and reflect any scope changes.
- Add one entry to `report/report.md` per change, newest at the top, using this format:

  ### YYYY-MM-DD — <short title>
  - Type: Feature / Fix / Design / Refactor / Removal
  - Summary: what changed and why
  - Files: list of changed files
  - Docs updated: plan.md / design/DESIGN.md (or "none")

## Unused or Obsolete Code

When a change makes existing code unused, redundant, or outdated:
1. Do not delete, comment out, or rewrite it on your own.
2. First report to me:
   - Which code (file and location) is affected and why it is no longer needed
   - Options (e.g., delete, comment out, refactor, keep as is) with pros and cons
   - Your recommended option
3. Wait for my explicit approval before making the change.
4. After approval, apply it and record it in `report/report.md` (Type: Removal or Refactor).

## Work Log

- Keep a running log in `report/worklog.md` for writing a project report later. After each work session or task, append an entry (newest at the top) with: date, what was done, problems encountered and how they were solved, key decisions and reasons, and any open issues. Create the file if it does not exist.