---
name: feedback-main-vs-team-repo
description: "작업은 항상 main 폴더에서, 개인 Dashboard 저장소는 사용자 전용 — 팀 저장소(dashboard_team)는 team 폴더로만 분리"
metadata:
  node_type: memory
  type: feedback
  originSessionId: 87f6917f-8b99-4854-81f1-7fe4443564b0
  modified: 2026-10-02T06:26:33.330Z
---

모든 작업은 `C:\Projects\Dashboard\main`에서 한다. main의 원격은 개인 저장소 seothewanderer/Dashboard 하나뿐이며, 이 저장소는 **사용자 작업 전용**이다(CLAUDE.md·report/ 등 개인 문서 포함 전체).

팀 공동 작업 저장소 seothewanderer/dashboard_team은 별도 폴더 `C:\Projects\Dashboard\team`(원격 = dashboard_team)으로만 다룬다. main에 팀 원격을 추가하거나, team 폴더에서 개발하거나, 팀원 변경을 main 이력에 섞지 않는다.

**Why:** 사용자가 2026-10-02 명시 — 개인 저장소는 자기 작업만 담고, 팀 공유본은 개인 문서를 뺀 별도 이력이어야 함.

**How to apply:** 팀에 반영할 때만 main → team으로 파일 복사(제외: CLAUDE.md, report/, guide/, 개인 README) 후 team에서 커밋, push는 사용자. 팀원 변경을 내 작업에 가져올 때는 사용자에게 먼저 묻고 main에 수동 반영(파일 단위 비교). 관련: [[project-drone-career-main]], [[project-home-env-git-plan]]
