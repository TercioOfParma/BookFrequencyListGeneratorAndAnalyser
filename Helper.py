from Book import Book
from BookCandidate import BookCandidate

def assess_book(filename, frequency_dictionary):
	to_save = Book(filename)
	frequency_reduces_difficulty = True
	total_clause_lengths = 0
	total_sentence_lengths = 0
	current_clause = 0
	current_sentence = 0
	no_sentences = 0
	no_clauses = 0 
	with open(filename, "r") as book_assess:
		for line in book_assess:
			line_length = line.split(" ")
			for word in line_length:
				if "." in word or "!" in word or "?" in word or ":" in word or ";" in word:
					total_sentence_lengths += current_sentence + 1
					total_clause_lengths += current_clause + 1
					current_sentence = 0
					current_clause = 0
					no_sentences += 1
					no_clauses +=1
				else:
					current_sentence += 1
				if "," in word or "\"" in word:
					total_clause_lengths += current_clause + 1
					current_clause = 0
					no_clauses += 1
				else:
					current_clause += 1
			
			to_save.no_sentences = no_sentences	
			to_save.no_clauses = no_clauses	
			if no_sentences != 0:
				to_save.average_sentence_length = total_sentence_lengths / no_sentences
			if no_clauses != 0:
				to_save.average_clause_length = total_clause_lengths / no_clauses
			cleaned = clean_string(line)
			while "" in cleaned:
				cleaned.remove("")
			for word in cleaned:
				#word = word.replace("u","v")
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
	return f"{book.name}, {book.word_count}, {book.unique_count}, {book.difficulty_score}, {book.learnt_alone}, {book.learnt_twice}, {book.average_sentence_length}, {book.average_clause_length}\n"
	
def output_books(books, output_name):
	with open(output_name, "w") as output:
		output.write("Name,Word Count,Unique Count, Difficulty Score,Words Learnt with only this book, Words learnt if read twice, Average Sentence Length, Average Clause Length\n")
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
	string = string.replace('>'," ")
	string = string.replace('<'," ")
	string = string.replace('['," ")
	string = string.replace(']'," ")
	string = string.replace('*'," ")
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
