# 6.00.2x Problem Set 2: Simulating robots

import math
import random

import ps2_visualize
import pylab

# For Python 2.7:
from ps2_verify_movement27 import testRobotMovement

# If you get a "Bad magic number" ImportError, you are not using 
# Python 2.7 and using most likely Python 2.6:


# === Provided class Position
class Position(object):
    """
    A Position represents a location in a two-dimensional room.
    """
    def __init__(self, x, y):
        """
        Initializes a position with coordinates (x, y).
        """
        self.x = x
        self.y = y
        
    def getX(self):
        return self.x
    
    def getY(self):
        return self.y
    
    def getNewPosition(self, angle, speed):
        old_x, old_y = self.getX(), self.getY()
        angle = float(angle)
        # Compute the change in position
        delta_y = speed * math.cos(math.radians(angle))
        delta_x = speed * math.sin(math.radians(angle))
        # Add that to the existing position
        new_x = old_x + delta_x
        new_y = old_y + delta_y
        return Position(new_x, new_y)

    def __str__(self):  
        return "(%0.2f, %0.2f)" % (self.x, self.y)


# === Problem 1
class RectangularRoom(object):
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.cleaned = []
    
    def cleanTileAtPosition(self, pos):
        tile = (math.floor(pos.x), math.floor(pos.y))
        if tile not in self.cleaned:
            self.cleaned.append(tile)

    def isTileCleaned(self, m, n):
        if (m, n) in self.cleaned:
            return True
        else:
            return False
    
    def getNumTiles(self):
        return self.width * self.height

    def getNumCleanedTiles(self):
        return len(self.cleaned)

    def getRandomPosition(self):
        return Position(random.random()*self.width, random.random()*self.height)

    def isPositionInRoom(self, pos):
        if pos.x < self.width and pos.y < self.height and pos.x >= 0 and pos.y >= 0:
            return True
        else:
            return False

# room = RectangularRoom(2,1)
# print "Successfully created a room of size " + str(room.getNumTiles())
# print "Number of clean tiles: " + str(room.getNumCleanedTiles())
# p = room.getRandomPosition()
# print "Random postion at " + str(p)
# print "Position at room: " + str(room.isPositionInRoom(p))
# room.cleanTileAtPosition(p)
# print "There are " + str(room.getNumCleanedTiles()) + " tiles have been cleaned"
# print room.isTileCleaned(math.floor(p.x), math.floor(p.y))

class Robot(object):
    def __init__(self, room, speed):
        self.room = room
        self.speed = speed
        self.pos = room.getRandomPosition()
        room.cleanTileAtPosition(self.pos)
        self.direction = random.choice(range(360))

    def getRobotPosition(self):
        return self.pos
    
    def getRobotDirection(self):
        return self.direction

    def setRobotPosition(self, position):
        self.pos = position

    def setRobotDirection(self, direction):
        self.direction = direction

    def updatePositionAndClean(self):
        raise NotImplementedError # don't change this!

class StandardRobot(Robot):
    def updatePositionAndClean(self):
        # print self.room.getNumCleanedTiles()
        newP = self.pos.getNewPosition(self.direction, self.speed)
        if self.room.isPositionInRoom(newP):
            self.room.cleanTileAtPosition(newP)
            self.setRobotPosition(newP)
        else:
            self.setRobotDirection(random.choice(range(360)))
            self.updatePositionAndClean()

# Uncomment this line to see your implementation of StandardRobot in action!
# testRobotMovement(StandardRobot, RectangularRoom)


# === Problem 3

    

def runSimulation(num_robots, speed, width, height, min_coverage, num_trials,
                  robot_type):
    total = 0
    
    def once():
        # anim = ps2_visualize.RobotVisualization(num_robots, width, height, 0.5)
        room = RectangularRoom(width, height)
        clock = 0
        robots = []
        for i in range(num_robots):
            robots.append(robot_type(room, speed))
        while room.getNumCleanedTiles() < room.getNumTiles()*min_coverage:
            clock += 1
            for robot in robots:
                # anim.update(room, robots)
                robot.updatePositionAndClean()  
        # anim.done()          
        return clock
    for i in range(num_trials):
        total += once()
    return float(total / num_trials)
    
    

# Uncomment this line to see how much your simulation takes on average
# print  runSimulation(1, 1.0, 10, 10, 0.75, 30, StandardRobot)

# runSimulation(2, 1.0, 5, 5, 1, 1, StandardRobot)




# === Problem 4
class RandomWalkRobot(Robot):
    def updatePositionAndClean(self):
        self.setRobotDirection(random.choice(range(360)))
        newP = self.pos.getNewPosition(self.direction, self.speed)
        if self.room.isPositionInRoom(newP):
            self.room.cleanTileAtPosition(newP)
            self.setRobotPosition(newP)
        else:
            self.setRobotDirection(random.choice(range(360)))
            self.updatePositionAndClean()
        
# testRobotMovement(RandomWalkRobot, RectangularRoom)

def showPlot1(title, x_label, y_label):
    """
    What information does the plot produced by this function tell you?
    """
    num_robot_range = range(1, 11)
    times1 = []
    times2 = []
    for num_robots in num_robot_range:
        print "Plotting", num_robots, "robots..."
        times1.append(runSimulation(num_robots, 1.0, 20, 20, 0.8, 20, StandardRobot))
        times2.append(runSimulation(num_robots, 1.0, 20, 20, 0.8, 20, RandomWalkRobot))
    pylab.plot(num_robot_range, times1)
    pylab.plot(num_robot_range, times2)
    pylab.title(title)
    pylab.legend(('StandardRobot', 'RandomWalkRobot'))
    pylab.xlabel(x_label)
    pylab.ylabel(y_label)
    pylab.show()

    
def showPlot2(title, x_label, y_label):
    """
    What information does the plot produced by this function tell you?
    """
    aspect_ratios = []
    times1 = []
    times2 = []
    for width in [10, 20, 25, 50]:
        height = 300/width
        print "Plotting cleaning time for a room of width:", width, "by height:", height
        aspect_ratios.append(float(width) / height)
        times1.append(runSimulation(2, 1.0, width, height, 0.8, 200, StandardRobot))
        times2.append(runSimulation(2, 1.0, width, height, 0.8, 200, RandomWalkRobot))
    pylab.plot(aspect_ratios, times1)
    pylab.plot(aspect_ratios, times2)
    pylab.title(title)
    pylab.legend(('StandardRobot', 'RandomWalkRobot'))
    pylab.xlabel(x_label)
    pylab.ylabel(y_label)
    pylab.show()
    

# showPlot1('title', 'number of robots', 'timespent')
# showPlot2('title', 'ratio', 'time')
