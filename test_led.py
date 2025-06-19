import os

def run() :
    allow_try = 0
    cmd = ""
    ledChk = 0
    # TODO Home path 적기
    HOMEPATH = "" 
    
    while True:
        if ledChk == 0:
            os.system(HOMEPATH + "/led_src/y_led_on.run")
            ledChk = 1
        else :
            ledChk = 0
            os.system(HOMEPATH + "/led_src/y_led_off.run")

        if allow_try == 50:
            cmd = "none"
            print('다름')
            break
        confidence = int(input("test: "))
        if confidence > 76:
            print("unlock")
            cmd = "pass"
            break
        else:
         #75 이하면 타인.. Locked!!!
            print("lock")
            allow_try += 1

        allow_try += 1
        print(allow_try)

    os.system(HOMEPATH + "/led_src/fron_door.run " + cmd)

    if ledChk == 1:
        os.system(HOMEPATH + "/led_src/y_led_off.run")
        
if __name__ == "__main__":
    #if isNull() == 0 :
        # 학습 시작
    #    models = trains()
    #else :
        # 학습 모델 가져오기
     #   models = importModel()

    # 얼굴인식
    run()