from gpiozero import LED

class LED_Control:
    
    def __init__(self):
        self.green_led = LED(6)
        self.red_led = LED(26)
        
    def green_LED(self):
        if self.green_led.on:
            self.green_led.off()
        else:
            self.green_led.on()
        
    def red_LED(self):
        if self.red_led.on:
            self.red_led.off()
        else:
            self.red_led.on()     