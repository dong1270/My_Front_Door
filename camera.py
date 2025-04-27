import cv2
import os
import time

def run(savePoint, name, i) :
    camera = cv2.VideoCapture(0)
    camera.set(3, 640)
    camera.set(4, 480)

    ret,frame = camera.read()
    if ret :
        time.sleep(5)
        frame = cv2.flip(frame, 1)
        cv2.imwrite(savePoint + name + "/" + "tests" + str(i) + ".jpg", frame)
    
        camera.release()
        cv2.destroyAllWindows()
    else :
        print("camera err")

def main():
    savePoint = './sample/'
    name = input("user name:")
    
    if not os.path.exists(savePoint + name) :
        os.mkdir(savePoint + name)
    
    for i in range(5):
        run(savePoint, name, i)
    
if __name__ == '__main__':
    main()