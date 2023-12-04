'''
big tree python package
    can construfct tree and export tree

    big tree set up
        pip install big tree
    to export image
        pip install 'bigtree[image]'
'''
'''
from bigtree import Node

a = Node("RM", data={"name": "RM"})
b = Node("Jin", data={"name": "Jin"}, parent=a)
c = Node("Jhope", data={"name": "Jhope"}, parent=a)
d = Node("V", data={"name": "V"}, parent=b)
e = Node("Jungkook", data={"name": "Jungkook"}, parent=b)
d = Node("Suga", data={"name": "SUga"}, parent=c)
f = Node("Jimin", data={"name": "Jimin"}, parent=d)
#(Node (a/b, name = "Jin"), Node(a/c, name = "Jhope"))

#Accessong children using 'children' attribute
print(a.children)

#depth
print(a.depth)
print(b.depth)

a.show(attr_list = ["name"])
'''
'''
    Mini Activity
        - create a new node as children of b with value of 'Junghook'
        - add children to c with a value of 'Suga'
        - from Suga add children of node Jimin Screen shot 
    Screen shot your code and result in our SB Laboratory
'''
#pip install 'bigtree[pandas]'
'''
from bigtree import list_to_tree

path_list = ["a/b/d", "a/b/e", "a/c"]
root = list_to_tree(path_list)

root.show()
'''
'''
#dictionary to tree
from bigtree import Node

path_dict = {
	"a": {"name": "RM"},
	"a/b": {"name": "Jin"},
	"a/c": {"name": "JHope"},
	"a/b/d": {"name": "V"},
	"a/b/e": {"name": "Jungkook"},
	"a/c/f": {"name": "Suga"}

}


#Create a dictionary to keep track of created nodes
created_nodes = {"a": Node("RM", data= path_dict["a"])}

#showing the tree structure with specified attributes
created_nodes["a"].show(attr_list = ["name"])

#create nodes and add them to the tree
for path, node_data in path_dict.items():
    # Skip the root node
    if path != "a":
        nodes = path.split("/")
        current_node = created_nodes[nodes[0]]
        for node in nodes[1:]:
            if node not in created_nodes:
                created_nodes[node] = Node(node_data["name"], parent=current_node, data=path_dict[path])
            current_node = created_nodes[node]

#showing the tree structure with specified attributes
created_nodes["a"].show(attr_list = ["name"])
'''
