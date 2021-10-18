import lgpio as l
import time

h = l.gpiochip_open(0)

l.gpio_claim_output(h, 17)
l.gpio_claim_output(h, 18)
l.gpio_claim_output(h, 27)

FREQ = 10000

try:
    while True:
        l.tx_pwm(h, 17, FREQ, 90)
        l.gpio_write(h, 18, 1)
        l.gpio_write(h, 27, 0)

        time.sleep(10)

        l.gpio_write(h, 18, 0)
        l.gpio_write(h, 27, 0)

        time.sleep(1)

        l.tx_pwm(h, 17, FREQ, 90)
        l.gpio_write(h, 18, 0)
        l.gpio_write(h, 27, 1)

        time.sleep(10)
except KeyboardInterrupt:
    l.gpio_write(h, 17, 0)
    l.gpio_write(h, 18, 0)
    l.gpio_write(h, 27, 0)
    l.gpiochip_close(h)