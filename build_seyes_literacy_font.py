"""
build_seyes_literacy_font.py
Tailors Andika Literacy font specifically for French Séyès ruled paper:
- Small letters without stems (a, c, e, o...): x-height = 1040 (1 green line up = 1 interligne)
- All capital letters (A-Z): reach exactly 2080 (2 green lines up = 2 interlignes)
- Small letters that are more than one line up (b, d, f, h, k, l, t): reach exactly 2080 (2 green lines up = 2 interlignes)
- Small letters with descenders (g, j, p, q, y): descenders reach exactly -1040 (1 interligne below baseline)
"""

import os
from fontTools.ttLib import TTFont
from fontTools.ttLib.tables._g_l_y_f import GlyphCoordinates

def build_font(font_path: str):
    print(f"Opening font {font_path}...")
    font = TTFont(font_path)
    glyf = font['glyf']
    cmap = font.getBestCmap()
    hmtx = font['hmtx']
    os2 = font['OS/2']

    X_HEIGHT = 1040
    TARGET_2_LINES = 2080   # Exactly 2 interlines above baseline
    TARGET_DESC = -1040     # Exactly 1 interline below baseline

    # Update OS/2 table metrics
    os2.sxHeight = X_HEIGHT
    os2.sCapHeight = TARGET_2_LINES
    os2.sTypoAscender = TARGET_2_LINES
    os2.sTypoDescender = TARGET_DESC

    # 1. Transform Ascenders: b, d, f, h, k, l, t
    ascender_chars = ['b', 'd', 'f', 'h', 'k', 'l', 't', 'thorn', 'eth']
    for ch in ascender_chars:
        gname = ch if ch in glyf else cmap.get(ord(ch) if len(ch) == 1 else -1)
        if not gname or gname not in glyf:
            continue
        g = glyf[gname]
        if g.isComposite():
            continue
        coords, endPts, flags = g.getCoordinates(glyf)
        cur_max = max(pt[1] for pt in coords)
        if cur_max > X_HEIGHT:
            new_coords = []
            for x, y in coords:
                if y > X_HEIGHT:
                    # stretch the stem from X_HEIGHT up to TARGET_2_LINES
                    new_y = X_HEIGHT + (y - X_HEIGHT) * (TARGET_2_LINES - X_HEIGHT) / (cur_max - X_HEIGHT)
                else:
                    new_y = y
                new_coords.append((x, int(round(new_y))))
            g.coordinates = GlyphCoordinates(new_coords)
            g.yMax = max(pt[1] for pt in new_coords)
            g.yMin = min(pt[1] for pt in new_coords)
            print(f"  ✓ Transformed ascender '{ch}' ({gname}): new yMax = {g.yMax}")

    # 2. Transform Descenders: p, q, g, j, y and variants
    descender_chars = ['p', 'q', 'g', 'j', 'y', 'g.SngBowl']
    for ch in descender_chars:
        gname = cmap.get(ord(ch)) if len(ch) == 1 and ord(ch) in cmap else ch
        if not gname or gname not in glyf:
            continue
        g = glyf[gname]
        if g.isComposite():
            continue
        coords, endPts, flags = g.getCoordinates(glyf)
        cur_min = min(pt[1] for pt in coords)
        if cur_min < 0:
            new_coords = []
            for x, y in coords:
                if y < 0:
                    new_y = y * abs(TARGET_DESC) / abs(cur_min)
                else:
                    new_y = y
                new_coords.append((x, int(round(new_y))))
            g.coordinates = GlyphCoordinates(new_coords)
            g.yMax = max(pt[1] for pt in new_coords)
            g.yMin = min(pt[1] for pt in new_coords)
            print(f"  ✓ Transformed descender '{ch}' ({gname}): new yMin = {g.yMin}")

    # 3. Transform ALL Capital letters A-Z
    cap_chars = [chr(c) for c in range(ord('A'), ord('Z')+1)]
    for ch in cap_chars:
        gname = cmap.get(ord(ch))
        if not gname or gname not in glyf:
            continue
        g = glyf[gname]
        if g.isComposite():
            continue
        coords, endPts, flags = g.getCoordinates(glyf)
        cur_max = max(pt[1] for pt in coords)
        cur_min = min(pt[1] for pt in coords)
        if cur_max > 0:
            scale_y = TARGET_2_LINES / cur_max
            # Proportional x scale so capitals retain natural harmonious proportions
            scale_x = 1.25
            new_coords = []
            for x, y in coords:
                new_y = int(round(y * scale_y))
                new_x = int(round(x * scale_x))
                new_coords.append((new_x, new_y))
            g.coordinates = GlyphCoordinates(new_coords)
            g.yMax = max(pt[1] for pt in new_coords)
            g.yMin = min(pt[1] for pt in new_coords)
            g.xMax = max(pt[0] for pt in new_coords)
            g.xMin = min(pt[0] for pt in new_coords)

            # Update advance width in hmtx
            adv, lsb = hmtx[gname]
            hmtx[gname] = (int(round(adv * scale_x)), int(round(lsb * scale_x)))
            print(f"  ✓ Transformed capital '{ch}' ({gname}): new yMax = {g.yMax}")

    # 4. Adjust Accents in Composite Capitals (e.g. Agrave, Eacute, Egrave, Circumflex)
    for gname in glyf.keys():
        g = glyf[gname]
        if g.isComposite():
            # Check if this composite has a capital letter as its base
            base_is_cap = False
            for comp in g.components:
                if comp.glyphName in [cmap.get(ord(c)) for c in cap_chars if cmap.get(ord(c))]:
                    base_is_cap = True
                    break

            if base_is_cap:
                for comp in g.components:
                    # If this component is the accent positioned above
                    if comp.glyphName not in [cmap.get(ord(c)) for c in cap_chars if cmap.get(ord(c))]:
                        if comp.y >= 300:
                            comp.y += (TARGET_2_LINES - 1460)  # +620 font units
                            comp.x = int(round(comp.x * 1.25))

    font.save(font_path)
    print(f"Successfully saved Séyès Literacy Font to {font_path}!")

if __name__ == "__main__":
    target = os.path.join(os.path.dirname(__file__), "assets", "fonts", "Andika-Regular.ttf")
    build_font(target)
