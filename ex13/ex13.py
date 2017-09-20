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
		"""Another name for push."""
		self.push(obj)

	def unshift(self):
		"""Removes the first item and returns it."""
		pass

	def remove(self, obj):
		pass

	def first(self):
		return self.begin

	def last(self):
		return self.end

	def count(self):
		return self.counter

	def get(self, index):
		"""Get the value at index."""
		pass

	def dump(self, mark):
		"""Debugging function that dumps the contents of the list. Not sure what mark is for"""
		pass

