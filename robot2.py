import gpiod as g
import multiprocessing as m  
import time
from math import *
#from vision import *

# F B L R
orientations = {
    "R": 0,
    "F": 90,
    "L": 180,
    "B": 270
}

# control pins used for the left motor
ENA = 17
IN1 = 18
IN2 = 27

# control pins used for the right motor
ENB = 22
IN3 = 23
IN4 = 24

# control pins used for the servo
SPIN = 25

# frequency utilised by the PWM (pulse width modulation)
FREQ = 50

# frequency utilised by the vast majority of servo PWM control
SFREQ = 50

CONFIG = g.line_request()
CONFIG.request_type = g.line_request.DIRECTION_OUTPUT

class Robot:

    # opening /sys/class/gpio/gpiochip0 to enable Linux's control of the Raspberry Pi's GPIO pins
    h = g.chip(0)

    def n (self, args):
        pass

    def __init__ (self, x, y, orientation):
        self.x = x
        self.y = y
        self.orientation = orientation
        self.ENAPWM = m.Process(target=self.n, args=(10,))
        self.ENBPWM = m.Process(target=self.n, args=(10,))
        #self.vision = Vision()

        # exports the GPIO pins so that they may be used for output
        self.h.get_line(ENA).request(CONFIG)
        self.h.get_line(IN1).request(CONFIG)
        self.h.get_line(IN2).request(CONFIG)
        self.h.get_line(ENB).request(CONFIG)
        self.h.get_line(IN3).request(CONFIG)
        self.h.get_line(IN4).request(CONFIG)
        self.h.get_line(SPIN).request(CONFIG)
        
    
    # This function instructs the robot to move forwards utilising the "power" value
    # The power value is asserted to be between 0 & 1
    # The power is then used to compute the duty cycle of the PWM (pulse-width modulation)
    # The longer the duty cycle, the faster the motor spins
    def forward(self, power: float):
        assert (power <= 1 and power >= 0)
        self.stopPWM(ENA)
        self.ENAPWM = m.Process(target=self.setPWM, args=(ENA, FREQ, power * 0.9))
        self.ENAPWM.start()
        self.setValue(IN1, 1)
        self.setValue(IN2, 0)
        self.stopPWM(ENB)
        self.ENBPWM = m.Process(target=self.setPWM, args=(ENB, FREQ, power * 0.9))
        self.ENBPWM.start()
        self.setValue(IN3, 0)
        self.setValue(IN4, 1)
    
    # This utilises the same premise as the "forward()" function, however, reversing the direction of each motor
    def reverse(self, power: float):
        assert (power <= 1 and power >= 0)
        global ENAPWM, ENBPWM
        self.stopPWM(ENA)
        self.ENAPWM = m.Process(target=self.setPWM, args=(ENA, FREQ, power * 0.9))
        self.ENAPWM.start()
        self.setValue(IN1, 0)
        self.setValue(IN2, 1)
        self.stopPWM(ENB)
        self.ENBPWM = m.Process(target=self.setPWM, args=(ENB, FREQ, power * 0.9))
        self.ENBPWM.start()
        self.setValue(IN3, 1)
        self.setValue(IN4, 0)
    
    # This turn function instructs the robot the robot to turn with 50% of its full power
    # The boolean variable specifies if the robot is turning clockwise or counter-clockwise
    def turn (self, isClockwise: bool):
        global ENAPWM, ENBPWM
        if isClockwise:
            self.stopPWM(ENA)
            self.ENAPWM = m.Process(target=self.setPWM, args=(ENA, FREQ, 0.75))
            self.ENAPWM.start()
            self.setValue(IN1, 0)
            self.setValue(IN2, 1)
            self.stopPWM(ENB)
            self.ENBPWM = m.Process(target=self.setPWM, args=(ENB, FREQ, 0.75))
            self.ENBPWM.start()
            self.setValue(IN3, 0)
            self.setValue(IN4, 1)
        else:
            self.stopPWM(ENA)
            self.stopPWM(ENA)
            self.ENAPWM = m.Process(target=self.setPWM, args=(ENA, FREQ, 0.75))
            self.ENAPWM.start()
            self.setValue(IN1, 1)
            self.setValue(IN2, 0)
            self.stopPWM(ENB)
            self.ENBPWM = m.Process(target=self.setPWM, args=(ENB, FREQ, 0.75))
            self.ENBPWM.start()
            self.setValue(IN3, 1)
            self.setValue(IN4, 0)
    
    # causes the robot to stop
    def stop (self):
        self.setValue(IN1, 0)
        self.setValue(IN2, 0)
        self.setValue(IN3, 0)
        self.setValue(IN4, 0)
        self.stopPWM(ENA)
        self.stopPWM(ENB)

    # This utilises an encoded "programString" to direct the robot's movement using the key terms of
    # "FBLR" to stand for forward, back, left, & and right to dictate how the robot should move throught the
    # environment. This is paired with an implementation of the A* pathfinding algorithm which returns its path
    # in this string format.
    def follow (self, programString):
        secondsPerDegree = (1/(2*degrees(asin(9/18.25))))*2.25

        i = 0
        while i < len(programString):
            if programString[i-1 if i > 0 else 0] != programString[i] or self.getBearing() != orientations[programString[i]]:
                rotation = orientations[programString[i]] - self.getBearing()
                if rotation < 0:
                    self.turn(True)
                else:
                    self.turn(False)
                time.sleep(abs(rotation) * secondsPerDegree)
                self.orientation += rotation
                
            j = 1
            while i+j < len(programString) and programString[i] == programString[i+j]:
                j += 1
            
            self.forward(1)
            #startTime = time.time()
            #while time.time()-startTime <= j:
                #if self.vision.withinRange(0.1):
                    #self.stop()
                    #time.sleep(5)
                #else:
                    #self.forward(1)
            time.sleep(j)

            if programString[i] == "F":
                self.y -= j
            elif programString[i] == "B":
                self.y += j
            elif programString[i] == "L":
                self.x -= j
            else:
                self.x += j
            
            i += j

    def setValue (self, pin, value):
        # sets the value of specific pin
        self.h.get_line(pin).set_value(value)
        
    def setPWM (self, pin, freq, duty):
        assert (freq <= 100)

        while True:
            self.setValue(pin, 1)
            time.sleep(duty * 1/freq)
            self.setValue(pin, 0)
            time.sleep((1-duty) * 1/freq)
   
    def stopPWM (self, pin):
        if pin == ENA:
            self.ENAPWM.terminate()
        else:
            self.ENBPWM.terminate()

        self.setValue(pin, 0)
                        
        
        
    # returns the current position of the robot
    def getPosition (self):
        return [self.x, self.y]

    # returns the current bearing of the robot
    def getBearing (self):
        return self.orientation

