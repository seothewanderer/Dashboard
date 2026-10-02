"""홈 (plan.md 9.1, research 4.3): M01 제목 → M02 드론 진입 → M03 데이터 오버뷰 → M04 이용 안내."""
from html import escape

import streamlit as st

from analytics.overview import overview
from components.effects import drone_hero, stat_tiles
from content.page_intros import HOME_SUBTITLE, HOME_TITLE
from content.usage_guide import FAQ, STEPS
from core import routing
from core.data_loader import load_table

# M02 (research 4.3): 진입 키, 표시, 한 줄 설명
ENTRIES = [
    {"key": "industry", "label": "P1 산업 이해", "desc": "활용 분야와 산업 규모 살펴보기"},
    {"key": "jobs", "label": "P2 직무 탐색", "desc": "하는 일과 필요한 기술 알아보기"},
    {"key": "learning", "label": "P3 준비 역량", "desc": "배울 기술과 교육 찾아보기"},
    {"key": "recruit.postings", "label": "P4 채용 공고", "desc": "직무·지역별 공고 조건 확인하기"},
    {"key": "recruit.companies", "label": "P5 기업 탐색", "desc": "관심 분야의 기업과 사업 알아보기"},
]


def _go(entry_key: str) -> None:
    page, _, sub = entry_key.partition(".")
    routing.go(page, sub=sub or None)


st.html(f'<header class="home-hero"><h1 class="home-hero__title">{escape(HOME_TITLE)}</h1>'
        f'<p class="home-hero__subtitle">{escape(HOME_SUBTITLE)}</p></header>')

# ---- M01·M02 드론 ----
hero = drone_hero(ENTRIES)
st.session_state["ui"]["home_menu_open"] = bool(hero.open)
st.session_state["ui"]["motion"] = bool(hero.motion)
if hero.go:
    _go(hero.go)
with st.expander("탐색 메뉴를 버튼으로 열기"):     # 드론을 쓸 수 없을 때의 대체 경로(research 4.3)
    with st.container(horizontal=True, key="home-entries"):
        for e in ENTRIES:
            if st.button(e["label"], key=f"home_{e['key'].replace('.', '_')}", help=e["desc"]):
                _go(e["key"])

# ---- M03 오버뷰 ----
ov = overview({n: load_table(n) for n in ["industry_size", "jobs", "job_skills", "courses", "offerings", "postings",
                                          "org"]})
st.html('<h2 class="section-title">이 대시보드에서 볼 수 있는 것</h2>')
stat_tiles([
    {"label": "산업의 범위 · 전국 통계", "value": ov["industry"]["companies"], "unit": "개 업체",
     "sub": f"{ov['industry']['year']}년 종사자 {ov['industry']['employees']:,}명"},
    {"label": "살펴볼 직무 · 사전", "value": ov["jobs"]["jobs"], "unit": "개 직무",
     "sub": f"직무–기술 관계 {ov['jobs']['relations']:,}개 · 현재 채용 직업 수 아님"},
    {"label": "찾아볼 학습 기회 · 고용24", "value": ov["learning"]["courses"], "unit": "개 과정",
     "sub": f"회차 {ov['learning']['offerings']:,}개 · 모집 상태 미확인"},
    {"label": "확인할 공고 · 수집 표본", "value": ov["recruit"]["postings"], "unit": "건 공고",
     "sub": f"탐색 조직 {ov['recruit']['orgs']:,}개(DART 보강 {ov['recruit']['dart']}개) · 서로 더하지 않음"},
], key="m03_tiles")
cols = st.columns(4)
for col, (label, page, sub) in zip(cols, [("산업 보기", "industry", None), ("직무 보기", "jobs", None),
                                          ("교육 보기", "learning", None), ("공고 보기", "recruit", "postings")]):
    if col.button(label, key=f"m03_{label}", icon=":material/arrow_forward:", width="stretch"):
        routing.go(page, sub=sub)
if cols[3].button("기업 보기", key="m03_기업", icon=":material/arrow_forward:", width="stretch"):
    routing.go("recruit", sub="companies")
st.caption(f"산업 매출 {ov['industry']['revenue_100m']:,.2f}억원({ov['industry']['year']}년, 세부표 합계). "
           "전국 산업 통계와 수집 표본은 서로 다른 자료입니다.")

# ---- M04 이용 안내 ----
st.html('<h2 class="section-title" id="guide">이렇게 이용해 보세요</h2>')
step_cols = st.columns(3)
for col, (no, title, body) in zip(step_cols, STEPS):
    col.html(f'<div class="guide-step"><span class="guide-step__no">{no}</span><p class="guide-step__title">'
             f'{escape(title)}</p><p class="guide-step__body">{escape(body)}</p></div>')
for q, a in FAQ:
    with st.expander(q):
        st.write(a)
