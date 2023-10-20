import cv2


def video():
    video = cv2.VideoCapture(0)
    first_frame = None
    while(True):
        check, frame = video.read()
        gray_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        gray_img = cv2.GaussianBlur(gray_img, (21,21),0)

        if first_frame is None:
            first_frame = gray_img
            continue
        
        deltaFrame = cv2.absdiff(first_frame,gray_img)
        thresh_delta = cv2.threshold(deltaFrame,80,255, cv2.THRESH_BINARY)[1]
        thresh_delta = cv2.dilate(thresh_delta,None,iterations=2)

        (cnts,_)= cv2.findContours(thresh_delta.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        for contour in cnts:
            if cv2.contourArea(contour) < 1000:
                continue

            (x,y,w,h) = cv2.boundingRect(contour)
            cv2.rectangle(frame, (x,y), (x+w, y+h), (0,255,0), 3)
        
        cv2.imshow("Video", frame)
        cv2.imshow("Video2", thresh_delta)
        if cv2.waitKey(1) & 0xFF == ord('q'): 
            break
    
    video.release()
    cv2.destroyAllWindows

if __name__ == "__main__":
    video()