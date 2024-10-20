import time
from pynput.mouse import Button, Controller as MouseController
from pynput.keyboard import Listener, KeyCode

# Initialize mouse controller
mouse = MouseController()

# Variables to store the mouse state
left_mouse_position = None
mouse_down = False
# Key codes for the desired keys
key_z = KeyCode(char='z')
key_x = KeyCode(char='x')
key_c = KeyCode(char='c')

# Define what happens when keys are pressed
def on_press(key):
    global left_mouse_position
    global mouse_down 
    
    # If 'Z' is pressed, wait for 3 seconds and then hold the left mouse button down
    if key == key_z:
        if mouse_down:
            mouse.release(Button.left)xccc
            print("Z released. Releasing left mouse button...") 
        else: 
            print("Z pressed. Holding left mouse button after a delay of 3 seconds...")
            time.sleep(3)
            mouse.press(Button.left)
        mouse_down = not mouse_down
    
    # If 'X' is pressed, store the current mouse position
    elif key == key_x:
        left_mouse_position = mouse.position
        print(f"X pressed. Remembering mouse position: {left_mouse_position}")
    
    # If 'C' is pressed, move the mouse back to the remembered position
    elif key == key_c and left_mouse_position is not None:
        print(f"C pressed. Moving mouse back to position: {left_mouse_position}")
        mouse.position = left_mouse_position


# Start listening to the keyboard
with Listener(on_press=on_press) as listener:
    print('Welcome to Flo\'s Click\n' +
          'Press Z to hold down left mouse, press X to remember your mouse\'s position and C to move it back'
          )
    listener.join()
