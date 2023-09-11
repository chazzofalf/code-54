import sys
import math
import diflet
class get_scramble_callable(sys.modules[__name__].__class__):
	def __init__(self):
		pass
	def string_to_chars(self,str):
		chars=[]
		for char in str:
			chars.append(char)
		return chars
	def chars_to_string(self,chars):
		str=""
		for char in chars:
			str=f'{str}{char}'
		return str
	def __call__(self,idx,key):
		my_cards=diflet(key)
		maxf=math.factorial(len(my_cards))
		maxf //= len(my_cards)
		my_picks=[]
		picks_left=len(my_cards)-1
		while picks_left > 0:
			pick_idx=(idx % math.factorial(picks_left+1)) // math.factorial(picks_left)
			my_picks.append(my_cards[pick_idx])
			del my_cards[pick_idx]
			picks_left -= 1
		my_picks.append(my_cards[0])
		return self.chars_to_string(my_picks)

if __name__=="__main__":
	print(get_scramble_callable()(int(sys.argv[1]),sys.argv[2]))
else:
	sys.modules[__name__].__class__ = get_scramble_callable
