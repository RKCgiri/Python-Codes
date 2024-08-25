import numpy

print("Printing Original array")
sampleArray = numpy.array([[34,43,73],[82,22,12],[53,94,66]]) 
print (sampleArray)

print("Array after deleting column 2 on row")
sampleArray = numpy.delete(sampleArray , 1, axis = 0) 
print (sampleArray)

arr = numpy.array([[10,10,10]])

print("Array after inserting column 2 on row")
sampleArray = numpy.insert(sampleArray , 1, arr, axis = 0) 
print (sampleArray)

print("Array after deleting column 2 on col")
sampleArray = numpy.delete(sampleArray , 1, axis = 1) 
print (sampleArray)

arr = numpy.array([[10,10,10]])

print("Array after inserting column 2 on col")
sampleArray = numpy.insert(sampleArray , 1, arr, axis = 1) 
print (sampleArray)