---
name: project-next-html-share
description: "HTML 공유본 규칙 — 만들 당시 앱 기능 전부 구현, v5(2026-10-02)에서 렌더링 맞춤 방식 확정, 남은 1280px 기준 단추"
metadata:
  node_type: memory
  type: project
  originSessionId: 87f6917f-8b99-4854-81f1-7fe4443564b0
  modified: 2026-10-02T08:46:00.989Z
---

HTML 공유본은 **만드는 당시의 앱 기능을 전부** 구현해야 한다(사용자, 2026-10-02). v5(html/v5_수정본_2026-10-02.html)에서 3D 홈·사이드바 아이콘·기업 탐색 S~X·채용 현황 Y까지 옮겨 완료했고, 예전 홈 토큰(`--hero-*`, TYPE `hero`·`nav-no`)도 삭제함.

- 사용자는 "저장해서 연 HTML과 VS Code에서 본 결과가 다르다"(글꼴 크기, 칸을 넘어 두 줄)를 신경 씀. v5에서 정한 방식: 글꼴 5개 굵기 내장 + 글꼴 로드 후 첫 그리기, 단추·칩 줄바꿈 금지, 좁은 칸은 container query로 축소(앱 effects.py·home_hero.css에도 같은 규칙).
- 남은 것: 1280px에서 기업 탐색 C01 '기준' 단추 묶음이 약 30px 넘쳐 옆 스크롤(사용자가 시간 관계로 건너뛰라고 함). file://에서 3D 동작 미확인(안 되면 정지 그림).
- 점검 방법: 8777(html-share)에서 1100·1280·1440px, 다크·라이트, 6화면에 scrollWidth>clientWidth 검사.

**Why:** 공유본은 팀원 기능 테스트용이라 앱과 같아야 하고, 사용자가 화면 차이에 민감함.
**How to apply:** 다음 공유본을 만들 때 v5 이후 바뀐 앱 기능을 모두 옮기고, 위 넓이·테마 점검을 반복. 관련: [[project-drone-career-main]]
