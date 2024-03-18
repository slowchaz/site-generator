from textnode import TextNode, text_node_to_html_node
from htmlnode import HTMLNode, LeafNode, ParentNode

def main():
    print("main")
    text_node = TextNode("just some text", "text")
    print(text_node_to_html_node(text_node))
main()
