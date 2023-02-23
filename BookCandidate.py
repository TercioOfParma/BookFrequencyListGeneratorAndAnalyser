import copy
import random

class BookCandidate:
	def __init__(self, books, freq_dict):
		self.order = self.generate_random_order(books)
		self.path_and_scores = {}
		self.absolute_frequencies = {} #This is the word count of every word so far
		self.travelling_frequency = copy.deepcopy(freq_dict)
		random.shuffle(self.order)
		self.total_difficulty = 0
		i = 0
		for key in self.order:
			self.path_and_scores[key] = books[key].generate_distance_score(self.travelling_frequency)
			self.update_absolute_frequencies(books[key].unique_words)
			self.strip_learnt_words()
			self.total_difficulty += self.path_and_scores[key]
			i = i + 1
		print(f"{self.total_difficulty}, {self.order}")
	
	def generate_random_order(self, books):
		order = []
		for book in list(books.keys()):
			order.append(book)
		random.shuffle(order)
		return order
	def update_absolute_frequencies(self, book_freq_dict):
		for word in book_freq_dict:
			if word in self.absolute_frequencies:
				self.absolute_frequencies[word] += book_freq_dict[word]
			else:
				self.absolute_frequencies[word] = book_freq_dict[word]
	
	def strip_learnt_words(self):
		keys = list(self.travelling_frequency.keys())
		for word in keys:
			if self.travelling_frequency[word] >= 12:
				del self.travelling_frequency[word]
