from textnode import TextNode, text_node_to_html_node
from inline_markdown import split_nodes_delimiter
from htmlnode import HTMLNode, LeafNode, ParentNode

text_type_text = "text"
text_type_bold = "bold"
text_type_italic = "italic"
text_type_code = "code"
text_type_link = "link"
text_type_image = "image"

def main():
    print("main")
    
    node = TextNode("This is a text with a `code block` word", text_type_text)
    new_nodes = split_nodes_delimiter([node], "`", text_type_code)
    print(new_nodes)


main()
