import cv2
import os

# Load bộ phát hiện khuôn mặt Haar Cascade
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

# Nhập tên người dùng
person_name = input("Nhập tên của bạn: ").strip()
person_path = os.path.join("faces_dataset", person_name)

# Tạo thư mục nếu chưa có
if not os.path.exists(person_path):
    os.makedirs(person_path)
    print(f"Thư mục {person_path} đã được tạo.")
# Mở wec
cap = cv2.VideoCapture(0)
count = 0  # Đếm số ảnh đã chụp

while True:
    ret, frame = cap.read()
    if not ret:
        break
    frame = cv2.flip(frame, 2)  # Lật ảnh theo trục dọc (1: ngang, 0: dọc, -1: cả hai)

    # Chuyển ảnh sang grayscale để nhận diện tốt hơn
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Phát hiện khuôn mặt
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5, minSize=(30, 30))

    for (x, y, w, h) in faces:
        roi_gray = gray[y:y+h, x:x+w]
        face_resized = cv2.resize(roi_gray, (100, 100))  # Resize về kích thước chuẩn

        # Lưu ảnh
        img_path = os.path.join(person_path, f"{count}.jpg")
        cv2.imwrite(img_path, face_resized)
        count += 1
        print(f"Lưu ảnh: {img_path}")

        # Vẽ hình chữ nhật quanh khuôn mặt
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # Hiển thị khung hình
    cv2.imshow("Face Capture", frame)

    # Thoát khi nhấn phím 'q' hoặc chụp đủ 50 ảnh
    if cv2.waitKey(1) & 0xFF == ord('q') or count >= 50:
        break

# Giải phóng tài nguyên
cap.release()
cv2.destroyAllWindows()
print("Hoàn thành thu thập dữ liệu!")
success = cv2.imwrite(img_path, face_resized)
if success:
    print(f"✅ Ảnh đã được lưu: {img_path}")
else:
    print(f"❌ Lỗi khi lưu ảnh: {img_path}")
if not os.path.exists(person_path):
    print(f"❌ Thư mục không tồn tại: {person_path}")
else:
    print(f"✅ Thư mục hợp lệ: {person_path}")
