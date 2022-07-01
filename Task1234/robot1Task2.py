# rcj_soccer_player controller - ROBOT B1

# Feel free to import built-in libraries
import math  # noqa: F401

# You can also import scripts that you put into the folder with controller
import utils
from rcj_soccer_robot import RCJSoccerRobot, TIME_STEP
import time


class MyRobot1(RCJSoccerRobot):
    def run(self):
        I = 0
        e = 0
        while self.robot.step(TIME_STEP) != -1:
            if self.is_new_data():
                data = self.get_new_data()  # noqa: F841

                while self.is_new_team_data():
                    team_data = self.get_new_team_data()  # noqa: F841
                    # Do something with team data

                if self.is_new_ball_data():
                    ball_data = self.get_new_ball_data()
                else:
                    # If the robot does not see the ball, stop motors
                    self.left_motor.setVelocity(0)
                    self.right_motor.setVelocity(0)
                    continue

                # Get data from compass
                heading = self.get_compass_heading()  # noqa: F841

                # Get GPS coordinates of the robot
                robot_pos = self.get_gps_coordinates()  # noqa: F841

                # Get data from sonars
                sonar_values = self.get_sonar_values()  # noqa: F841

                self.left_motor.setVelocity(10)
                print(math.degrees(heading))
                
                
                t1 = time.time()

                v = 0
                T = 0.000003
                Kp = 0.05
                KI = 0.05
                Kd = 0.000001
                e_temp = e
                e = 30 - math.degrees(heading)
                P = Kp*e
                I = I + KI * T *e
                D = Kd*(e - e_temp)/T
                w = P + I + D

                vr = (2*v + 0.085*w)/0.04
                vl = (2*v - 0.085*w)/0.04

                if -0.05 < vr < 0.05:
                    vr = 0

                if -0.05 < vl < 0.05:
                    vl = 0
                
                self.left_motor.setVelocity(vr)
                self.right_motor.setVelocity(vl)

                t2 = time.time()

                dt = t2 - t1 
                time.sleep(dt-T)
            
                '''# Compute the speed for motors
                direction = utils.get_direction(ball_data["direction"])

                # If the robot has the ball right in front of it, go forward,
                # rotate otherwise
                if direction == 0:
                    left_speed = 7
                    right_speed = 7
                else:
                    left_speed = direction * 4
                    right_speed = direction * -4

                # Set the speed to motors
                self.left_motor.setVelocity(left_speed)
                self.right_motor.setVelocity(right_speed)

                # Send message to team robots
                self.send_data_to_team(self.player_id)
                '''
