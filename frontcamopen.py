import cv2

# VideoCapture objesini oluşturun
cap = cv2.VideoCapture(0)

# Kamera başarıyla açılırsa devam edin
if not cap.isOpened():
    print("Hata: Kamera açılamadı.")
else:
    # Sonsuz bir döngüde kameradan görüntü alın
    while True:
        # Kameradan bir kare okuyun
        ret, frame = cap.read()

        # Eğer kare okunamazsa döngüyü sonlandırın
        if not ret:
            print("Hata: Kare okunamadı.")
            break

        # Görüntüyü ekranda gösterin
        cv2.imshow("Kamera", frame)

        # Klavyeden 'q' tuşuna basıldığında döngüyü sonlandırın
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

# Kullanılan kaynakları serbest bırakın
cap.release()

# Pencereyi kapatın
cv2.destroyAllWindows()
