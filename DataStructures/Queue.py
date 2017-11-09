from LinkedList import LinkedList


class Queue(object):
	"""Basic implementation of a Queue structure

		Attributes:
			queue_list: holds the LinkedList used to implement the Queue

	"""
	def __init__(self):
		"""Default Constructor

			It creates an empty queue.
		"""
		self.queue_list = LinkedList()

	def add(self, value):
		"""Adds an element to the queue."""
		self.queue_list.insert(value)

	def peek(self):
		"""Returns the first element in the queue"""
		if self.is_empty():
			return None

		return self.queue_list.head.val

	def remove(self):
		"""Removes the next element in the queue and returns its value."""
		if self.is_empty():
			raise Exception("Queue is empty")

		return self.queue_list.delete(0)

	def is_empty(self):
		"""Checks whether the queue is empty or not"""
		return self.queue_list is None

	def __str__(self):
		"""Specifies how to print the queue

			The printing of the queue looks like:
			=( a b c d )=>

			where a,b,c,d are elements in the queue and "d" is the first in the queue.
		"""
		output = ""

		current = self.queue_list.head

		while current is not None:
			output = str(current.val) + " " + output

			current = current.next

		output = "=( " + output + ")=>"
		return output


if __name__ == '__main__':
	# Some test cases

	# Queue Creation
	queue = Queue()

	# Inserting some elements to the queue
	queue.add(1)
	queue.add(2)
	queue.add(3)
	queue.add(4)
	queue.add(5)
	queue.add(6)

	# Check that the elements has been inserted
	print queue

	# Check peek method
	print queue.peek()

	# Check remove method
	print queue.remove()

	print queue



