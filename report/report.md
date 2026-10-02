# report.md — 변경 기록

### 2026-10-02 — 24차: v5 공유 HTML + 렌더링 맞춤
- Type: Feature / Design
- Summary: 요청 Z.
  - html/v5_수정본_2026-10-02.html(16.6MB): v4 이후 앱 기능 전부.
    - 3D 홈: Three.js 4개 파일을 HTML에 넣고 Blob 모듈로 불러옴 → 인터넷 없이 동작. 실패하면 정지 그림.
    - 사이드바 01~04 아이콘·04 이름/접기 분리, 기업 탐색(기준 전환·함께 하는 분야·C04A·넘기기·정렬 한 줄), 카드 자동 펼침, 채용 현황 경력·학력 펼치기, 기준일 9월 18일.
    - 쓰지 않게 된 예전 홈 토큰 삭제(`--hero-*`, TYPE `hero`·`nav-no`), 공유본의 예전 홈·기업 더보기 팝업 코드 삭제(사용자 승인).
  - 렌더링 맞춤:
    - 글꼴 400~800 다섯 굵기 내장, font-display:block, 글꼴을 다 불러온 뒤 첫 그리기(최대 2.5초).
    - 단추·칩·탭·라벨 줄바꿈 금지.
    - 좁은 칸(container query): 요약 타일 ≤820px 아이콘·여백·숫자·라벨 축소, ≤600px 아이콘을 위로. 홈 요약 카드 ≤760px 화살표 숨김, ≤640px 2열. 그래프 카드 ≤360px 단추 묶음 여백 축소(공유본).
  - 확인(8777, 1100·1280·1440px, 다크·라이트): 6화면 넘침 없음(1280px 기업 탐색 기준 단추만 약간 옆 스크롤, 사용자 지시로 건너뜀), 콘솔 오류 없음. 테스트 81개 통과.
  - 확인 못 한 것: 파일 더블클릭(file://)에서 3D 동작(미리보기 창이 file:// 이동을 막음).
- Files: components/effects.py, components/home_hero.css, components/home_hero.js, core/theme.py, scripts/build_interactive.py, scripts/interactive/(app.css, charts.js, logic.js, main.js, pages.js, template.html, ui.js), html/v5_수정본_2026-10-02.html
- Docs updated: design/DESIGN.md(§12.11 Z), html/README.md

### 2026-10-02 — 23차 수정: 홈 상단바 없앰·간격, 채용 현황 경력·학력 펼치기
- Type: Design
- Summary: 요청 Y.
  - 홈에서만 상단바(서비스명·화면 이름·탐색 경로 접기)를 그리지 않음. 홈에서는 탐색 경로 접기 단추가 없어짐을 보고함.
  - 홈 간격 104·136 → 48px, FAQ 제목 아래 24 → 8px.
  - 채용 현황 경력·학력 그래프를 '경력·학력 조건 보기' 펼치기(기본 닫힘)로 옮기고, 얇은 막대(굵기 2/3, 줄 높이 30px)로 바꿈.
  - 확인(8502, 1440×900): 홈 상단바 없음·간격, 펼치기 열림 시 두 그래프.
  - 테스트 81개 통과(탐색 경로 접기 테스트는 02 화면에서 확인하게 바꿈).
- Files: app.py, core/theme.py, components/charts.py, views/recruit/postings.py, static/css/base.css, tests/test_app_smoke.py
- Docs updated: design/DESIGN.md(§12.11)

### 2026-10-02 — 집(새 PC) 환경용 guide 폴더
- Type: Feature (개발 환경)
- Summary:
  - guide/ 폴더 추가(개인 저장소 전용, 팀 저장소 제외 목록에 추가).
    - README: 순서 안내.
    - setup.ps1: Python 3.12 확인 → .venv → requirements-lock 설치 → build_data → pytest. -CopyClaude로 메모리·launch.json 복사, 이미 있으면 건너뜀. BOM 저장, 문법 검사 통과.
    - HANDOFF.md: 결정·대기 중 질문·다음 할 일.
    - claude/memory·claude/launch.json 복사본.
  - .venv·대화 기록 원본은 올리지 않음.
- Files: guide/README.md, guide/setup.ps1, guide/HANDOFF.md, guide/claude/(memory 8개, launch.json)
- Docs updated: none

### 2026-10-02 — 22차 수정: 기업 정렬 한 줄·전체에도 방산 우선, 카드 자동 펼침 일관화
- Type: Feature / Design
- Summary: 요청 X.
  - 기업 카드: '방산 관련만 보기' + 정렬 한 줄(정렬 글자 숨김). 자동 정렬은 분야·키워드를 고르지 않은 전체에도 방산 관련 우선(이전 '미선택이면 이름순' 규칙을 사용자 지시로 변경, 테스트도 바꿈).
  - 카드 펼치기를 03 규칙(기본 닫힘, 그래프·연결 칩·검색으로 고르면 펼침, 해제해도 닫지 않음)으로 02·04 채용 현황·04 기업 탐색에 통일. 기업 카드는 예전 '조건이 좁혀지면 펼침'(키 없음)에서 같은 규칙의 열림 상태 키로 바꿈.
  - 확인(8502, 1440×900):
    - 기업 카드 기본 닫힘, 한 줄 정렬, 전체 264개에서 니어스랩·유비파이(방산 관련) 먼저.
    - 공간정보 칩 → 기업 카드 펼침, 대졸 칩 → 공고 카드 펼침, 02 대분류 → 직무 카드 펼침.
  - 테스트 81개 통과.
- Files: analytics/companies.py, views/recruit/companies.py, views/recruit/postings.py, views/p02_jobs.py, tests/test_analytics.py
- Docs updated: plan.md(9.6), design/DESIGN.md(§12.11)

### 2026-10-02 — '기업 더보기' 팝업 코드 삭제
- Type: Removal
- Summary: 사용자 승인으로 삭제. 21차 수정에서 카드 넘기기로 바뀌어 쓰이지 않게 된 components/dialogs.py의 _company_list, RENDER 'company_list', '목록으로' 분기, paginate import. 기업 탐색에서 쓰던 '_company_ranked'·more_page는 이미 쓰이지 않음. 테스트 통과.
- Files: components/dialogs.py
- Docs updated: none

### 2026-10-02 — 21차 수정: 선택 단추 둥근 묶음 통일, 카드 넘기기(현재/전체·순환)
- Type: Design / Feature
- Summary: 요청 W.
  - 모든 화면의 하나만 고르는 단추 묶음(segmented_control)을 C01 기준 단추처럼 둥근 한 덩어리 + 고른 것만 반전으로 통일(밑줄 탭 모양 제외).
  - 공통 넘기기를 '이전 10개 · 현재/전체 · 다음 10개'로 바꾸고 순환 이동(1/27에서 이전 → 27/27).
  - 기업 탐색 '기업 더보기' 팝업을 같은 넘기기로 바꿈.
  - 확인(8502, 1440×900): 정렬 단추 모양, 1/27 → 27/27 → 1/27.
  - 테스트 81개 통과.
- Files: components/filters.py, views/recruit/companies.py, static/css/base.css
- Docs updated: plan.md(9.6), design/DESIGN.md(§12.11)

### 2026-10-02 — 20차 수정: '방산 관련' 문구, C01 기준 단추 묶음, 채용 공고 기준일
- Type: Design / Content
- Summary: 요청 V.
  - 화면의 '방산 근거'를 '방산 관련'으로 바꿈(01 I02, 04 C01·함께 하는 분야·토글 도움말·정렬, 그래프 설명, 집단 이름 '방산 관련 미확인').
  - C01 기준 단추 3개를 한 덩어리 둥근 틀에 넣고, 고른 것만 반전. 이름은 전체 기업 수 / 채용 기업 수 / 채용 공고 수(사용자 결정: '채용 중인' 대신 '채용').
  - 채용 공고 기준일을 2026년 9월 18일로 통일(사용자가 수집 일자를 확인해 정정, 이전 기록의 9월 14일을 바로잡음).
    - content/module_meta.POSTINGS_AS_OF 하나를 04 KPI·홈 요약 카드·홈 안내·FAQ가 함께 씀.
    - FAQ '채용 공고와 교육은 언제 기준인가요?': 9월 18일 기준 채용 중이던 공고, 채용 기업 = 그 공고를 낸 곳, 이후 변동은 원문 확인.
  - 확인(8502, 1440×900, 라이트): 단추 묶음·반전, 채용 기업 수 전환, 04 KPI '2026년 9월 18일 수집 기준', 홈 FAQ 새 질문.
  - 테스트 81개 통과.
- Files: analytics/companies.py, analytics/defense.py, views/recruit/companies.py, views/recruit/postings.py, views/p01_industry.py, views/home.py, content/module_meta.py, content/usage_guide.py, static/css/base.css
- Docs updated: design/DESIGN.md(§12.11)

### 2026-10-02 — 19차 수정: 기업 탐색 분야 그래프 기준 바꾸기 + 함께 하는 분야
- Type: Feature
- Summary: 요청 U(구상안 A·B).
  - C01 위 단추로 기준 전환(기업 수 / 공고 있는 기업 수 / 연결 공고 수). 막대 순서·더보기·방산 빨강이 기준을 따름.
  - 분야를 고르면 카드 안 아래에 '그 분야 기업들이 함께 하는 분야' 겹친 막대(상위 8). 막대를 누르면 그 분야로 바꿔 봄.
  - B는 처음 제안처럼 같은 막대에 겹치면 세 겹이 되어 읽기 어려워 아래에 따로 둠.
  - 새 계산: analytics/companies.area_basis_counts·area_cooccurrence. '기업 수' 기준은 기존 값과 같음(테스트).
  - 확인(8502, 1440×900):
    - 공고 있는 기업 수 → 감시·정찰·수색 14.
    - 방역/방제/살포 선택 → 함께 하는 분야(감시·정찰·수색 65 등).
    - 공간정보 막대 클릭 → 선택 전환.
  - 테스트 81개 통과(2개 추가).
- Files: analytics/companies.py, views/recruit/companies.py, content/module_meta.py(C01P·C01N), static/css/base.css, tests/test_analytics.py
- Docs updated: plan.md(9.6), design/DESIGN.md(§12.11)

### 2026-10-02 — 18차 수정: 기업 탐색 분야 막대·빨간 막대 통일·사이드바 펼치기 단추
- Type: Design / Feature
- Summary: 요청 T.
  - 04 C01에 방산 빨간 겹친 막대(01과 같음).
  - 01·04 숨은 분야 선택 시 '분야 더보기' 자동 펼침.
  - 모든 방산 막대 모양 통일(근거 단계 구분 없이 빨강+빗금)과 hover 시 빨강 유지(빨간 글로우).
  - 사이드바 04: 이름 = 채용 현황 이동, ^ = 하위 메뉴 펼치기·접기만.
  - 확인(8502, 1440×900):
    - 기업 탐색 C01 빨간 막대, 공고 노출 빨강 통일.
    - ^ 두 번 = 접힘·펼침(주소 그대로), 이름 = /recruit?sub=postings.
    - 01 환경측량 칩 → 자동 펼침.
  - hover 빨강 유지는 차트 설정으로 반영했고, 화면 캡처 확인은 미리보기 창이 그려지지 않아 못 함.
  - 테스트 79개 통과.
- Files: components/charts.py, views/recruit/companies.py, views/p01_industry.py, components/shell.py, static/css/base.css
- Docs updated: design/DESIGN.md(§12.11)

### 2026-10-02 — 방산 근거 집단 관련 코드 삭제
- Type: Removal
- Summary: 사용자 승인으로 삭제. 17차 수정에서 근거 집단 그래프·칩을 지우면서 쓰이지 않게 된 코드.
  - analytics/companies.py: group_counts, CompanyFilters.defense_group과 그 필터 분기.
  - content/module_meta.py: C01G.
  - 테스트 test_area_counts_apply_other_filters는 근거 집단 필터 대신 '수집 공고 연결됨' 필터로 같은 규칙(분야 자기 필터만 제외)을 확인하게 바꿈.
  - 테스트 79개 통과.
  - HTML 공유본(scripts/interactive/pages.js)의 예전 기업 탐색은 아직 C01G를 쓴다. 다음 공유본에서 앱과 맞출 때 정리한다.
- Files: analytics/companies.py, content/module_meta.py, views/recruit/companies.py, tests/test_analytics.py
- Docs updated: none

### 2026-10-02 — 17차 수정: 홈 직무 아이콘 + 04 기업 탐색 그래프 정리
- Type: Design / Feature / Removal
- Summary: 요청 S.
  - 홈 요약 카드 직무 아이콘: 24px 원본을 원·곡선으로 다시 그림(움직임은 원본에서 읽음, 굵기는 다른 KPI 아이콘과 같게).
  - 04 기업 탐색:
    - C01 '분야 더보기'를 01과 같은 흐림 미리보기 + 단추로 바꿈. 더보기 단추 테두리는 01·04 모두 없앰.
    - '방산 근거 집단' 그래프와 근거 집단 칩 필터 삭제(사용자 지시). C01 옆(5:5)에 채용 공고 노출을 둠.
    - 채용 공고 노출: '방산 강조' 꺼짐 = 기업 전체 상위 10(방산 빨강), 켜짐 = 방산 관련 기업만.
  - 확인(8502, 1440×900, 라이트):
    - 기업 탐색 = 흐린 더보기, 테두리 없음, 23곳 중 10곳(방산 빨강).
    - 방산 강조 켜면 '방산 관련 기업의 채용 공고 노출'(42곳 중 10곳). 01 더보기 테두리 없음.
    - 홈 직무 아이콘 선 깔끔.
  - 테스트 79개 통과.
- Files: scripts/make_kpi_icons.py, static/img/kpi_job_*.webp, views/recruit/companies.py, content/module_meta.py(C04A 추가), static/css/base.css
- Docs updated: plan.md(9.6), design/DESIGN.md(§12.11)

### 2026-10-02 — 16차 수정: 홈 요약 카드(누르면 이동 + 아이콘)
- Type: Feature / Design
- Summary: 요청 R, 사용자 선택 C안.
  - 요약 카드 4칸이 단추가 됨: 왼쪽 아이콘, 오른쪽 화살표. 직무 → 02, 학습 → 03, 공고 → 04 채용 현황, 기업 → 04 기업 탐색.
  - hover는 드론 메뉴 패널과 같은 초록 배경 + 왼쪽 막대, 아이콘 GIF 반복.
  - 아이콘: 손바닥 사람·디플로마(새 GIF), 종이 두 장·건물(기존 KPI 아이콘). make_kpi_icons.py에 job·learning 추가, 기존 아이콘은 바이트 그대로.
  - '탐색 조직' → '관련 기업 · 264개 기업'.
  - 확인(8502, 1440×900): 카드 hover(초록 배경·움직이는 아이콘), 직무 → /jobs, 관련 기업 → /recruit?sub=companies.
  - 테스트 79개 통과.
- Files: components/home_hero.js·.css·.py, views/home.py, core/theme.py, scripts/make_kpi_icons.py, static/img/kpi_job*·kpi_learning*(새)
- Docs updated: design/DESIGN.md(§12.11)

### 2026-10-02 — 예전 홈 드론 부품 삭제
- Type: Removal
- Summary: 사용자 승인으로 삭제.
  - components/effects.py의 drone_hero(_DRONE_SVG·_HERO_CSS·_HERO_JS·부품 등록)를 지움. 14차 수정에서 home_hero로 바뀌어 쓰이지 않게 됨.
  - 예전 드론 크기 값(theme --hero-* 7개)과 글자 크기 hero·nav-no는 HTML 공유본 빌드(scripts/interactive/app.css)의 예전 홈·사이드바가 아직 쓴다. 그래서 다음 공유본에서 홈을 옮길 때 함께 지운다(사용자 조건: 다음 공유본은 그때 기능 전부 구현).
- Files: components/effects.py
- Docs updated: plan.md(폴더 구조), design/DESIGN.md(§10 Home drone 행)

### 2026-10-02 — 15차 수정: 사이드바 아이콘 반복, 드론 패널 아이콘, 드론 시선
- Type: Design / Feature
- Summary: 요청 Q.
  - 사이드바 01~04 아이콘이 마우스를 올린 동안 계속 반복(01 KPI 카드처럼, 홈 아이콘은 그대로).
  - 드론 메뉴 패널 5개:
    - 'P1~P5' 글자를 삭제하고 정적 아이콘을 붙임(물음표·돋보기·책·사람·01 KPI 건물).
    - 글자 14→16px·12→13px, 위아래 여백 8→12px, 폭 200→216px.
  - 드론 시선: 메뉴를 펼치기 전후 모두 무대 위 마우스 쪽을 패널 hover와 같은 정도로 바라봄.
  - 확인(8502, 1440×900, 라이트): 마우스 왼쪽 위·오른쪽 아래 → 드론 방향 바뀜, 패널 아이콘 5개 표시.
  - 테스트 79개 통과.
- Files: scripts/make_nav_icons.py, static/img/nav_*_hover.webp, components/home_hero.js·.css·.py, views/home.py, core/theme.py
- Docs updated: design/DESIGN.md(§12.11)

### 2026-10-02 — 14차 수정: 홈 화면(팀원 Home 반영) + 사이드바 아이콘
- Type: Feature / Design / Removal
- Summary: 요청 P(팀원 home-only.html 기준).
  - 홈 = 제목 → 요약 카드 4개 → 3D 드론 무대 → 로드맵 이용 안내 → 자주 묻는 질문.
  - 새 부품 home_hero:
    - 공역 배경, Three.js 3D 드론, 5개 패널.
    - 드론이 커지고 작아지는 동작, 날아오는 진입, 패널 바라보기.
    - 패널 방향으로 날아간 뒤 그 화면으로 이동(팀원 판에 없던 부분). 홈에 돌아오면 그 방향에서 복귀.
  - 사용자 결정에 따른 처리:
    - Three.js 0.169.0은 내려받아 static/vendor/three에 둠.
    - 제목·설명 문구는 유지.
    - 대체 메뉴 펼치기, 산업 KPI 묶음, '○○ 보기' 단추 5개, 매출 캡션은 삭제.
    - FAQ는 현재 기능 기준으로 다시 씀.
  - 사이드바 01~04 번호는 물음표·돋보기·책·사람 아이콘으로 바꿈(마우스를 올리면 GIF 움직임 재생, 선 굵기는 홈 아이콘 기준). 사람 아이콘은 선을 다시 그림.
  - 팀원 값(크기·색)은 theme.py --hm-* 토큰으로 옮김.
  - 확인(8502, 1440×900, 다크·라이트):
    - 첫 진입 비행, 메뉴 열기·닫기(Esc 포함), 패널 바라보기.
    - P2 → 02 이동, 홈 복귀 시 오른쪽에서 돌아옴. P4 → 04 채용 현황(?sub=postings).
    - 움직임 멈춤, 아이콘 hover 애니메이션.
  - 테스트 79개 통과(홈 대체 단추 테스트 → 진입·복귀 비행 순서 테스트로 교체).
- Files: components/home_hero.py·.js·.css(새), views/home.py, content/usage_guide.py, components/shell.py, core/theme.py, static/css/base.css, static/vendor/three/(새, LICENSE 포함), static/img/nav_*(새), scripts/make_nav_icons.py(새), tests/test_app_smoke.py
- Docs updated: plan.md, design/DESIGN.md(§12.11)

### 2026-10-02 — 첫 git 커밋(중간 저장)
- Type: Chore
- Summary: main 폴더를 저장소 루트로 https://github.com/seothewanderer/Dashboard (main, 비공개)에 첫 커밋.
  - 원격의 첫 커밋(README.md)을 그대로 이어받아 그 위에 커밋함(강제 덮어쓰기 없음).
  - 포함: 코드·테스트·문서, data 전체(raw 포함, 다른 PC에서 다시 빌드 가능), design/DESIGN.md와 폰트 9개, static.
  - 제외(.gitignore): .venv, 캐시, html/*.html 공유본(build_interactive.py로 다시 만듦, html/README.md만 올림), design/archive.
- Files: .gitignore(새)
- Docs updated: none

### 2026-10-02 — 네 번째 HTML 공유본(v4 수정본): 10~13차 수정 반영
- Type: Feature
- Summary: 팀원 홈 화면 변경 테스트용 공유본.
  - html/v4_수정본_2026-10-02.html(10.7MB): L·M·N·O 라운드를 JS로 옮김.
  - 02 3D 네트워크와 04 지도+막대는 앱 부품(job_graph3d·linked_chart_map)의 JS·CSS를 빌드 때 그대로 넣어 같은 동작. 3D 배치 계산은 analytics/job_layout.py로 분리해 앱·공유본이 함께 씀(앱 동작 변화 없음).
  - 확인: 화면 6개 오류 없음. 02 대분류·방산·전체·보러가기·별 선택, 04 대졸 45건·비율 36/99·방산만 36건·스크랩하러 가기, 기업 카드 10개, 03 공고 기술 그래프 채용 탭에서만.
  - 테스트 79개 통과.
- Files: scripts/build_interactive.py, scripts/interactive/(core·charts·ui·pages·main.js, app.css, template.html), analytics/job_layout.py(새), components/job_graph3d.py, html/v4_수정본_2026-10-02.html(새), html/README.md
- Docs updated: none

### 2026-10-02 — 13차 수정: 카드 테두리, 검색 상자 통일, 02 근거 유형 삭제
- Type: Design / Feature / Removal
- Summary: 요청 O.
  - 카드 기본 테두리를 보이게 함.
  - 검색 상자 공통 부품으로 02·04 자유 입력 검색을 바꿈(입력 추천 + 전체 목록 + 직접 입력).
  - 02 근거 유형 필터 삭제(사용자 지시).
  - 02 검색 시 직무 카드 펼치기 열림.
  - 확인: 02 '자율' → 2개 직무·카드 열림, 04 '방제' → 88개 기업, 오류 없음.
  - analytics.jobs.filter_jobs의 evidence 인자는 화면에서 쓰지 않게 됨(HTML 공유본 JS는 그대로).
  - 테스트 79개 통과.
- Files: components/search_box.py(새), views/p02_jobs.py, views/recruit/companies.py, content/module_meta.py, static/css/base.css
- Docs updated: design/DESIGN.md(§12.10)

### 2026-10-02 — '내 조건'을 나의 탐색 경로로, 목표 직무 강조 토글을 카드 펼치기 안으로
- Type: Feature / Design
- Summary: 요청 N14·N15.
  - '나의 탐색 경로' 패널 맨 아래 '내 조건'(학력·경력·희망 지역, 저장됨). 공고 상세 '내 조건과 비교' 표와 03 교육 정렬이 다시 사용자 입력을 받음.
  - 04 채용 현황의 '목표 직무 관련 강조' 토글을 공고 카드 펼치기 안으로.
  - 남은 확인: analytics.postings.filter_by_profile은 여전히 화면에서 쓰지 않음(테스트만), 기업 탐색 화면의 목표 강조 토글 위치는 그대로.
  - 테스트 79개 통과.
- Files: components/shell.py, views/recruit/postings.py, static/css/base.css
- Docs updated: design/DESIGN.md(§12.9)

### 2026-10-02 — 04 비율 보기 0% 위치 수정
- Type: Fix
- Summary: 요청 N13. charts.thin_diverging_hbar를 누적에서 겹침(barGap -100%)으로 바꿔 0% 라벨이 가운데 오른쪽에 붙게 함. 화면 확인(GIS/측량·기타·PM/기획의 0%).
- Files: components/charts.py
- Docs updated: none

### 2026-10-02 — 04 거르기 단추와 그래프 필터 통일
- Type: Feature
- Summary: 요청 N12(사용자 결정: 그래프 필터로 통일).
  - 위 '공고 조건으로 거르기'의 학력·경력 칩(여러 개, 공고 값 전부)과 지역 드롭다운이 경력·학력 막대, 지도와 같은 상태를 공유. 그래프 아래 칩은 삭제.
  - 확인: 위 '대졸' → 45건·막대 강조, 막대 클릭 → 해제·135건.
  - 끊긴 연결(확인 요청)
    - 학력·경력·희망 지역을 입력하는 곳이 없어짐 → 공고 상세 팝업 '내 조건과 비교'는 예전에 저장된 값만 쓰거나 '입력 없음'.
    - 03 교육 정렬의 희망 지역 우선도 새 입력이 없음.
    - analytics.postings.filter_by_profile은 화면에서 쓰지 않게 됨(테스트만 사용).
  - 테스트 79개 통과.
- Files: views/recruit/postings.py
- Docs updated: design/DESIGN.md(§12.9)

### 2026-10-02 — 04 희망 지역 드롭다운, 빨간 막대 끝 둥글게
- Type: Design
- Summary: 요청 N11.
  - 희망 지역: 펼치기 대신 드롭다운 선택 상자(레이아웃 유지).
  - thin_split_hbar: 이어 붙이던 누적 대신 겹친 막대(barGap -100%)로 바꿔 빨강 끝도 둥글게. 툴팁은 방산·그 외·합계 그대로.
  - 테스트 79개 통과.
- Files: components/charts.py, views/recruit/postings.py, static/css/base.css
- Docs updated: design/DESIGN.md(§12.9)

### 2026-10-02 — 04 직무·지역 그래프를 03과 같은 모양으로, 내 조건 한 줄
- Type: Design
- Summary: 요청 N10.
  - 막대: 03 키워드 막대와 같은 얇은 막대(charts.thin_split_hbar·thin_diverging_hbar 새로 추가). 연동 부품 크기 계산도 03과 같게.
  - 카드 안 직무·지역 칩은 빼고 안내 한 줄(03과 같게).
  - 내 조건: 이름을 단추 왼쪽에 둔 한 줄 구성.
  - 쓰지 않게 된 코드는 없음(stacked_hbar·diverging_hbar는 다른 곳에서 계속 사용).
  - 테스트 79개 통과.
- Files: components/charts.py, components/linked_chart_map.py, views/recruit/postings.py, static/css/base.css
- Docs updated: design/DESIGN.md(§12.9)

### 2026-10-02 — 12차 수정 후속(04 채용 현황): 직무·지역 연동 그래프, 비율 토글, 방산만 보기, 안내 상자
- Type: Feature / Design / Fix
- Summary: 요청 N5~N9.
  - 직무 막대(왼쪽) + 지역 지도(오른쪽) 연동 카드로 합침(03과 같은 방식, 새 부품 linked_chart_map). 지역 공고 수 = 지도, 직무별 방산/그 외 = 막대.
  - '비율(%)로 보기' 토글.
  - 이 화면 전용 '방산 관련 기업만 보기'(아래 전체 필터): 02·기업 탐색의 방산 강조는 그대로. 공고 카드 안 중복 토글 삭제.
  - 비교 안내: 파란 상자 안에 같은 폭(200px) 파란 테두리 단추.
  - 방패 GIF 교체.
  - 수정한 오류: 방산만 보기를 켜면 '내 조건과 차이 99건을 뺐습니다'로 잘못 표시되던 것(방산 필터를 안내 뒤로 옮김).
  - 테스트 79개 통과.
- Files: views/recruit/postings.py, components/linked_chart_map.py(새), core/theme.py, static/css/base.css, static/img/kpi_shield*, scripts/make_kpi_icons.py
- Docs updated: plan.md(v0.22 비고), design/DESIGN.md(§12.9)

### 2026-10-02 — 12차 수정(04 채용 현황): KPI 아이콘 카드, 내 조건 정리, 직무 그래프 합침, 비교 안내
- Type: Feature / Design
- Summary: 요청 N(revision_requests.md N).
  - KPI 카드(01과 같은 형식)
    - 수집 공고 135건(종이, 2026년 9월 14일 수집 기준).
    - 공고의 기업 수 76개(건물).
    - 방산 관련 기업 비율 13.2%(방패·빨강, 76곳 중 10곳 · 공고 36건).
  - 내 조건: 희망 지역 펼치기, 방산 강조 토글을 영역 안 오른쪽으로.
  - 직무 그래프: 방산/그 외 2구분 + '공고 수/비율' 토글(H07 합침).
  - 비교: 목표 직무·스크랩이 없으면 안내 + 이동 단추.
  - 함께 바꾼 것
    - 공고 카드 펼치기 제목·키 고정(02와 같은 이유: 다시 만들어지며 화면이 튀지 않게, 단추로 열 수 있게). 조건을 좁혀도 자동으로 펼쳐지지 않음.
    - 스크롤 부품 위치 확인을 4초까지 늘림.
  - 테스트 79개 통과.
- Files: views/recruit/postings.py, components/effects.py, components/scroll.py, scripts/make_kpi_icons.py, static/img/kpi_posting*·kpi_shield*(새)
- Docs updated: plan.md(9.5.3), design/DESIGN.md(§12.9)

### 2026-10-01 — 02 단추를 누를 때 화면이 위로 튀는 문제 수정
- Type: Fix
- Summary: 요청 M12.
  - 원인 1: 카드 펼치기가 제목(건수)·열림 조건이 바뀔 때마다 새로 만들어지며 잠깐 접혀 페이지 높이가 줄었음.
  - 원인 2: '방산 강조 중' 안내 줄이 그래프 위에서 생겼다 사라짐.
  - 수정
    - 펼치기 제목('직무 카드 보기')과 키를 고정. 건수는 안쪽 쪽 표시에 둠. 여닫기는 사용자와 '보러가기' 단추만.
    - 02의 안내 줄 제거(상태는 빨강 단추가 표시).
  - 확인: 1440×900, 카드 펼친 상태에서 단추 8번 → 위치 변화 0px. 오류 없음.
  - 동작 변경: 조건을 좁혀도 카드 펼치기가 자동으로 열리지 않음.
  - 테스트 79개 통과.
- Files: views/p02_jobs.py
- Docs updated: design/DESIGN.md(§12.8)

### 2026-10-01 — 방산 강조 저장 안 함(02 기본 = 전체 보기)
- Type: Fix
- Summary: 요청 M11.
  - 원인: 방산 강조가 브라우저에 저장돼, 다시 열면 02가 '방산 관련 직무' 켜짐으로 시작.
  - 수정(사용자 결정): 저장 목록에서 뺌 → 항상 '전체 보기' 상태로 시작. 예전에 저장된 값은 무시.
  - 다른 화면 영향: 04 채용·기업 탐색의 '방산 강조'도 다시 열면 꺼져 있음.
  - 테스트 79개 통과(새 테스트 1개).
- Files: core/persistence.py, tests/test_persistence.py
- Docs updated: plan.md(7.2 저장 항목)

### 2026-10-01 — 02 오른쪽 열 여백 한 번 더(M10)
- Type: Design
- Summary: 방산·전체 단추와 '대분류' 사이, 대분류 칩과 '중분류' 사이 여백 24px → 40px. '보러가기' 단추 위 구분선 삭제(사용자 지시, 요청 M10).
- Files: static/css/base.css, views/p02_jobs.py
- Docs updated: design/DESIGN.md(§12.8)

### 2026-10-01 — 11차 수정 후속 6(02 중분류 흐림·구분선 통일·여백·단추 높이)
- Type: Design
- Summary: 요청 M9.
  - 방산 보기 중 중분류 칩도 흐리게 함.
  - J01 그래프 아래 구분선을 오른쪽 구분선과 통일. 다른 화면 차트 카드의 구분선은 그대로이며, 통일 범위를 넓힐지 확인 필요.
  - 오른쪽 열 구분선 위 여백을 늘림.
  - '보러가기' 단추 높이를 1.2배로.
  - 테스트 78개 통과.
- Files: views/p02_jobs.py, static/css/base.css
- Docs updated: design/DESIGN.md(§12.8)

### 2026-10-01 — 11차 수정 후속 5(02 방산 칩 흐림·구분선)
- Type: Design
- Summary: 요청 M8.
  - 방산 보기 중에는 방산 관련 직무가 없는 대분류 칩을 흐리게 함(위치 기준 CSS를 그때만 넣음).
  - 구분선은 이름 위·선 아래로 바꾸고 더 선명한 선 색을 씀.
  - 테스트 78개 통과.
- Files: views/p02_jobs.py, static/css/base.css
- Docs updated: design/DESIGN.md(§12.8)

### 2026-10-01 — 11차 수정 후속 4(02 그래프 폭·단추 고정·단추 상호 해제)
- Type: Design / Feature / Fix
- Summary: 요청 M7.
  - 배치: 오른쪽 열은 내용 폭만큼만 쓰고 그래프를 넓힘. '보러가기'는 열 맨 아래 고정, 바로 위에 구분선.
  - 단추: '전체 보기'와 '방산 관련 직무'는 서로 해제.
  - 오류: 다시 붙은 캔버스의 CSS 높이가 빠져 그래프가 낮게 보이던 문제 수정.
  - 테스트 78개 통과.
- Files: views/p02_jobs.py, components/job_graph3d.py, static/css/base.css
- Docs updated: design/DESIGN.md(§12.8)

### 2026-10-01 — 11차 수정 후속 3(02 오른쪽 열 정리, 스크롤 수정)
- Type: Design / Fix
- Summary: 요청 M6.
  - 오른쪽 열 구성
    - 위 방산·전체 단추(꺼짐 = 테두리, 켜짐 = 채움, '방산 관련 직무').
    - 구분선 '대분류' 아래 칩 한 줄에 하나.
    - 구분선 '중분류' 아래 중분류(선택 전 안내 문구).
    - 맨 아래 '관련 직무 카드 보러가기'.
    - 모두 오른쪽 정렬, 열은 그래프 높이까지 늘어남.
  - 스크롤 수정: 방산·전체·칩을 눌러도 카드 쪽으로 내려가던 문제.
  - 테스트 78개 통과.
- Files: views/p02_jobs.py, components/scroll.py, static/css/base.css
- Docs updated: design/DESIGN.md(§12.8)

### 2026-10-01 — 11차 수정 후속 2(02 3D 네트워크 오른쪽 열·이름·색)
- Type: Design / Feature
- Summary: 요청 M5.
  - 오른쪽 열
    - 칩 오른쪽 정렬.
    - 빨강 '방산 가지 보기' + 초록 '전체 보기' 단추. 02 필터 줄의 방산 토글은 제거, 상태는 같아 04와 연동.
    - 맨 아래 초록 '관련 직무 카드 보러가기'(카드 펼치기 열고 스크롤).
  - 그래프
    - 층별 초록을 더 밝게 함.
    - 강조 중에는 관련 없는 가지 이름을 숨김(마우스를 올리면 보임).
    - 확대 상태의 흔들림은 대분류·중분류 순으로 작고 느리게.
  - 테스트 78개 통과.
- Files: views/p02_jobs.py, components/job_graph3d.py, components/scroll.py(새), core/theme.py, static/css/base.css
- Docs updated: design/DESIGN.md(§12.8)

### 2026-10-01 — 11차 수정 후속(02 3D 네트워크)
- Type: Design / Removal
- Summary: 요청 M4.
  - 삭제(사용자 지시): 2D 네트워크 코드(charts.job_network·NET_ROOT·R1~R3).
  - 회전
    - 자동 회전 최대 속도를 낮춤.
    - 마우스를 올리면 정지, 끌기로만 회전.
  - 배치·모양
    - 대분류·중분류 칩을 오른쪽 열로 옮김. 그래프 높이 = 폭×0.9.
    - 선택 확대: 대분류 1.45, 중분류 1.9.
    - 층별 초록 진하기를 달리 함(새 토큰).
  - 방산 강조 시 방산 가지 외에는 흐리게(회색 아님).
  - 가운데 이름 '드론 직무'(숫자 삭제).
  - 남긴 것: theme.CHART net_* 일부는 HTML 공유본 JS 2D 사본이 사용. net_h 값은 420(3D 최소 높이)으로 바뀌어 다음 공유본을 만들 때 2D 그래프 높이도 420이 됨.
- Files: components/charts.py, components/job_graph3d.py, views/p02_jobs.py, core/theme.py, static/css/base.css
- Docs updated: plan.md(v0.21 비고), design/DESIGN.md(§12.8)

### 2026-10-01 — 11차 수정(02 직무 탐색): 네트워크 클릭 오류 수정, 3D 홀로그램 네트워크
- Type: Fix / Feature / Design
- Summary: 요청 M(revision_requests.md M).
  - 오류: 선(링크) 클릭 시 이름 형식 차이로 IndexError → 선·없는 이름 무시.
  - J01 네트워크를 3D로 교체(components/job_graph3d.py)
    - 구 3겹(대분류·중분류·직무) 가지 배치.
    - 마우스 위치 회전, 자동 자전, 끌기.
    - 선택 가지를 앞으로·확대, 방산 직무 빨강, 방산 강조 시 일반 직무 회색.
  - 다른 기능 영향
    - 대분류·중분류 칩·카드 필터 연결은 그대로.
    - 차트 '표로 보기'는 그대로.
    - HTML 공유본 v3는 이전(2D) 그대로.
  - 쓰지 않게 된 코드(삭제 안 함, 확인 요청): components/charts.py job_network·NET_ROOT·R1~R3, theme.CHART의 net_zoom_*·net_edge_ring·net_aspect·net_fan_deg·net_focus_scale·net_dim_*·net_edge_on.
  - 테스트 78개 통과.
- Files: views/p02_jobs.py, components/job_graph3d.py(새), core/theme.py, .claude/launch.json(확인용 8502 서버 추가)
- Docs updated: plan.md(v0.21), design/DESIGN.md(§12.8)

### 2026-10-01 — 카드 단추 글자 굵게, 책갈피 그림 교체
- Type: Design
- Summary: 요청 L6. 별·책갈피 단추 글자를 굵게(버튼 굵기 토큰). 책갈피 GIF를 새 파일로 교체해 모양 WebP 다시 생성(이전 책갈피 GIF는 사용자 지시로 교체).
- Files: static/css/base.css, scripts/make_card_icons.py, static/img/card_bookmark.gif·card_bookmark_*.webp
- Docs updated: design/DESIGN.md(§12.7)

### 2026-10-01 — 10차 수정: 카드 단추(별·책갈피), 선택 카드 강조, 카드 펼치기·필터 토글
- Type: Design / Feature
- Summary: 요청 L(revision_requests.md L).
  - 03: 공고 기술 그래프 펼치기는 '채용 키워드로 찾기' 탭에서만.
  - 카드·상세 팝업의 초록 단추 = 그라데이션.
  - 직무 = 별 '해당 직무 선택', 교육·공고·기업 = 책갈피 '스크랩'. scripts/make_card_icons.py가 GIF를 모양 WebP(빈·채움·채워지는·비워지는)로 변환.
  - 스크랩·선택 카드: 살짝 떠오름 + 초록 테두리·그림자(사용자 선택 C안), 해제하면 원래대로.
  - 02 직무·04 공고·04 기업 카드 → 펼치기(기본 닫힘, 조건으로 좁히면 펼친 채) + '방산 관련만 보기' 필터 토글(그래프는 그대로).
  - 03 교육 카드: '드론 관련만 보기' 토글. 드론 수집 과정은 항상 초록 띠·'드론 교육' 배지.
  - 다른 기능 영향
    - '목표로 선택' 문구가 '해당 직무 선택'으로 바뀜.
    - 기존 '방산 강조' 토글은 그대로.
    - 02 J05 키워드 결과 카드는 펼치기 없이 그대로(요청 범위 밖).
    - HTML 공유본은 v3까지(이번 변경 미반영).
  - 테스트 78개 통과.
- Files: components/cards.py, components/dialogs.py, components/icon_button.py(새), components/filters.py, views/p02_jobs.py, views/p03_learning.py, views/recruit/postings.py, views/recruit/companies.py, core/theme.py, static/css/base.css, scripts/make_card_icons.py(새), static/img/card_*(새)
- Docs updated: plan.md(v0.20), design/DESIGN.md(§12.7)

### 2026-10-01 — 9차 수정(03 준비 역량 수정2) + 세 번째 HTML 공유본(v3)
- Type: Feature / Fix / Design
- Summary: 요청 K(revision_requests.md K).
  - 03 순서: 지도·키워드 막대(맨 위) → '키워드로 교육 찾기'(교육 키워드 / 채용 키워드 탭) → 공고 기술 그래프 펼치기 → 교육 과정 펼치기.
  - 채용 키워드: 공고 기술 중 관련 교육이 있는 42개, 괄호 = 관련 과정 수(공고 수는 검색창 목록과 아래 그래프에 표시). 지역 조건은 두 방식 공통.
  - 공고 기술 그래프 막대 클릭 → 채용 키워드로 찾기. 관련 교육이 없으면 안내 문구(이전엔 오류).
  - 오류 수정: 일치 과정 0개일 때 빈 결과의 열이 없어 생기던 AttributeError.
  - 영문 짧은 키워드 단어 경계 일치(과정명·NCS명). 넘어온 '선택한 기술' 검색 결과도 같은 규칙.
  - HTML v3: 01(KPI 아이콘 카드, 추이 선 그리기, 방산 겹침 막대, 미리보기 흐림, 국가 R&D 상시·히트맵 칸 클릭·연구 과제 탐색 7,819개)과 03(J·K) 반영. 다른 화면은 v2와 같음.
  - 테스트 78개 통과(새 테스트 2개).
- Files: views/p03_learning.py, analytics/learning.py, tests/test_analytics.py, scripts/build_interactive.py, scripts/interactive/(core·logic·charts·ui·pages·main.js, app.css), html/v3_수정본_2026-10-01.html(새), html/README.md, .claude/launch.json(공유본 확인용 정적 서버 추가)
- Docs updated: plan.md(v0.19 — 9.4 S04, 9.8), design/DESIGN.md(§12.6)

### 2026-10-01 — 8차 수정(03 준비 역량): 키워드 검색, 지역 지도 + 키워드 막대, 교육 과정 펼치기
- Type: Feature / Design / Fix
- Summary: 요청 J(revision_requests.md J, 03만 수정).
  - J2-1 데이터: 1차 수집 과정의 검색어가 전처리에서 '드론' 하나로 합쳐져 단추 9개뿐이었음.
    - scripts/make_course_keywords.py가 수집 원본(../DataCollect/work24, 읽기만)에서 과정별 검색어 관계표를 만들고, build_data.py가 courses.search_keywords를 다시 채움.
    - 단추 17개: 초경량비행장치 47, 드론조종 40, 무인비행 24, 항공촬영 5, 무인항공 4, 드론제작 4, 자율비행 2, 비행제어 1 추가, VTOL 1→3, 드론 148→137.
    - 0건 검색어 5개(UAV·비행제어기·Pixhawk·DJI·GIS)는 캡션으로 안내.
  - J2: 검색창(여러 개) + 칩. 개수는 '(40)' 작은 회색. 여러 개 = 하나라도 해당.
  - J1: 기본 화면에 지도(전체 → 고른 키워드의 과정 수) + 키워드별 과정 수 막대.
    - 지도에 마우스를 올리면 그 지역 막대로 바로 바뀌고, 지도 클릭 = 지역 필터, 막대 클릭 = 키워드 필터.
    - 새 부품 components/linked_map.py(components.v2 + static/vendor/echarts.min.js).
  - J3: '교육 과정 보기' 펼치기. 기본 닫힘·전체 438개, 조건을 고르면 자동 펼침·필터, 10개씩.
  - 삭제(사용자 결정): '언제 시작하나' 월별 그래프. 함께 쓰이지 않게 된 analytics.learning.month_counts·region_counts(회차 기준)도 삭제.
  - 다른 화면 영향:
    - 02·S02·S03에서 넘어오는 '선택한 기술'은 그대로 동작(추가 필터 칩).
    - 단일 키워드 칩 상태(learn_course_kw)는 여러 키워드 상태(learn_kws)로 바뀜. 정적 공유본 ?kw= 예시도 이 상태로 연결.
    - HTML 공유본(v2)은 미반영.
  - 테스트 76개 통과.
- Files: views/p03_learning.py, components/linked_map.py(새), analytics/learning.py, content/module_meta.py, static/css/base.css, static/vendor/echarts.min.js(새, 복사), scripts/make_course_keywords.py(새), scripts/build_data.py, data/bridges/course_search_keywords.csv(새)
- Docs updated: plan.md(v0.18 — 9.4 S04), design/DESIGN.md(§12.5), ENVIRONMENT.md(§6), data/bridges/README.md

### 2026-10-01 — 7차 수정(01 산업 이해): KPI 카드 재디자인, 추이 선 그리기, 분야 미리보기 흐림
- Type: Design
- Summary: 요청 I(revision_requests.md I, 01만 수정).
  - I1: 업체·매출·종사자 카드를 A안으로. 왼쪽 원 안에 첨부 GIF 아이콘(건물·매출 막대·사람), 테마 초록. 마우스를 올린 동안 움직이고(움직임 끔이면 정지), 제목은 카드 제목 크기, 숫자는 34px 초록, 여백 축소.
    - GIF는 홈 아이콘과 같은 방식(scripts/make_kpi_icons.py)으로 색을 뺀 모양 WebP(기본 1장 + 반복 움직임)로 변환.
    - stat_tiles에 선택 항목 `icon` 추가. 아이콘이 없는 홈 카드는 그대로(다른 화면 영향 없음).
  - I2: '연도별 추이' 펼칠 때 그래프를 새로 그려, 선이 왼쪽→오른쪽으로 1.4초 동안 그려짐.
  - I3: 접힌 상태에서 다음 분야 2개를 흐리게 미리 보여 주고(아래로 갈수록 흐림), 바로 아래 가운데 '⌄ 분야 더보기' 단추.
  - 테스트 76개 통과.
- Files: views/p01_industry.py, components/effects.py, components/charts.py, core/theme.py, static/css/base.css, scripts/make_kpi_icons.py, static/img/kpi_*.gif·webp
- Docs updated: plan.md(v0.17 — 9.2 I01·I02), design/DESIGN.md(§12.4)

### 2026-10-01 — 6차 수정(01 산업 이해): 방산 겹침, 기술 그래프 합침, 연구 과제 탐색
- Type: Feature / Design
- Summary: 요청 H(revision_requests.md H, 팀원 검토 반영, 01만 수정).
  - 분야 막대에 방산 근거 기업 수 겹침(H2), '분야 더보기' 토글 → ⌄ 단추(H3).
  - '방산 태그 과제의 기술 분야'와 '연구하는 기술'을 하나의 겹친 막대로(H1). 연도별 그래프와 나란히, 국가 R&D 영역 상시 표시(H7).
  - 활용 분야 셀 클릭 → 두 태그 과제 목록(H6). '연구 과제 탐색' 펼치기(전체/기술/기술×활용 분야, 10개씩, 선택 시 자동 펼침)(H7).
  - '이 분야' → '드론 분야', 분야 상세는 분야 이름(H4).
  - 다른 화면 영향 보고: 04 기업 탐색 C01은 숫자 같고 모양만 다름, HTML v2 미반영.
  - 테스트 76개 통과.
- Files: views/p01_industry.py, components/charts.py, analytics/industry.py, analytics/companies.py, content/module_meta.py, scripts/build_interactive.py
- Docs updated: plan.md(v0.16 — 9.2 I02·I03·I04), design/DESIGN.md(§12.3)

### 2026-10-01 — 두 번째 HTML 공유본(v2 수정본): 기능이 살아 있는 단일 파일
- Type: Feature
- Summary: 요청 G1(revision_requests.md G).
  - `html/v2_수정본_2026-10-01.html`(8.9MB, 오프라인)은 데이터 JSON + JavaScript 앱 + ECharts 5.6.0 + Pretendard를 한 파일에 담음.
  - analytics/ 계산 규칙을 JavaScript로 옮겨 화면 7개와 앱 기능 거의 전부를 재현:
    - 차트 클릭·칩 필터 연동, 카드·페이지 넘김, 상세 팝업(이동·되돌아가기)
    - 직무 네트워크 확대, 교육 키워드, 내 조건 칩
    - 스크랩 3개·나의 탐색 경로·해제, 목표 직무·방산 강조, 라이트/다크·브라우저 저장
  - 주요 수치 11개를 파이썬 결과와 대조해 일치.
- Files: scripts/build_interactive.py, scripts/interactive/{template.html,app.css,core.js,logic.js,charts.js,ui.js,pages.js,main.js,vendor/echarts.min.js}, html/v2_수정본_2026-10-01.html, html/README.md, ENVIRONMENT.md
- Docs updated: plan.md(v0.15 — 9.8.1)

### 2026-10-01 — 5차 수정(F1~F9): 방산 하이라이트(빨강), 직무 네트워크, 교육 키워드 칩, 목표 직무 강조, 사이드바·차트 정리
- Type: Feature / Design / Removal
- Summary: report/revision_requests.md F절.
  - F1: 01 보조 열(공고 지도·경력) 제거, 분야 영역 전체 폭.
  - F2·F6: 방산 색 주황 → 빨강(DESIGN §12.1 적용).
    - 기업·공고·직무 카드: 항상 빨강 테두리·띠·'방산 관련 기업'/'방산기업 근무처' 배지.
    - 01: 연도별 R&D 방산 태그 누적·기술 분야 막대(I04).
    - 04 채용 현황: 직무별 공고 누적(방산 관련 기업/그 외/미연결)과 방산 vs 그 외 직무 구성 비교(H07).
    - 04 기업 탐색: 방산 관련 기업 공고 노출(C04). 02에 '방산 강조' 토글. 03 교육은 제외(사용자 결정).
  - F3: J01 트리맵 → 직무 네트워크(선택 가지 확대·나머지 흐리고 작게, 중분류 부채꼴, 방산 직무 빨강).
  - F4: 03 검색창 → 수집 검색 키워드 9개 칩, 넘어온 기술은 '선택한 기술' 칩.
  - F5: 03·04 '목표 직무 관련 강조' 토글(분류·기술·사업 분야 이유 배지, 나머지 옅게).
  - F7: 04 하위 메뉴 글꼴 70%, 04 안에서 접기/펼치기(원인: 04에 있으면 항상 펼침으로 그림), 펼침 상태 비저장.
  - F8: 차트 제목 24px, 가로 막대 22px·행 42px, 세로 막대 32px, 축 글자 한 단계 작게.
  - F9: 탐색 경로 담긴 단계 강조.
  - 테스트 76개 통과(분석 함수 테스트 6개 추가).
- Files: core/{theme,state,persistence}.py, components/{charts,cards,badges,filters,shell}.py, analytics/{common,postings,learning,companies,industry,jobs}.py, views/{p01_industry,p02_jobs,p03_learning}.py, views/recruit/{postings,companies}.py, content/module_meta.py, static/css/base.css, tests/test_analytics.py
- Docs updated: plan.md(v0.14 — 9.2·9.3·9.4·9.7·9.7.1), design/DESIGN.md(§12.2)

### 2026-09-30 — 4차 수정(E1~E7): 글꼴 1.2배, 스크랩 3개·녹색 버튼, 대한민국 지도, 나의 탐색 경로, 그라데이션, 방산 빨강 제안
- Type: Feature / Design / Removal
- Summary: report/revision_requests.md E절. E1 본문 글꼴 1.2배(사이드바·카드 유지, 카드 제목만 1.2배, Streamlit 위젯 글자 포함). E2 교육·공고 카드의 '학습 계획에 선택'·'비교 공고로 선택' 삭제, 세 카드 스크랩 버튼 녹색. 충돌 2 결정으로 공고 팝업 '비교 공고로 선택', plan.learning·compare_posting_id·관련 함수·테스트 삭제. E3 지역 타일 → 대한민국 시·도 지도(KOSTAT 2013 단순화 GeoJSON, data/reference). 값 농도·0건·클릭 선택·툴팁·선택 강조 유지, 광역시 라벨 지시선. 04 직무·지역 행 1:1로 조정. E4 '나의 탐색 경로', 01 목표 직무 해제. E5 교육·공고·기업 스크랩 종류별 최대 3개(초과 시 막고 안내). E6 녹색 그라데이션(버튼·막대). E7 방산 빨강 제안값 DESIGN.md에 기록(미적용). 마무리: 나란한 차트 카드 높이 맞춤(03 지도·월별, 04 직무·지역), 신규 분석 함수 테스트 2개 추가. 충돌 3: 04 H06 → 목표 직무와 스크랩 공고 비교(분류 관계·기술 언급·공고 키워드·원문 조건). 충돌 4: 학력·경력·희망 지역은 04 필터 영역의 '내 조건' 칩(차이 확인 공고만 제외, 03 교육 정렬에도 사용). 테스트 71개 통과.
- Files: core/theme.py, core/state.py, components/{charts,cards,dialogs,shell,effects}.py, views/{p01_industry,p03_learning}.py, views/recruit/postings.py, analytics/postings.py, content/{usage_guide,module_meta,page_intros}.py, static/css/base.css, tests/{test_state,test_persistence,test_analytics}.py, data/reference/skorea_provinces_geo_simple.json
- Docs updated: design/DESIGN.md(§12.1), plan.md(v0.13 — 7.1 상태·규칙, H01·H06·S04, 9.7)

### 2026-09-30 — 3차 수정: 준비 경로 4단계·스크랩 1개씩, 사전 역량·결과물 삭제, J05 키워드로 직무 찾기
- Type: Feature / Removal
- Summary: 3차 수정 요청 D4·D6·D7(report/revision_requests.md). 사용자 동의 후 삭제: 오른쪽 준비 경로의 02 사전 역량·04 제작할 결과물, 03의 사전 기술 체크(S01)·'내가 배우려는 기술만' 토글·결과물 편집 제안(S06), 기술 자기보고·결과물 상태와 함수, 브라우저 저장 항목 skills, 관련 문구·CSS·테스트. 준비 경로를 목표 직무 / 학습 내용 / 채용 공고 스크랩 / 관심 기업 스크랩 4단계로 재구성하고 각 단계에 스크랩 '해제' 추가. 교육·공고·기업 스크랩은 종류별 1개, 새로 스크랩하면 교체. 상단 '스크랩 N' 삭제. 충돌 결정 반영: 02 J05를 '직무 키워드 또는 보유 기술로 직무 찾기'(키워드 칩·검색 → 직무 카드)로 변경, 04 '내 조건과 비교'는 스크랩한 공고 사용, 직무 스크랩 버튼 삭제, 목표 직무를 바꿔도 스크랩 유지. 스크랩 버튼과 계획 선택 버튼 통합은 보류. 테스트 70개 통과.
- Files: core/state.py, core/persistence.py, components/shell.py, components/cards.py, components/dialogs.py, views/p02_jobs.py, views/p03_learning.py, views/recruit/postings.py, content/page_intros.py, content/usage_guide.py, content/module_meta.py, static/css/base.css, tests/test_state.py, tests/test_persistence.py
- Docs updated: plan.md(v0.12 — 7.1 상태 스키마·규칙, 7.2 저장 대상, J05·S01·S06, 9.7 준비 경로), design/DESIGN.md(§11.2 준비 경로 해제 버튼)

### 2026-09-30 — 3차 수정: 사이드바 로고·번호·홈 아이콘, 준비 경로 따라오기, 홈 드론 클릭·크기
- Type: Design / Fix
- Summary: 3차 수정 요청(report/revision_requests.md D1~D3, D5, D8, D9). 사이드바 서비스명을 메뉴보다 크게(22px·800, 녹색 점 강조, 아래 구분선). 메뉴 번호를 이름과 분리해 고정 폭 칸에 같은 폭 숫자로 그려 홈~04 이름 시작 위치를 맞춤(04만 7px 어긋나던 링크 내부 간격도 제거). 홈 기호를 사용자가 준 움직이는 집 아이콘으로 교체(기본 = 첫 프레임, 마우스를 올리면 입체까지 한 번 재생 후 유지, 글자색을 따라 라이트/다크 대응). 오른쪽 준비 경로를 스크롤해도 화면 위쪽에 붙어 따라오게 함(패널이 아닌 열에 sticky). 확인 중 발견한 문제 수정: 폭 1440px 근처에서 준비 경로가 본문 아래로 떨어지던 줄바꿈. 홈 드론 두 번째 클릭이 깜빡이기만 하던 문제 수정(재실행 때 늦은 상태값을 다시 적용하던 것), 메뉴를 열기 전에는 큰 드론·열면 작은 드론으로 0.3초 전환. D4·D6·D7(준비 경로 개편·삭제)은 삭제 목록과 충돌 사항을 정리해 사용자 확인 대기. 테스트 70개 통과.
- Files: components/shell.py, components/effects.py, core/theme.py, static/css/base.css, static/img/home.gif(원본), static/img/home_rest.webp, static/img/home_hover.webp, scripts/make_home_icon.py, report/revision_requests.md
- Docs updated: design/DESIGN.md(§3 기호, §7 Navigation, §10 드론·홈 아이콘, §11.2 준비 경로 고정, §12 D10·D16)

### 2026-09-30 — 첫 HTML 공유본 저장 (v1 초안본)
- Type: Feature
- Summary: 팀 공유용 정적 HTML `html/v1_초안본_2026-09-30.html`(7.2MB, 오프라인) 저장. 7개 화면(홈, 01, 02, 03, 03 예시(검색어 CAD), 04 채용 현황, 04 기업 탐색), 다크 테마, 차트 24개(이미지), '근거 자세히' 숫자 표 14개, 사이드바·화면 안 버튼·드론 메뉴·상단 선택으로 화면 전환. 앱에 내보내기 모드(`?export=1`: 기본 상태, 애니메이션 끔, 표를 정적 HTML 표로, 테마 토글 숨김)를 추가하고, 브라우저 캡처 함수(`scripts/export_capture.js`)와 수신·조립 스크립트(`scripts/export_html.py`)를 작성. 캡처 중 발견한 문제 수정: 펼치기 안 차트 폭 0(캡처 전 모두 펼침), 차트 캔버스 층 겹침, 오프라인에서 아이콘이 글자로 보임(아이콘 제거), 트리맵이 진한 녹색 면으로 채워짐(농도 직접 계산). 테스트 70개 통과.
- Files: core/export_mode.py, app.py, components/{chart_card,charts,effects}.py, views/p03_learning.py, core/theme.py, scripts/export_html.py, scripts/export_capture.js, html/v1_초안본_2026-09-30.html, html/README.md, ENVIRONMENT.md
- Docs updated: plan.md(v0.11 — 9.8 구현 방식·저장 기록)

### 2026-09-30 — 무한 재실행(흐려짐·로딩 지연) 수정, 호버 흐림 제거, 사이드바 메뉴 정리
- Type: Fix / Design
- Summary: 2차 수정 요청(report/revision_requests.md C1~C3). 실행 로그 계측으로 초당 약 15회의 무한 재실행을 확인 — 원인은 브라우저 저장 컴포넌트가 실행마다 저장값을 다시 보내던 것(복원 완료가 파이썬에 전달되지 않음). 저장값은 세션 식별값당 한 번만 보내고, 파이썬은 컴포넌트 반환값으로 한 번 복원 후 한 번만 다시 그리도록 수정 → 페이지 이동 1회당 실행 1회(서버 30~240ms), 화면 흐림 사라짐. 차트 호버 시 다른 표시를 흐리게 하던 효과 제거(가리킨 표시의 강조·글로우만 유지). 접힌 '근거 자세히'의 AgGrid 표를 '표로 보기' 토글로 지연 로드, 04 전용 ?sub= 쿼리가 다른 페이지 주소에 남던 문제 제거. 사이드바 메뉴 17px, 홈~04 항목 높이 44px·간격 48px 통일(원인: page_link 기본 여백 1.75px), 홈 표시 "⌂ 홈". 테스트 70개 통과.
- Files: components/browser.py, app.py, components/charts.py, components/chart_card.py, core/routing.py, core/theme.py, components/shell.py, static/css/base.css
- Docs updated: design/DESIGN.md(§2·§5·§6.4·§7·§8·§10·§11.3·§12 D8·D10·D15) / plan.md(변경 이력)

### 2026-09-30 — 디자인 시스템 Green Deck 전환 + 사이드바·테마 토글·호버 효과
- Type: Design / Feature
- Summary: 사용자 수정 요청(report/revision_requests.md A1~A5, B1~B4) 반영. DESIGN.md를 Green Deck 기준으로 재작성(Pretendard 폰트와 사용자 '방산 vs 일반' 규칙·프로젝트 결정 유지, 라이트 색은 사용자 스크린샷 실측, 이전 문서는 design/archive/로 보관). 대비·색각 검증 결과 녹색 버튼 글자(다크 검정), 라이트 보조 글자(#6B6B6B), 방산 주황 유지(#F59B23 불가), 선택=반전 칩(청록 폐기)을 원문과 다르게 정하고 문서에 명시. theme.py·config.toml·base.css를 새 토큰으로 교체해 영역 톤 구분(사이드바·카드 #181818 / 메인 #121212, 라이트 #F3F0EF / #F9F6F5 / #FFFFFF). 사이드바 240px·메뉴 15px 한 줄·슬라이드 전환, '04 채용·기업 탐색' 클릭 시 채용 현황 이동+하위 메뉴 펼침, 하단 ☀ 라이트/☾ 다크 토글(첫 방문 다크, Streamlit 테마 저장값 변경 후 새로고침)과 선택 상태 브라우저 저장·복원(plan 7.2 앞당김). 호버 효과: ECharts 강조(글로우·나머지 흐림·값/비율/순위 툴팁), 카드·타일·버튼·메뉴 호버, streamlit-aggrid 인터랙티브 표(행 호버·정렬·필터·검색, 1.64에서 그리드 폭 0 문제 보정). 테스트 70개 통과, 브라우저에서 라이트·다크·테마 전환·상태 유지·B4·호버·표 확인.
- Files: design/DESIGN.md, design/archive/DESIGN_chapter_2026-09-30.md, core/theme.py, core/persistence.py, .streamlit/config.toml, static/css/base.css, static/fonts/Pretendard-ExtraBold.otf, components/{charts,effects,browser,tables,shell,chart_card,dialogs}.py, views/recruit/postings.py, app.py, tests/{test_app_smoke,test_persistence}.py, requirements.txt, requirements-lock.txt, ENVIRONMENT.md, report/revision_requests.md
- Docs updated: plan.md(v0.9) / design/DESIGN.md(전면 교체)

### 2026-09-30 — P4 기본 화면 + 시각 효과 모듈
- Type: Feature / Design
- Summary: research 12장 '기본 탐색' 모듈 구현. 홈(M01 드론 진입·M02 P1~P5·M03 오버뷰 카운트업·M04 안내), 01 산업(I01 KPI·추이, I02 분야 막대↔칩↔상세·직무/기업 이동, 지역·경력 보조, I03 NTIS 기술·히트맵·근거 과제), 02 직무(J01 트리맵→중분류→카드 10개, J02·J03 상세 팝업, J05 보유 기술 히트맵), 03 준비 역량(S01 자기 체크, S02 학습 이유·리소스 그룹, S03 공고 언급, S04 키워드 교육 검색·그룹·지역 타일·월별 막대·카드, S06 결과물 제안), 04 채용 현황(H01 KPI·직무·지역 타일, H02 경력·학력·직무×경력·고용형태, H04 카드·상세, H06 조건 비교), 04 기업 탐색(C01 분야·근거 집단 막대·키워드·정렬·10개·더보기 팝업, C02·C03 상세). 사용자 요청에 따라 차트를 Plotly 대신 ECharts(streamlit-echarts 0.7)로 그려 등장·전환 애니메이션·클릭 선택을 쓰고, Streamlit 내장 components.v2로 홈 드론(SVG, 링 파동·부유·P1~P5)과 숫자 카운트업을 구현. 모든 색·치수·움직임은 core/theme.py 토큰에서만 가져오고 동작 줄이기 설정을 따름. Q2(방산 집단 배정)·Q13(조직 유형 필터 제외) 기본안 확정, Q5 SVG 임시 결정. 교육 회차 지역 표준화(province_std: 경기도→경기, 전남광주는 별도 표기). 카드 행동을 위해 state 변경 함수(스크랩·목표·학습 계획·결과물·비교 공고·기술 자기보고)와 오른쪽 경로의 선택 요약을 함께 구현. 테스트 65개 통과(분석 규칙 15, 상태 4, 스모크 12 포함). 브라우저에서 라이트·다크, 1440/375px, 드론→P5, 막대 클릭→칩·상세, 방산 강조(건수 불변), 상세 팝업, 목표 선택→03 연동, 교육 검색(CAD 241개) 확인.
- Files: analytics/{common,defense,companies,postings,jobs,learning,industry,overview}.py, core/{theme,state,datasets}.py, components/{charts,chart_card,effects,cards,dialogs,filters,badges,shell}.py, content/{module_meta,activity_tags,usage_guide}.py, data/content/project_suggestion.csv, views/{home,p01_industry,p02_jobs,p03_learning}.py, views/recruit/{postings,companies}.py, app.py, scripts/build_data.py, static/css/base.css, tests/{test_analytics,test_state,test_app_smoke}.py, requirements.txt, requirements-lock.txt, ENVIRONMENT.md
- Docs updated: plan.md(v0.8) / design/DESIGN.md(§10.1 ECharts 구현, §12.2 움직임 추가 — Proposed, 드론 SVG 예외)

### 2026-09-30 — P3 앱 셸
- Type: Feature
- Summary: 진입점과 공통 셸 구현. 페이지 5개(`st.navigation` 숨김 + 직접 그린 사이드바 메뉴), '04 채용·기업 탐색' 펼침 메뉴와 하위 2개, 중앙 하위 탭(SubNav 모양), 검정 상단바(서비스명·현재 화면·스크랩 수·준비 경로 접기), 좌측 하단 문맥 안내(페이지 기본 안내), 오른쪽 '내가 선택한 준비 경로' 5단계 빈 상태, 분석 화면 상단 소개(research 3.9 문구), 홈 M01 제목과 P1~P5 이동 버튼(M02 대체 경로). 디자인 토큰을 `core/theme.py` 한 곳에 두고 `:root` 변수로 주입, 스타일은 `static/css/base.css`에서 토큰만 참조. 04 하위 페이지 상태는 위젯 키 `sub` 하나로 사이드바·탭이 공유하고 `routing.sync_sub()`로 URL `?sub=`와 동기화(`bind="query-params"`는 코드에서 URL 설정 불가라 미사용). 브라우저 확인: 1440px에서 사이드바 160 / 중앙 920 / 오른쪽 240px, 1280px에서 오른쪽 224px, 375px에서 오른쪽 패널이 본문 아래로, 가로 스크롤 없음, 라이트·다크 모두 확인, Pretendard 로드 확인. 스모크 테스트 12개 포함 전체 46개 통과.
- Files: app.py, run.ps1, core/theme.py, core/state.py, core/routing.py, components/__init__.py, components/shell.py, components/page_intro.py, content/page_intros.py, content/module_meta.py, views/*.py, views/recruit/*.py, static/css/base.css, .streamlit/config.toml(사이드바 테마), tests/test_app_smoke.py, ../.claude/launch.json(미리보기 실행 설정)
- Docs updated: plan.md(v0.7) / design/DESIGN.md(§12.1 셸 토큰, G3 적용 내용)

### 2026-09-30 — P2 관계표(브리지) 초안
- Type: Feature
- Summary: `scripts/draft_bridges.py`로 1차 구현에 필요한 관계표 5개 초안을 `data/bridges/`에 생성(모두 `draft`). 공고–기업 135행(연결 53 = 정확 일치 52 + 법인 표기 차이 1, 미연결 82 유지), 기업 식별 22행(LIG `CMP0003→CMP0002` 1건만 ID 불일치 — DART 목록 행에 한정), 분야–직무 390행(규칙 A 17줄), 직무–공고분류 362행(규칙 B 18줄, direct/adjacent/broad), 기술 사전 617행(616개 기술; 대소문자·공백·하이픈만 동일시, C++/C/C++·ROS/ROS2 분리). 기존 파일은 덮어쓰지 않음(검토 보호). `build_data.py`가 브리지를 `bridge_*` 테이블로 적재하고 검토 상태·참조 무결성·공고당 1행을 검사. 검토 안내 `data/bridges/README.md`. 테스트 34개 통과.
- Files: scripts/draft_bridges.py, scripts/build_data.py, tests/test_bridges.py, data/bridges/*.csv(5), data/bridges/README.md, data/processed/bridge_*.parquet(생성물)
- Docs updated: plan.md(v0.6)

### 2026-09-30 — P1 데이터 계층
- Type: Feature
- Summary: `scripts/build_data.py`가 raw CSV를 결측 감사 → 제외 컬럼 제거 → plan 6.2 테이블 변환(프로필·DART 개요·방산 인증 한글 컬럼은 영문으로 정규화, 로컬 DB 전환 대비) → 계약 검사(plan 6.5) → `data/processed/*.parquet` 35개 + `quality_audit` + `reports/data_audit.md` 생성. 결측 판정에 원본의 결측 표시 문자열(`공개정보 확인 불가` 등 3종)을 포함해 기업 프로필 컬럼 33개가 제외됨(주소·규모·직원 수·매출 등 → C02 표시 항목 축소). union 파일은 제외 컬럼을 양쪽에 통일해 NCS 표준코드 컬럼 제외. `core/data_loader.py`는 `load_table(name)` 단일 접근점 + 빌드 상태(미빌드·원본 변경) 감지. 별도 `audit_data.py` 대신 build_data.py가 감사 리포트를 함께 생성. 테스트 23개 통과.
- Files: core/__init__.py, core/config.py, core/quality.py, core/data_loader.py, scripts/build_data.py, pytest.ini, tests/test_data_contract.py, tests/test_quality.py, data/processed/*(생성물), reports/data_audit.md(생성물)
- Docs updated: plan.md(v0.5)

### 2026-09-30 — P0 환경·데이터 배치
- Type: Feature
- Summary: Python 3.12.10 설치(winget, python.org 설치 파일) 후 `main/.venv` 생성, 패키지 버전 고정(streamlit 1.64.0, plotly 6.9.0, pandas 2.3.3, pyarrow 25.0.1, pytest 9.1.1). plan.md 2장 폴더 골격 생성. `scripts/place_raw_data.py`로 datas.zip에서 raw 39개·reference 4개·DART 4묶음(표 128, 목록 4)을 배치하고 원본과 SHA-256 일치 확인(총 175개 파일). Pretendard 300~700을 `static/fonts/`로 복사하고 `.streamlit/config.toml`을 DESIGN §9.2~9.3대로 작성, 설치된 streamlit에서 키 인식 확인. 사용자 지시 2건을 계획에 반영: 향후 로컬 DB 전환(6.1 규칙, P9), 팀 공유용 HTML 버전 저장(9.8, `html/`).
- Files: .venv/, requirements.txt, requirements-lock.txt, ENVIRONMENT.md, .streamlit/config.toml, scripts/place_raw_data.py, static/fonts/*.otf(5), data/raw/**, data/reference/*, 빈 폴더(core, analytics, components, content, views, static, data/bridges·content·processed, reports, tests, html)
- Docs updated: plan.md(v0.4) / design/DESIGN.md(폰트 상태)

### 2026-09-30 — 구현 전 문서 정리 (리서치 결과 반영)
- Type: Fix
- Summary: 구현 시작 전에 main 폴더 문서와 datas.zip·research.md·로컬 환경을 대조하고, 불일치와 사용자 결정을 문서에 반영했다. 코드·데이터 파일은 만들지 않았다.
  - 실측 확인(변경 없음): CSV 59개 분류(raw 39 / reference 4 / 제외 16) 누락·중복 없음, 행 수 26종·조인·방산 분류·공고–기업 정확 일치(22개명/52행)·DART 128표 모두 plan과 일치.
  - CLAUDE.md: `design/design.md` 표기 8곳 → 실제 파일명 `design/DESIGN.md`.
  - plan.md v0.3: 머리말 상태 갱신, Python 3.12 확정(로컬 미설치 → P0 선행 설치), config.toml은 DESIGN §9.3 참조로 일원화, 결측 표 누락 2개 컬럼 추가, `evidence_strength` 6종·`보조`(2건) Q2에 추가, 방산 참고 표본 n, DESIGN 연동(프로젝트 토큰 이름), 폴더 트리(design 폰트·report·static/fonts), Q10·Q11 추가.
  - DESIGN.md: 폰트 미배치 상태 표기, 방산 표본 예시를 testDash 수치(22건/6개사)에서 main 데이터 기준으로 교정, 잘못된 참조(plan §8 → §6.4) 수정, G2 결정(`--project-select` 청록, Proposed) 및 §12.1 프로젝트 토큰 표 추가.
- Files: CLAUDE.md, plan.md, design/DESIGN.md, report/report.md
- Docs updated: plan.md / design/DESIGN.md
