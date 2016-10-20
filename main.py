from Evaluator import Evaluator
def main():
	evaluator = Evaluator('2*x+2*y')
	print(evaluator.toString())
	varList = {} toString
	for var in evaluator.getVariableList(): 
		varList[var] = 2
	print(evaluator.evaluate(varList))

main()