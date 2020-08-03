import frontend
import backend
import info
import pandas
import numpy

# gets the score and program of the person
data= frontend.score()
score = data[0]
program = data[1]

# searches the list of programs and gets the columnNum
columnNum = backend.setY(program)

# sets x to be the number of entries 
x = numpy.arange(0,info.nonZeroCount(columnNum))

# sets y to be the entire column of data
y = info.returnData(columnNum)

# get the polynomial - this will be graphed
z = backend.getPolynomial (x,y,columnNum)
z1D = numpy.poly1d (z)

# the cPoint is the point at which the applicant is at.
# get the polynomial inverse - we will use the inverse to find the cPoint.
zInverse = backend.getPolynomialInverse (x,y, columnNum)
zInverse1D = numpy.poly1d (zInverse)

score = float (score)

# get the antiderivative
integral= numpy.polyint(z1D,1)

# get cPoint
cPoint = numpy.polyval (zInverse1D, score)



# evaluate the antiderivative:

# get full area 
fullArea = (numpy.polyval (integral, info.nonZeroCount(columnNum)))- (numpy.polyval (integral, 0))

# get partial area
partArea = (numpy.polyval (integral, cPoint))- (numpy.polyval (integral, 0))

# get the percentage 
percentage = partArea*100/fullArea

# get top and bottom points of the cPoint's line
topPoint = numpy.polyval (z, info.nonZeroCount(columnNum))
bottomPoint = numpy.polyval (z, 0)

# display the plot
frontend.displayPlot (z1D, columnNum, cPoint, topPoint, bottomPoint, percentage, score)


