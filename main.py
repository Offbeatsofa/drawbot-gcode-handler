from pygrbl_streamer import GrblStreamer
import keyboard
import time

g = GrblStreamer(port='COM3', baudrate=115200)
g.progress_callback = lambda pct, cmd: print(f'{pct}%')

def handleInput(keyboardEvent):
    g.connect
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
        case '0':
            print('sending iron man')
            g.send_file('ironman_0001.gcode')
        case '1':
            print('sending spiderman')
            g.send_file('spiderman_0001.gcode')
        case '9':
            print('sending saturn')
            g.send_file('saturn_0001.gcode')
        case 'a':
            print('sending turtle')
            g.send_file('turtle_0001.gcode')
        case 'l':
            print('sending mandalorian')
            g.send_file('mandalorian_0001.gcode')
        case 'enter':
            print('sending stormtrooper')
            g.send_file('stormtrooper_0001.gcode')
        case '`':
            print('sending tiki')
            g.send_file('tiki_0001.gcode')
        case 'f2':
            print('sending bee and flower')
            print('error: file not added')
        case 'f8':
            print('sending flowers')
            g.send_file('flowers_0001.gcode')
        case 'home':
            print('sending bubbles')
            g.send_file('bubbles_0001.gcode')
        case _:
            print(f'key {keyboardEvent.name} not mapped to a file')
    g.disconnect()


keyboard.on_press(handleInput)
keyboard.wait('esc')
print('Exiting program')