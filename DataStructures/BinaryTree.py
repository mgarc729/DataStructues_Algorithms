class BinaryNode(object):
	def __init__(self, val):
		self.val = val
		self.left = None
		self.right = None

	def insert(self, val):

		if val <= self.val:
			if self.left is None:
				self.left = BinaryNode(val)
			else:
				self.left.insert(val)
		else:
			if self.right is None:
				self.right = BinaryNode(val)
			else:
				self.right.insert(val)

	def in_order_traversal(self):
		output = ""

		if self.left is not None:
			output += self.left.in_order_traversal()

		output += str(self.val) + " "

		if self.right is not None:
			output += self.right.in_order_traversal()

		return output

	def pre_order_traversal(self):
		output = ""

		output += str(self.val) + " "

		if self.left is not None:
			output += self.left.pre_order_traversal()

		if self.right is not None:
			output += self.right.pre_order_traversal()
		return output


	def post_order_traversal(self):
		output = ""

		if self.left is not None:
			output += self.left.pre_order_traversal()

		if self.right is not None:
			output += self.right.pre_order_traversal()

		output += str(self.val) + " "

		return output


class BinaryTree(object):
	def __init__(self):
		self.root = None

	def insert(self, val):
		new_node = BinaryNode(val)

		if self.root is None:
			self.root = new_node
		else:
			self.root.insert(val)


	def delete(self, val):
		pass

	def search(self, val):
		pass

	def in_order_traversal(self):
		return self.root.in_order_traversal()

	def pre_order_traversal(self):
		return self.root.pre_order_traversal()

	def post_order_traversal(self):
		return self.root.post_order_traversal()


if __name__ == "__main__":
	test_node = BinaryNode(10)

	test_node.insert(5)
	test_node.insert(15)
	test_node.insert(13)
	test_node.insert(20)

	print test_node.in_order_traversal()
	print test_node.pre_order_traversal()
	print test_node.post_order_traversal()