import cv2 # for access the camera
import random # for random the number to generate the monster stats
from pyzbar.pyzbar import decode # to decode/read the barcode


# Accessing y camera for barcode scanning. Change to phone camera for later moblie app version.

# # Open camera ( 0 is usually refers to the default camera)
# cap = cv2.VideoCapture(0)

# while True:
#     ret, frame = cap.read() # Capture frame-by-frame
#     cv2.imshow('Frame', frame) # Display the resulting frame
#     if cv2.waitkey(1) & 0xFF == ord('q'): # Break the loop if 'q'q is pressed
#         break

# # When everything done, release the capture.
# cap.release()
# cv2.destroyAllWindows()

# function to scan the barcode, decode which uses above + more

def scan_barcode():
    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # Decode the barcode in the frame
        decoded_objects = decode(frame)
        for obj in decoded_objects:
            barcode_data = obj.data.decode("utf-8")
            print(f"Barcode: {barcode_data}")

            # Release the capture and return the barcode data
            cap.release()
            cv2.destroyAllWindows()
            return barcode_data

        # display the frame
        cv2.imshow('Barcode Scanner', frame)

        # Break the loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyALLWindows()
    return None


# Generate monster stats using the scanned barcode
def generate_monster_stats():
    barcode = scan_barcode() # Scan the barcode first

    if barcode: # Generating random stats for the monster
        monster_name = f"Monster {barcode}" # You can use the barcode value in the name/will change later for db of monster names.random
        monster_hp = random.randint(0, 100) # Random HP between 0-100
        monster_attack = random.randint(0, 50) # Random Attack between 0-50
        monster_defense = random.randint(0, 50) # Random defense between 0-50

        return {
            'name': monster_name,
            'hp': monster_hp,
            'attack': monster_attack,
            'defense': monster_defense
        }

# example usage
monster = generate_monster_stats()
if monster:
    print(monster)