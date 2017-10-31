class ListNode(object):
	def __init__(self, x):
		self.val = x
		self.next = None
		self.count = 0

	def __str__(self):
		current = self
		output = ""

		while current is not None:
			output += str(current.val) + " -> "
			current = current.next

		output += "END"
		return output


class LinkedList(object):
	"""Linked List Implementation

		This class implements the basics of a linked list.

	"""
	def __init__(self):
		self.head = None
		self.last = self.head
		self.count = 0

	def insert(self, value):

		if isinstance(value, ListNode):
			newNode = value
		else:
			newNode = ListNode(value)

		if self.head is None:
			self.head = newNode
			self.last = self.head
		else:
			self.last.next = newNode
			self.last = self.last.next

		self.count += 1

		return newNode

	def delete(self, index):
		if self.is_empty():
			raise IndexError("List is empty.")

		if index > self.count - 1:
			raise IndexError("Out of boundary index.")

		if index == 0:
			value = self.head.val
			self.head = self.head.next
			self.count -= 1
			return value

		aux = None
		current = self.head
		count = 0
		while current is not None:
			if count == index:
				value = current.val
				aux.next = current.next
				self.count -= 1
				return value

			count += 1
			aux = current
			current = current.next

	def is_empty(self):
		return self.count == 0;

	def __getitem__(self, item):
		if item >= self.count:
			raise IndexError("Out of range.")

		current_index = 0
		current = self.head

		while current is not None:
			if current_index == item:
				return current.val

			current_index += 1
			current = current.next

	def __str__(self):
		output = ""
		current = self.head

		while current is not None:
			output += str(current.val) + " -> "
			current = current.next

		output += "END"
		return output

	def k_to_last(self, k):
		if k is 0:
			raise ValueError("K value has to be greater than 1.")
		count = 0
		current = self.head
		k_th_element = self.head

		while current is not None:
			if count > k - 1:
				k_th_element = k_th_element.next

			count += 1
			current = current.next

		if count < k:
			raise ValueError("The K element is bigger than the size of the list.")

		return k_th_element.val

	def delete_middle(self):
		"""Deletes the middle node in the link list

		Finds the middle node in the link list and deletes it in O(n) time.

		:return:
		"""
		if self.head is None:
			raise ValueError("Cannot find an element in an empty list")

		current = self.head
		mid_index = 0
		count = 0
		aux = None
		mid = self.head

		while current is not None:
			if mid_index < int(count/2):
				aux = mid
				mid = mid.next
				mid_index += 1
			count += 1
			current = current.next

		if aux is None:
			self.head = self.head.next
		else:
			aux.next = mid.next

		del mid

	def intersects_n_2(self, second_list):
		if not isinstance(second_list, LinkedList):
			raise ValueError("The argument has to be a LinkedList")
		current = self.head

		while current is not None:
			current_2 = second_list.head
			while current_2 is not None:
				if current is current_2:
					return current
				current_2 = current_2.next

			current = current.next

		return None

	def intersects_n(self, second_list):
		if not isinstance(second_list, LinkedList):
			raise ValueError("The argument has to be a LinkedList")
		current = self.head
		ids = {}

		while current is not None:
			ids[id(current)] = id(current)
			current = current.next

		current = second_list.head
		while current is not None:
			try:
				ids[id(current)]
				return current
			except KeyError:
				pass
			current = current.next
		return None


# test cases
if __name__ == "__main__":
	myList = LinkedList()

	myList.insert(1)
	myList.insert(2)
	myList.insert(3)
	myList.insert(4)
	myList.insert(5)
	node = myList.insert(6)
	myList.insert(7)
	myList.insert(8)
	myList.insert(9)
	myList.insert(10)
	# myList.insert(11)

	myList_2 = LinkedList()
	myList_2.insert(11)
	myList_2.insert(22)
	myList_2.insert(33)
	myList_2.insert(44)
	myList_2.insert(55)
	myList_2.insert(66)
	node_2 = myList_2.insert(node)


	myList.delete(0)

	print myList
	myList.delete(2)

	print myList