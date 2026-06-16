from pygrbl_streamer import GrblStreamer # type: ignore
import keyboard

g = GrblStreamer(port='COM3', baudrate=115200)
g.progress_callback = lambda pct, cmd: print(f'{pct}%')

def handleInput(keyboardEvent):
    match keyboardEvent.name:
        case 'a':
            print('sending file a')
        case 'b':
            print('sending file b')
        case 'c':
            print('sending file c')

keyboard.on_press(handleInput)

keyboard.wait('esc')
print('Exiting program')
#g.connect()
#g.send_file('circle.gcode')   # any size, constant memory, starts instantly
#g.disconnect()