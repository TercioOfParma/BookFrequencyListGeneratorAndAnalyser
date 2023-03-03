from math import sqrt

class Book:
	def __init__(self, name):
		self.name = name
		self.word_count = 0
		self.unique_count = 0 #May Add grammatical features later 
		self.unique_words = {} 
		self.freq_dict = {}
		self.learnt_alone = 0
		self.no_sentences = 0
		self.no_clauses = 0 #Those divided by commas
		self.average_sentence_length = 0
		self.average_clause_length = 0
		self.aggregate_difficulty = 0 #This is the combined total of all of the words
		self.difficulty_score = 0 #I might remove proper nouns later, not sure
		self.learnt_twice = 0
		self.uncommon_words = 0
		self.proportion_known = 0
		self.known_words = 0
	def generate_difficulty_score(self):
		self.difficulty_score = (((self.aggregate_difficulty / self.word_count) * self.average_sentence_length) + (self.uncommon_words / self.word_count)) * (1 - self.proportion_known)
		
	def generate_learnt_words(self):
		for word in self.unique_words:
			if self.unique_words[word] >= 12:
				self.learnt_alone = self.learnt_alone + 1
			if self.unique_words[word] >= 6:
				self.learnt_twice += 1
				
	def generate_freq_dict(self):
		sorted_unique = sorted(self.unique_words.items() , key=lambda x:x[1], reverse=True)
		i = 1
		for word in sorted_unique:
			index = word[0]
			self.freq_dict[index] = i
			i += 1
			
	def generate_distance_score(self, template_dict): #Template dict is the big frequency dict that we care about
		score = 0 
		for word in self.freq_dict:
			if word in template_dict:
				base_diff = template_dict[word] - self.freq_dict[word]
				score += sqrt(base_diff * base_diff)
			else:
				score += 200 #40,000th word
		return score
