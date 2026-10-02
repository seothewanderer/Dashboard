---
name: project-next-html-share
description: "다음 HTML 공유본(v5~) 조건 — 만들 당시 앱 기능 전부 구현(새 3D 홈·사이드바 아이콘 포함), 그때 예전 드론 토큰 삭제"
metadata:
  node_type: memory
  type: project
  originSessionId: 87f6917f-8b99-4854-81f1-7fe4443564b0
  modified: 2026-10-02T03:25:46.798Z
---

다음 HTML 공유본은 **만드는 당시의 앱 기능을 전부** 구현해야 한다(사용자, 2026-10-02). 지금 바로 만들라는 것은 아님.

- 2026-10-02 기준 공유본(scripts/interactive, v4)에 아직 없는 것: 새 3D 홈(components/home_hero.js·.css — 요약 카드, Three.js 드론, 패널 아이콘, 진입·출발·복귀 비행, 마우스 시선), 홈 로드맵 4단계·FAQ 새 문구, 사이드바 01~04 아이콘(hover 반복).
- 공유본은 인터넷 없이 동작해야 하므로 static/vendor/three 4개 파일을 HTML에 넣고 Blob 모듈로 불러와야 함(앱과 같은 loadThree 방식, G.vendor 대신 내장 글).
- 04 기업 탐색도 v4 이후 바뀜(2026-10-02 S): C01 흐림 더보기, 방산 근거 집단(C01G)·칩 삭제, C04 일반/방산 전환(C04A). 공유본 pages.js는 아직 C01G를 씀 → 옮길 때 정리. 홈 요약 카드 C안(클릭 이동·아이콘)도.
- 홈을 옮길 때 함께 지울 것(사용자 삭제 승인됨, 공유본 app.css가 아직 사용 중이라 미룸): core/theme.py `--hero-*` 7개, TYPE `hero`·`nav-no`, scripts/interactive/app.css의 예전 .hero/.ring/.go/.nav-no 규칙.

**Why:** 공유본은 팀원 기능 테스트용이라 앱과 같아야 함. 토큰 삭제를 먼저 하면 공유본 빌드의 예전 홈이 깨짐.
**How to apply:** 사용자가 공유 HTML 생성을 요청하면 이 목록부터 확인하고 v4 이후 바뀐 기능을 모두 옮긴 뒤 빌드·검증. 관련: [[project-drone-career-main]]
