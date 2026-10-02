"""시각 효과 컴포넌트 (Streamlit 내장 components.v2). 색은 :root 토큰(var)만, 움직임은 theme.MOTION.

- stat_tiles: StatTile(DESIGN §6.23) + 숫자 카운트업
- drone_hero: 홈 M01·M02 (research 4.3) — 링 파동, 완만한 부유, 클릭 시 P1~P5 펼침, ESC 접기
모든 움직임은 prefers-reduced-motion 과 사용자 '움직임 멈추기'(ui.motion)를 따른다.
"""
import streamlit as st

from core import export_mode, theme

_TILES_CSS = """
.tiles{display:grid;grid-template-columns:repeat(var(--cols),minmax(0,1fr));gap:var(--gutter);font-family:var(--font-sans)}
.tile{background:var(--surface);border-radius:var(--radius-md);padding:var(--space-lg);display:flex;flex-direction:column;gap:var(--space-xs);
  opacity:0;transform:translateY(var(--space-xs));animation:rise var(--rise) var(--ease-standard) forwards;
  transition:background var(--duration-base) var(--ease-standard),transform var(--duration-fast) var(--ease-standard)}
.tile:hover{background:var(--surface-2);transform:scale(var(--hover-scale))}
.tile:hover .value{color:var(--primary)}
.tile:nth-child(2){animation-delay:60ms}.tile:nth-child(3){animation-delay:120ms}.tile:nth-child(4){animation-delay:180ms}
.label{font:var(--font-label);letter-spacing:var(--type-label-ls);color:var(--text-2);margin:0}
.value{font:var(--font-data);letter-spacing:var(--type-data-ls);color:var(--text);margin:0;white-space:nowrap;transition:color var(--duration-fast) var(--ease-standard)}
.unit{font:var(--font-body);color:var(--text-2);margin-left:var(--space-xxs)}
.sub{font:var(--font-caption);color:var(--text-2);margin:0}
.tile.kpi{flex-direction:row;align-items:center;gap:var(--space-md);padding:var(--space-md) var(--space-lg)}
.ico{flex:none;width:var(--kpi-icon);height:var(--kpi-icon);border-radius:var(--radius-full);background:var(--accent-soft);display:grid;place-items:center}
.ico::before{content:"";width:var(--kpi-glyph);height:var(--kpi-glyph);background:var(--primary);
  -webkit-mask:var(--rest) center/contain no-repeat;mask:var(--rest) center/contain no-repeat}
.tile.kpi:hover .ico::before{-webkit-mask-image:var(--hover);mask-image:var(--hover)}
.kpi .label{font:var(--font-card-title);letter-spacing:0;color:var(--text)}
.kpi .value{font:var(--font-kpi);letter-spacing:var(--type-kpi-ls);color:var(--primary)}
.kpi--defense .ico{background:var(--defense-soft)}
.kpi--defense .ico::before{background:var(--defense-strong)}
.kpi--defense .value,.tile.kpi--defense:hover .value{color:var(--defense-strong)}
@keyframes rise{to{opacity:1;transform:none}}
@media (max-width:1024px){.tiles{grid-template-columns:repeat(2,minmax(0,1fr))}}
@media (max-width:767px){.tiles{grid-template-columns:1fr}}
@media (prefers-reduced-motion:reduce){.tile{animation:none;opacity:1;transform:none}.tile:hover{transform:none}}
"""

_TILES_JS = """
export default function(component) {
  const { data, parentElement } = component;
  let root = parentElement.querySelector('.tiles');
  if (!root) { root = document.createElement('div'); root.className = 'tiles'; parentElement.appendChild(root); }
  root.style.setProperty('--cols', data.cols);
  Object.entries(data.type_vars).forEach(([k, v]) => root.style.setProperty(k, v));   // 카드: 원래 글자 크기(요청 E1)
  root.style.setProperty('--rise', data.motion ? '400ms' : '0ms');
  root.innerHTML = '';
  const reduce = !data.motion || window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  const fmt = (v, d) => v.toLocaleString('ko-KR', {minimumFractionDigits: d, maximumFractionDigits: d});
  data.items.forEach((it) => {
    const el = document.createElement('div');
    el.className = it.icon ? 'tile kpi' + (it.tone === 'defense' ? ' kpi--defense' : '') : 'tile';   // tone defense = 빨강(요청 N1)
    const body = `<p class="label"></p><p class="value"><span class="num"></span><span class="unit"></span></p><p class="sub"></p>`;
    // 아이콘 카드(01 KPI, 요청 I1): 왼쪽 원 안 아이콘, 마우스를 올린 동안 움직임(움직임 끔이면 멈춘 그림만)
    el.innerHTML = it.icon ? `<span class="ico" aria-hidden="true"></span><div>${body}</div>` : body;
    if (it.icon) {
      const ico = el.querySelector('.ico');
      ico.style.setProperty('--rest', it.icon.rest);
      ico.style.setProperty('--hover', reduce ? it.icon.rest : it.icon.hover);
    }
    el.querySelector('.label').textContent = it.label;
    el.querySelector('.unit').textContent = it.unit || '';
    el.querySelector('.sub').textContent = it.sub || '';
    const num = el.querySelector('.num');
    root.appendChild(el);
    if (reduce) { num.textContent = fmt(it.value, it.decimals || 0); return; }
    const start = performance.now(), dur = data.duration;
    const step = (now) => {
      const p = Math.min(1, (now - start) / dur), e = 1 - Math.pow(1 - p, 3);   // cubic-out, 튀지 않음
      num.textContent = fmt(it.value * e, it.decimals || 0);
      if (p < 1) requestAnimationFrame(step);
    };
    requestAnimationFrame(step);
  });
}
"""

_tiles = st.components.v2.component("stat_tiles", css=_TILES_CSS, js=_TILES_JS)


def stat_tiles(items: list[dict], *, key: str, cols: int = 4) -> None:
    """items: {label, value, unit, decimals, sub, icon, tone}. 값은 계산된 실제 수치만. tone="defense" = 빨강 카드(요청 N1).
    icon(선택) = static/img/kpi_<icon>_rest/hover.webp 이름 — 있으면 아이콘 카드 모양(01 KPI, 요청 I1)."""
    items = [it | {"icon": {s: theme.img_uri(f"kpi_{it['icon']}_{s}") for s in ("rest", "hover")}} if it.get("icon") else it
             for it in items]
    _tiles(data={"items": items, "cols": cols, "motion": st.session_state["ui"]["motion"] and not export_mode.on(),
                 "duration": theme.MOTION["countup_ms"], "type_vars": theme.UNSCALED}, key=key)


_DRONE_SVG = """
<svg class="drone" viewBox="0 0 320 200" aria-hidden="true">
  <g class="body">
    <line x1="160" y1="100" x2="62" y2="58" class="arm"/><line x1="160" y1="100" x2="258" y2="58" class="arm"/>
    <line x1="160" y1="100" x2="62" y2="142" class="arm"/><line x1="160" y1="100" x2="258" y2="142" class="arm"/>
    <rect x="128" y="82" width="64" height="36" rx="12" class="hull"/>
    <circle cx="160" cy="100" r="7" class="lens"/>
    <rect x="146" y="118" width="28" height="12" rx="4" class="gimbal"/>
    <g class="rotor" style="transform-origin:62px 58px"><ellipse cx="62" cy="58" rx="40" ry="6" class="prop"/></g>
    <g class="rotor r2" style="transform-origin:258px 58px"><ellipse cx="258" cy="58" rx="40" ry="6" class="prop"/></g>
    <g class="rotor r2" style="transform-origin:62px 142px"><ellipse cx="62" cy="142" rx="40" ry="6" class="prop"/></g>
    <g class="rotor" style="transform-origin:258px 142px"><ellipse cx="258" cy="142" rx="40" ry="6" class="prop"/></g>
    <circle cx="62" cy="58" r="5" class="hub"/><circle cx="258" cy="58" r="5" class="hub"/>
    <circle cx="62" cy="142" r="5" class="hub"/><circle cx="258" cy="142" r="5" class="hub"/>
  </g>
</svg>
"""

_HERO_CSS = """
.hero{position:relative;height:var(--hero-h);background:var(--surface);border-radius:var(--radius-lg);overflow:hidden;
  font-family:var(--font-sans);color:var(--text)}
.core{position:absolute;left:50%;top:50%;width:var(--hero-drone-w-lg);height:var(--hero-drone-h-lg);transform:translate(-50%,-50%);border:0;padding:0;
  background:transparent;cursor:pointer;border-radius:var(--radius-lg);
  transition:width var(--duration-slide) var(--ease-standard),height var(--duration-slide) var(--ease-standard)}
.hero.open .core{width:var(--hero-drone-w);height:var(--hero-drone-h)}   /* 닫힘: 크게, 열림: 작게 + 메뉴 (요청 D9) */
.core:focus-visible{outline:var(--focus-w) solid var(--text);outline-offset:var(--space-xs)}
.ring{position:absolute;left:50%;top:50%;width:var(--hero-ring);height:var(--hero-ring);margin:calc(var(--hero-ring) / -2) 0 0 calc(var(--hero-ring) / -2);border-radius:50%;
  border:var(--card-border-w) solid var(--primary);opacity:0;pointer-events:none}
.hero.move .ring{animation:pulse 2s var(--ease-standard) infinite}
.hero.move .ring.b{animation-delay:1s}
.hero.open .ring{animation:none;opacity:0}
.drone{width:100%;height:100%;overflow:visible}
.hero.move .body{animation:float 4s ease-in-out infinite alternate}
.hero.move .rotor{animation:spin 0.6s linear infinite}.hero.move .rotor.r2{animation-direction:reverse}
.arm{stroke:var(--text-3);stroke-width:5;stroke-linecap:round}
.hull{fill:var(--surface-2);stroke:var(--text);stroke-width:2}
.lens{fill:var(--primary)}.gimbal{fill:var(--surface-2);stroke:var(--text-3);stroke-width:1.5}
.prop{fill:none;stroke:var(--text);stroke-width:2;opacity:.85}.hub{fill:var(--text)}
.core:hover .hull{stroke:var(--primary)}.core:hover .lens{fill:var(--primary-hover)}
.menu{position:absolute;inset:0;pointer-events:none}
.go{position:absolute;pointer-events:auto;display:flex;flex-direction:column;align-items:flex-start;gap:var(--space-xxs);
  min-width:var(--hero-entry-w);padding:var(--space-xs) var(--space-md);border-radius:var(--radius-md);cursor:pointer;
  background:var(--surface-2);border:none;color:var(--text);
  text-align:left;opacity:0;transform:scale(.96);transition:opacity var(--duration-base) var(--ease-standard),transform var(--duration-fast) var(--ease-standard),background var(--duration-fast) var(--ease-standard)}
.go:hover{background:var(--accent-soft);box-shadow:inset var(--indicator-w) 0 0 var(--primary)}
.hero.open .go:hover{transform:scale(var(--hover-scale))}
.hero.open .p5:hover{transform:translateX(-50%) scale(var(--hover-scale))}
.go:focus-visible{outline:var(--focus-w) solid var(--text);outline-offset:var(--indicator-w)}
.go b{font:var(--font-button);letter-spacing:0}
.go span{font:var(--font-caption);color:var(--text-2)}
.hero.open .go{opacity:1;transform:none}
.hero:not(.open) .go{visibility:hidden}
.p1{left:6%;top:12%}.p2{right:6%;top:12%}.p3{left:4%;bottom:14%}.p4{right:4%;bottom:14%}.p5{left:50%;bottom:4%;transform:translateX(-50%)}
.hero.open .p5{transform:translateX(-50%)}
.toggle{position:absolute;right:var(--space-md);top:var(--space-md);font:var(--font-caption);color:var(--text-2);
  background:var(--surface-2);border:none;border-radius:var(--radius-full);
  padding:var(--space-xxs) var(--space-sm);cursor:pointer}
.toggle:hover{color:var(--text)}
@keyframes pulse{0%{transform:scale(.55);opacity:.6}100%{transform:scale(1.7);opacity:0}}
@keyframes float{from{transform:translateY(calc(-1 * var(--space-xxs))) rotate(-1.2deg)}to{transform:translateY(var(--space-xxs)) rotate(1.2deg)}}
@keyframes spin{to{transform:rotate(360deg)}}
@media (max-width:767px){.hero{height:auto;padding-bottom:var(--space-md)}.core{position:relative;left:auto;top:auto;transform:none;margin:var(--space-lg) auto 0;display:block;width:calc(var(--hero-drone-w) * .8);height:calc(var(--hero-drone-h) * .8)}
  .ring{top:calc(var(--space-lg) + var(--hero-drone-h) * .4)}.menu{position:static;display:grid;grid-template-columns:1fr 1fr;gap:var(--space-xs);padding:var(--space-md)}
  .go{position:static;transform:none!important;min-width:0}.hero:not(.open) .menu{display:none}}
@media (prefers-reduced-motion:reduce){.hero .ring,.hero .body,.hero .rotor{animation:none!important}.go{transition:none}}
"""

_HERO_JS = """
export default function(component) {
  const { data, parentElement, setStateValue, setTriggerValue } = component;
  let hero = parentElement.querySelector('.hero');
  const fresh = !hero;
  if (fresh) {
    hero = document.createElement('div'); hero.className = 'hero';
    hero.innerHTML = `<span class="ring"></span><span class="ring b"></span>
      <button class="core" type="button" aria-expanded="false" aria-label="탐색 메뉴 열기">${data.svg}</button>
      <div class="menu"></div><button class="toggle" type="button"></button>`;
    parentElement.appendChild(hero);
  }
  const core = hero.querySelector('.core'), menu = hero.querySelector('.menu'), toggle = hero.querySelector('.toggle');
  menu.innerHTML = '';
  data.entries.forEach((e, i) => {
    const b = document.createElement('button'); b.type = 'button'; b.className = `go p${i + 1}`;
    b.innerHTML = '<b></b><span></span>'; b.querySelector('b').textContent = e.label; b.querySelector('span').textContent = e.desc;
    b.dataset.key = e.key;
    b.onclick = () => setTriggerValue('go', e.key);
    menu.appendChild(b);
  });
  const buttons = [...menu.querySelectorAll('.go')];
  const apply = (open) => {
    hero.classList.toggle('open', open);
    core.setAttribute('aria-expanded', String(open));
    core.setAttribute('aria-label', open ? '탐색 메뉴 접기' : '탐색 메뉴 열기');
    buttons.forEach((b) => b.tabIndex = open ? 0 : -1);
  };
  const setMotion = (on) => { hero.classList.toggle('move', on); toggle.textContent = on ? '움직임 멈추기' : '움직임 재생'; };
  // 처음 그릴 때만 저장된 상태를 적용한다. 클릭 뒤 재실행에서 받는 data는 한 박자 늦은 값이라
  // 다시 적용하면 방금 닫은 메뉴가 다시 열린다(요청 D8: 두 번째 클릭이 깜빡이기만 하던 원인).
  if (fresh) { apply(!!data.open); setMotion(!!data.motion); }
  core.onclick = () => { const open = !hero.classList.contains('open'); apply(open); setStateValue('open', open); };
  toggle.onclick = () => { const on = !hero.classList.contains('move'); setMotion(on); setStateValue('motion', on); };
  hero.onkeydown = (ev) => {
    if (ev.key === 'Escape' && hero.classList.contains('open')) { apply(false); setStateValue('open', false); core.focus(); }
  };
}
"""

_hero = st.components.v2.component("drone_hero", html="", css=_HERO_CSS, js=_HERO_JS)


def drone_hero(entries: list[dict], *, key: str = "drone_hero"):
    """entries: {key, label, desc}. 반환값의 go = 선택한 진입 키(트리거), open·motion = 현재 상태."""
    ui = st.session_state["ui"]
    return _hero(data={"svg": _DRONE_SVG, "entries": entries, "open": ui["home_menu_open"], "motion": ui["motion"]},
                 key=key, default={"open": ui["home_menu_open"], "motion": ui["motion"]},
                 on_open_change=lambda: None, on_motion_change=lambda: None, on_go_change=lambda: None)
