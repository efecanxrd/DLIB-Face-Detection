import cv2
import dlib

DLIBdetector = dlib.get_frontal_face_detector()
DLIBpredictor = dlib.shape_predictor("shape_68.dat")
capture = cv2.VideoCapture(0)

def node():
    _, frame = capture.read() 

    gray = cv2.cvtColor(src=frame, code=cv2.COLOR_BGR2GRAY) 
    faces = DLIBdetector(gray) 
    for face in faces: 
        x1 = face.left() 
        y1 = face.top() 
        x2 = face.right() 
        y2 = face.bottom() 
        landmarks = DLIBpredictor(image=gray, box=face) 
        for n in range(0,68): 
            x = landmarks.part(n).x 
            y = landmarks.part(n).y 
            cv2.circle(img=frame, center=(x,y), radius=2, color=(0,255,0),thickness=-1)
    
    cv2.imshow(winname="Cam",mat=frame) 

while True:
    node()
    if cv2.waitKey()== 27: 
        break

capture.release()
cv2.destroyAllWindows()