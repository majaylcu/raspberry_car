import RPi.GPIO as GPIO
import time

class DcMotor:
    def __init__(self, forwardpin, backwardpin, forwardpin2, backwardpin2):
        try:
            GPIO.cleanup()
        except:
            pass
        self.forwardpin = forwardpin
        self.backwardpin = backwardpin
        self.forwardpin2 = forwardpin2
        self.backwardpin2 = backwardpin2
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.forwardpin, GPIO.OUT)
        GPIO.setup(self.backwardpin, GPIO.OUT)
        GPIO.setup(self.forwardpin2, GPIO.OUT)
        GPIO.setup(self.backwardpin2, GPIO.OUT)


    def forward_rotation(self):

        GPIO.output(self.backwardpin, GPIO.LOW)
        GPIO.output(self.backwardpin2, GPIO.LOW)
        GPIO.output(self.forwardpin, GPIO.HIGH)
        GPIO.output(self.forwardpin2, GPIO.HIGH)
        print("Running Forward!")

    def backward_rotation(self):
        GPIO.output(self.forwardpin, GPIO.LOW)
        GPIO.output(self.forwardpin2, GPIO.LOW)
        GPIO.output(self.backwardpin, GPIO.HIGH)
        GPIO.output(self.backwardpin2, GPIO.HIGH)
        print("DC Motor running Backward")

    def left_turn(self):
        GPIO.output(self.forwardpin, GPIO.HIGH)
        GPIO.output(self.forwardpin2, GPIO.LOW)
        GPIO.output(self.backwardpin, GPIO.LOW)
        GPIO.output(self.backwardpin2, GPIO.LOW)

    def right_turn(self):
        GPIO.output(self.forwardpin, GPIO.LOW)
        GPIO.output(self.forwardpin2, GPIO.HIGH)
        GPIO.output(self.backwardpin, GPIO.LOW)
        GPIO.output(self.backwardpin2, GPIO.LOW)

    def stop(self):
        GPIO.output(self.forwardpin, GPIO.LOW)
        GPIO.output(self.forwardpin2, GPIO.LOW)
        GPIO.output(self.backwardpin, GPIO.LOW)
        GPIO.output(self.backwardpin2, GPIO.LOW)
        print("DC Motor has been stopped")


motor = DcMotor(17, 22, 24, 25)


def operation(option):
    if option == 1:
        motor.stop()
        motor.forward_rotation()
    elif option == 2:
        motor.stop()
        motor.backward_rotation()
    elif option == 3:
        motor.stop()
    elif option == 4:
        motor.forward_rotation()
    elif option == 5:
        motor.stop()
        GPIO.cleanup()
        exit(0)
    elif option == 6:
        motor.left_turn()
    elif option == 7:
            motor.right_turn()
    else:
            pass



if __name__ == '__main__':
    try:
        while True:
            usage = "1 - Forward rotation\n2 - Backward Rotation\n3 - Stop\n4 - Start\n5 - Exit\n6 - left\n7 - right"
            print(usage)
            try :
                option = int(input("Please provide a valid input : "))
            except ValueError:
                continue
            if option > 7 or option == 0 or option == "":
                raise ValueError
            else:
                operation(option)
                time.sleep(1)

    except Exception as e:
        print("Please Try again")
        print(e)
    finally:
        try:
            motor.stop()
            GPIO.cleanup()
        except:
            pass

