import sys
import math
import diflet
class get_unscramble_callable(sys.modules[__name__].__class__):
	def __init__(self):
		pass
	def string_to_chars(self,str):
		chars=[]
		for char in str:
			chars.append(char)
		return chars
	def __call__(self,shuffle,key):
		my_cards=diflet(key)
		my_cards_len=len(my_cards)
		max_number=math.factorial(my_cards_len)
		pick_idxs=[]
		my_shuffle=self.string_to_chars(shuffle)
		for f in shuffle:
			pick_idx=my_cards.index(f)
			pick_idxs.append(pick_idx)
			del my_cards[pick_idx]
			# print(len(my_cards))
		pick_idxs = pick_idxs[:-1]
		# print(pick_idxs)
		# print(len(pick_idxs))
		m=max_number//my_cards_len
		rv=0
		tg=len(pick_idxs)
		for f in pick_idxs:
			rv += f*m
			m //= tg
			tg -= 1
		return rv
	
		
if __name__=="__main__":
	print(get_unscramble_callable()(sys.argv[1],sys.argv[2]))
else:
	sys.modules[__name__].__class__=get_unscramble_callable
