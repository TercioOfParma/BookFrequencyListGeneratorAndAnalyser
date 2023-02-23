import Helper
import sys

word_freq = {}
open_file = "vulgata.txt"
save_file = "frequencies_latin.csv"
if sys.argv[1]:
	open_file = sys.argv[1]
if sys.argv[2]: 
	save_file = sys.argv[2]
to_save = open(save_file, 'w')
with open(open_file) as vulgata:
	to_save.write('Word,Frequencies\n')
	for line in vulgata:
		print(line)
		to_analyse = Helper.clean_string(line)
		for word in to_analyse:
			if word in word_freq:
				word_freq[word] = word_freq[word] + 1
			else:
				word_freq[word] = 1

word_freq = sorted(word_freq.items(), key=lambda x: x[1], reverse=True)
i = 1
for word in word_freq:
	if word[0] and word[0] != ' ':
		to_save.write(f"{word[0]},{i}\n")
		i = i + 1
	
to_save.close()

