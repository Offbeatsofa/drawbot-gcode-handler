from pygrbl_streamer import GrblStreamer # type: ignore
import keyboard

g = GrblStreamer(port='COM4', baudrate=115200)
g.progress_callback = lambda pct, cmd: print(f'{pct}%')

def handleInput(keyboardEvent):
    match keyboardEvent.name:
        case 'a':
            print('sending file a')
            g.send_file('gcodes\ufo_0001.gcode')
        case 'b':
            print('sending file b')
            g.send_file('gcodes\saturn_0001.gcode')
        case 'c':
            print('sending file c')
            g.send_file('gcodes\spiderman_0001.gcode')
        case 'd':
            print('sending file d')
            g.send_file('gcodes\mandalorian_0001.gcode')
        case 'e':
            print('sending file e')
            g.send_file('gcodes\turtle_0001.gcode')
        case 'f':
            print('sending file f')
            g.send_file('gcodes\yoda_0001.gcode')
        case 'g':
            print('sending file g')
            g.send_file('gcodes\ironman_0001.gcode')

keyboard.on_press(handleInput)

g.connect()
keyboard.wait('esc')
print('Exiting program')
g.disconnect()