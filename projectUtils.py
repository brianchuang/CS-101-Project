from py_expression_eval import Parser
import numpy
class Evaluator: 

	def __init__(self, func = 'x'): 
		self.parser = Parser()
		self.expr   = self.parser.parse(func)

	def toString(self): 
		self.expr.toString()

	def getVariableList(self): 
		return self.expr.variables()

	def evaluate(self, vars): 
		return self.parser.evaluate(self.expr.toString(), vars)

class Datifier: 

	def __init__(self, lowerBound = -10, upperBound = 10, pace = 1, evaluator = Evaluator()):
		self.pace = pace
		self.lowerBound = lowerBound
		self.upperBound = upperBound
		self.evaluator = evaluator
		self.points = []

	def fillPoints(self):
		arg = self.evaluator.getVariableList()[0]
		for x in numpy.arange(self.lowerBound, self.upperBound, self.pace):
			self.points.append(self.evaluator.evaluate({arg: x}))
		return self.points

class MusicMapper: 

	def __init__(self): 
		self.MUSIC_SCALE = ['C', 'D', 'E', 'F', 'G', 'A', 'B']

	def transformToMusic(self, dataPoints, transform = Evaluator(), start = 'A'):
		deltaList = []
		arg = transform.getVariableList()[0]

		for index in range(len(dataPoints)-1):
			point1 = dataPoints[index]
			point2 = dataPoints[index + 1]
			deltaList.append(point2 - point1)

		transformedPoints = []
		for delta in deltaList:
			transformedPoints.append(transform.evaluate({arg: delta}))

		scale = max(transformedPoints) - min(transformedPoints)
		musicMap = []
		currentNote = self.MUSIC_SCALE.index(start)
		for point in transformedPoints:
			currentNote+= point
			musicMap.append( self.MUSIC_SCALE[int(currentNote)%len(self.MUSIC_SCALE)] )
			#musicMap.append(point)
		return musicMap
