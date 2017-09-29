from ex16 import *
from ex14 import DoubleLinkedList
from random import randint
max_numbers = 30

def random_list(count):
	numbers = DoubleLinkedList()
	for i in range(count, 0, -1):
		numbers.shift(randint(0, 10000))
	return numbers

def presorted_list():
	numbers = DoubleLinkedList()
	numbers.push(1)
	numbers.push(2)
	numbers.push(3)
	numbers.push(4)
	numbers.push(5)
	return numbers

def homogenous_list():
	numbers = DoubleLinkedList()
	numbers.push(1)
	numbers.push(1)
	numbers.push(1)
	numbers.push(1)
	numbers.push(1)
	return numbers

def is_sorted(numbers):
	node = numbers.begin
	while node and node.next:
		if node.value > node.next.value:
			#print("first is", node.value,"next is", node.next.value)
			return False
		else:
			node = node.next
	return True

def test_bubble_sort():
	numbers = random_list(max_numbers)
	#numbers.dump('test_bubble_sort')
	sorting.bubble_sort(numbers)

	assert is_sorted(numbers)

	numbers2 = presorted_list()
	sorting.bubble_sort(numbers2)
	assert is_sorted(numbers2)

	numbers3 = homogenous_list()
	sorting.bubble_sort(numbers3)
	assert is_sorted(numbers3)

def test_merge_sort():
	numbers = random_list(max_numbers)

	sorting.merge_sort(numbers)

	assert is_sorted(numbers)

	numbers2 = presorted_list()
	sorting.merge_sort(numbers2)
	assert is_sorted(numbers2)

	numbers3 = homogenous_list()
	sorting.merge_sort(numbers3)
	assert is_sorted(numbers3)

def test_quick_sort():
	numbers = random_list(max_numbers)

	sorting.quick_sort(numbers)

	assert is_sorted(numbers)

	numbers2 = presorted_list()
	sorting.quick_sort(numbers2)
	assert is_sorted(numbers2)

	numbers3 = homogenous_list()
	sorting.quick_sort(numbers3)
	assert is_sorted(numbers3)