from textnode import TextNode
from htmlnode import HTMLNode, LeafNode

def main():
    print("main")
    
    leafnode = LeafNode("p", "This is a paragraph of text.")
    print(leafnode.to_html())

    leafnode2 = LeafNode("a", "Click me!", {"href": "www.example.com"})
    print(leafnode2.to_html())

main()
