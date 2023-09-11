import sys
import diflet
class splitter_callable(sys.modules[__name__].__class__):
	def __init__(self):
		pass
	def __call__(self,encoded,key):
		my_cards=diflet(key)
		split=[]
		my_encoded=encoded
		while len(my_encoded) > 0:
			split.append(my_encoded[:len(my_cards)])
			my_encoded = my_encoded[len(my_cards):]
		return split

if __name__=="__main__":
	print(splitter_callable()(sys.argv[1],sys.argv[2]))
else:
	sys.modules[__name__].__class__ = splitter_callable
