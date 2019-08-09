from creational_demo import Room, Wall, Door, Maze


class MazeGame(object):
    def make_maze(self):
        return Maze()

    def make_room(self, room_no):
        return Room(room_no)

    def make_door(self, room1: Room, room2: Room):
        return Door(room1, room2)

    def make_wall(self):
        return Wall()

    def create_maze(self):
        maze = self.make_maze()
        room1 = self.make_room(1)
        room2 = self.make_room(2)
        door = self.make_door(room1, room2)

        maze.add_room(room1)
        maze.add_room(room2)

        room1.set_side('North', self.make_wall())
        room1.set_side('East', door)
        room1.set_side('South', self.make_wall())
        room1.set_side('West', self.make_wall())

        room2.set_side('North', self.make_wall())
        room2.set_side('East', self.make_wall())
        room2.set_side('South', self.make_wall())
        room2.set_side('West', door)


class BoomedWall(Wall):
    """
    一面被炸毁的墙，此处仅为示例
    """
    def __init__(self):
        super(BoomedWall, self).__init__()


class RoomWithBomb(Room):
    """
    一个带炸弹的房间，此处仅为示例
    """
    def __init__(self, room_no):
        super(RoomWithBomb, self).__init__(room_no)


class BombedMazeGame(MazeGame):
    def make_wall(self):
        return BoomedWall()

    def make_room(self, room_no):
        return RoomWithBomb

