import cv2
import glob

resized = []
i=0
for img in glob.glob("CompVision/sample_images/*.jpg"):
    n = cv2.imread(img)
    resize = cv2.resize(n,(100,100))
    i = i+1
    cv2.imshow(f"{i}",resize)
    cv2.waitKey()
    cv2.destroyAllWindows()
    cv2.imwrite("CompVision/resized_img/img"+f"_resized_{i}.jpg",resize)