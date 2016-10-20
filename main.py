from projectUtils import Evaluator, Datifier
import math
def main():
	evaluator = Evaluator('sin(x)')
	print(evaluator.toString())
	datafier = Datifier(lowerBound = 0, upperBound = math.pi * 4, pace = math.pi/2, evaluator = evaluator)
	print(datafier.fillPoints())

main()