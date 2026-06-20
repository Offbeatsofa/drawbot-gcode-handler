import keyboard # type: ignore
import time

def handleInput(keyboardEvent):
    match keyboardEvent.name:
        case 'a':
            print('you just typed a')
        case 'b':
            print('you just typed b')
        case 'c':
            print('you just typed c')
        case 'd':
            print('you just typed d')

keyboard.on_press(handleInput)
print(time.time())
timevar = time.time()
time.sleep(1)
print(f'time variable: {timevar} \nactual time: {time.time()}')

keyboard.wait('esc')