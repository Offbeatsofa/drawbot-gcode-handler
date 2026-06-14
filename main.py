from pygrbl_streamer import GrblStreamer

g = GrblStreamer(port='COM3', baudrate=115200)
g.progress_callback = lambda pct, cmd: print(f'{pct}%')

g.connect()
g.send_file('circle.gcode')   # any size, constant memory, starts instantly
g.disconnect()