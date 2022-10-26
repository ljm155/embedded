from asyncore import loop
from inspect import _void
import RPi.GPIO as GPIO
import time

SW = [5,6,13,19]

PWMA = 18
PWMB = 23
AIN1 = 22
AIN2 = 27
BIN1 = 25
BIN2 = 24

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

try:
    while True:
        for i in range (4):
            if GPIO.input(SW[i]):                   # 스위치에 입력이 들어오면 각 스위치에 해당하는 동작 실행
                motor(SW[i])
                print('SW',i+1)
                while GPIO.input(SW[i]):continue    # 스위치를 누르고 있는 동안에만 동작되도록 해줌
            else:                                   # 스위치에서 손을 뗐을 때 바퀴가 모두 정지함
                GPIO.output(AIN1,0)
                GPIO.output(AIN2,1)
                GPIO.output(BIN1,0)
                GPIO.output(BIN2,1)
                L_Motor.ChangeDutyCycle(0)
                R_Motor.ChangeDutyCycle(0)

except KeyboardInterrupt:
    pass

GPIO.cleanup()