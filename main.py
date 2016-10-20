from projectUtils import Evaluator, Datifier, MusicMapper
import math
def main():
	expr = raw_input('Continous function: ')
	lowBound = eval(raw_input('Lower bound: '))
	upBound = eval(raw_input('Upper bound: '))
	incr = eval(raw_input('Increment: '))
	transf = raw_input('Transform function: ')
	evaluator = Evaluator(expr)
	datafier = Datifier(lowerBound = lowBound, upperBound = upBound, pace = incr, evaluator = evaluator)
	mapper = MusicMapper()
	musicMap = mapper.transformToMusic(datafier.fillPoints(), transform = Evaluator('exp(x)'))
	print musicMap
main()