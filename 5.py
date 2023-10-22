import tkinter as tk
import RPi.GPIO as GPIO

# Set the GPIO mode and warnings
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Define the GPIO pins for the LEDs
RED_PIN = 17
BLUE_PIN = 18
GREEN_PIN = 27

# Initialize the GPIO pins
GPIO.setup(RED_PIN, GPIO.OUT)
GPIO.setup(BLUE_PIN, GPIO.OUT)
GPIO.setup(GREEN_PIN, GPIO.OUT)

# Define the initial state of the LEDs
led_states = {RED_PIN: False, BLUE_PIN: False, GREEN_PIN: False}

# Function to toggle the LED state
def toggle_led_state(pin):
    led_states[pin] = not led_states[pin]
    GPIO.output(pin, led_states[pin])

# Function to exit the application
def exit_application():
    root.destroy()

# Define the functions to control the LEDs
def function1():
    print("Button 1 was pressed!")
    toggle_led_state(RED_PIN)

def function2():
    print("Button 2 was pressed!")
    toggle_led_state(BLUE_PIN)

def function3():
    print("Button 3 was pressed!")
    toggle_led_state(GREEN_PIN)

# Create the main application window
root = tk.Tk()
root.title("Light Control")

# Create and configure the buttons with different colors for the LEDs
button1 = tk.Button(root, text="RED", command=function1, bg="red", width=10, height=2)
button2 = tk.Button(root, text="BLUE", command=function2, bg="blue", width=10, height=2)
button3 = tk.Button(root, text="GREEN", command=function3, bg="green", width=10, height=2)

# Add the "Light Control" heading with improved style
heading_label = tk.Label(root, text="Light Control", font=("Helvetica", 24))
heading_label.grid(row=0, column=0, columnspan=2, pady=20)

# Center the buttons
button1.grid(row=1, column=0, pady=10)
button2.grid(row=2, column=0, pady=10)
button3.grid(row=3, column=0, pady=10)

# Create an "Exit" button
exit_button = tk.Button(root, text="Exit", command=exit_application, bg="gray", width=10, height=2)
exit_button.grid(row=4, column=0, pady=10)

# Start the main loop
root.mainloop()