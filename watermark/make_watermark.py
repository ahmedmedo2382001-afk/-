# يعمل صورة العلامة المائية (PNG شفافة) مرة واحدة
from PIL import Image, ImageDraw, ImageFont

FONT = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
LINES = [("عينة", 150), ("أحمد", 90), ("+201102134374", 80)]

def shape(t):
    # Pillow مع raqm بيظبط الحروف العربي واتجاهها لوحده
    return t

W, H = 1000, 520
img = Image.new("RGBA", (W, H), (0, 0, 0, 0))
d = ImageDraw.Draw(img)
y = 20
for text, size in LINES:
    font = ImageFont.truetype(FONT, size, layout_engine=ImageFont.Layout.RAQM)
    t = shape(text)
    w = d.textlength(t, font=font)
    # ظل أسود خفيف عشان العلامة تبان على الخلفيات الفاتحة والغامقة
    d.text(((W - w) / 2 + 4, y + 4), t, font=font, fill=(0, 0, 0, 160))
    d.text(((W - w) / 2, y), t, font=font, fill=(255, 255, 255, 255))
    y += size + 40
img = img.rotate(-15, expand=True, resample=Image.BICUBIC)
img.save("watermark.png")
print("watermark.png", img.size)
