#!/usr/bin/python3
# for text files (linefeed/carriage return munging, use rt/wt)
# for binary files (exe, bin, img, gif, jpg use rb/wb)
def filter(input, output):
	for line in input:
		filtered = line.replace("to", "for")
		print("line", filtered, end='')
		output.write(filtered)

readmode = 'r'
writemode = 'w'
file_treatment = 't' # t=>text; b=>binary

with open('workfile', mode=readmode+file_treatment) as in_f:
	with open('copyfile', mode=writemode+file_treatment) as out_f:
		filter(in_f, out_f)
print("bye")
