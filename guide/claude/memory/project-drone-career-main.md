---
name: project-drone-career-main
description: 본 구현 프로젝트 C:\Projects\Dashboard\main(드론 진로 탐색 대시보드)의 문서 체계·사용자 결정·선행 조건
metadata:
  node_type: memory
  type: project
  originSessionId: 87f6917f-8b99-4854-81f1-7fe4443564b0
  modified: 2026-10-02T02:24:21.941Z
---

`C:\Projects\Dashboard\main` — 드론 진로 탐색 Streamlit 대시보드 본 구현 루트. testDash([[project-drone-dashboard-testdash]])와 별개. 기준 문서: `CLAUDE.md`(작업 규칙), `plan.md`(범위, 우선), `design/DESIGN.md`(시각, 우선), `report/report.md`(변경 기록, 최신이 위). plan과 DESIGN이 충돌하면 멈추고 질문.

**사용자 결정 (2026-09-30):** Python은 **3.12 가상환경**(3.14에서 testDash가 잘 돌아도 호환성 우선 — 다시 3.14를 권하지 말 것). Pretendard OTF는 사용자가 `design/`에 직접 넣음(P3 선행). 선택·학습 색(G2)은 Claude 판단 위임 → `--project-select` 청록(#007a70 / #3cc8b4, Proposed), theme.py 1곳만 바꾸면 되게. 결측 규칙은 [[feedback-exclude-high-missing-data]] 그대로.

**Why:** 사용자는 구현 전 리서치·문서 정합을 먼저 요구했고, "시작 범위"로 문서 정리를 먼저 선택했다.

**추가 지시 (2026-09-30):** ① 화면 확정 후 마지막에 데이터 소스를 로컬 DB로 전환(plan 6.1·P9) → 데이터 접근은 `core/data_loader.load_table(name)` 한 곳만. ② 확인받은 결과물은 `main/html/`에 `v<n>_<초안본|수정본|수정본2|최종본>_<날짜>.html`로 누적 저장(plan 9.8). ③ 매 작업 후 `report/worklog.md`에 로그(CLAUDE.md 규칙). ④ 환경·모듈 버전은 `main/ENVIRONMENT.md`에 기록.

**How to apply:** 작업 시작 전 plan.md 해당 단계(P0~P8) 확인. testDash 수치(방산 22건/6개사 등)를 main 문서·화면에 섞지 말 것 — main 수치는 빌드 산출값으로 계산. P0 완료(2026-09-30, Python 3.12.10 설치·.venv·데이터 배치). 항상 `.venv\Scripts\python.exe` 사용. P1(빌드)·P3(셸) 완료, P2 브리지는 사용자 검토 대기. 04 하위 페이지 상태는 위젯 키 `sub` 하나 + `routing.sync_sub()`(bind 옵션은 코드에서 URL 설정 불가라 미사용). 미리보기는 `C:\Projects\Dashboard\.claude\launch.json`(run.ps1 경유), 파이썬 모듈 수정 후엔 서버 재시작 필요.

**P4 (2026-09-30):** 사용자가 '다양한 시각 효과 모듈 사용 + 기존 작업과 일관성'을 요청 → 차트는 ECharts(`streamlit-echarts` 0.7, `components/charts.py`), 드론·카운트업은 내장 `st.components.v2`(`components/effects.py`). 색·치수·움직임은 `core/theme.py`(SERIES·CHART·MOTION)에서만. Plotly는 미사용이지만 삭제는 사용자 확인 대기. Q2·Q13 기본안 확정. 테스트는 v2 컴포넌트 등록 때문에 AppTest마다 모듈 재import 필요.

**디자인 전환 (2026-09-30):** DESIGN.md가 Green Deck(다크 우선, 녹색 #1DB954)으로 교체됨 — 이전 Chapter 문서는 `design/archive/`. 폰트 Pretendard·사용자 방산 규칙은 유지 요청. 라이트 색은 사용자 스크린샷 실측값. 선택=반전 칩(청록 폐기), 방산 주황 #D53B00 유지. 테마 토글은 사이드바 하단 ☀/☾ → Streamlit localStorage `stActiveTheme-<경로>-v2` 변경+새로고침, 선택 상태는 `drone-career-v1`에 저장. 수정 요청은 `report/revision_requests.md`에 먼저 정리하는 방식을 사용자가 요구함. 표는 streamlit-aggrid(1.64에서 그리드 폭 0 → custom_css로 보정).

**git (2026-10-02):** `main` 폴더 = 저장소 루트, 원격 https://github.com/seothewanderer/Dashboard (main, 비공개). 첫 커밋 2eff9fb(README 커밋 위, 강제 push 없음). 포함: data 전체(raw 포함)·design/DESIGN.md+폰트 9개. 제외(.gitignore): .venv·캐시·html/*.html·design/archive. 이 세션에서 push는 권한 확인에서 막혀 사용자가 직접 실행 → 커밋은 내가, push 명령은 사용자에게 안내. 사용자는 채팅을 한국어로 원함. 다음 단계: 팀원 홈 화면 변경을 내 코드에 적용.

**팀 저장소 (2026-10-02):** https://github.com/seothewanderer/dashboard_team (비공개, 공동 작업용). 로컬 C:/Projects/Dashboard/team = 별도 clone. 개인 저장소 이력을 넘기지 않으려고 main의 파일 중 CLAUDE.md·report/(worklog·revision_requests·report)·README.md를 빼고 복사해 커밋(0725735). 앞으로 팀에 반영할 때도 같은 제외 목록으로 main → team 복사 후 커밋, push는 사용자.

**주의 (2026-09-30 버그):** components.v2의 setStateValue는 곧 재실행 → 매 실행 호출하면 무한 루프(화면 전체가 흐려지고 로딩이 끝나지 않음). '한 번만 보내기'는 JS에서 보장하고 파이썬은 컴포넌트 반환값으로 읽을 것. 흐림 증상이 보이면 app.py에 실행 시작/완료 로그를 임시로 찍어 확인. 사용자는 차트 호버 시 다른 요소가 흐려지는 효과를 원하지 않음.
