import sys

sys.path.append('/Users/manuelgarciacruz/Documents/Projects/Practice/DataStructures')

from LinkedList import LinkedList

class StringBuilder(object):
	def __init__(self):
		self.string = LinkedList()

	def append(self, value):
		self.string.insert(value)

	def __str__(self):
		output = ""
		current = self.string.head

		while current is not None:
			if current.next is not None:
				output += current.val + " "
			else:
				output += current.val
			current = current.next

		return output

	def toString(self):
		return self.__str__()


if __name__ == '__main__':
	stringBuilder = StringBuilder()
	words = ['en','la','casa','de','tula']

	for word in words:
		stringBuilder.append(word)

	print stringBuilder.toString()
