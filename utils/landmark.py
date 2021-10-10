import math

MAX_ERROR = 0.5
MIN_OBSERVATIONS = 15 # minimum number of times that a landmark must be observed before its classified as a permanent landmark
LIFE = 50

MAX_RANGE = 1
MAX_SAMPLE = 10 # this is the initial random sample to establish a line trend
MIN_LINE_POINTS = 30 # a line landmark cannot be established unless you have a minimum of 40 points
#RANSAC algorithm
RANSAC_TOLERANCE = 0.05 # the maximum distance a line can be away from a point
RANSAC_CONSENSUS = 30 # the minimum number of points for a line to be established


class Landmark:

    pos = [-1,-1]
    id = -1
    life = LIFE # the number of times that a landmark can not be observed before it expires
    totalTimesObserved = 0 # the number of times the landmark has been observed
    a = -1 # gradient of the line
    b = -1 # y-intercept of the line
    rangeError = 0
    bearingError = 0

    def __init__ (self, x, y):
        self.pos = [x, y]
