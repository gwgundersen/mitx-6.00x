import unittest
import random
import __builtin__

import ps7

'''
class Problem_1(unittest.TestCase):
    def test_1(self):
        -Check if Position objects are created with floats
        -Check if the random.seed function isn't being called
    def test_2(self):
        -Check if the first tile is cleaned
        -Check if the direction is being defined before position
        -Check if the direction is being returned as an integer
    def test_3(self):
        -Check if random.randint isn't called with end at 360
        -Check if the round function isn't being called

class Problem_2(unittest.TestCase):
    def test_1(self):
        -Check if the direction is being changed a single time 
        in updatePositionAndClean() method
        -Check if the setRobotDirection() method is being called 
        on the updatePositionAndClean() method
    def test_2(self):
        -Check if the robot is cleaning the new tile it's moving to, 
        rather than the old tile it's moving from
        -Check if the updatePositionAndClean() method is changing the 
        robot's position
class Problem_3(unittest.TestCase):
    def test_1(self):
        -Check if return value for runSimulation() is a float
        -Check if room is being reset after each trial
'''

class Problem_1(unittest.TestCase):
    def test_1(self):
        '''
        -Check if Position objects are created with floats
        -Check if the random.seed function isn't being called
        '''
        temp_init = ps7.Position.__init__
        def custom_init(*args):
            test = isinstance(args[1], float) and isinstance(args[2], float)
            msg = 'A Position object must be created using floats.'
            self.assertTrue(test, msg)
            return temp_init(*args)
        ps7.Position.__init__ = custom_init

        temp_seed = random.seed
        def custom_seed(*args):
            msg = 'The random.seed function must not be used.'
            self.assertTrue(False, msg)
            return temp_seed(*args)
        random.seed = custom_seed

        room = ps7.RectangularRoom(8, 8)
        robot = ps7.StandardRobot(room, 1.0)
        room.getRandomPosition()
        reload(random)
        reload(ps7)

    def test_2(self):
        '''
        -Check if the first tile is cleaned
        -Check if the direction is being defined before position
        -Check if the direction is being returned as an integer
        '''
        temp_method = ps7.RectangularRoom.getRandomPosition
        random_state = random.getstate()
        def custom_method(*args):
            test = random.getstate() != random_state
            msg = ('In the Robot class you need to define ' + 
                   'the direction before the position.')
            self.assertTrue(test, msg)
            return temp_method(*args)
        ps7.RectangularRoom.getRandomPosition = custom_method

        room = ps7.RectangularRoom(8, 8)
        robot = ps7.StandardRobot(room, 1.0)
        pos = robot.getRobotPosition()
        x = int(pos.getX())
        y = int(pos.getY())
        test = room.isTileCleaned(x, y)
        msg = ('The tile the robot is first put on ' + 
               'must be cleaned during creation.')
        self.assertTrue(test, msg)

        direction = robot.getRobotDirection()
        test = isinstance(direction, int)
        msg = ('The direction should be an integer.')
        self.assertTrue(test, msg)
        reload(ps7)

    def test_3(self):
        '''
        -Check if random.randint isn't called with end at 360
        -Check if the round function isn't being called
        '''
        temp_function = random.randint
        def custom_function(*args):
            test = args[1] != 360
            msg = ('The random.randint() function includes the end in ' + 
                   'the results. You only need directions from 0 to 359.')
            self.assertTrue(test, msg)
            return temp_function(*args)
        random.randint = custom_function

        temp_builtin = __builtin__.round
        def custom_builtin(*args):
            msg = ('You shouldn\'t be using the round() function. It can ' + 
                   'distort the results enough to fail the checker.')
            self.assertTrue(False, msg)
            return temp_builtin(*args)
        __builtin__.round = custom_builtin

        room = ps7.RectangularRoom(8, 8)
        robot = ps7.StandardRobot(room, 1.0)
        reload(random)
        reload(__builtin__)

class Problem_2(unittest.TestCase):
    def test_1(self):
        '''
        -Check if the direction is being changed a single time 
        in updatePositionAndClean() method
        -Check if the setRobotDirection() method is being called 
        on the updatePositionAndClean() method
        '''
        temp_method = ps7.StandardRobot.setRobotDirection
        self.count = 0
        def custom_method(*args):
            self.count += 1
            return temp_method(*args)
        ps7.StandardRobot.setRobotDirection = custom_method

        room = ps7.RectangularRoom(8, 8)
        robot = ps7.StandardRobot(room, 1.0)
        for _ in range(room.getNumTiles()):
            robot.updatePositionAndClean()
            if self.count != 0:
                break
        else:
            msg = ('The setRobotDirection() method isn\'t being ' + 
                   'called on the updatePositionAndClean() method.')
            self.assertTrue(False, msg)
        test = self.count == 1
        msg = ('In the updatePositionAndClean() method if the position is ' + 
               'invalid you\'re supposed to set a new robot direction and ' + 
               'not move during that step.')
        self.assertTrue(test, msg)
        reload(ps7)

    def test_2(self):
        '''
        -Check if the robot is cleaning the new tile it's moving to, 
        rather than the old tile it's moving from
        -Check if the updatePositionAndClean() method is changing the 
        robot's position
        '''
        room = ps7.RectangularRoom(8, 8)
        robot = ps7.StandardRobot(room, 1.0)
        pos = robot.getRobotPosition()
        for _ in range(room.getNumTiles()):
            robot.updatePositionAndClean()
            if pos != robot.getRobotPosition():
                break
        else:
            msg = ('The updatePositionAndClean() method isn\'t ' + 
                   'changing the robot\'s position.')
            self.assertTrue(False, msg)
        pos = robot.getRobotPosition()
        test = room.isTileCleaned(int(pos.getX()), int(pos.getY()))
        msg = ('In the updatePositionAndClean() method you\'re cleaning ' + 
               'the old tile the robot is moving from, you need to clean ' + 
               'the new tile the robot is moving to.')
        self.assertTrue(test, msg)

class Problem_3(unittest.TestCase):
    def test_1(self):
        '''
        -Check if return value for runSimulation() is a float
        '''
        result = ps7.runSimulation(1, 1.0, 2, 2, 0.5, 2, ps7.StandardRobot)
        test = isinstance(result, float)
        msg = ('The runSimulation() function must return a float')
        self.assertTrue(test, msg)

    def test_2(self):
        '''
        -Check if room is being reset after each trial
        '''
        temp_method = ps7.RectangularRoom.__init__
        self.count = 0
        def custom_method(*args):
            self.count += 1
            return temp_method(*args)
        ps7.RectangularRoom.__init__ = custom_method

        ps7.runSimulation(1, 1.0, 2, 2, 0.5, 2, ps7.StandardRobot)
        test = self.count > 1
        msg = ('The RectangularRoom object is only being created once, ' + 
               'you\'re probably not resetting the room after each trial.')
        self.assertTrue(test, msg)
        reload(ps7)

if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(Problem_1))
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(Problem_2))
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(Problem_3))
    unittest.TextTestRunner(verbosity=2).run(suite)
