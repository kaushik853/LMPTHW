from ex14 import DoubleLinkedList

class Dictionary(object):
	'''
	Transcription of Zed's prototype dictionary class
	Terms: 
	bucket = a list within the Map list that contains key value pairs
	slot = a key value pair within a bucket
	node = any generic node within a DoubleLinkedList
	'''
	def __init__(self,num_buckets=256):
		'''Initialize a map with num_buckets number of buckets.
		Basically a list of lists'''
		self.map = DoubleLinkedList()
		for i in range(0, num_buckets):
			self.map.push(DoubleLinkedList())

	def hash_key(self, key):
		'''Take a key and create a number, then convert it to 
		an index for the Map's buckets.
		Basically creates a randomized index for each key'''
		return hash(key) % self.map.count()

	def get_bucket(self, key):
		'''Given a key, find the bucket where it lives'''
		bucket_id = self.hash_key(key)
		print("get_bucket() calling get() on",self.map, "with",bucket_id)
		return self.map.get(bucket_id)

	def get_slot(self, key, default=None):
		'''return the bucket and node (key,value) for a given key
		Hmmm, the 'default' parameter never gets used'''

		print("get_slot() calling get_bucket() with",self,key)
		bucket = self.get_bucket(key)

		if bucket:
			node = bucket.begin
			#Not sure why an index is needed, since it's never
			#used later
			i = 0

			while node:
				if key == node.value[0]:
					return bucket, node
				else:
					node = node.next
					i += 1

		return bucket, None

	def get(self, key, default=None):
		'''Take a key and get the its full slot and value, or the default
		Hmmmm, Zed's code ends with "or node" which doesn't make
		sense to me. Changed to "or default"'''
		print("get() calling get_slot() with",self, key)
		bucket, node = self.get_slot(key, default=default)
		return node and node.value[1] or default

	def set(self, key, value):
		'''Set a key to the given value, replacing any old values'''
		bucket, slot = self.get_slot(key)

		if slot:
			'''key already exists, replace it'''
			'''Why does Zed use python builtin lists here, rather than the
			DoubleLinkedLists we've been using?'''
			slot.value = (key, value)
		else:
			bucket.push((key,value))

	def delete(self, key):
		'''Deletes a given key from the map'''
		bucket = self.get_bucket(key)
		node = bucket.begin

		while node:
			k, v = node.value
			if key == k:
				bucket.detach_node(node)
				break

	def list(self):
		'''Prints out the map'''
		bucket_node = self.map.begin
		while bucket_node:
			slot_node = bucket_node.value.begin
			while slot_node:
				print(slot_node.value)
				slot_node = slot_node.next
			bucket_node = bucket_node.next




