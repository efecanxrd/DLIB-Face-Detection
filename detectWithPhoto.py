import cv2
import dlib

detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

def node():
    frame = cv2.imread("nn.jpg")

    gray = cv2.cvtColor(src=frame, code=cv2.COLOR_BGR2GRAY) 
    faces = detector(gray) 
    for face in faces: 
        x1 = face.left() 
        y1 = face.top() 
        x2 = face.right() 
        y2 = face.bottom() 
        landmarks = predictor(image=gray, box=face) 
        for n in range(0,68): 
            x = landmarks.part(n).x 
            y = landmarks.part(n).y 
            cv2.circle(img=frame, center=(x,y), radius=2, color=(0,255,0),thickness=-1)
    cv2.imshow(winname="Cam",mat=frame) 

while True:
    node()
    if cv2.waitKey(delay=1)== 27: 
            break

cv2.destroyAllWindows()
exit()
