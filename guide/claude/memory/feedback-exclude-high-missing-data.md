---
name: feedback-exclude-high-missing-data
description: "결측이 많은 컬럼/지표는 과감히 제외하고, 이전·이후 모든 작업에 같은 기준을 적용 (사용자 결정)"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 8f9ddce3-f30a-4126-9c1d-bc0b167e42bd
  modified: 2026-09-21T07:17:48.219Z
---

결측이 많은 데이터는 대체·보정하지 말고 **과감히 제외**한다. 기존 작업뿐 아니라 이후 작업에도 동일하게 적용.

**Why:** 드론 대시보드 작업에서 기획안의 "자격증 연계 과정 취업률 35.7% vs 20.7%"가 취업률 결측 91.5%(107/1,262건, 4개 기관)에 기대고 있음을 보여주자, 사용자가 이 방향을 명시적으로 선택했다.

**How to apply:** 컬럼 결측률 50% 이상 제외, 30~50%는 '주의' 배지 + 표본 n 표기, 0·평균으로 채우지 않음. 구현은 `testDash/core/quality.py`(audit/drop_excluded). 새 데이터가 들어와도 이 감사를 통과시킨 뒤 사용하고, 제외 목록은 화면·README에 근거와 함께 남긴다. [[project-drone-dashboard-testdash]]

main 프로젝트 적용(2026-09-30): 빈칸뿐 아니라 원본의 결측 표시 문자열(`공개정보 확인 불가` 등, `main/core/quality.py` MISSING_TOKENS)도 결측으로 센다. `불명`·`미공개`·`없음`은 범주라 세지 않는다. 합치는 파일은 한쪽 제외 시 양쪽 제외.
