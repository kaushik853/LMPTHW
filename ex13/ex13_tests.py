from ex13 import *

def test_push():
	colors = SingleLinkedList()
	colors.push("Pthalo Blue")
	assert colors.count() == 1
	colors.push("Ultramarine Blue")
	assert colors.count() == 2

def test_pop():
	colors = SingleLinkedList()
	colors.push("Magenta")
	colors.push("Alizarin")
	assert colors.pop() == "Alizarin"
	assert colors.pop() == "Magenta"
	assert colors.pop() == None

# def test_unshift():
# 	colors = SingleLinkedList()
# 	colors.push("Viridian")
# 	colors.push("Sap Green")
# 	colors.push("Van Dyke")
# 	assert colors.unshift() == "Viridian"
# 	assert colors.unshift() == "Sap Green"
# 	assert colors.unshift() == "Van Dyke"
# 	assert colors.unshift() == None
def test_shift():
	colors = SingleLinkedList()
	colors.shift("Cadmium Orange")
	assert colors.count() == 1
	colors.shift("Carbazole Violet")
	assert colors.count() == 2
	assert colors.pop() == "Cadmium Orange"
	assert colors.count() == 1
	assert colors.pop() == "Carbazole Violet"
	assert colors.count() == 0

# 41    def test_remove():
# 42        colors = SingleLinkedList()
# 43        colors.push("Cobalt")
# 44        colors.push("Zinc White")
# 45        colors.push("Nickle Yellow")
# 46        colors.push("Perinone")
# 47        assert colors.remove("Cobalt") == 0
# 48        colors.dump("before perinone")
# 49        assert colors.remove("Perinone") == 2
# 50        colors.dump("after perinone")
# 51        assert colors.remove("Nickle Yellow") == 1
# 52        assert colors.remove("Zinc White") == 0
# 53
# 54     def test_first():
# 55        colors = SingleLinkedList ()
# 56        colors.push("Cadmium Red Light")
# 57        assert colors.first() == "Cadmium Red Light"
# 58        colors.push("Hansa Yellow")
# 59        assert colors.first() == "Cadmium Red Light"
# 60        colors.shift("Pthalo Green")
# 61        assert colors.first() == "Pthalo Green"
# 62
# 63     def test_last ():
# 64        colors = SingleLinkedList()
# 65        colors.push("Cadmium Red Light")
# 66        assert colors.last() == "Cadmium Red Light"
# 67        colors.push("Hansa Yellow")
# 68        assert colors.last() == "Hansa Yellow"
# 69        colors.shift("Pthalo Green")
# 70        assert colors.last() == "Hansa Yellow"
# 71
# 72     def test_get():
# 73        colors = SingleLinkedList ()
# 74        colors.push("Vermillion")
# 75        assert colors.get(0) == "Vermillion"
# 76        colors.push("Sap Green")
# 77        assert colors.get(0) == "Vermillion"
# 78        assert colors.get(1) == "Sap Green"
# 79        colors.push("Cadmium Yellow Light")
# 80        assert colors.get(0) == "Vermillion"
# 81        assert colors.get(1) == "Sap Green"
# 82        assert colors.get(2) == "Cadmium Yellow Light"
# 83        assert colors.pop() == "Cadmium Yellow Light"
# 84        assert colors.get(0) == "Vermillion"
# 85        assert colors.get(1) == "Sap Green"
# 86        assert colors.get(2) == None
# 87        colors.pop ()
# 88        assert colors.get(0) == "Vermillion"
# 89        colors.pop ()
# 90        assert colors.get(0) == None
