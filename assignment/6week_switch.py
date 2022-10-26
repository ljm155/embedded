import RPi.GPIO as GPIO
import time

SW = [5, 6, 13, 19]

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(SW[0],GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(SW[1],GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(SW[2],GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(SW[3],GPIO.IN,pull_up_down=GPIO.PUD_DOWN)

swNum = [0,0,0,0] # 각 스위치가 눌린 횟수 저장
swStatus=[0,0,0,0] # 스위치의 이전 상태 저장

try:
    while True:
        for i in range(4):
            if (swStatus[i]==0 and GPIO.input(SW[i])==1):   # 스위치가 0에서 1로 바뀔 때 눌린횟수를 증가하고 문장출력.
                swNum[i]+=1                                 # 스위치가 눌린 횟수 증가
                print("'SW",i+1,"click'",",",swNum[i])
                while GPIO.input(SW[i]):continue            # 스위치가 눌려있는동안 상태변화 x
            swStatus[i] = GPIO.input(SW[i])                 # 스위치의 현재상태 값을 이전상태에 저장
            time.sleep(0.01)                                # 채터링 방지를 위해 딜레이 10ms
except KeyboardInterrupt:
    pass

GPIO.cleanup()