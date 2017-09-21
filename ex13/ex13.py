class SingleLinkedListNode(object):

	def __init__(self, value, nxt):
		self.value = value
		self.next = nxt

	def __repr__(self):
		nval = self.next and self.next.value or None
		return f'[{self.value}:{repr(nval)}]'
		
class SingleLinkedList(object):

	def __init__(self):
		self.begin = None
		self.end = None
		self.counter = 0

	def push(self, obj):
		"""Append to the end of the list"""
		node = SingleLinkedListNode(obj, None)
		#print("Counter =", self.counter)
		if self.counter == 0:
			#print("Setting begin to",self.node)
			self.begin = node
		#print("Incrementing counter to", self.counter + 1)
		self.counter += 1
		#print("Setting end to", self.node)
		if self.end:
			self.end.next = node
		self.end = node

	def pop(self):
		"""Remove last item and return"""
		if not self.end:
			return None
		if self.begin == self.end:
			popped = self.end
			self.begin = None
			self.end = None
			self.counter = 0
			return popped.value
		else:
			popped = self.end
			node = self.begin
			while node.next != self.end:
				node = node.next
			self.end = node
			node.next = None
			self.counter -= 1
			return popped.value

	def shift(self, obj):
		"""Append to the begining of a list"""
		node = SingleLinkedListNode(obj, None)
		if self.counter == 0:
			self.end = node
		self.counter += 1
		if self.begin:
			node.next = self.begin
		self.begin = node

	def unshift(self):
		"""Removes the first item and returns it."""
		if not self.begin:
			return None
		if self.begin == self.end:
			shifted = self.begin
			self.begin = None
			self.end = None
			self.counter = 0
			return shifted.value
		else:
			shifted = self.begin
			node = shifted.next
			self.begin = node
			self.counter -= 1
			return shifted.value

	def remove(self, obj):
		if not self.begin:
			return None
		node = self.begin
		index = 0
		while node.value != obj:
			if node == self.end:
				return None
			node = node.next
			index +=1
		if index == 0:
			self.unshift()
			return 0
		if index == self.count() - 1:
			self.pop()
			return index
		else:
			prevNode = self.begin
			while prevNode.next != node:
				prevNode = prevNode.next
			prevNode.next = node.next
			self.counter -= 1
			return index

	def first(self):
		return self.begin.value

	def last(self):
		return self.end.value

	def count(self):
		return self.counter

	def get(self, index):
		"""Get the value at index."""
		if not self.begin:
			return None
		if index > self.count() - 1:
			return None
		node = self.begin
		counter = 0
		while counter < index:
			node = node.next
			counter +=1
		return node.value

	def dump(self, mark):
		"""Debugging function that dumps the contents of the list"""
		print(mark)
		if not self.begin:
			print("Empty")
		else:
			node = self.begin
			print(node)
			while node != self.end:
				node = node.next
				print(node)