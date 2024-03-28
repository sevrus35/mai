class Robot:
  
    def __init__(self):
        self.is_moving = False

    def move_forward(self):
        self.is_moving = True
        print("Robot is moving forward.")

    def rotate(self, angle):
        print(f"Robot is rotating {angle} degrees.")

    def stop(self):
        self.is_moving = False
        print("Robot has stopped.")


class PowerSwitch:
    
    def __init__(self):
        self.is_on = False

    def check_status(self):
        if self.is_on:
            print("Power switch is on.")
        else:
            print("Power switch is off.")

    def turn_off(self):
        if self.is_on:
            self.is_on = False
            print("Power switch is turned off.")
            if hasattr(robot, 'is_moving'):
                robot.stop()

class DieselEngine(PowerSwitch):
    
    def turn_on(self):
        if not self.is_on:
            self.is_on = True
            print("Diesel engine is turned on.")


#  usage
robot = Robot()
power_switch = DieselEngine()  
power_switch.check_status()  
power_switch.turn_on()
robot.move_forward()
robot.rotate(90)
power_switch.turn_off()
robot.stop()  