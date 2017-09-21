from ex14 import *

def test_push():
	colors = DoubleLinkedList()
	colors.push("Pthalo Blue")
	assert colors.count() == 1
	colors._invariant()
	colors.push("Ultramarine Blue")
	assert colors.count() == 2
	colors._invariant()

def test_pop():
	colors = DoubleLinkedList()
	colors.push("Magenta")
	colors.push("Alizarin")
	assert colors.pop() == "Alizarin"
	assert colors.pop() == "Magenta"
	assert colors.pop() == None
	colors._invariant()

def test_unshift():
	colors = DoubleLinkedList()
	colors.push("Viridian")
	colors.push("Sap Green")
	colors.push("Van Dyke")
	assert colors.unshift() == "Viridian"
	assert colors.unshift() == "Sap Green"
	assert colors.unshift() == "Van Dyke"
	assert colors.unshift() == None
	colors._invariant()

def test_shift():
	colors = DoubleLinkedList()
	colors.shift("Cadmium Orange")
	assert colors.count() == 1
	colors._invariant()
	colors.shift("Carbazole Violet")
	assert colors.count() == 2
	assert colors.pop() == "Cadmium Orange"
	assert colors.count() == 1
	assert colors.pop() == "Carbazole Violet"
	assert colors.count() == 0
	colors._invariant()

def test_remove():
	colors = DoubleLinkedList()
	colors.push("Cobalt")
	colors.push("Zinc White")
	colors.push("Nickle Yellow")
	colors.push("Perinone")
	assert colors.remove("Cobalt") == 0
	colors._invariant()
	colors.dump("before perinone")
	assert colors.remove("Perinone") == 2
	colors.dump("after perinone")
	assert colors.remove("Nickle Yellow") == 1
	assert colors.remove("Zinc White") == 0
	colors._invariant()

def test_first():
	colors = DoubleLinkedList ()
	colors.push("Cadmium Red Light")
	assert colors.first() == "Cadmium Red Light"
	colors.push("Hansa Yellow")
	assert colors.first() == "Cadmium Red Light"
	colors._invariant()
	colors.shift("Pthalo Green")
	assert colors.first() == "Pthalo Green"
	colors._invariant()

def test_last ():
	colors = DoubleLinkedList()
	colors.push("Cadmium Red Light")
	assert colors.last() == "Cadmium Red Light"
	colors.push("Hansa Yellow")
	assert colors.last() == "Hansa Yellow"
	colors._invariant()
	colors.shift("Pthalo Green")
	assert colors.last() == "Hansa Yellow"
	colors._invariant()

def test_get():
	colors = DoubleLinkedList ()
	colors.push("Vermillion")
	assert colors.get(0) == "Vermillion"
	colors.push("Sap Green")
	assert colors.get(0) == "Vermillion"
	assert colors.get(1) == "Sap Green"
	colors.push("Cadmium Yellow Light")
	assert colors.get(0) == "Vermillion"
	assert colors.get(1) == "Sap Green"
	assert colors.get(2) == "Cadmium Yellow Light"
	assert colors.pop() == "Cadmium Yellow Light"
	assert colors.get(0) == "Vermillion"
	assert colors.get(1) == "Sap Green"
	assert colors.get(2) == None
	colors._invariant()
	colors.pop ()
	assert colors.get(0) == "Vermillion"
	colors.pop ()
	assert colors.get(0) == None
	colors._invariant()