# HANDOFF — 인수인계 (2026-10-02 기준)

새 세션(집 PC 등)에서 이어 갈 때 먼저 읽는 문서. 자세한 이력은 `report/report.md`(변경 기록, 최신이 위), `report/revision_requests.md`(요청 A~X), `report/worklog.md`(작업 로그).

## 1. 프로젝트

- 드론 진로 탐색 Streamlit 대시보드. 루트 `C:\Projects\Dashboard\main`, Python 3.12 `.venv`, Streamlit 1.64.
- 기준 문서: `plan.md`(범위) · `design/DESIGN.md`(디자인, 새 값은 §12에 "Proposed (not in source)") · `CLAUDE.md`(작업 규칙).
- 화면: 홈 / 01 산업 이해 / 02 직무 탐색 / 03 준비 역량 / 04 채용·기업 탐색(채용 현황·기업 탐색).

## 2. 작업 규칙(사용자 지시, 계속 유지)

- 모든 요청은 `report/revision_requests.md`에 먼저 적고, 끝나면 `report/report.md`·`report/worklog.md`, 필요하면 `plan.md`·`DESIGN.md`를 갱신.
- 충돌·모순·구현이 어렵거나 기능이 사라지는 경우 → 멈추고 질문/보고. 이름이 나오지 않은 것은 마음대로 바꾸거나 지우지 않음.
- 쓰이지 않게 된 코드는 먼저 보고하고 승인 후 삭제.
- 값은 `core/theme.py` 토큰만(하드코딩 금지). 데이터는 `core/data_loader.load_table`로만. 결측 50% 이상 열은 제외. 다운로드는 허락 후.
- 사용자 Streamlit 서버(8501)는 건드리지 않음. 확인은 미리보기 설정 `drone-dashboard-check`(8502), HTML 확인은 `html-share`(8777).
- 커밋은 Claude, push는 사용자. 채팅은 한국어.

## 3. 저장소

| 폴더 | 원격 | 쓰임 |
|---|---|---|
| `C:\Projects\Dashboard\main` | seothewanderer/Dashboard (비공개) | 모든 작업. 개인 전용(CLAUDE.md·report/·guide/ 포함) |
| `C:\Projects\Dashboard\team` | seothewanderer/dashboard_team (비공개) | 팀 공유본만. main → team 복사(제외: CLAUDE.md, report/, guide/, 개인 README) 후 커밋 |

- 팀 저장소 첫 커밋: 0725735 (2026-10-02). 팀원 변경을 내 작업에 가져올 때는 사용자에게 먼저 묻고 파일 단위로 main에 반영.

## 4. 오늘(2026-10-02)까지 한 큰 일

- 홈: 팀원 Home을 반영한 3D 드론(`components/home_hero.py/.js/.css`, Three.js 0.169.0은 `static/vendor/three`). 진입·패널 쪽 출발·복귀 비행, 마우스 시선, 패널 아이콘, 요약 카드 C안(누르면 이동·GIF 아이콘), 로드맵 4단계, FAQ.
- 사이드바 01~04 아이콘(hover 반복), 04 상위 메뉴 이름(이동)·^(펼치기만) 분리.
- 04 기업 탐색: C01 기준 전환(전체 기업 수 / 채용 기업 수 / 채용 공고 수)·함께 하는 분야·흐림 더보기, C04 일반/방산 공고 노출 전환, 근거 집단 그래프 삭제, 정렬은 늘 방산 관련 우선.
- 공통: 방산 막대 모양 통일 + hover에도 빨강, 하나만 고르는 단추 = 둥근 묶음, 카드 넘기기 '이전·현재/전체·다음'(순환), 카드 펼치기 자동 열림 규칙(03과 같음), 화면 문구 '방산 근거' → '방산 관련'.
- 채용 공고 기준일 = 2026년 9월 18일(`content/module_meta.POSTINGS_AS_OF` 하나로).

## 5. 대기 중(사용자 결정 필요)

- 다음 HTML 공유본: 만들 때 그 시점 앱 기능 전부 구현(지금 공유본 v4는 예전 홈·기업 탐색). 그때 함께 지울 것: theme `--hero-*`, TYPE `hero`·`nav-no`, `scripts/interactive`의 예전 홈·C01G 코드.
- 예전부터 남은 확인 항목:
  - `analytics.postings.filter_by_profile`(테스트에서만 쓰임) 삭제 여부
  - echarts.min.js 두 곳(scripts/interactive/vendor, static/vendor) 중복
  - 공유본 JS의 `CH.jobNetwork`와 theme.CHART `net_*` 키(앱·v4 모두 미사용)
  - treemap 코드, `data/content/project_suggestion.csv`, plotly·Pretendard-Light 정리
  - 차트 카드 아래 구분선 통일
- 선택 사항(제안만 함): 04 채용 현황 '방산 관련 기업만 보기'로도 카드 자동 펼침, 04/03 밑줄 탭도 둥근 묶음으로, C04 일반 공고 노출 상위 10 아래 더보기.

## 6. 주의

- `views/recruit/*.py`처럼 페이지가 import하는 모듈을 고치면 서버 재시작이 필요(페이지 파일 자체는 새로고침으로 반영).
- Streamlit 정적 파일은 text/plain으로 와서 JS 모듈(Three.js)은 Blob으로 불러온다(`home_hero.js` loadThree).
- 1.64의 선택 단추 구분 속성은 `data-variant`(segmented_control / pills).
- clone 직후 '원본이 빌드 이후 바뀌었습니다' → `scripts/build_data.py` 한 번(setup.ps1이 실행).
