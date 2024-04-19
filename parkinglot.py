from easygopigo3 import EasyGoPiGo3
import picamera
import time

gpg = EasyGoPiGo3()

# Initialize PiCamera
camera = picamera.PiCamera()

# Function to check if a parking slot is occupied
def is_slot_occupied(distance_threshold=30):
    # Read distance from sensor
    distance = gpg.init_distance_sensor().read_mm()

    # Check if distance is less than threshold
    if distance < distance_threshold:
        return True
    else:
        return False

# Function to move the robot through parking slots and update status in a text file
def move_through_parking_slots(num_slots=10, filename="parking_status.txt"):
    for _ in range(2):  # Repeat twice
        gpg.drive_cm(100)  # Move forward 1 meter
        gpg.turn_degrees(90)  # Turn 90 degrees
        gpg.turn_degrees(-90)  # Turn back to initial state
        
        # Open file in write mode to clear previous content
        with open(filename, "w") as file:
            file.write("")

        for slot in range(1, num_slots + 1):
            # Move robot to next parking slot
            print(f"Moving to parking slot {slot}")

            # Check if slot is occupied
            occupied = is_slot_occupied()

            # Update status in text file
            with open(filename, "a") as file:
                file.write(f"Parking Slot {slot}: {'Occupied' if occupied else 'Empty'}\n")

            time.sleep(1)  # Adjust sleep time as needed

    gpg.stop()  # Stop the robot after completing the task

    print("Finished moving through all parking slots")

move_through_parking_slots()
