from ex14 import DoubleLinkedList

class sorting(object):

	def bubble_sort(numbers):
		'''Slightly optimized bubble sort, recognizing that 
		for each pass n through a list, the nth largest number
		is correctly placed, so we can stop checking the last n-1
		item
		Pseudocode from wikipedia:
		procedure bubbleSort( A : list of sortable items )
		    n = length(A)
		    repeat
		        swapped = false
		        for i = 1 to n-1 inclusive do
		            if A[i-1] > A[i] then
		                swap(A[i-1], A[i])
		                swapped = true
		            end if
		        end for
		        n = n - 1
		    until not swapped
		end procedure
		'''
		n = numbers.count()

		while True:
			swapped = False
			index=1
			node = numbers.begin
			while index < n:
				if node.value > node.next.value:
					node.value, node.next.value = node.next.value, node.value
					swapped = True
				index += 1
				node = node.next
			n -= 1
			#numbers.dump(n)
			if swapped == False:
				return numbers
				break

	def merge_sort(numbers):
		'''
		Pseudocode from wikipedia:
		function merge_sort(list m)
		    if length of m ≤ 1 then
		        return m

		    var left := empty list
		    var right := empty list
		    for each x with index i in m do
		        if i < (length of m)/2 then
		            add x to left
		        else
		            add x to right

		    left := merge_sort(left)
		    right := merge_sort(right)

		    return merge(left, right)
		   '''
		if numbers.count() <= 1:
			return numbers

		left = DoubleLinkedList()
		right = DoubleLinkedList()
		split = numbers.count()/2
		while numbers.count() > 0:
			if split > 0:
				left.push(numbers.unshift())
				split -= 1
			else:
				right.push(numbers.unshift())

		left = sorting.merge_sort(left)
		right = sorting.merge_sort(right)

		return sorting.merge(left, right)

	def merge(left, right):
		'''	   
		function merge(left, right)
		    var result := empty list

		    while left is not empty and right is not empty do
		        if first(left) ≤ first(right) then
		            append first(left) to result
		            left := rest(left)
		        else
		            append first(right) to result
		            right := rest(right)

		    while left is not empty do
		        append first(left) to result
		        left := rest(left)
		    while right is not empty do
		        append first(right) to result
		    right := rest(right)
		return result
		'''
		result = DoubleLinkedList()
		while left.count() > 0 and right.count() > 0:
			if left.begin.value <= right.begin.value:
				result.push(left.unshift())
			else:
				result.push(right.unshift())
		while left.count() > 0:
			result.push(left.unshift())
		while right.count() > 0:
			result.push(right.unshift())
		return result

	def quick_sort(numbers):
		if numbers.count() <= 1:
			return numbers
		result = DoubleLinkedList()

		#There are many different strategies for picking a pivot
		#This allows for flexibility in defining the pivot
		pivot = numbers.end

		#Now send the list to partition() and get back two lists,
		#one that contains values less than, and one that has 
		#values greater than the pivot
		left, right = sorting.partition(numbers, pivot)

		#Prepend the sorted left side to the pivot and append the 
		#sorted right side
		sorting.quick_sort(left)
		while left.count()> 0:
			result.push(left.unshift())
		result.push(pivot)
		sorting.quick_sort(right)
		while right.count() > 0:
			result.push(right.unshift())
		return result

	def partition(numbers, pivot):
		
		'''The original partition scheme described by C.A.R. Hoare 
		uses two indices that start at the ends of the array being 
		partitioned, then move toward each other, until they detect 
		an inversion: a pair of elements, one greater than or equal 
		to the pivot, one lesser or equal, that are in the wrong 
		order relative to each other. The inverted elements are 
		then swapped'''

		left = DoubleLinkedList()
		right = DoubleLinkedList()

		numbers.detach_node(pivot)
		i = numbers.begin
		j = numbers.end

		while True:
			while i.value <= pivot.value:
				if i == numbers.end:
					break
				i = i.next
	
			while j.value >= pivot.value:
				if j == numbers.begin:
					break
				j = j.prev

		#Trying to avoid having to tack on index numbers to my
		#double linked lists. Using a "position()" function to 
		#calculate the position instead

			if sorting.position(numbers, i) < sorting.position(numbers, j):
				i.value, j.value = j.value, i.value
			else:
				if i.value > pivot.value:
					split = sorting.position(numbers, i) -1
				else:
					split = sorting.position(numbers, i)

				while numbers.count() >0:
					if split > 0:
						print("split=",split,"num=",numbers.begin)
						left.push(numbers.unshift())
						split -=1
					else:
						print("split=",split,"num=",numbers.begin)
						right.push(numbers.unshift())
				break

		return left, right

	def position(numbers, node):
		print("Node passed to position=",node)
		index = 1
		place = numbers.begin
		while node != place:
			place = place.next
			index +=1
		return index
		


