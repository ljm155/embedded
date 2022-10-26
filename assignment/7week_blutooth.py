import threading
import time
import serial
import RPi.GPIO as GPIO


bleSerial = serial.Serial("/dev/ttyS0", baudrate=9600, timeout=0.1)

gData=""

SW = [5,6,13,19]

PWMA = 18
PWMB = 23
AIN1 = 22
AIN2 = 27
BIN1 = 25
BIN2 = 24

# 자동차 셋팅
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(SW[0],GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(SW[1],GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(SW[2],GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(SW[3],GPIO.IN,pull_up_down=GPIO.PUD_DOWN)

GPIO.setup(PWMA,GPIO.OUT)
GPIO.setup(PWMB,GPIO.OUT)
GPIO.setup(AIN1,GPIO.OUT)
GPIO.setup(AIN2,GPIO.OUT)
GPIO.setup(BIN1,GPIO.OUT)
GPIO.setup(BIN2,GPIO.OUT)


L_Motor = GPIO.PWM(PWMA,500)
R_Motor = GPIO.PWM(PWMB,500)
L_Motor.start(0)
R_Motor.start(0)

def motor(sw): # 바퀴를 움직이는 함수
    if sw==5:                       # 전진(좌,우 앞으로)
        GPIO.output(AIN1,0)
        GPIO.output(AIN2,1)
        GPIO.output(BIN1,0)
        GPIO.output(BIN2,1)
        L_Motor.ChangeDutyCycle(100)
        R_Motor.ChangeDutyCycle(100)
    elif sw==6:                     # 우회전(좌 앞으로, 우 뒤로)
        GPIO.output(AIN1,0)
        GPIO.output(AIN2,1)
        GPIO.output(BIN1,1)
        GPIO.output(BIN2,0)
        L_Motor.ChangeDutyCycle(50)
        R_Motor.ChangeDutyCycle(50)
    elif sw==13:                    # 좌회전(좌 뒤로, 우 앞으로)
        GPIO.output(AIN1,1)
        GPIO.output(AIN2,0)
        GPIO.output(BIN1,0)
        GPIO.output(BIN2,1)
        L_Motor.ChangeDutyCycle(50)
        R_Motor.ChangeDutyCycle(50)
    elif sw==19:                    # 후진(좌,우 뒤로)
        GPIO.output(AIN1,1)
        GPIO.output(AIN2,0)
        GPIO.output(BIN1,1)
        GPIO.output(BIN2,0)
        L_Motor.ChangeDutyCycle(100)
        R_Motor.ChangeDutyCycle(100)
    elif sw==20:                    # 정지
        GPIO.output(AIN1,0)
        GPIO.output(AIN2,1)
        GPIO.output(BIN1,0)
        GPIO.output(BIN2,1)
        L_Motor.ChangeDutyCycle(0)
        R_Motor.ChangeDutyCycle(0)

def serial_thread():                # bt app에서 데이터를 읽어와 gData에 저장
    global gData
    while True:
        data = bleSerial.readline()
        data = data.decode()
        gData = data

def main():                         # 입력된 gData에 따라 자동차 구동
    global gData
    try:
        while True:
            if gData.find("go") >= 0:
                gData=""
                print("ok go")
                motor(5)
            elif gData.find("back") >= 0:
                gData=""
                print("ok back")
                motor(19)
            elif gData.find("left") >= 0:
                gData=""
                print("ok left")
                motor(13)
            elif gData.find("right") >= 0:
                gData=""
                print("ok right")
                motor(6)
            elif gData.find("stop") >= 0:
                gData=""
                print("ok stop")
                motor(20)

    except KeyboardInterrupt:
        pass

if __name__=='__main__':
    task1 = threading.Thread(target = serial_thread)
    task1.start()
    main()
    bleSerial.close()
    