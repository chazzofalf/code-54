import sys
import ast
class joiner_callable(sys.modules[__name__].__class__):
	def __init__(self):
		pass
	def __call__(self,listx):
		out="".join(listx)
		return out

if __name__=="__main__":
	print(joiner_callable()(ast.literal_eval(sys.argv[1])))
else:
	sys.modules[__name__].__class__ = joiner_callable
