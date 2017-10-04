from ex14 import *

class Dictionary(object):

	def __init__(self, n=256):
		self.Map = DoubleLinkedList()
		for i in range(0,n):
			self.Map.push(DoubleLinkedList())

	def hash_key(self, key):
		return hash(key) % self.Map.count()

	def get(self, key):
		node, value = self.get_node(key)
		return node and value or None

	def get_node(self, key):
		bucket = self.get_bucket(key)
		node = bucket.begin
		while node:
			if node.value.begin.value == key:
				return node.value.begin.value, node.value.end.value
			else:
				node = node.next
		return None, None

	def get_bucket(self, key):
		hashed_key = self.hash_key(key)
		#Uses the DoubleLinkedList get() function to walk the 
		#index of the Map to get the bucket with index equal to 
		#the hash value of the key modulo the number of buckets
		return self.Map.get(hashed_key)

	def set(self, key, value):
		bucket = self.get_bucket(key)
		node = bucket.begin
		#Check to see if the key already exists
		while node:
			if node.value.begin.value == key:
				bucket.detatch_node(node)
				break
			else:
				node = node.next

		#Now, go ahead and add it
		new_node = DoubleLinkedList()
		new_node.push(key)
		new_node.push(value)
		bucket.push(new_node)

	def delete(self, key):
		bucket = self.get_bucket(key)
		node = bucket.begin
		#Check to see if the key exists
		while node:
			if node.value.begin.value == key:
				bucket.detach_node(node)
				break
			else:
				node = node.next

	def list(self):
		dictToList = DoubleLinkedList()
		bucket = self.Map.begin
		while bucket:
			node = bucket.value.begin
			while node:
				dictToList.push(node.value.begin.value) 
				dictToList.push(node.value.end.value)
				node = node.next
			bucket = bucket.next
		return dictToList

