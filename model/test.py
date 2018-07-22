import matlab.engine

engine = matlab.engine.start_matlab()
array = [1,2,3,4,5]
array = matlab.double(array)
a = engine.sum(array, nargout = 1)
print a


