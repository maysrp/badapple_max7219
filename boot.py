import max7219,json
import time
from machine import Pin, SPI
spi = SPI(1, baudrate=400000, polarity=1, phase=0, sck=Pin(4), mosi=Pin(2))
ss = Pin(5, Pin.OUT)
display = max7219.Matrix8x8(spi, ss, 16)
def image(img_list):
    st=time.ticks_ms()   
    display.fill(0)     
    for i in img_list:
        display.hline(32*(i[1]//8)+i[0],i[1]%8,i[2],1)
    display.show()
    c=time.ticks_ms()-st
    if c<100:
        time.sleep_ms(90-c)
with open('bad.data','r') as f:
    for i in f:
        try:
            z=json.loads(i)
            image(z)
        except Exception as e:
            pass
        gc.collect()
