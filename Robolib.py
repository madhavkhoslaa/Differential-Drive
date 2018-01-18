class Robo:
    try:
        import sys
        import time
        import RPi.GPIO as GPIO
        mode = GPIO.getmode()
        GPIO.cleanup()
        GPIO.setmode(GPIO.BOARD) # or set as GPIO.setmode(GPIO.BCM) according to prefrence
    except:
        print('Install the dependencies')
    def __init__(self , Left_1 , Left_2 , Right_1 , Right_2 , Enl , Enr): #For the current built PWM is not there
        self.Left_1 = Left_1
        self.Left_2 - Left_2
        self.Right_1 = Right_1
        self.Right_2 = Right_2
        self.Enl = Enl
        self.Enr = Enr
        start_time = time.time()
        GPIO.setup(self.Left_1 , GPIO.OUT)
        GPIO.setup(self.Left_2 , GPIO.OUT)
        GPIO.setup(self.Right_1 , GPIO.OUT)
        GPIO.setup(self.Right_2, GPIO.OUT)
        GPIO.setup(self.Enl , GPIO.OUT)
        GPIO.setup(self.Enr, GPIO.OUT)
        def left_toggle(self , togg , time):
            curr = time.time()
            step = curr + time
            if togg == 1:
                while curr < step:
                    curr = time.time()
                    GPIO.output(self.Left_1 , True)
                    GPIO.output(self.Left_2 , False)
            if togg == 0 :
                while curr < step:
                    curr = time.time()
                    GPIO.output(self.Left_1 , False)
                    GPIO.output(self.Left_2 , True)
        def right_toggle(self , togg , time):
            curr = time.time()
            step = curr + time
            if togg == 1:
                while curr < step:
                    curr = time.time()
                    GPIO.output(self.Right_1, True)
                    GPIO.output(self.Right_2 ,False)
            if togg == 0:
                while curr < step:
                    curr = time.time()
                    GPIO.output(self.Right_2, False)
                    GPIO.output(self.Right_1 ,True)

        def forward(self , time):
            curr = time.time()
            step = curr + time
            while curr < step:
                curr = time.time()
                GPIO.output(self.Left_1 , True)
                GPIO.output(self.Left_2 ,False)
                GPIO.output(self.Right_1 , True)
                GPIO.output(self.Right_2 ,False)
        def backward(self , time):
            curr = time.time()
            step = curr
            while curr < step:
                curr = time.time()
                GPIO.output(self.Left_1,False)
                GPIO.output(self.Left_2,True)
                GPIO.output(self.right_toggle , True)
                GPIO.output(self.Right_1 ,False)
                pass
    def servo(self):
        pass
