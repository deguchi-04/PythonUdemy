import cv2
import time 

def face_pic():
    face = cv2.CascadeClassifier("CompVision/faces/haarcascade_frontalface_default.xml")
    img = cv2.imread("CompVision/faces/news.jpg")
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face.detectMultiScale(gray_img, scaleFactor=1.1, minNeighbors=5)

    for x,y,w,h in faces:
        img = cv2.rectangle(img,(x,y), (x+w, y+h), (0,255,0),3)

    resized = cv2.resize(img, (int(img.shape[1]/3), int(img.shape[0]/3)))
    cv2.imshow("Show", resized)
    cv2.waitKey(0)
    cv2.destroyAllWindows

def video():
    video = cv2.VideoCapture(0)
    face = cv2.CascadeClassifier("CompVision/faces/haarcascade_frontalface_default.xml")
    while(True):
        check, frame = video.read()
        gray_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face.detectMultiScale(gray_img, scaleFactor=1.1, minNeighbors=5)
        for x,y,w,h in faces:
            frame = cv2.rectangle(frame,(x,y), (x+w, y+h), (0,255,0),3)

        cv2.imshow("Video", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'): 
            break
    
    video.release()
    cv2.destroyAllWindows

if __name__ == "__main__":
    video()