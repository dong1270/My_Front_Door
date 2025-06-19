import cv2
import os
import time

def run(savePoint, name, i) :
    data_path = 'sample/' + name + '/'
    face_pics = [f for f in os.listdir(data_path) if os.path.isfile(os.path.join(data_path, f))]
    
    file_cnt = len(face_pics)
    
    camera = cv2.VideoCapture(1)
    camera.set(3, 640)
    camera.set(4, 480)

    ret,frame = camera.read()
    if ret :
        time.sleep(0.5)
        frame = cv2.flip(frame, 1)
        cv2.imwrite(savePoint + name + "/" + name + "img" + str(file_cnt + i) + ".jpg", frame)

        print(savePoint + name + "/" + name + "img" + str(file_cnt + i) + ".jpg")
        camera.release()
        cv2.destroyAllWindows()
    else :
        print("camera err")

def main():
    savePoint = './sample/'
    name = input("user name:")
    
    if not os.path.exists(savePoint + name) :
        os.mkdir(savePoint + name)
    
    for i in range(20):
        run(savePoint, name, i)
    
if __name__ == '__main__':
    main()