#CONTRERAS, Aleianna Clarisse C
from bigtree import Node, list_to_tree

a = Node("A", data={"name": "A"})
b = Node("B", data={"name": "B"}, parent=a)
c = Node("C", data={"name": "C"}, parent=b)
d = Node("D", data={"name": "D"}, parent=b)
e = Node("E", data={"name": "E"}, parent=d)
f = Node("F", data={"name": "F"}, parent=d)
g = Node("G", data={"name": "G"}, parent=a)
h = Node("H", data={"name": "H"}, parent=g)
i = Node("I", data={"name": "I"}, parent=h)
j = Node("J", data={"name": "J"}, parent=h)
l = Node("L", data={"name": "L"}, parent=j)
k = Node("K", data={"name": "K"}, parent=h)
m = Node("M", data={"name": "M"}, parent=k)

a.show(attr_list=["name"])

print("Root: ",a.data['name'])
leaves = a.leaves
print("Leaves: ", [leaf.data["name"] for leaf in leaves])
h_ancestors =h.ancestors
print("Ancestors of H: ", [ancestors.data["name"]for ancestors in h_ancestors])
g_decscendant = g.descendants
print("Decsendants of G: ", [decsendant.data["name"]for decsendant in g_decscendant])
sibling_i=i.siblings
print("Siblings of I: ", [sibling.data["name"]for sibling in sibling_i])
k_parent=k.parent
print("Parent of K: ", [k_parent.data['name']])
d_children=d.children
print("Children of D: ", [children.data["name"]for children in d_children])



def height(self):
    if not self.children:
        return False
    else:
        return 1 + max(child.height() for child in self.children)
    
Node.height = height
print("Height of the tree: ", a.height())
print("Height of node G: ", g.height()-1)
print("Level of node H: ",h.depth-1)
print("Level of node A: ",a.depth-1)
print("Height of the node E: ", e.depth-1)
print("Draw the subtrees of node H:")
subtreeH = ["h/i","h/j/l", "h/k/m"]
rootH = list_to_tree(subtreeH)
rootH.show()
