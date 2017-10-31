def contained(word_1, word_2):
	"""Checks if word 1 is contained in word 2

		Checks if all the letters from word 1 are in word_2 and in the same cuantities.
		This will assure that they will have only one letter different

	:param word_1: Word with less letters
	:param word_2: Word with more letters
	:return: True if word_1 is contained in word_2. False otherwise
	"""
	last_index = -1

	for letter in word_1:
		found = False
		for index in range(last_index + 1, len(word_2)):
			if letter == word_2[index]:
				last_index = index
				found = True
				break;

		if not found:
			return False

	return True

	pass

def has_one_letter_different(word_1, word_2):
	differences = 0

	for index in range(0, len(word_2)):
		if word_2[index] is not word_1[index]:
			differences += 1

	return (differences is not 0) and differences is 1


def has_one_edit(word_1, word_2):
	"""Verifies if there is an edit between two words

	There are three types of edits that can be performed on strings: insert a character, remove a character,
	or replace a character. Given two strings, write a function to check if they are one edit (or zero edits) away.


	:param word_1:
	:param word_2:
	:return: True if there is an edit between them, False otherwise.
	"""

	if abs(len(word_1) - len(word_2)) > 1:
		return False

	# same length. It means that a replace happened
	if len(word_1) == len(word_2):
		return has_one_letter_different(word_2, word_1)

	# Difference in lenght by 1. This means that a letter was removed or inserted.
	# The word with less letters has to have the same letters that in the word with more.

	if len(word_1) - len(word_1) < 0:	# word_1 has less letters
		return contained(word_1, word_2)
	else:								# word_2 has less letters
		return  contained(word_2, word_1)

if __name__ == '__main__':
	print has_one_edit('baka', 'aka')