"""
创建型模式2——生成器模式
"""
from abc import ABCMeta, abstractmethod
from creational_demo import Room, Wall, Door, DIRECTIONS


class MazeBuilder(object, metaclass=ABCMeta):
    """
    迷宫生成器的抽象类，用于定义迷宫生成器必须实现的方法
    """
    @abstractmethod
    def build_maze(self):
        pass

    @abstractmethod
    def build_room(self, room_no: int):
        pass

    @abstractmethod
    def build_door(self, room1_no: int, room2_no: int):
        pass

    @abstractmethod
    def get_maze(self):
        pass


class StandardMazeBuilder(MazeBuilder):
    """
    一个标准迷宫生成器，继承于Mazebuilder
    """
    def __init__(self):
        """
        初始化一个字典用于存放迷宫中的房间
        """
        self._current_maze = {}

    def build_maze(self):
        """
        每次调用创建迷宫就会初始化迷宫房间字典
        :return:
        """
        self._current_maze = {}

    def build_room(self, room_no):
        """
        创建一个房间，并将其加入迷宫房间字典中
        :param room_no: 房间编号
        :return:
        """
        if room_no not in self._current_maze.keys():
            room = Room(room_no)
            self._current_maze[room_no] = room

            for direction in DIRECTIONS:
                room.set_side(direction, Wall())

    def build_door(self, room1_no, room2_no):
        """
        为两个房间之间创建一道门，通过_common_wall确定门所在的方位
        :param room1_no: 房间1编号
        :param room2_no: 房间2编号
        :return:
        """
        room1 = self._current_maze[room1_no]
        room2 = self._current_maze[room2_no]
        door = Door(room1, room2)

        room1.set_side(self._common_wall(room1, room2), door)
        room2.set_side(self._common_wall(room2, room1), door)

    def get_maze(self):
        """
        返回迷宫信息
        :return: 返回迷宫字典
        """
        return self._current_maze

    def _common_wall(self, room1: Room, room2: Room):
        """
        假设迷宫宽度为8个房间，如果相邻或者在迷宫中模8相等，才能获得方位。
        :param room1: 房间1编号
        :param room2: 房间2编号
        :return:
        """
        room1_no = room1.get_no()
        room2_no = room2.get_no()

        if room2_no == room1_no + 1 and room1_no % 8 != 0:
            return 'East'

        if room1_no == room2_no + 1 and room2_no % 8 != 0:
            return 'West'

        if room1_no % 8 == room2_no % 8 and room1_no // 8 == room2_no // 8 + 1:
            return 'North'

        if room1_no % 8 == room2_no % 8 and room2_no // 8 == room1_no // 8 + 1:
            return 'South'

        return None


class MazeGame(object):
    """
    迷宫游戏类，这里仅仅实现创建迷宫的方法
    """
    def create_maze(self, builder):
        builder.build_maze()

        builder.build_room(1)
        builder.build_room(2)
        builder.build_door(1, 2)

        return builder.get_maze()

game = MazeGame()
builder = StandardMazeBuilder()
a = game.create_maze(builder)
for direction in DIRECTIONS:
    print(a[2].get_side(direction))
