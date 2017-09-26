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

