import lgpio as l
import time

h = l.gpiochip_open(0)
l.gpio_claim_output(h, 11)

try:
    while True:
        l.gpio_write(h, 11, 1)
        time.sleep(1)
    
        l.gpio_write(h, 11, 0)
        time.sleep(1)
except KeyboardInterrupt:
    l.gpio_write(h, 11, 0)
    l.gpiochip_close(h)