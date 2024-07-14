from pynput import mouse
import datetime
from infi.clickhouse_orm import Database

from task3.models import Mouse, MouseBuffer


db = Database('shurik')
db.create_table(Mouse)
db.create_table(MouseBuffer)

PREVIOUS_POSITION = [0, 0]


def on_move(x, y):
    global PREVIOUS_POSITION, db
    timestamp = datetime.datetime.now()
    x, y = round(x), round(y)
    x_delta, y_delta = abs(x - PREVIOUS_POSITION[0]), abs(y - PREVIOUS_POSITION[1])
    PREVIOUS_POSITION = [x, y]
    mouse_doings = MouseBuffer(
        x_cords=x,
        y_cords=y,
        x_delta=x_delta,
        y_delta=y_delta,
        clientTimeStamp=timestamp,
        target=1)
    db.insert(mouse_doings)


def on_click(x, y, button, pressed):
    global db
    timestamp = datetime.datetime.now()
    x, y = round(x), round(y)
    mouse_doings = MouseBuffer(
        x_cords=x,
        y_cords=y,
        x_delta=0,
        y_delta=0,
        clientTimeStamp=timestamp,
        target=2)
    db.insert(mouse_doings)


def on_scroll(x, y, dx, dy):
    global db
    timestamp = datetime.datetime.now()
    x, y = round(x), round(y)
    mouse_doings = MouseBuffer(
        x_cords=x,
        y_cords=y,
        x_delta=dx,
        y_delta=dy,
        clientTimeStamp=timestamp,
        target=3)
    db.insert(mouse_doings)


with mouse.Listener(
        on_move=on_move,
        on_click=on_click,
        on_scroll=on_scroll) as MouseListener:
    print("start")
    MouseListener.join()
