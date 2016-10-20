from py_expression_eval import Parser
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