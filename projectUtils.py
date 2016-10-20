from py_expression_eval import Parser
import numpy
class Evaluator: 

	def __init__(self, func = 'x'): 
		self.parser = Parser()
		self.expr   = self.parser.parse(func)

	def toString(self):
		return self.expr.simplify({}).toString() 

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