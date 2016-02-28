import RPi.GPIO as GPIO
import time
from Adafruit_PWM_Servo_Driver import PWM

pwm = PWM( 0x60, debug=False)
pwm.setPWMFreq(1600)

GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)
# set mode to en/phase
GPIO.output(17, GPIO.HIGH)

in1 = 5
in2 = 4

in3 = 8
in4 = 9

in5 = 0
in6 = 1

in7 = 2
in8 = 3

in9 = 10
in10 = 11

in11 = 7
in12 = 6

# Test motor one
# phase is 8, enable = 9
pwm.setPWM(in1,0,0)
pwm.setPWM(in2,0,0)
pwm.setPWM(in3,0,0)
pwm.setPWM(in4,0,0)
pwm.setPWM(in5,0,0)
pwm.setPWM(in6,0,0)
pwm.setPWM(in7,0,0)
pwm.setPWM(in8,0,0)
pwm.setPWM(in9,0,0)
pwm.setPWM(in10,0,0)
pwm.setPWM(in11,0,0)
pwm.setPWM(in12,0,0)
time.sleep(2)
print "Set forward"
pwm.setPWM(in1,0,0)
pwm.setPWM(in2,0,4095)
pwm.setPWM(in3,0,0)
pwm.setPWM(in4,0,4095)
pwm.setPWM(in5,0,0)
pwm.setPWM(in6,0,4095)
pwm.setPWM(in7,0,0)
pwm.setPWM(in8,0,4095)
pwm.setPWM(in9,0,0)
pwm.setPWM(in10,0,4095)
pwm.setPWM(in11,0,0)
pwm.setPWM(in12,0,4095)
time.sleep(2)
print "stop"
pwm.setPWM(in1,0,0)
pwm.setPWM(in2,0,0)
pwm.setPWM(in3,0,0)
pwm.setPWM(in4,0,0)
pwm.setPWM(in5,0,0)
pwm.setPWM(in6,0,0)
pwm.setPWM(in7,0,0)
pwm.setPWM(in8,0,0)
pwm.setPWM(in9,0,0)
pwm.setPWM(in10,0,0)
pwm.setPWM(in11,0,0)
pwm.setPWM(in12,0,0)
time.sleep(2)
print "Set reverse"
pwm.setPWM(in1,0,4095)
pwm.setPWM(in2,0,4095)
pwm.setPWM(in3,0,4095)
pwm.setPWM(in4,0,4095)
pwm.setPWM(in5,0,4095)
pwm.setPWM(in6,0,4095)
pwm.setPWM(in7,0,4095)
pwm.setPWM(in8,0,4095)
pwm.setPWM(in9,0,4095)
pwm.setPWM(in10,0,4095)
pwm.setPWM(in11,0,4095)
pwm.setPWM(in12,0,4095)
time.sleep(2)
print "stop"
pwm.setPWM(in1,0,0)
pwm.setPWM(in2,0,0)
pwm.setPWM(in3,0,0)
pwm.setPWM(in4,0,0)
pwm.setPWM(in5,0,0)
pwm.setPWM(in6,0,0)
pwm.setPWM(in7,0,0)
pwm.setPWM(in8,0,0)
pwm.setPWM(in9,0,0)
pwm.setPWM(in10,0,0)
pwm.setPWM(in11,0,0)
pwm.setPWM(in12,0,0)


# cleanup
GPIO.cleanup()
