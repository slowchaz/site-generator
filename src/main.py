from textnode import TextNode
from htmlnode import HTMLNode, LeafNode, ParentNode

def main():
    print("main")
    
    node = ParentNode(
        "p",
        [
            LeafNode("b", "Bold text"),
            LeafNode(None, "Normal text"),
            LeafNode("i", "italic text"),
            LeafNode(None, "Normal text"),
        ],
    )   

    print(node.to_html())

main()
