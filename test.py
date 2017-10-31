from operator import itemgetter


class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

	def insert(self, x):
		if x <= self.val:
			if self.left is None:
				self.left = TreeNode(x)
			else:
				self.left.insert(x)
		else:
			if self.right is None:
				self.right = TreeNode(x)
			else:
				self.right.insert(x)

	def toString(self):
		output = ""
		if self.left:
			output += self.left.toString()

		output += str(self.val),

		if self.right:
			output += self.right.toString()

		return output


class BinaryTree(object):
	def __init__(self, x):
		if x:
			self.root = TreeNode(x)
		else:
			self.root = None

	def insert(self, x):
		if self.root is None:
			self.root = self.__init__(x)
		else:
			self.root.insert(x)

	def __str__(self):
		if self.root:
			return self.root.toString()
		else:
			return ""


class ListNode(object):
	def __init__(self, x):
		self.val = x
		self.next = None

	def __str__(self):
		current = self
		output = ""

		while current is not None:
			output += str(current.val) + " -> "
			current = current.next

		output += "END"
		return output


def create_list(values):
	if values:
		head = ListNode(values[0])
		current = head
		for value in values[1:]:
			current.next = ListNode(value)
			current = current.next

		return head
					
	
	
a = create_list([1,5,10,20,30,44])
b = create_list([18, 23, 26, 27, 56])
c = create_list([6, 25, 36, 37, 40, 46])

lists = [a,b,c]


#newList = sorted(lists, key=lambda node: node.val)

tree = BinaryTree(None)

for list in lists:
	current = list
	while current is not None:
		tree.insert(current.val)
		current = current.next

print tree
