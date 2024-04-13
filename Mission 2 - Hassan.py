from easygopigo3 import EasyGoPiGo3
import time

# Initialize GoPiGo robot
gpg = EasyGoPiGo3()


# Initialize distance sensor
distance_sensor = gpg.init_distance_sensor()
time.sleep(3)

path_length = 0  # Initialize path length variable

try:
    while True:
        # Read distance in cm
        distance = distance_sensor.read()  # Convert mm to cm
        
        # Obstacle avoidance logic
        if distance < 20:  # If an obstacle is too close (adjust threshold as needed)
            # Back up
            gpg.stop()
            gpg.backward()
            time.sleep(0.1)
            gpg.stop()
            
            # Alternate between turning left and right
            if distance_sensor.read() < 20:  # Check if there's still an obstacle after backing up
                gpg.right()  # Turn right
                time.sleep(1)
            else:
                gpg.left()  # Turn left
                time.sleep(1)
            gpg.stop()
        else:
            # Move forward
            gpg.forward()

        time.sleep(0.1)  # Wait 0.1 second before taking the next measurement

except KeyboardInterrupt:
    pass