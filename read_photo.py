import cv2
import pytesseract
from PIL import Image

# Tesseract'ın kurulu olduğu yolu belirt
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'  # Tesseract yolunu güncelle

# Görüntüyü yükle
# Görüntüyü aç
image = Image.open('captcha.png')

# Görüntüyü işle (opsiyonel)
# image = image.convert('L')  # Gri tonlamaya çevir
# image = image.point(lambda x: 0 if x < 128 else 255, '1')  # İkili görüntüye dönüştür

# OCR uygula
text = pytesseract.image_to_string(image, config='--psm 10 --oem 3 -c tessedit_char_whitelist=0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ')

# Sonucu yazdır
print("Okunan metin:", text.strip())














