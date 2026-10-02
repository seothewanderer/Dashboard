"""01 산업 이해 KPI 카드 아이콘 만들기 (요청 I1, 2026-10-01).

원본 static/img/kpi_{company,revenue,employee}.gif(흰 바탕 검은 선)를 홈 아이콘(make_home_icon.py)과 같은 방식으로
색을 뺀 알파 마스크 WebP로 바꾼다. 색은 CSS(mask-image + 테마 초록)가 입혀 라이트/다크에 모두 맞는다.
- kpi_<이름>_rest.webp : 기본 상태 한 프레임(모양이 가장 다 보이는 프레임)
- kpi_<이름>_hover.webp: 그 프레임에서 시작해 한 바퀴 도는 움직임, 마우스를 올린 동안 반복
실행: .venv\\Scripts\\python.exe scripts\\make_kpi_icons.py
"""
from PIL import Image, ImageSequence

from core.config import ROOT

IMG = ROOT / "static" / "img"
SCALE = 4
# 이름: 기본 프레임 고르는 법 — max = 선이 가장 진한 프레임(매출 막대가 다 오른 때, 종사자 눈 뜬 때), 0 = 첫 프레임(창 불 모두 켜짐)
ICONS = {"company": 0, "revenue": "max", "employee": "max",
         "posting": 0, "shield": 0}   # 04 채용 현황 KPI(요청 N1): 종이 = 겹친 두 장, 방패 = 체크 방패 첫 프레임(요청 N8에서 GIF 교체)


def to_mask(frame: Image.Image) -> Image.Image:
    gray = frame.convert("L").resize((frame.width * SCALE, frame.height * SCALE), Image.NEAREST)
    out = Image.new("RGBA", gray.size, (0, 0, 0, 0))
    out.putalpha(gray.point(lambda v: 255 - v))     # 검은 선 = 불투명
    return out


def main() -> None:
    for name, rest in ICONS.items():
        frames = [(to_mask(f), f.info.get("duration", 40)) for f in ImageSequence.Iterator(Image.open(IMG / f"kpi_{name}.gif"))]
        ink = [sum(v * n for v, n in enumerate(f.getchannel("A").histogram())) for f, _ in frames]
        i = ink.index(max(ink)) if rest == "max" else rest
        frames[i][0].save(IMG / f"kpi_{name}_rest.webp", lossless=True)
        loop = frames[i:] + frames[:i]              # 기본 프레임에서 시작해 끊김 없이 이어지게
        loop[0][0].save(IMG / f"kpi_{name}_hover.webp", save_all=True, append_images=[f for f, _ in loop[1:]],
                        duration=[d for _, d in loop], loop=0, lossless=True)
        print(f"{name}: frames={len(frames)} rest={i}")


if __name__ == "__main__":
    main()
