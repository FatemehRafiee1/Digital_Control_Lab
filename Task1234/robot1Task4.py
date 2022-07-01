# rcj_soccer_player controller - ROBOT B1

# Feel free to import built-in libraries
import math  # noqa: F401

# You can also import scripts that you put into the folder with controller
import utils
from rcj_soccer_robot import RCJSoccerRobot, TIME_STEP
import time


class MyRobot1(RCJSoccerRobot):
    def run(self):
        I_pos = 0
        I_angle = 0
        e_pos = 0
        e_angle = 0
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
               # print("angle:", math.degrees(heading), end = "    ")
               # print("position:", robot_pos[1])
               # print("start")
               # print(ball_data["direction"][0])
                
               # print(robot_pos)
               # print(ball_data["direction"])
                
                
                t1 = time.time()

                T = 0.000003

                kp = 30
                ki = 20
                kd = 0.00001
               

                angle = math.atan2(ball_data["direction"][0], ball_data["direction"][1])
                e_angle = angle - (math.pi/2)

                e_pos = 1/ball_data['strength'] * 10

                e_temp_pos = e_pos
                P_pos = e_pos * kp
                I_pos = I_pos + ki * T *e_pos
                D_pos = kd*(e_pos - e_temp_pos)/T

                e_temp_angle = e_angle
                P_angle = e_angle * kp
                I_angle = I_angle + ki * T *e_angle
                D_angle = kd*(e_pos - e_temp_angle)/T
                
                vl = P_pos + P_angle * -1 + I_pos + I_angle * -1 + D_pos + D_angle * -1
                vr = P_pos + P_angle + I_pos + I_angle + D_pos + D_angle

                if -0.1 < vr < 0.1:
                    vr = 0

                if -0.1 < vl < 0.1:
                    vl = 0

                self.left_motor.setVelocity(vl)
                self.right_motor.setVelocity(vr)

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
