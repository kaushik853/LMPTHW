class DoubleLinkedListNode(object):
 
	def __init__(self, value, nxt, prev):
		self.value = value
		self.next = nxt
		self.prev = prev

	def __repr__(self):
		nval = self.next and self.next.value or None
		pval = self.prev and self.prev.value or None
		return f"[{self.value}, {repr(nval)}, {repr(pval)}]"

class DoubleLinkedList(object):

	def __init__(self):
		self.begin = None
		self.end = None
		self.counter = 0

	def push(self, obj):
		"""Append to the end of the list"""
		self._invariant()
		node = DoubleLinkedListNode(obj, None, self.end)
		if self.counter == 0:
			self.begin = self.end = node
		else:
			self.end.next = node
			self.end = node
		self.counter +=1

	def pop(self):
		"""Remove last item and return"""
		self._invariant()
		if not self.end:
			return None
		if self.begin == self.end:
			popped = self.end.value
			self.begin = None
			self.end = None
			self.counter = 0
			return popped
		else:
			popped = self.end
			self.end = self.end.prev
			self.end.next = None
			self.counter -= 1
			return popped.value

	def shift(self, obj):
		"""Append to the begining of a list"""
		self._invariant()
		node = DoubleLinkedListNode(obj, self.begin, None)
		if self.counter == 0:
			self.end = node
		else:
			self.begin.prev = node
		self.counter += 1
		self.begin = node

	def unshift(self):
		"""Removes the first item (from begin) and returns it."""
		self._invariant()
		if not self.begin:
			return None
		if self.begin == self.end:
			shifted = self.begin.value
			self.begin = None
			self.end = None
			self.counter = 0
			return shifted
		else:
			shifted = self.begin.value
			self.begin = self.begin.next
			self.begin.prev = None
			self.counter -= 1
			return shifted

	def detach_node(self, node):
		"""You'll need to use this operation sometimes, but mostly
			inside remove(). It should take a node, and detach it from the
			list, whether the node is at the front, end, or in the middle."""
		self._invariant()
		if node == self.begin == self.end:
			self.begin = None
			self.end = None
		elif node == self.begin:
			node.next.prev = None
			self.begin = node.next
		elif node == self.end:
			node.prev.next = None
			self.end = node.prev
		else:
			node.next.prev = node.prev
			node.prev.next = node.next
		self.counter -= 1

	def remove(self, obj):
		"""Finds a matching item and removes it from the list."""
		self._invariant()
		if not self.begin:
			return None
		node = self.begin
		index = 0
		while node.value != obj:
			if node == self.end:
				return None
			node = node.next
			index +=1
		self.detach_node(node)
		return index

	def first(self):
		"""Returns a *reference* to the first item, does not remove."""
		self._invariant()
		if not self.begin:
			return None
		else:
			return self.begin.value

	def last(self):
		"""Returns a reference to the last item, does not remove."""
		self._invariant()
		if not self.end:
			return None
		else:
			return self.end.value

	def count(self):
		"""Counts the number of elements in the list."""
		return self.counter

	def get(self, index):
		"""Get the value at index."""
		self._invariant()
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
		"""Debugging function that dumps the contents of the list."""
		self._invariant()
		if not self.begin:
			print("Empty")
		else:
			node = self.begin
			print(node)
			while node != self.end:
				node = node.next
				print(node)
				
# 1. Are there zero elements? Then self.begin and self.end need to be None.

# 2. If there is one element, then self.begin and self.end have to be equal (point at same node).

# 3. The first element must always have a prev that is None.

# 4. The last element must always have a next that is None.


	def _invariant(self):
		if self.count() == 0:
			assert self.begin == self.end == None
		elif self.count() == 1:
			assert self.begin == self.end
			assert self.begin.prev == None
			assert self.end.next == None
		else:
			assert self.begin.prev == None
			assert self.end.next == None
