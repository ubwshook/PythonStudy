"""
创建型设计模式的demo例子，这个例子并未使用某个设计模式，
后面会根据这个例示对其重构，来实现各种设计模式
"""

DIRECTIONS = ('East', 'West', 'North', 'South')

class MapSite(object):
    """
    类MapSite是所有迷宫组件的公共抽象类。我了简化例子，MapSite仅定义了一个操作Enter，它取决于你在进入什么。
    如果你进入一个房间，那么你的位置会发生改变。如果你试图进入一扇门，那么这两件事中就有一件会发生：如果们是开
    着的，你进入另一个房间。如果门是关着的，那么你就会碰壁。
    """
    def enter(self):
        """
        Enter是为更加复杂的有些操作提供了一个简单基础。例如，如果你在一个房间中说“向东走”，
        游戏只能确定直接在东边是哪一个MapSite并对它调用Enter。特定子类的Enter操作将计算
        出你的位置是发生改变，还是碰壁。
        :return:
        """
        pass


class Room(MapSite):
    """
    Room是MapSite的一个具体子类，而MapSite定义了迷宫中构件之间的主要关系。
    Room是指向其他MapSite对象的引用，并保存一个房间号，用来标识迷宫中的房间
    """
    def __init__(self, room_no):
        super(Room, self).__init__()
        self._room_no = room_no
        self._sides = {}
        for direction in DIRECTIONS:
            self._sides[direction] = None

    def get_side(self, direction):
        return self._sides[direction]

    def set_side(self, direction, map_site):
        if direction not in ['East', 'West', 'North', 'South']:
            print("Dirction is invalid!")

        self._sides[direction] = map_site

    def get_no(self):
        return self._room_no


class Wall(MapSite):
    """
    这个类描述的是墙，在demo中是比较简单的
    """
    def __init__(self):
        super(Wall, self).__init__()


class Door(MapSite):
    """
    这个类描述的是门这个对象
    """
    def __init__(self, room1: Room, room2: Room):
        super(Door, self).__init__()
        self._room1 = room1
        self._room2 = room2
        self._is_open = 0

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


class Maze(object):
    """
    迷宫中房间集合的类，可以向迷宫中添加或者获取房间
    """
    def __init__(self):
        self.rooms = {}

    def add_room(self, room: Room):
        self.rooms[room.get_no()] = room

    def get_room(self, room_no):
        return self.rooms[room_no]


class MazeGame(object):
    """
    Maze游戏类，没有完整去实现功能，我们主要关注创建型模式，所以这里只描述创建函数的实现。
    """
    @staticmethod
    def create_maze():
        maze = Maze()
        room1 = Room(1)
        room2 = Room(2)
        door = Door(room1, room2)

        maze.add_room(room1)
        maze.add_room(room2)

        room1.set_side('North', Wall())
        room1.set_side('East', door)
        room1.set_side('South', Wall())
        room1.set_side('West', Wall())

        room2.set_side('North', Wall())
        room2.set_side('East', Wall())
        room2.set_side('South', Wall())
        room2.set_side('West', door)

        return maze

