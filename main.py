from pygrbl_streamer import GrblStreamer
import keyboard
import time

finishTime = 0
startTime = 0
g = GrblStreamer(port='COM3', baudrate=115200)
g.progress_callback = lambda pct, cmd: progressBar(pct)

def progressBar(pct):
    print('\033[H\033[J', end = '')
    print('Progress: ', end = '')
    for i in range(25):
        if pct >= (i+1)*4:
            print('█', end = '')
        else:
            print('░', end = '')    
    print(f' ({pct}%)')

def handleInput(keyboardEvent):
    global finishTime
    global startTime 
    startTime = time.time()
    if time.time() - finishTime <= 3:
        print('Drawbot not ready')
        return
    g.connect()
    match keyboardEvent.name:
        case 'esc':
            print('Exiting program')
        case '3':
            print('Printing ufo')
            time.sleep(0.5)
            g.send_file('ufo.nc')
        case '-':
            print('Printing stegosaurus')
            time.sleep(0.5)
            g.send_file('stegosaurus.nc')
        case '`':
            print('Printing tiki')
            time.sleep(0.5)
            g.send_file('tiki.nc')
        case '0':
            print('Printing iron man')
            time.sleep(0.5)
            g.send_file('Iron Man.nc')
        case '1':
            print('Printing Spider-man')
            g.send_file('Spiderman.nc')
        case '9':
            print('Printing saturn')
            time.sleep(0.5)
            g.send_file('Saturn.nc')
        case 'a':
            print('Printing turtle')
            time.sleep(0.5)
            g.send_file('turtle.nc')
        case 'l':
            print('Printing mandalorian')
            time.sleep(0.5)
            g.send_file('Mando.nc')
        case 'enter':
            print('Printing stormtrooper')
            time.sleep(0.5)
            g.send_file('stormtrooper.nc')
        case 'f2':
            print('Printing bee and flower')
            print('error: file not added')
        case 'f8':
            print('Printing flowers')
            time.sleep(0.5)
            g.send_file('flowers.nc')
        case 'home':
            print('Printing bubbles')
            time.sleep(0.5)
            g.send_file('Bubbles.nc')
        case 'd':
            print('Printing r2d2')
            time.sleep(0.5)
            g.send_file('R2d2.nc')
        case 'p':
            print('Printing Parrot')
            time.sleep(0.5)
            g.send_file('Parrot.nc')
        case 'end':
            print('Printing Cow')
            time.sleep(0.5)
            g.send_file('Cow.nc')
        case ';':
            print('Printing geometric')
            time.sleep(0.5)
            g.send_file('Geometric.nc')
        case 'q':
            print('Printing captain america')
            time.sleep(0.5)
            g.send_file('CaptainAmerica.nc')
        case 'z':
            print('Printing names')
            time.sleep(0.5)
            g.send_file('names.nc')
        case 'e':
            print('Printing ufo w/ alien')
            time.sleep(0.5)
            g.send_file('UFOalien.nc')
        case _:
            print(f'key {keyboardEvent.name} not mapped to a file')
    g.disconnect()
    finishTime = time.time()
    print(f'Finished! Draw time: {round((finishTime - startTime), 2)} seconds')

keyboard.on_press(handleInput)
keyboard.wait('esc')