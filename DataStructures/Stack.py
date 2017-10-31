class Stack(object):
	def __init__(self):
		self.stack = []

	def pop(self):
		if not self.is_empty():
			value = self.stack[-1]
			del self.stack[-1]
			return value
		return None

	def peek(self):
		return self.stack[-1]

	def push(self, value):
		self.stack.append(value)

	def is_empty(self):
		return len(self.stack) == 0

	def __str__(self):
		output = ""
		for index in range(len(self.stack) - 1, -1, -1):
			output += str(self.stack[index]) + "\n"

		return output


if __name__ == '__main__':
	stack = Stack()

	stack.push(1)
	stack.push(2)
	stack.push(3)
	stack.push(4)
	stack.push(5)
	stack.push(6)
	stack.push(7)

	print stack

	stack.pop()

	print stack


