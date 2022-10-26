import RPi.GPIO as GPIO
import time

BUZZER = 12
SW = [5,6,13,19]
Notes = [831,740,659,494]       # WestMinster Quarter 기본 악보

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(BUZZER,GPIO.OUT)
GPIO.setup(SW[0],GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(SW[1],GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(SW[2],GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(SW[3],GPIO.IN,pull_up_down=GPIO.PUD_DOWN)

p = GPIO.PWM(BUZZER,261)
p.start(50)

try:
    while True:
        p.start(0)                              # 듀티사이클 0으로 시작
        for i in range(4):
            if GPIO.input(SW[i]):               # 각 스위치에 입력이 들어오면 해당 주파수로 변경 후 듀티사이클을 50으로 설정하여 소리 재생
                p.ChangeFrequency(Notes[i])
                p.ChangeDutyCycle(50)
            while GPIO.input(SW[i]):continue    # 입력이 유지되는 동안에만 재생하고 입력이 없을땐 PWM stop
        p.stop()

except KeyboardInterrupt:
    pass

p.stop()
GPIO.cleanup()