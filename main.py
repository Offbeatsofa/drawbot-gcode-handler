from pygrbl_streamer import GrblStreamer
import keyboard
import time

finishTime = 0
startTime = 0
g = GrblStreamer(port='COM3', baudrate=115200)
g.progress_callback = lambda pct, cmd: progressBar(pct)

def progressBar(pct):
    print('\033[F\033[0K', end = '')
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
            print('Printing ufo\n')
            time.sleep(0.5)
            g.send_file('ufo.nc')
        case '-':
            print('Printing stegosaurus\n')
            time.sleep(0.5)
            g.send_file('stegosaurus.nc')
        case '`':
            print('Printing tiki\n')
            time.sleep(0.5)
            g.send_file('tiki.nc')
        case '0':
            print('Printing iron man\n')
            time.sleep(0.5)
            g.send_file('Iron Man.nc')
        case '1':
            print('Printing Spider-man\n')
            g.send_file('Spiderman.nc')
        case '9':
            print('Printing saturn\n')
            time.sleep(0.5)
            g.send_file('Saturn.nc')
        case 'a':
            print('Printing turtle\n')
            time.sleep(0.5)
            g.send_file('turtle.nc')
        case 'l':
            print('Printing mandalorian\n')
            time.sleep(0.5)
            g.send_file('Mando.nc')
        case 'enter':
            print('Printing stormtrooper\n')
            time.sleep(0.5)
            g.send_file('stormtrooper.nc')
        case 'f2':
            print('Printing bee and flower\n')
            print('error: file not added')
        case 'f8':
            print('Printing flowers\n')
            time.sleep(0.5)
            g.send_file('flowers.nc')
        case 'home':
            print('Printing bubbles\n')
            time.sleep(0.5)
            g.send_file('Bubbles.nc')
        case 'd':
            print('Printing r2d2\n')
            time.sleep(0.5)
            g.send_file('R2d2.nc')
        case 'p':
            print('Printing Parrot\n')
            time.sleep(0.5)
            g.send_file('Parrot.nc')
        case 'end':
            print('Printing Cow\n')
            time.sleep(0.5)
            g.send_file('Cow.nc')
        case ';':
            print('Printing geometric\n')
            time.sleep(0.5)
            g.send_file('Geometric.nc')
        case 'q':
            print('Printing captain america\n')
            time.sleep(0.5)
            g.send_file('CaptainAmerica.nc')
        case 'z':
            print('Printing names\n')
            time.sleep(0.5)
            g.send_file('names.nc')
        case 'e':
            print('Printing ufo w/ alien\n')
            time.sleep(0.5)
            g.send_file('UFOalien.nc')
        case _:
            print(f'key {keyboardEvent.name} not mapped to a file')
    g.disconnect()
    finishTime = time.time()
    print(f'Finished! Draw time: {round((finishTime - startTime), 2)} seconds')

keyboard.on_press(handleInput)
keyboard.wait('esc')