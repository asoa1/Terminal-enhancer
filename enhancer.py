import cv2
import time
from colorama import init, Fore, Style

# Initialize colorama to work on Windows terminals as well
init()

def print_banner():
    banner = """
     _   _           _     _  __     __                  
    | | | |         | |   (_)/ _|   / _|                 
    | |_| | __ _ ___| |__  _| |_   | |_ ___  _ __ _   _  
    |  _  |/ _` / __| '_ \| |  _|  |  _/ _ \| '__| | | | 
    | | | | (_| \__ \ | | | | |    | || (_) | |  | |_| | 
    |_| |_|\__,_|___/_| |_|_|_|    |_| \___/|_|   \__,_| 
    """

    print(Fore.YELLOW + Style.BRIGHT + banner + Style.RESET_ALL)

def take_picture():
    # Open the default camera (0 or -1 for the default camera, adjust if needed)
    cap = cv2.VideoCapture(0)

    # Check if the camera opened successfully
    if not cap.isOpened():
        print("Error: Could not open camera")
        return

    print_banner()

    picture_count = 1
    while True:
        ret, frame = cap.read()

        if not ret:
            print("Error: Can't receive frame (stream end?). Exiting...")
            break

        # Save the captured frame/image
        image_name = f"picture_{picture_count}.jpg"
        cv2.imwrite(image_name, frame)
        print(f"Picture {picture_count} captured!")
        picture_count += 1

        # Wait for 5 seconds before capturing the next image
        time.sleep(5)

    # Release the camera and close the window
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    take_picture()
