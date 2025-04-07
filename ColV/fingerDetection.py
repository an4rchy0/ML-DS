import cv2
from cvzone.HandTrackingModule import HandDetector

# Inisialisasi detektor tangan
detector = HandDetector(detectionCon=0.8, maxHands=2)

# Membuka kamera
cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Mendeteksi tangan
    hands, img = detector.findHands(frame)

    # Menampilkan gambar dengan deteksi tangan
    cv2.imshow('Hand Detection', img)

    # Keluar dengan menekan tombol 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Menutup kamera dan jendela
cap.release()
cv2.destroyAllWindows()
