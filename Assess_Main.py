import os 
import Helper
from BookCandidate import BookCandidate
import sys

folder = "Books"
dict_filename = "frequencies.csv"
if len(sys.argv) > 1:
	if "IS_HASH_SPLIT" in sys.argv[1]:
		split_filename = sys.argv[2]
		folder = sys.argv[3]
		dict_filename = sys.argv[4]
		books = {}
		with open(split_filename, "r") as split_file:
			index = "Preface.txt"
			books[index] = ""
			for line in split_file:
				if "#####" in line:
					index = line.replace("#####","").replace("\n","").replace(","," ") + "txt"
					books[index] = ""
				else:
					books[index] += line
			for filename in books.keys():
				if books[filename] != "":
					to_save = open(folder + "/" + filename, "w")
					to_save.write(books[filename])
					to_save.close()	
	else:
		folder = sys.argv[1]
		dict_filename = sys.argv[2]

os.chdir(folder)
books_to_assess = os.listdir()
os.chdir("..")
frequency_dict = Helper.load_freq_dict(dict_filename)
os.chdir(folder)
books = {}
for title in books_to_assess:
	books[title] = Helper.assess_book(title, frequency_dict)
os.chdir("..")
Helper.output_books(books, "Difficulty_analysis_" + folder + ".csv")
