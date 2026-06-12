"""Strip the light background from the Infinara logo and build favicon set."""
from PIL import Image

SRC = r"C:\Users\Karta\OneDrive\Desktop\Infinara Ventures Tech Logo - Energy Impact.png"
OUT = r"C:\Users\Karta\OneDrive\Desktop\infinara-ventures\assets"

img = Image.open(SRC).convert("RGBA")
px = img.load()
w, h = img.size

# Background is a near-white/light-gray gradient; logo colors (navy/blue/green)
# are all saturated or dark, so a luminance+saturation threshold is safe.
SOLID = 190   # >= fully transparent (bg gradient runs ~205-250)
SOFT = 172    # SOFT..SOLID = feathered edge
for y in range(h):
    for x in range(w):
        r, g, b, a = px[x, y]
        mx, mn = max(r, g, b), min(r, g, b)
        sat = mx - mn
        if sat < 26:  # gray-ish only
            if mn >= SOLID:
                px[x, y] = (r, g, b, 0)
            elif mn >= SOFT:
                alpha = int(a * (SOLID - mn) / (SOLID - SOFT))
                px[x, y] = (r, g, b, alpha)

img.save(rf"{OUT}\infinara-logo.png")

# Crop the cube mark for the favicon (content bbox of the top ~62% of the image)
mark_region = img.crop((0, 0, w, int(h * 0.64)))
bbox = mark_region.getbbox()
mark = mark_region.crop(bbox)
# square-pad with margin
side = int(max(mark.size) * 1.12)
sq = Image.new("RGBA", (side, side), (0, 0, 0, 0))
sq.paste(mark, ((side - mark.width) // 2, (side - mark.height) // 2), mark)

sq.resize((512, 512), Image.LANCZOS).save(rf"{OUT}\infinara-mark-512.png")
sq.resize((180, 180), Image.LANCZOS).save(rf"{OUT}\apple-touch-icon.png")
sq.resize((32, 32), Image.LANCZOS).save(rf"{OUT}\favicon-32.png")
sq.resize((16, 16), Image.LANCZOS).save(rf"{OUT}\favicon-16.png")
sq.resize((256, 256), Image.LANCZOS).save(
    r"C:\Users\Karta\OneDrive\Desktop\infinara-ventures\favicon.ico",
    sizes=[(16, 16), (32, 32), (48, 48), (64, 64)],
)

# Also keep full transparent logo bbox-trimmed
full_bbox = img.getbbox()
img.crop(full_bbox).save(rf"{OUT}\infinara-logo.png")
print("done", img.size, "mark:", mark.size)
