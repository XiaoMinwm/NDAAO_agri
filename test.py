from data_input import datainput
from trans_label import label
import re

print(','.join(label('0010111111111','1110101111111')))
#[sym, vec]=datainput(9)
#for vector in vec:
#	if not re.match(r'0\d.txt', ''.join(vector)):
#		print(''.join(vector))