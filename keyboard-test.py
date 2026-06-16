import keyboard # type: ignore

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

keyboard.wait('esc')