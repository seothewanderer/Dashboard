"""하위 페이지 '기업 탐색' (plan.md 9.6, research 3.2·3.2.1·8.2): C01 분야 막대(01과 같은 계산)·근거 집단 →
결과 수 → 카드 10개 → '기업 더보기' 팝업. 집계 순서: 전체 필터 → 정렬 → 10개."""
from html import escape

import pandas as pd
import streamlit as st

from analytics import companies as C
from analytics.common import paginate, split_tags
from analytics.defense import GROUP_ORDER, TIER
from components import cards, charts, dialogs
from components.chart_card import chart_card
from components.search_box import search_box
from components.filters import (as_list, defense_status_line, defense_toggle, goal_status_line, goal_toggle,
                                handoff_banner, only_toggle, toggle_value)
from core import routing
from core.data_loader import load_table
from core.datasets import company_frame

TOP_N = 8
AREA, GROUP, POSTED, KEYWORD, SORT, MULTI = "co_area", "co_group", "co_posted", "co_kw", "co_sort", "co_multi"


def _convert_area() -> None:
    """단일 ↔ 여러 분야 전환 시 칩 값 형식(값 ↔ 목록)을 맞춘다."""
    cur = as_list(st.session_state.get(AREA))
    st.session_state[AREA] = cur if st.session_state[MULTI] else (cur[0] if cur else None)


def render() -> None:
    comp = company_frame()
    handoff = routing.consume_handoff("recruit.companies")
    if handoff:
        if handoff.get("area"):
            areas = handoff["area"]
            st.session_state[MULTI] = len(areas) > 1
            st.session_state[AREA] = areas if len(areas) > 1 else areas[0]
        st.session_state["co_ids"] = handoff.get("company_ids")
    ids = st.session_state.get("co_ids")
    if ids:
        name = comp.set_index("company_id").loc[ids[0], "company_name_normalized"]
        handoff_banner(f"'{escape(name)}' 기업에서 이동해 왔습니다", "co_clear_ids",
                       lambda: st.session_state.update({"co_ids": None}))

    multi = st.session_state.get(MULTI, False)
    f = C.CompanyFilters(area=as_list(st.session_state.get(AREA)), defense_group=as_list(st.session_state.get(GROUP)),
                         has_posting=bool(st.session_state.get(POSTED)), keyword=st.session_state.get(KEYWORD) or "")
    base = comp[comp.company_id.isin(ids)] if ids else comp

    with st.container(horizontal=True, vertical_alignment="bottom", key="co-filterbar"):
        # 키워드 = 검색 상자(요청 O2): 기업명·사업 분야·드론 세부 분야가 목록으로 뜨고, 목록에 없는 말도 검색
        search_box("키워드", comp["company_name_normalized"].tolist() + [a for ar in comp["areas"] for a in ar]
                   + [s for v in comp["drone_subfields"] for s in split_tags(v)],
                   key=KEYWORD, placeholder="예: 방제, 매핑, 안티드론 · 입력하거나 펼쳐서 찾기", width=320)
        st.toggle("수집 공고 연결됨", key=POSTED, help="검토 전 연결 후보를 포함합니다.")
        st.toggle("여러 분야 선택", key=MULTI, help="같은 분류 안에서는 '하나 이상'으로 합칩니다.",
                  on_change=_convert_area)
        defense_toggle()
        goal_on = goal_toggle()
    defense_status_line()

    counts = C.area_counts(base, f)
    left, right = st.columns([3, 2], gap="medium")
    with left:
        show_all = st.session_state.get("co_area_all", False)
        view = counts if show_all else counts.head(TOP_N)
        missing = [a for a in f.area if a not in set(view.business_category)]
        view = pd.concat([view, counts[counts.business_category.isin(missing)]])
        with chart_card("C01", title="분야별 기업·기관", subtitle="다른 조건 적용 · 분야 선택 전 분포", n=len(base),
                        table=counts.rename(columns={"business_category": "분야", "n": "기업·기관 수"})):
            opt, h = charts.hbar(view.business_category.tolist(), view.n.tolist(), selected=f.area,
                                 unit="개 기업·기관", tooltip_note="분야 간 중복 포함")
            charts.render(opt, "c01_area", h, on_click=lambda n: toggle_value(AREA, n, multi=multi))
            st.toggle(f"분야 더보기 (전체 {len(counts)}개)", key="co_area_all")
            st.pills("분야", counts.business_category.tolist(), key=AREA, label_visibility="collapsed",
                     selection_mode="multi" if multi else "single")
    with right:
        gc = C.group_counts(base, f)
        highlight = st.session_state["ui"]["highlight_defense"]
        with chart_card("C01G", title="방산 근거 집단", n=len(base),
                        subtitle="직접확인은 수집 자료 범위의 확인이며 공식 지정과 다릅니다",
                        table=gc.rename(columns={"defense_group": "집단", "n": "기업·기관 수"})):
            opt, h = charts.hbar(gc.defense_group.tolist(), gc.n.tolist(), selected=f.defense_group, unit="개",
                                 tiers=[TIER.get(g) for g in gc.defense_group], highlight=highlight)
            charts.render(opt, "c01_group", h, on_click=lambda n: toggle_value(GROUP, n, multi=True))
            st.pills("근거 집단", GROUP_ORDER, key=GROUP, selection_mode="multi", label_visibility="collapsed")

    # ---- 결과: 전체 필터 → 정렬 → 10개 ----
    result = C.filter_companies(base, f)

    # ---- C04 방산 관련 기업의 채용 공고 노출 (요청 F2) ----
    dfn = result[result.defense_group.map(lambda g: bool(TIER.get(g)))]
    if len(dfn):
        exposed = dfn[dfn.posting_count.gt(0)].sort_values(["posting_count", "company_name_normalized"],
                                                          ascending=[False, True])
        silent = dfn[dfn.posting_count.eq(0)].company_name_normalized.sort_values().tolist()
        with chart_card("C04", key="c04-exposure", n=len(dfn),
                        subtitle=f"방산 관련 기업 {len(dfn)}곳 중 수집 공고가 연결된 곳 {len(exposed)}곳",
                        table=dfn[["company_name_normalized", "defense_group", "posting_count"]].rename(columns={
                            "company_name_normalized": "기업·기관", "defense_group": "근거 집단", "posting_count": "연결 공고 수"})):
            if len(exposed):
                opt, h = charts.hbar(exposed.company_name_normalized.tolist(), exposed.posting_count.tolist(), unit="건",
                                     tiers=[TIER.get(g) for g in exposed.defense_group])
                charts.render(opt, "c04_bar", h)
            if silent:
                st.caption(f"수집 공고 0건 {len(silent)}곳: " + ", ".join(silent[:8]) + (" 외" if len(silent) > 8 else "")
                           + " · 수집 시점에 공고가 확인되지 않았다는 뜻이며 채용이 없다는 뜻은 아닙니다.")
    # 기업 카드는 펼치기 안(요청 L5): 기본 닫힘, 조건을 고르면 펼친 채로. 안에 '방산 관련만' 필터 토글
    DEF_ONLY = "companies_only_defense"
    if st.session_state.get(DEF_ONLY):
        result = result[result.defense_group.map(lambda g: bool(TIER.get(g)))]
    narrowed = len(result) < len(base) or bool(st.session_state.get(DEF_ONLY))
    with st.expander(f"기업 카드 보기 · {len(result):,}개", expanded=narrowed):
        only_toggle(DEF_ONLY, "방산 관련만 보기", "defense", "방산 근거가 있는 기업·기관 카드만 봅니다. 위 그래프는 그대로입니다.")
        mode = st.segmented_control("정렬", ["auto", "name"], key=SORT, default="auto", required=True,
                                    format_func={"auto": "자동(방산 근거 우선)", "name": "이름순"}.get)
        ranked = C.sort_companies(result, f, mode or "auto")
        if goal_on:                                       # 목표 직무 관련 강조(요청 F5)
            goal = st.session_state["plan"]["goal_job_id"]
            ranked = ranked.assign(goal_reason=C.goal_reasons(ranked, {"job_id": goal},
                                                              load_table("bridge_application_job_bridge")))
            goal_status_line(int(ranked.goal_reason.notna().sum()), len(ranked))
        first, total = paginate(ranked, 0)
        note = " · 선택 결과 안에서 원문 직접확인 → 교차출처 → 인접 후보 → 미확인 순, 우수성·채용 순위 아님" \
            if C.is_sorted_by_defense(f, mode or "auto") else " · 이름순"
        st.html(f'<p class="result-count">조건에 맞는 기업·기관 <b>{total}</b>개 · 현재 1~{len(first)}{escape(note)}</p>')
        cards.grid(first, cards.company_card)
        if total == 0:
            st.info("조건에 맞는 기업이 없습니다. 필터를 해제해 보세요.")
        if total > 10:
            st.session_state["_company_ranked"] = ranked

            def _more():
                st.session_state["page"]["companies"]["more_page"] = 1
                dialogs.open_dialog("company_list", None)

            st.button(f"기업 더보기 (11~{min(20, total)}번째부터)", key="co_more", icon=":material/expand_more:",
                      on_click=_more)
