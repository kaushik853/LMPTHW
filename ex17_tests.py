from ex17 import *

def test_set():
	states = Dictionary()
	states.set('Texas','TX')
	states.set('Illinois','IL')
	assert states.get('Texas') == 'TX'
	assert states.get('Illinois') == 'IL'

def test_get():
	states = Dictionary()
	states.set('Texas','TX')
	states.set('Illinois','IL')
	value = states.get('Texas')
	assert value == 'TX'

def test_get_node():
	states = Dictionary()
	states.set('Texas','TX')
	states.set('Illinois','IL')
	key, value = states.get_node('Illinois')
	assert key == 'Illinois'
	assert value == 'IL'
	key, value = states.get_node('Texas')
	assert key == 'Texas'
	assert value == 'TX'

def test_get_bucket():
	#Pretty much reimplements the function. Need a better way to test
	states = Dictionary()
	states.set('Texas','TX')
	hashed_key = states.hash_key('Texas')
	bucket = states.Map.get(hashed_key)
	assert bucket == states.get_bucket('Texas')

def test_delete():
	states = Dictionary()
	states.set('Texas','TX')
	states.set('Illinois','IL')
	states.delete('Texas')
	assert states.get('Texas') == None

def test_hashes():
	#Pretty much reimplementing the function again
	dict1 = Dictionary(10)
	dict2 = Dictionary(100)
	dict3 = Dictionary(1000)
	Illinois10 = hash('Illinois') % 10
	Illinois100 = hash('Illinois') % 100
	Illinois1000 = hash('Illinois') % 1000
	assert dict1.hash_key('Illinois') == Illinois10
	assert dict2.hash_key('Illinois') == Illinois100
	assert dict3.hash_key('Illinois') == Illinois1000

def test_list():
	#Trying to make the test not depend on the order of the dictionary
	states = Dictionary()
	states.set('Texas','TX')
	states.set('Illinois','IL')
	list1 = states.list()
	a = list1.pop()
	b = list1.pop()
	c = list1.pop()
	d = list1.pop()
	assert a == 'TX' or c == 'TX'
	assert b == 'Illinois' or d == 'Illinois'
