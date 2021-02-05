import keyboard

def on_press_reaction(event):
    print('any key was pressed')

keyboard.on_press(on_press_reaction)

# Blocks until you press esc.
keyboard.wait('esc')
