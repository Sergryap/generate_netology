class FlatIterator:
	def __init__(self, s):
		self.s = s

	def __iter__(self):
		self.ind = 0
		return self

	def __next__(self):

		if self.ind == len(self.s):
			raise StopIteration
		if not isinstance(self.s[self.ind], (list, tuple, set)):
			value = self.s[self.ind]
			self.ind += 1
			return value
		else:
			# меняем первоначальные значения перед следующим стэком вызова
			self.s = list(self.s[self.ind]) + self.s[self.ind + 1:]
			self.ind = 0
			return self.__next__()


def flat_generator(s):
	i = 0
	while True:
		if i == len(s):
			break
		if not isinstance(s[i], (list, tuple, set)):
			yield s[i]
			i += 1
		else:
			s = list(s[i]) + s[i + 1:]
			i = 0


nested_list = [{1, (None, True, 'dd')}, (2, [55, ['ff', 'hh', ['mm', 'jjjjj']], 6666]), 777, 10, [55, 77], 'hh']

for item in FlatIterator(nested_list):
	print(item)
print([i for i in FlatIterator(nested_list)])

for item in flat_generator(nested_list):
	print(item)
