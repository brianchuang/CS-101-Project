from projectUtils import Evaluator, Datafier, MusicMapper
import math
import pysynth as ps
def main():
	expr = raw_input('Continous function: ')
	lowBound = eval(raw_input('Lower bound: '))
	upBound = eval(raw_input('Upper bound: '))
	incr = eval(raw_input('Increment: '))
	transf = raw_input('Transform function: ')
	evaluator = Evaluator(expr)
	datafier = Datafier(lowerBound = lowBound, upperBound = upBound, pace = incr, evaluator = evaluator)
	mapper = MusicMapper()
	musicMap = mapper.transformToMusic(datafier.fillPoints())
	ps.make_wav(musicMap, fn = "test.wav")
main()