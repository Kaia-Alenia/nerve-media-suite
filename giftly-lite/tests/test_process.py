import sys
import os
sys.path.append('src')

from PIL import Image
print("Before main import, PIL registered formats:", getattr(Image, 'ID', None))
Image.init()
print("After init, PIL registered formats:", getattr(Image, 'ID', None))

from main import AleniaGiftlyLite

print("After main import, PIL registered formats:", getattr(Image, 'ID', None))

app = AleniaGiftlyLite()
app.path = '/media/alejandro/D/Pixelart/assets_pixelart'
app._process(320, 180, 2, 12, "NONE")
