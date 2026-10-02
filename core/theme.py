"""디자인 토큰의 단일 원천 — design/DESIGN.md (Green Deck, 2026-09-30).

모드 공통 값은 BASE, 라이트/다크별 값은 MODE. 모두 CSS 변수로 주입하며
views/components/static CSS는 var(--…)만 쓴다(값 리터럴 금지). 차트·표(iframe)는 color()로 실제 값을 받는다.
"""
import base64
import functools
from pathlib import Path

import streamlit as st

from core.config import ROOT

FONT_SANS = ('"Pretendard",-apple-system,BlinkMacSystemFont,"Apple SD Gothic Neo","Malgun Gothic",'
             'Arial,Helvetica,sans-serif')

# DESIGN §5 타이포: (size, line-height, weight, tracking)
TYPE = {
    "hero": ("64px", "72px", 800, "-0.03em"), "page-title": ("32px", "40px", 700, "-0.02em"),
    "section-title": ("24px", "32px", 700, "-0.01em"), "card-title": ("16px", "22px", 700, "0"),
    "chart-title": ("20px", "26px", 700, "-0.01em"),   # 차트 카드 제목(요청 F8: 카드 제목보다 크게)
    "body": ("14px", "22px", 400, "0"), "body-small": ("12px", "18px", 400, "0"),
    "label": ("11px", "16px", 700, "0.1em"), "caption": ("12px", "18px", 400, "0"),
    "nav": ("17px", "24px", 700, "0"), "data": ("28px", "34px", 700, "-0.02em"),
    "nav-no": ("19px", "24px", 800, "0"),        # 메뉴 번호(이름보다 살짝 크게, 요청 D2)
    "brand": ("22px", "28px", 800, "-0.02em"),   # 사이드바 서비스명(메뉴보다 크게, 요청 D1)
    "button": ("14px", "20px", 700, "0.05em"),
    "kpi": ("34px", "40px", 800, "-0.02em"),     # 01 KPI 카드 숫자(요청 I1, Proposed)
}

BASE = {
    "--font-sans": FONT_SANS,
    # 간격 (DESIGN §6.2)
    "--space-xxs": "4px", "--space-xs": "8px", "--space-sm": "12px", "--space-md": "16px", "--space-lg": "24px",
    "--space-xl": "32px", "--space-xxl": "48px", "--space-3xl": "64px", "--space-section": "40px",
    "--gutter": "24px", "--page-margin": "32px", "--container-max": "1600px",
    # 반경 (DESIGN §6.3)
    "--radius-xs": "2px", "--radius-sm": "4px", "--radius-md": "8px", "--radius-lg": "12px", "--radius-full": "9999px",
    # 레이아웃 (DESIGN §6.4)
    "--sidebar-w": "240px", "--roadmap-w": "260px", "--roadmap-w-compact": "240px", "--topbar-h": "56px",
    "--nav-item-h": "44px",       # 사이드바 메뉴 항목 높이(홈~04 동일, 요청 2026-09-30)
    "--nav-no-w": "36px",         # 번호·홈 아이콘 칸 폭(이름 시작 위치를 맞춤, 요청 D2)
    "--nav-icon": "22px",         # 홈 아이콘 크기(번호 글자 높이에 맞춤, 요청 D3)
    "--nav-sub-ratio": "0.7",
    "--preview-fade-h": "110px",  # 01 분야 미리보기 흐림 높이(약 2.5줄, 요청 I3)
    "--preview-blur": "3px",
    "--kpi-icon": "64px", "--kpi-glyph": "40px",   # 01 KPI 카드 아이콘 원·그림 크기(요청 I1, Proposed)
    "--holo-scan-opacity": "1",   # 02 3D 직무 네트워크 가로줄(홀로그램, 요청 M2, Proposed)
    "--note-btn-w": "200px",   # 04 비교 안내 상자 단추 폭(같은 폭, 요청 N9, Proposed)
    "--card-icon": "18px", "--picked-scale": "1.02", "--picked-glow": "18px",   # 카드 버튼 아이콘·선택 카드(요청 L, Proposed)
    "--faded-opacity": "0.45",   # 목표 직무와 관련 없는 카드(강조 ON, 요청 F5)     # 04 하위 메뉴 글꼴 = 상위 메뉴의 70% (요청 F7)
    "--control-h": "40px", "--button-h": "32px", "--button-pad-x": "32px",
    # 선·표시
    "--border-w": "1px", "--indicator-w": "3px", "--focus-w": "1px", "--card-border-w": "2px", "--badge-pad-y": "2px",
    "--measure": "640px",
    # 움직임 (DESIGN §10)
    "--ease-standard": "cubic-bezier(0.2,0,0,1)", "--duration-fast": "150ms", "--duration-base": "200ms",
    "--duration-slide": "300ms", "--hover-scale": "1.04", "--hover-lift": "-2px",
    # 방산 대조색 (DESIGN §12.1 빨강, 요청 F2 — 테마와 무관). 배지 글자는 진한 빨강 위 흰색(8.99:1)
    "--defense-strong": "#E22134", "--defense-deep": "#8E1B26", "--defense-candidate": "rgba(226,33,52,0.4)",
    "--on-defense": "#FFFFFF", "--defense-grad-start": "#8E1B26", "--defense-grad-end": "#E22134",
    # 홈 드론 (DESIGN §10, Proposed)
    "--hero-h": "380px", "--hero-drone-w": "300px", "--hero-drone-h": "190px", "--hero-ring": "220px",
    "--hero-entry-w": "168px",
    "--hero-drone-w-lg": "528px", "--hero-drone-h-lg": "330px",   # 메뉴를 열기 전 큰 드론 (요청 D9)
    # 그림자 (DESIGN §7 tooltip, §6.1 light level 3)
    "--shadow-tip": "0 4px 12px rgba(0,0,0,0.4)",
}
# 글꼴 크기 배율 (요청 E1): 본문 전체 1.2배. 사이드바·카드는 원래 크기(TYPE 그대로), 카드 제목만 1.2배.
FONT_SCALE = 1.2
SIDEBAR_ONLY = ("nav", "nav-no", "brand")          # 사이드바 전용 역할은 배율 없음
UNSCALED_SCOPES = ('section[data-testid="stSidebar"]', '[class*="st-key-card-"]')   # 원래 크기로 되돌리는 범위
SCALED_IN_CARDS = ("card-title",)


def _scaled(value: str, role: str) -> str:
    if role in SIDEBAR_ONLY:
        return value
    return f"{round(float(value.removesuffix('px')) * FONT_SCALE)}px"


def _type_vars(scaled: bool) -> dict[str, str]:
    out = {}
    for role, (size, lh, weight, ls) in TYPE.items():
        if scaled:
            size, lh = _scaled(size, role), _scaled(lh, role)
        out[f"--font-{role}"] = f"{weight} {size}/{lh} {FONT_SANS}"
        out[f"--type-{role}-size"], out[f"--type-{role}-lh"] = size, lh
        out[f"--type-{role}-weight"], out[f"--type-{role}-ls"] = str(weight), ls
    return out


BASE |= _type_vars(scaled=True) | {"--native-text": f"calc(0.875rem * {FONT_SCALE})"}   # Streamlit 기본 위젯 글자(0.875rem)
UNSCALED = {k: v for k, v in _type_vars(scaled=False).items()
            if not any(k.startswith((f"--font-{r}", f"--type-{r}-")) for r in SCALED_IN_CARDS)} | {"--native-text": "0.875rem"}

# DESIGN §4.1 다크(기본) · §4.2 라이트(스크린샷 추출) · §4.3 차트
MODE = {
    "dark": {
        "--bg": "#121212", "--sidebar-bg": "#181818", "--surface": "#181818", "--surface-2": "#282828",
        "--surface-3": "#333333", "--border": "#282828", "--text": "#FFFFFF", "--text-2": "#A7A7A7",
        "--text-3": "#B3B3B3", "--control": "#535353", "--outline": "#727272", "--primary": "#1DB954",
        "--primary-hover": "#1ED760", "--on-primary": "#000000", "--accent-soft": "rgba(29,185,84,0.16)",
        "--select-bg": "#FFFFFF", "--select-fg": "#000000", "--warning": "#F59B23", "--error": "#E22134",
        "--shadow-dialog": "none",
        "--chart-primary": "#1DB954", "--chart-highlight": "#53E076", "--chart-dim": "#2C5636",
        "--chart-track": "#282828", "--chart-grid": "rgba(255,255,255,0.06)", "--chart-axis": "#A7A7A7",
        "--chart-muted": "#535353", "--tip-bg": "#282828", "--tip-fg": "#FFFFFF",
        "--grad-start": "#15A448", "--grad-end": "#1ED760", "--grad-hover-start": "#1DB954", "--grad-hover-end": "#3BE477",
        "--chart-grad-start": "#15A448", "--chart-grad-end": "#1ED760",
        "--defense-soft": "rgba(226,33,52,0.16)", "--picked-shadow": "rgba(29,185,84,0.35)", "--holo-core": "rgba(29,185,84,0.10)", "--note-bg": "rgba(61,157,243,0.20)", "--note-fg": "#C7EBFF", "--note-hover": "rgba(61,157,243,0.25)", "--net-core": "#5CF294", "--net-major": "#2ECC6B", "--net-middle": "#22A556", "--net-job": "#53E076", "--holo-scan": "rgba(29,185,84,0.06)",   # 선택 카드 그림자(요청 L4)
    },
    "light": {
        "--bg": "#F9F6F5", "--sidebar-bg": "#F3F0EF", "--surface": "#FFFFFF", "--surface-2": "#F3F4F5",
        "--surface-3": "#FFFFFF", "--border": "#E5E2E1", "--text": "#121212", "--text-2": "#6B6B6B",
        "--text-3": "#3A3A3A", "--control": "#D1D1D1", "--outline": "#C0C0BE", "--primary": "#0A873A",
        "--primary-hover": "#0B7A35", "--on-primary": "#FFFFFF", "--accent-soft": "#E0EDE2",
        "--select-bg": "#121212", "--select-fg": "#FFFFFF", "--warning": "#F59B23", "--error": "#E22134",
        "--shadow-dialog": "0 4px 12px rgba(0,0,0,0.12)",
        "--chart-primary": "#0A873A", "--chart-highlight": "#0A873A", "--chart-dim": "#C2DAC9",
        "--chart-track": "#F3F0EF", "--chart-grid": "#EFEBEA", "--chart-axis": "#6B6B6B",
        "--chart-muted": "#D1D1D1", "--tip-bg": "#282828", "--tip-fg": "#FFFFFF",
        "--grad-start": "#04762F", "--grad-end": "#0A873A", "--grad-hover-start": "#036A2A", "--grad-hover-end": "#0B7A35",
        "--chart-grad-start": "#04762F", "--chart-grad-end": "#1AB050",
        "--defense-soft": "#FFE5E5", "--picked-shadow": "rgba(10,135,58,0.30)", "--holo-core": "rgba(10,135,58,0.07)", "--note-bg": "rgba(28,131,225,0.10)", "--note-fg": "#004280", "--note-hover": "rgba(28,131,225,0.12)", "--net-core": "#0B9A43", "--net-major": "#2BAE5C", "--net-middle": "#63C486", "--net-job": "#0A873A", "--holo-scan": "rgba(10,135,58,0.04)",   # 선택 카드 그림자(요청 L4)
    },
}

# 차트 치수 (DESIGN §8, §11.3)
CHART = {"row_h": 42, "bar_w": 22, "dim": 0.35, "glow": 12, "pad": 8, "pad_sm": 4, "value_gutter": 64,
         "label_w": 160, "heat_row_h": 28, "heat_extra": 48, "treemap_h": 320,
         "cell_radius": 4, "tree_alpha": (0.22, 0.62), "tile_radius": 6, "map_h": 460, "map_aspect": 0.85,
         # 직무 네트워크 (요청 F3): 노드 크기, 선택 시 확대/축소 배율, 흐림, 확대 비율, 높이
         "net_root": 46, "net_major": 30, "net_middle": 18, "net_job": 7, "net_focus_scale": 1.4, "net_dim_scale": 0.55,
         "net_dim_opacity": 0.18, "net_edge_on": 0.55, "net_zoom_major": 1.7, "net_zoom_middle": 2.6, "net_edge_ring": 0.96, "net_aspect": 1.35, "net_fan_deg": 170, "net_h": 420, "net_h_max": 720, "bar_max_w": 32, "bar_radius": 4, "spark_h": 72, "stroke": 2,
         "marker": 6, "tip_pad": [8, 12], "tip_radius": 4, "tip_font": 12}

MOTION = {"chart_enter_ms": 500, "chart_update_ms": 300, "easing": "cubicOut", "countup_ms": 900,
          "line_draw_ms": 1400}   # 선 그래프 왼쪽→오른쪽 그리기(요청 I2)

BASE_CSS = ROOT / "static" / "css" / "base.css"


def mode() -> str:
    return "light" if st.context.theme.type == "light" else "dark"   # 다크 우선 (DESIGN §1)


def tokens(m: str | None = None) -> dict[str, str]:
    return BASE | MODE[m or mode()]


def color(name: str, m: str | None = None) -> str:
    """이름으로 실제 값 조회(차트·iframe용). 예: color("chart-primary")."""
    return tokens(m)[f"--{name}"]


def px(role: str) -> int:
    """본문(배율 적용) 글자 크기 px — 차트·표 등 본문 요소용."""
    return int(_scaled(TYPE[role][0], role).removesuffix("px"))


@functools.cache
def _image_vars() -> dict[str, str]:
    """사이드바 홈 아이콘(make_home_icon.py)·카드 버튼 별·책갈피(make_card_icons.py, 요청 L)를 CSS 변수(data URI)로."""
    img = ROOT / "static" / "img"
    home = {f"--home-icon-{n}": f"url(data:image/webp;base64,{base64.b64encode((img / f'home_{n}.webp').read_bytes()).decode()})"
            for n in ("rest", "hover")}
    return home | {f"--card-{i}-{s}": img_uri(f"card_{i}_{s}") for i in ("star", "bookmark")
                   for s in ("rest", "hover", "on", "off")}


@functools.cache
def img_uri(name: str) -> str:
    """static/img/<name>.webp 를 CSS url(data URI)로 — 쓰는 화면에서만 넘긴다(01 KPI 아이콘, 요청 I1)."""
    return f"url(data:image/webp;base64,{base64.b64encode((ROOT / 'static' / 'img' / f'{name}.webp').read_bytes()).decode()})"


def inject_css() -> None:
    """토큰(:root 변수)과 static/css/base.css 를 매 실행 첫머리에 주입."""
    root = ";".join(f"{k}:{v}" for k, v in (tokens() | _image_vars()).items())
    unscaled = ";".join(f"{k}:{v}" for k, v in UNSCALED.items())
    st.html(f"<style>:root{{{root}}}\n{','.join(UNSCALED_SCOPES)}{{{unscaled}}}\n"
            f"{Path(BASE_CSS).read_text(encoding='utf-8')}</style>")
