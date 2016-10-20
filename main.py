from projectUtils import Evaluator, Datifier, MusicMapper
import math
def main():
	evaluator = Evaluator('x^2')
	print(evaluator.toString())
	datafier = Datifier(lowerBound = -10, upperBound = 10, pace = 1, evaluator = evaluator)
	print(datafier.fillPoints())
	mapper = MusicMapper()
	musicMap = mapper.transformToMusic(datafier.fillPoints(), transform = Evaluator('exp(x)'))
	print musicMap
main()