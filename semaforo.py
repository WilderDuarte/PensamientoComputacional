# generated by mBlock5 for HaloCode
# codes make you happy

import event, halo, time
import time

@event.start
def on_start():
    while True:
      halo.led.show_all(94, 208, 1, 50)
      time.sleep(4)
      halo.led.show_all(255, 208, 0, 50)
      time.sleep(3)
      halo.led.show_all(208, 0, 0, 50)
      time.sleep(2)
