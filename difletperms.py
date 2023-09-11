import sys
import difletcnt
import math
def difletperm_func(name):
	cnt=difletcnt(name)	
	return math.factorial(cnt)

class difletperm_callable(sys.modules[__name__].__class__):
	def __call__(self,name):
		return difletperm_func(name)
def main():
	if len(sys.argv) == 2:
		print(difletperm_func(sys.argv[1]))

if __name__ == "__main__":
	main()
else:
	sys.modules[__name__].__class__ = difletperm_callable

