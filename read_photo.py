import cv2
import pytesseract

# Tesseract'ın kurulu olduğu yolu belirt
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'  # Tesseract yolunu güncelle

# Görüntüyü yükle
image_path = 'sayi_goruntusu2.png'
img = cv2.imread(image_path)

# Görüntüyü gri tonlamaya çevir
#gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Görüntüdeki gürültüyü azaltmak için Gaussian Blur uygulayabiliriz
#blurred = cv2.GaussianBlur(gray, (5, 5), 0)

# Threshold işlemi (görüntüyü daha net hale getirir)
_, thresh = cv2.threshold(img, 150, 255, cv2.THRESH_BINARY)

# Pytesseract ile OCR işlemi yap
metin = pytesseract.image_to_string(img, config='--psm 6')

# Konsola metni yazdır
print("Görüntüdeki metin:", metin)

# OCR işlemi yapılan resmi göster (isteğe bağlı)
cv2.imshow('Görüntü', thresh)
cv2.waitKey(0)
cv2.destroyAllWindows()














