"""
Visualize a phylogenetic tree with ete
"""

from ete3 import Tree

def convert_to_string(tree):
    """Returns tree in format used by ete library, Newick format"""
    string = ""
    #add any children that the node may have
    if tree.children:
        for child in tree.children:
            if child.name is None:
                #the child is an internal node, so has no name
                #add its children
                string += "(" + convert_to_string(child) + "),"
            else:
                #the child is a leaf, add with name
                string += str(child.name) + ","
        string = string[:-1]
    return string

def render_to_image(phylogeny, filename="mytree.png"):
    s = convert_to_string(phylogeny)
    print(s)
    t = Tree(s + ";") #needs a semicolon!
    t.render(filename, w=183, units="mm")


