import sys
import get_unscramble
# alias for get_unscramble
class unshuffle_callable(sys.modules[__name__].__class__):
	def __init__(self):
		pass
	def __call__(self,shuffle,key):
		return get_unscramble(shuffle,key)

if __name__=="__main__":
	print(unshuffle_callable()(sys.argv[1],sys.argv[2]))
else:
	sys.modules[__name__].__class__ = unshuffle_callable
