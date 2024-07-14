from enum import Enum
from infi.clickhouse_orm import Model, MergeTree, Int16Field, Enum16Field, DateTimeField, BufferModel, Buffer


class targetEnum(Enum):
    move = 1
    click = 2
    scroll = 3


class Mouse(Model):
    x_cords = Int16Field()
    y_cords = Int16Field()
    x_delta = Int16Field()
    y_delta = Int16Field()
    clientTimeStamp = DateTimeField()
    target = Enum16Field(targetEnum)

    engine = MergeTree(order_by=[clientTimeStamp], date_col='timestamp')


class MouseBuffer(BufferModel, Mouse):
    engine = Buffer(Mouse)
