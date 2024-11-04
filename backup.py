import time  # Import time to add a delay

try:
    from pynput.keyboard import Controller, Listener, Key
except ImportError:
    import os
    print("Installing 'pynput' library...")
    os.system("pip install pynput")
    from pynput.keyboard import Controller, Listener, Key

# Step 1: Set up a keyboard controller to type out messages
keyboard_controller = Controller()

# Step 2: Define a function to listen for 'Tab' key press and type "Hello, World!"
def automated_typing():
    print("Listening for 'Tab' key to type 'Hello, World!'. Press 'Ctrl+C' to exit.")
    
    # Define what happens when 'Tab' is pressed
    def on_press(key):
        if key == Key.tab:
            # Suppress any console output and type "Hello, World!"
            keyboard_controller.type("Hello, World!")
            # Adding a delay to prevent repeated typing if 'Tab' is held
            time.sleep(0.5)

    # Start listener for key press events
    with Listener(on_press=on_press) as listener:
        listener.join()  # Keep the program running and listening

# Run the function to start listening for key events
automated_typing()
