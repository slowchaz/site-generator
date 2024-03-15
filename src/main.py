from textnode import TextNode
from htmlnode import HTMLNode

def main():
    print("main")
    html_node = HTMLNode(props={"href": "https://www.google.com", "target": "_blank"})
    print(html_node.props_to_html())

main()
