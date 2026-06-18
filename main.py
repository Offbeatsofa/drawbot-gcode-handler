from pygrbl_streamer import GrblStreamer
import keyboard
import time

g = GrblStreamer(port='COM4', baudrate=115200)
g.progress_callback = lambda pct, cmd: print(f'{pct}%')

def handleInput(keyboardEvent):
    match keyboardEvent.name:
        case '3':
            print('sending ufo')
            g.send_file('ufo_0001.gcode')
        case '-':
            print('sending stegosaurus')
            g.send_file('stegosaurus_0001.gcode')
        case '`':
            print('sending tiki')
            g.send_file('tiki_0001.gcode')

            
keyboard.on_press(handleInput)

g.connect()
keyboard.wait('esc')
print('Exiting program')
g.disconnect()