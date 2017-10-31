from itertools import permutations

def permute(word):
	perms = [''.join(p) for p in permutations(word)]
	return perms

def reverse_word(word):
	output = ""
	for index in range(len(word)-1, -1,-1):
		output += word[index]

	return output

def is_Palindrome(word):
	reverse = reverse_word(word)
	return reverse == word

def palindrome_Permutation(word):
	"""Given a string, write a function to check if it is a permutation of a palindrome.

		A palindrome is a word or phrase that is the same forwards and backwards. A permutation is a rearrangement
		of letters.The palindrome does not need to be limited to just dictionary words.

		EXAMPLE
		Input: Tact Coa
		Output: True (permutations: "taco cat". "atco cta". etc.)
	"""
	palindromes = []

	# Calculate every permutation
	permutations = permute(word.strip().replace(" ",""))

	# check permutations for palindrome
	for word in permutations:
		if is_Palindrome(word):
			palindromes.append(word)

	# return results
	return len(palindromes) is not 0


if __name__ == '__main__':
	# print permute('ataat')
	print palindrome_Permutation('aat aat')