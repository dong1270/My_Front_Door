# 참고 링크 : https://blog.naver.com/chandong83/221695462391

import cv2
import numpy as np
from os import listdir
from os.path import isdir, isfile, join
import time

face = cv2.CascadeClassifier('./data/haarcascades/haarcascade_frontalface_default.xml')

def train(name):
    data_path = 'sample/' + name + '/'
    face_pics = [f for f in listdir(data_path) if isfile(join(data_path, f))]
    
    Training_Data , Labels = [], []
    
    for i, files in enumerate(face_pics) :
        image_path =  data_path + face_pics[i]
        images = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
        
        if images is None :
            continue
        
        Training_Data.append(np.asarray(images, dtype=np.uint8))
        Labels.append(i)
        
    if len(Labels) == 0 :
        print('There is no data to train')
        return None
    
    Labels = np.asarray(Labels, dtype=np.int32)
    
    # create model
    model = cv2.face.LBPHFaceRecognizer.create()
    
    # running
    model.train(np.asarray(Training_Data), np.asarray(Labels))
    
    return model

def trains():
    data_path = 'sample'
    model_dirs = 'faces/'
    # 디렉토리 색출
    model_dirs = [f for f in listdir(data_path) if isdir(join(data_path, f))]
    
    # 학습 모델 저장할 디셔너리
    models = {}
    for model in model_dirs:
        print('model :' + model)
        # running start
        result = train(model)
        # 학습 실패 시
        if result is None :
            continue
        
        # 학습 모델 export
        result.write("./model/" + model + ".yml")
        
        models[model] = result
        
    return models


def face_detector(img, size = 0.5):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face.detectMultiScale(gray, 1.3, 5)
    
    if faces is ():
        return img, []
    for(x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h),(0, 255, 255), 2)
        roi = img[y: y+h, x: x+w]
        roi = cv2.resize(roi, (200, 200))
        
    return img, roi

def run(models) :
    cap = cv2.VideoCapture(1)
    allow_try = 0
    
    while True:
        #카메라로 부터 사진 한장 읽기 
        ret, frame = cap.read()
        # 얼굴 검출 시도 
        if allow_try == 200:
            print('다름')
            break
            
        image, face = face_detector(frame)
        
        try:            
            min_score = 999       #가장 낮은 점수로 예측된 사람의 점수
            min_score_name = ""   #가장 높은 점수로 예측된 사람의 이름
            
            #검출된 사진을 흑백으로 변환 
            face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)

            #위에서 학습한 모델로 예측시도
            for key, model in models.items():
                result = model.predict(face)                
                if min_score > result[1]:
                    min_score = result[1]
                    min_score_name = key
                    
            #min_score 신뢰도이고 0에 가까울수록 자신과 같다는 뜻이다.         
            if min_score < 500:
                # 0~100표시하려고 한듯 
                confidence = int(100*(1-(min_score)/300))
                
            #75 보다 크면 동일 인물로 간주해 UnLocked! 
            if confidence > 76:
                print("unlock: " + str(confidence))
                break
            else:
            #75 이하면 타인.. Locked!!!
                print("lock")
                allow_try += 1
        except:
            pass
        allow_try += 1
        print(allow_try)
        
    cv2.waitKey(1)
    
    cap.release()
    cv2.destroyAllWindows()
    
    
def exportsModel(models):
    filePath = open('./model/model.xml', 'w', encoding='UTF-8')
    
    # filePath.write('{ \n')
    for line in models :
        filePath.writelines(str(models[line]) + "\n")
        # print(models[line])
    # filePath.write('}')
    
    filePath.close()
    
def importModel() :
    model = {}
    key = 0
    
    data_path = './model/'
    model_dir = [f for f in listdir(data_path) if isfile(join(data_path, f))]
    
    for line in model_dir :
        value = cv2.face.LBPHFaceRecognizer.create()
        value.read(data_path + line)
        model[line] = value
        value.clear()
    
    return model

def isNull() :
    data_path = './model/'
    return len([f for f in listdir(data_path) if isfile(join(data_path, f))])

if __name__ == "__main__":
    models = trains()
    if isNull() == 0 :
        # 학습 시작
        models = trains()
    else :
        # 학습 모델 가져오기
        models = importModel()
        
    # 얼굴인식
    run(models)
