from inline_markdown import extract_markdown_images, extract_markdown_links, split_nodes_image, split_nodes_link
from textnode import TextNode, text_type_text

def main():
    print("main")

    node = TextNode(
        "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
        text_type_text,
    )
    new_nodes = split_nodes_image([node])
    print(new_nodes)

    print("complete")


main()
