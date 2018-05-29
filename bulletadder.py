#! python3
#bullet adder -adds bullets before lines

import pyperclip
pyperclip.copy('hello dear\n what\n')
	
text = pyperclip.paste()

#seperate lines 
lines = text.split('\n')
for i in range(len(lines)):
	lines[i] = '*'+lines[i]
text = '\n'.join(lines)
pyperclip.copy(text)
