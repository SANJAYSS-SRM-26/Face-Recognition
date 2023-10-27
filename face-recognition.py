import cv2
face_cascade = cv2.CascadeClassifier("D:/face-recognition/haarcascade_frontalface_default.xml")
video_cap = cv2.VideoCapture(0)
while True:
    ret, video_data = video_cap.read()
    if not ret:
        print("Error reading frame from the camera.")
        break
    col = cv2.cvtColor(video_data, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(col, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30), flags=cv2.CASCADE_SCALE_IMAGE)
    for (x, y, w, h) in faces:
        cv2.rectangle(video_data, (x, y), (x + w, y + h), (0, 255, 0), 2)
    cv2.imshow("face_recognition", video_data)
    if cv2.waitKey(10) == ord("a"):
        break
video_cap.release()
cv2.destroyAllWindows()
