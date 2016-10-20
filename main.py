from projectUtils import Evaluator, Datifier, MusicMapper
import math
import pysynth as ps
def main():
	evaluator = Evaluator('x')
	print(evaluator.toString())
	datafier = Datifier(lowerBound = -10, upperBound = 10, pace = 1, evaluator = evaluator)
	print(datafier.fillPoints())
	mapper = MusicMapper()
	musicMap = mapper.transformToMusic(datafier.fillPoints())
	ps.make_wav(musicMap, fn = "test.wav")
main()