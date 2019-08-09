from abstract_factory import MazeFactory, MazeGame
from creational_demo import Maze, Wall, MapSite, DIRECTIONS
from copy import deepcopy


class Room(MapSite):
    """
    Room是MapSite的一个具体子类，而MapSite定义了迷宫中构件之间的主要关系。
    Room是指向其他MapSite对象的引用，并保存一个房间号，用来标识迷宫中的房间
    """
    def __init__(self):
        super(Room, self).__init__()
        self._room_no = None
        self._sides = {}
        for direction in DIRECTIONS:
            self._sides[direction] = None

    def init(self, room_no):
        self._room_no = room_no

    def get_side(self, direction):
        return self._sides[direction]

    def set_side(self, direction, map_site):
        if direction not in ['East', 'West', 'North', 'South']:
            print("Dirction is invalid!")

        self._sides[direction] = map_site

    def get_no(self):
        return self._room_no


class Door(MapSite):
    """
    这个类描述的是门这个对象
    """
    def __init__(self):
        super(Door, self).__init__()
        self._room1 = None
        self._room2 = None
        self._is_open = 0

    def init(self, room1, room2):
        self._room1 = room1
        self._room2 = room2

    def other_side_from(self, room):
        """
        获取一个房间另一面的房间
        :param room:
        :return: 输入room另一面的room
        """
        if room.get_no() == self._room1.get_no():
            return self._room2
        elif room.get_no() == self._room2.get_no():
            return self._room1
        else:
            print("Room is wrong!")
            return None


class MazePrototypeFactory(MazeFactory):
    """
    使用原型模式的抽象工厂
    """
    def __init__(self, room, wall, door, maze):
        """
        初始化函数设置原型
        :param room: 房间原型
        :param wall: 墙壁原型
        :param door: 门原型
        :param maze: 迷宫原型
        """
        self._prototype_maze = maze
        self._prototype_room = room
        self._prototype_wall = wall
        self._prototype_door = door

    def make_wall(self):
        return deepcopy(self._prototype_wall)

    def make_room(self, room_no):
        """
        利用原型构建房间，这里使用的原型，需要调用初始化之后才能使用，这与之前不同。
        :param room_no: 房间号
        :return:
        """
        room = deepcopy(self._prototype_room)
        room.init(room_no)
        return room

    def make_door(self, room1, room2):
        door = deepcopy(self._prototype_door)
        door.init(room1, room2)
        return door

    def make_make(self):
        return deepcopy(self._prototype_maze)


game = MazeGame()
# 为工厂添加原型
factory = MazePrototypeFactory(Room(), Wall(), Door(), Maze())
maze = game.create_maze(factory)
for direction in DIRECTIONS:
    print(direction, maze.get_room(1).get_side(direction))


