# guide — 집(새 PC)에서 같은 개발 환경 만들기

2026-10-02 작성. 이 폴더는 개인 저장소(Dashboard) 전용이다. 팀 저장소(dashboard_team)에는 올리지 않는다.

| 파일 | 내용 |
|---|---|
| `setup.ps1` | Python 3.12 확인 → `.venv` 생성 → 패키지 설치(`requirements-lock.txt`) → 데이터 빌드 → 테스트. `-CopyClaude`를 붙이면 Claude 메모리·미리보기 설정도 복사 |
| `HANDOFF.md` | 인수인계: 지금까지의 결정, 대기 중인 질문, 다음 할 일, 주의점 |
| `claude/memory/` | Claude Code 메모리 복사본(작업 규칙·결정 기억) |
| `claude/launch.json` | 미리보기 서버 설정 복사본(원래 위치: `C:\Projects\Dashboard\.claude\launch.json`, 저장소 밖) |

## 순서

1. **Python 3.12.10 설치** (없을 때만)
   ```
   winget install --id Python.Python.3.12 -e --scope user
   ```
2. **같은 경로로 받기** — Claude 메모리 폴더 이름이 경로에서 정해지므로 `C:\Projects\Dashboard\main` 그대로
   ```
   git clone https://github.com/seothewanderer/Dashboard.git C:\Projects\Dashboard\main
   ```
3. **환경 준비 + Claude 설정 복사**
   ```
   cd C:\Projects\Dashboard\main
   powershell -ExecutionPolicy Bypass -File guide\setup.ps1 -CopyClaude
   ```
4. **실행 확인**: `.\run.ps1` → http://localhost:8501
5. **Claude Code**: `C:\Projects\Dashboard` 폴더에서 새 세션을 열고 "guide/HANDOFF.md 읽고 이어서 하자"라고 시작.

## 올리지 않은 것과 이유

- `.venv`(약 435MB): 이 PC 경로가 박혀 있어 다른 PC에서 동작하지 않음 → `setup.ps1`이 새로 만든다.
- 대화 기록 원본(약 62MB): 용량이 크고 모든 내용이 담겨 있음 → 대신 `HANDOFF.md`와 메모리로 이어 간다.
- html 공유본 파일(`html/*.html`): `scripts/build_interactive.py`로 다시 만든다.

## 저장소 규칙(요약)

- 작업은 항상 `main` 폴더에서. `main`은 개인 저장소(Dashboard)에만 연결.
- 팀 공유는 별도 폴더 `C:\Projects\Dashboard\team`(dashboard_team)으로만. 집에서 팀 작업이 필요하면 그때 따로 clone:
  `git clone https://github.com/seothewanderer/dashboard_team.git C:\Projects\Dashboard\team`
- 커밋은 Claude가, push는 사용자가 직접.
