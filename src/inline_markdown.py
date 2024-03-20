from textnode import (
        TextNode,
        text_type_text,
        text_type_bold,
        text_type_italic,
        text_type_code
)

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    node_list = []

    for node in old_nodes:
        if type(node) is not TextNode:
            node_list.append(node)
        else:
            split_nodes = []
            segments = node.text.split(delimiter)
            if len(segments) % 2 == 0:
                raise ValueError("Invalid markdown")
            for i in range(len(segments)):
                if segments[i] == "":
                    continue
                if i % 2 == 0:
                    split_nodes.append(TextNode(segments[i], text_type_text))
                else:
                    split_nodes.append(TextNode(segments[i], text_type))
            node_list.extend(split_nodes)

    return node_list
