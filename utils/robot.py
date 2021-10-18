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
ENA = 7
IN1 = 11
IN2 = 12

# control pins used for the right motor
ENB = 13
IN3 = 15
IN4 = 16

FREQ = 10000

class Robot:

    h = l.gpiochip_open(0)

    l.gpio_claim_output(h, ENA)
    l.gpio_claim_output(h, IN1)
    l.gpio_claim_output(h, IN2)
    l.gpio_claim_output(h, ENB)
    l.gpio_claim_output(h, IN3)
    l.gpio_claim_output(h, IN4)

    def __init__ (self, x, y, orientation):
        self.x = x
        self.y = y
        self.orientation = orientation
    
    # use a duty cycle of <= 90%
    def forward(self, power: float):
        assert (power <= 1 and power >= 0)
        l.tx_pwm(h, ENA, FREQ, power * 90)
        l.gpio_write(h, IN1, 1)
        l.gpio_write(h, IN2, 0)
        l.tx_pwm(h, ENB, FREQ, power * 90)
        l.gpio_write(h, IN3, 0)
        l.gpio_write(h, IN4, 1)
    
    def reverse(self, power: float):
        assert (power <= 1 and power >= 0)
        l.tx_pwm(h, ENA, FREQ, power * 90)
        l.gpio_write(h, IN1, 0)
        l.gpio_write(h, IN2, 1)
        l.tx_pwm(h, ENB, FREQ, power * 90)
        l.gpio_write(h, IN3, 1)
        l.gpio_write(h, IN4, 0)
    
    def turn (self, isClockwise: bool):
        if isClockwise:
            l.tx_pwm(h, ENA, FREQ, 45)
            l.gpio_write(h, IN1, 0)
            l.gpio_write(h, IN2, 1)
            l.tx_pwm(h, ENB, FREQ, 45)
            l.gpio_write(h, IN3, 0)
            l.gpio_write(h, IN4, 1)
        else:
            l.tx_pwm(h, ENA, FREQ, 45)
            l.gpio_write(h, IN1, 1)
            l.gpio_write(h, IN2, 0)
            l.tx_pwm(h, ENB, FREQ, 45)
            l.gpio_write(h, IN3, 1)
            l.gpio_write(h, IN4, 0)
    
    def stop (self):
        l.gpio_write(h, IN1, 0)
        l.gpio_write(h, IN2, 0)
        l.gpio_write(h, IN3, 0)
        l.gpio_write(h, IN4, 0)

    def follow (self, programString):
        spd = 0.01

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
            while programString[i] == programString[i+j] and i+j < len(programString):
                j += 1
            self.forward(1)
            time.sleep(j)
            i += j
        

    def getPosition (self):
        return [self.x, self.y]

    def getBearing (self):
        return self.orientation
