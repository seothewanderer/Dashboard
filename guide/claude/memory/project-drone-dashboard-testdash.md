---
name: project-drone-dashboard-testdash
description: 드론 산업 인력시장 Streamlit 예시 대시보드(testDash)의 결정 사항·구조·주의점
metadata: 
  node_type: memory
  type: project
  originSessionId: 8f9ddce3-f30a-4126-9c1d-bc0b167e42bd
  modified: 2026-09-21T08:15:22.336Z
---

`C:\Projects\Dashboard\testDash` — 보여들이(2)조 기획안 기반 교육·채용 중심 Streamlit 대시보드 (2026-09-21 작성). 기존 Dashboard 폴더의 DataCollect/DataPreprocessing/DataVisualize(고용24 수집·전처리·노트북)와는 별개의 하위 프로젝트.

**사용자 결정:** 채용 데이터는 2차 정제본 135건만 사용 / 종사자 수(17,204)는 제외 / 다크·라이트 전환 지원 / 결측 많은 데이터 제외([[feedback-exclude-high-missing-data]]). 방산 = 주황, 그 외 = 파랑으로 색 고정.

**구조:** app.py → views/(9화면) → analytics/(집계+호버 카드) → components/(chart_card, drone_chart 커스텀 컴포넌트) → core/(loader·quality·theme·state). 화면 폴더는 `pages/`가 아니라 `views/` — `pages/`면 딥링크 시 app.py를 우회한다.

**Why 주의점:** 방산목록 기업(27개사 일치)은 22건·6개사뿐이라 '방산 대 민간' 비교가 아니다. 취업률·수료율은 결측으로 제외됨. Streamlit 파일 감시가 로컬 모듈 변경을 즉시 반영하지 않아 코드 수정 후 서버 재시작이 필요했다.

**정적 공유본:** `python scripts/export_html.py` → `dist/drone_workforce_dashboard.html`(약 6MB 단일 파일, 오프라인). views를 가짜 st로 실행해 기록하는 방식이라 views/analytics를 고치면 재실행 필요. 필터는 기본값 고정, 내 조건 진단은 JS로 재구현(점수식 변경 시 views/matcher.py와 static_export/app.js 양쪽 수정).

**How to apply:** 새 화면/차트는 `chart_card(fig, info=Info(...), table=...)` 패턴과 `analytics/common.py` 빌더를 재사용. 검증은 `python tests/test_smoke.py`(34개 시나리오). 실행은 `.\run.ps1`. 상세는 testDash/README.md.
