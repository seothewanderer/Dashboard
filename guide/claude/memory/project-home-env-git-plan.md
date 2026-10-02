---
name: project-home-env-git-plan
description: "사용자가 \"집 환경을 위해 git 작업 하자\"라고 하면 그대로 다시 안내할 계획(2026-10-02 합의) — guide 폴더·setup.ps1·메모리 이전·최종 push"
metadata:
  node_type: memory
  type: project
  originSessionId: 87f6917f-8b99-4854-81f1-7fe4443564b0
  modified: 2026-10-02T02:28:00.898Z
---

사용자가 "집 환경을 위해 git 작업 하자"(비슷한 말 포함)라고 하면 아래 내용을 **그대로 다시 안내**한 뒤 진행한다. 저장소 정보는 [[project-drone-career-main]]의 git 항목 참고.

**배경 (2026-10-02):** 첫 커밋 2eff9fb는 홈 화면 적용 중 큰 충돌에 대비한 되돌리기용 임시 저장. 오늘 작업이 모두 끝나면 마지막에 최종 push → 집 PC에서 pull/clone해 같은 개발 환경을 구축하는 것이 목표.

**진행 상태 (2026-10-02):** guide/ 폴더 생성 완료(README·setup.ps1·HANDOFF.md·claude/memory·claude/launch.json) 후 개인 저장소에 커밋, push는 사용자. 사용자가 순서를 바로잡음: guide를 먼저 만들고 커밋해야 한 번의 push로 올라감. 이후 메모리를 바꾸면 guide/claude/memory 복사본도 갱신.

**합의한 계획:**
1. 홈 화면 작업은 `home-merge` 같은 별도 브랜치에서(꼬이면 main으로 돌아가면 됨, 기록 삭제 불필요) — 제안 단계, 사용자 확정 전.
2. 오늘 작업 끝나면 저장소에 `guide/` 폴더 생성:
   - 설치 가이드 문서(Python 3.12.10 설치 등 직접 해야 할 순서)
   - `guide/setup.ps1`: Python 3.12 확인 → .venv 생성 → requirements-lock.txt 설치 → 테스트 실행까지 한 번에
   - `launch.json` 복사본(원본은 저장소 밖 `C:\Projects\Dashboard\.claude\launch.json`)
   - Claude 메모리 복사본 `guide/claude/memory/`(원본 `C:\Users\acorn\.claude\projects\C--Projects-Dashboard\memory\`, 약 10KB)
   - 인수인계 문서(결정 사항·대기 중 질문·다음 할 일·주의점) — 집에서 새 세션에 "이 문서 읽고 이어서"
3. 최종 커밋은 Claude, push는 사용자가 직접(이 세션에서 push는 권한 확인에서 막힘).
4. 집에서: 같은 경로 `C:\Projects\Dashboard\main`에 clone(메모리 폴더명이 경로 기반이라 경로를 맞춰야 이어짐) → setup.ps1 실행 → 메모리를 `~/.claude/projects/C--Projects-Dashboard/memory/`로 복사 → 새 세션.

**올리지 않기로 한 것과 이유:**
- `.venv`(435MB): 이 PC 경로가 박혀 있어 다른 PC에서 동작 안 함 → requirements-lock.txt로 재생성.
- 대화 기록 원본 .jsonl(이번 세션 52.5MB, 전체 약 62MB): GitHub 50MB 경고, 갱신마다 통째로 쌓임, 파일 내용·명령 출력까지 담겨 비공개라도 부담 → 필요하면 USB·클라우드로 따로. 대신 인수인계 문서.
- clone 후 '원본이 빌드 이후 바뀌었습니다' 안내가 뜰 수 있음(파일 시각 재설정) → build_data.py 1회 실행.
