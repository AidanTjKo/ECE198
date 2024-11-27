import cv2
from cvzone.HandTrackingModule import HandDetector
import serial
import time

ser = serial.Serial(
    port='/dev/cu.usbmodem1203',
    baudrate=115200,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS

)
ser.writeTimeout = 0 
ser.isOpen()

# TM1 = 15
# ser.write(str(TM1).encode())


def map_coordinates_to_led_index(coord, x_max=1300, y_max=650, grid_size=8):
    """
    Maps (x, y) coordinates onto a single LED index (1-64) for an 8x8 matrix.

    Args:
        x (int): x-coordinate of the input.
        y (int): y-coordinate of the input.
        x_max (int): Maximum range of x-coordinates.
        y_max (int): Maximum range of y-coordinates.
        grid_size (int): Size of the grid (e.g., 8 for 8x8 matrix).

    Returns:
        int: Index of the LED (1-64).
    """
    # Map x to column (0-indexed)
    col = int((coord[0] / x_max) * (grid_size - 1))
    
    # Map y to row (0-indexed)
    row = int((coord[1] / y_max) * (grid_size - 1))

    # Calculate 1-based index
    led_index = row * grid_size + col + 1

    return led_index;


# # Example usage
# x = 1300
# y = 650
# led_index = map_coordinates_to_led_index(x, y)

# print(f"Coordinates ({x}, {y}) map to LED matrix index: {led_index}")




detector = HandDetector(detectionCon=0.8, maxHands=1)

video = cv2.VideoCapture(0)

while True:
    ret, frame = video.read()
    frame = cv2.flip(frame, 1)
    hands, img = detector.findHands(frame)

    if hands:
        for hand in hands:
            lmList = hand["lmList"]  # Landmark list
            bbox = hand["bbox"]      # Bounding box
            center = hand["center"]  # Center of hand
            handType = hand["type"]  # Left or Right hand

            # print(f"Hand Type: {handType}")
            # print(f"Bounding Box: {bbox}")
            print(f"Hand Center: {center}")
            # Example: Highlight the hand center
            print(map_coordinates_to_led_index(center))
            cv2.circle(frame, center, 10, (0, 255, 0), cv2.FILLED)

            # # Display coordinates on the frame

            cv2.putText(frame, f"Center: {center}", (center[0] - 50, center[1] - 50), 
                        cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 1)
            


            coords = map_coordinates_to_led_index(center);
            ser.write(str(center).encode())

    #show the camera
    cv2.imshow("frame", frame)
    k = cv2.waitKey(1)
    if k == ord("k"):
        break


    time.sleep(0.4);
video.release()
cv2.destroyAllWindows()

#find port command ls /dev/cu.*
