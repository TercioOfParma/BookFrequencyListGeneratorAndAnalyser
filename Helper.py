from Book import Book
from BookCandidate import BookCandidate

def assess_book(filename, frequency_dictionary):
	to_save = Book(filename)
	frequency_reduces_difficulty = True
	with open(filename, "r") as book_assess:
		for line in book_assess:
			cleaned = clean_string(line)
			while "" in cleaned:
				cleaned.remove("")
			for word in cleaned:
				new_difficulty = 0 
				to_save.word_count = to_save.word_count + 1
				if not word in frequency_dictionary:
					frequency_dictionary[word] = 4000 #Make it a somewhat difficult word
				if not word in to_save.unique_words:
					to_save.unique_words[word] = 1 #This adds it to a dictionary to scale difficulty of words
					to_save.unique_count = to_save.unique_count + 1
					new_difficulty = frequency_dictionary[word]
				elif word in to_save.unique_words:
					to_save.unique_words[word] = to_save.unique_words[word] + 1
					if frequency_reduces_difficulty:
						new_difficulty = frequency_dictionary[word] / to_save.unique_words[word]
					else:
						new_difficulty = frequency_dictionary[word]
				to_save.aggregate_difficulty = to_save.aggregate_difficulty + new_difficulty
		to_save.generate_difficulty_score()
		to_save.generate_learnt_words()
		to_save.generate_freq_dict()
	return to_save


def generate_book_csv_line(book):
	return f"{book.name}, {book.word_count}, {book.unique_count}, {book.difficulty_score}, {book.learnt_alone}, {book.learnt_twice}\n"
	
def output_books(books, output_name):
	with open(output_name, "w") as output:
		output.write("Name,Word Count,Unique Count, Difficulty Score,Words Learnt with only this book, Words learnt if read twice\n")
		for title in books:
			output.write(generate_book_csv_line(books[title]))
		output.close()
		
def load_freq_dict(filename):
	frequencies = {}
	with open(filename, "r") as freq_dict:
		first_line = False
		for line in freq_dict:
			sections = line.split(',')
			if first_line:
				key = sections[0]
				value = sections[1].replace('\n','')
				frequencies[key] = int(value)
			first_line = True
	return frequencies 
	
	
def clean_string(string):
	string = string.replace(','," ")
	string = string.replace('#',"")
	string = string.replace('.'," ")
	string = string.replace(':'," ")
	string = string.replace(';'," ")
	string = string.replace('\"'," ")
	string = string.replace('\''," ")
	string = string.replace('.'," ")
	string = string.replace(','," ")
	string = string.replace('\r'," ")
	string = string.replace('\n'," ")
	string = string.replace('!'," ")
	string = string.replace('?'," ")
	string = string.split(" ")

	return string
