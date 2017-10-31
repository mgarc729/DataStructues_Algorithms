def string_compression(string):
	"""Implement a method to perform basic string compression using the counts of repeated characters.

	For example, the string aabcccccaaa would become a2b1c5a3. If the "compressed" string would not become smaller
	than the original string, your method should return the original string. You can assume the string
	has only uppercase and lowercase letters (a - z).

	:param string: string to be compressed
	:return: compressed version of the string
	"""
	output = ""

	last_letter = ''
	count = 0

	for letter in string:
		if letter is not last_letter:
			if last_letter is not "":
				output += str(count)

			count = 0
			output += letter
			last_letter = letter
		count += 1

	output += str(count)


	if len(output) > len(string):
		return string
	else:
		return output

if __name__ == '__main__':
	print string_compression('aabcccccaaa')