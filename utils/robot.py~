import lgpio as l
import time

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

# frequency utilised by the PWM (pulse width modulation)
FREQ = 10000

class Robot:

    # opening /dev/gpiochip0 to enable Linux's control of the Raspberry Pi's GPIO pins
    h = l.gpiochip_open(0)

    def __init__ (self, x, y, orientation):
        self.x = x
        self.y = y
        self.orientation = orientation

        # exports the GPIO pins so that they may be used for output
        l.gpio_claim_output(self.h, ENA)
        l.gpio_claim_output(self.h, IN1)
        l.gpio_claim_output(self.h, IN2)
        l.gpio_claim_output(self.h, ENB)
        l.gpio_claim_output(self.h, IN3)
        l.gpio_claim_output(self.h, IN4)
    
    # This function instructs the robot to move forwards utilising the "power" value
    # The power value is asserted to be between 0 & 1
    # The power is then used to compute the duty cycle of the PWM (pulse-width modulation)
    # The longer the duty cycle, the faster the motor spins
    def forward(self, power: float):
        assert (power <= 1 and power >= 0)
        l.tx_pwm(self.h, ENA, FREQ, power * 90)
        l.gpio_write(self.h, IN1, 1)
        l.gpio_write(self.h, IN2, 0)
        l.tx_pwm(self.h, ENB, FREQ, power * 90)
        l.gpio_write(self.h, IN3, 0)
        l.gpio_write(self.h, IN4, 1)
    
    # This utilises the same premise as the "forward()" function, however, reversing the direction of each motor
    def reverse(self, power: float):
        assert (power <= 1 and power >= 0)
        l.tx_pwm(self.h, ENA, FREQ, power * 90)
        l.gpio_write(self.h, IN1, 0)
        l.gpio_write(self.h, IN2, 1)
        l.tx_pwm(self.h, ENB, FREQ, power * 90)
        l.gpio_write(self.h, IN3, 1)
        l.gpio_write(self.h, IN4, 0)
    
    # This turn function instructs the robot the robot to turn with 50% of its full power
    # The boolean variable specifies if the robot is turning clockwise or counter-clockwise
    def turn (self, isClockwise: bool):
        if isClockwise:
            l.tx_pwm(self.h, ENA, FREQ, 75)
            l.gpio_write(self.h, IN1, 0)
            l.gpio_write(self.h, IN2, 1)
            l.tx_pwm(self.h, ENB, FREQ, 75)
            l.gpio_write(self.h, IN3, 0)
            l.gpio_write(self.h, IN4, 1)
        else:
            l.tx_pwm(self.h, ENA, FREQ, 75)
            l.gpio_write(self.h, IN1, 1)
            l.gpio_write(self.h, IN2, 0)
            l.tx_pwm(self.h, ENB, FREQ, 75)
            l.gpio_write(self.h, IN3, 1)
            l.gpio_write(self.h, IN4, 0)
    
    # causes the robot to stop
    def stop (self):
        l.gpio_write(self.h, IN1, 0)
        l.gpio_write(self.h, IN2, 0)
        l.gpio_write(self.h, IN3, 0)
        l.gpio_write(self.h, IN4, 0)

    # This utilises an encoded "programString" to direct the robot's movement using the key terms of
    # "FBLR" to stand for forward, back, left, & and right to dictate how the robot should move throught the
    # environment. This is paired with an implementation of the A* pathfinding algorithm which returns its path
    # in this string format.
    def follow (self, programString):
        spd = 0.2

        for i in range(len(programString)):
            if programString[i-1 if i > 0 else 0] != programString[i] or self.getBearing() != orientations[programString[i]]:
                rotation = orientations[programString[i]] - self.getBearing()
                if rotation < 0:
                    self.turn(True)
                else:
                    self.turn(False)
                time.sleep(abs(rotation) * spd)
                self.orientation += rotation
                
            j = 1
            while programString[i] == programString[i+j]:
                if i+j < len(programString) - 1:
                    j += 1
                else:
                    break
            self.forward(1)
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
        

    # returns the current position of the robot
    def getPosition (self):
        return [self.x, self.y]

    # returns the current bearing of the robot
    def getBearing (self):
        return self.orientation
