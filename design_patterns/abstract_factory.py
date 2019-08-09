"""
创建型模式1——抽象工厂模式
"""
from creational_demo import Maze, Wall, Room, Door


class MazeFactory(object):
    """
    工厂类，定义各个组件如何生成
    可以被覆写，定制不同工厂类
    """
    def make_maze(self):
        return Maze()

    def make_wall(self):
        return Wall()

    def make_door(self, room1: Room, room2: Room):
        return Door(room1, room2)

    def make_room(self, room_no: int):
        return Room(room_no)


class EnchantedDoor(Door):
    """
    一个被施加了魔法的门，这里没有具体实现仅简单继承
    """
    def __init__(self, room1: Room, room2: Room):
        super(EnchantedDoor, self).__init__(room1, room2)


class EnchantedRoom(Room):
    """
    一个被施加了魔法的房间，这里没有具体实现仅简单继承
    """
    def __init__(self, room_no):
        super(EnchantedRoom, self).__init__(room_no)


class EnchantedMazeFactory(MazeFactory):
    """
    用于创建施加了魔法迷宫的工厂类，可以生成施加魔法的
    """
    def make_door(self, room1: Room, room2: Room):
        return EnchantedDoor(room1, room2)

    def make_room(self, room_no: int):
        return EnchantedRoom(room_no)


class MazeGame(object):
    """
    Maze游戏类, 这里设计的create_maze函数可以接收工厂对象进行类型初始化。
    """
    def create_maze(self, factory):
        maze = factory.make_maze()
        room1 = factory.make_room(1)
        room2 = factory.make_room(2)
        door = factory.make_door(room1, room2)

        maze.add_room(room1)
        maze.add_room(room2)

        room1.set_side('North', factory.make_wall())
        room1.set_side('East', door)
        room1.set_side('South', factory.make_wall())
        room1.set_side('West', factory.make_wall())
        room2.set_side('North', factory.make_wall())
        room2.set_side('East', factory.make_wall())
        room2.set_side('South', factory.make_wall())
        room2.set_side('West', door)

        return maze

# 创建一个施加了魔法的迷宫
game = MazeGame()
game.create_maze(EnchantedMazeFactory())


