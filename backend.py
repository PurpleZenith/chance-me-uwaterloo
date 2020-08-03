import numpy
import info
import frontend
import matplotlib.pyplot as plt
import math


def setY(program):
    programList = info.programList()
    columnNum = programList.index (program)
    return columnNum


def getPolynomial (x, y,columnNum):
    degree = math.ceil(math.log (info.nonZeroCount(columnNum)))
    z = numpy.polyfit (x,y,degree) # inverse polynomial
    return z


def getPolynomialInverse (x, y,columnNum):
    degree = math.ceil(math.log (info.nonZeroCount(columnNum)))
    zz = numpy.polyfit (y,x,degree) # inverse polynomial
    return zz