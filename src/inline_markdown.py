import re
from textnode import (
        TextNode,
        text_type_text,
        text_type_bold,
        text_type_italic,
        text_type_code,
        text_type_image,
        text_type_link
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

def split_nodes_image(old_nodes):
    new_nodes = []

    for node in old_nodes:
        if type(node) is not TextNode:
            new_nodes.append(node)
        
        images = extract_markdown_images(node.text)
        if not images:
            new_nodes.append(node)

        text_to_split = node.text
        for alt_text, image_url in images:
            parts = text_to_split.split(f"![{alt_text}]({image_url})", 1)

            if parts[0]:
                new_nodes.append(TextNode(parts[0], text_type_text))

            new_nodes.append(TextNode(alt_text, text_type_image, image_url))

            text_to_split = parts[1] if len(parts) > 1 else ""

        if text_to_split:
            new_nodes.append(TextNode(text_to_split, text_type_text))


    return new_nodes

def split_nodes_link(old_nodes):
    new_nodes = []

    for node in old_nodes:
        if type(node) is not TextNode:
            new_nodes.append(node)

        links = extract_markdown_links(node.text)
        if not links:
            new_nodes.append(node)

        text_to_split = node.text
        for alt_text, link_url in links:
            parts = text_to_split.split(f"[{alt_text}]({link_url})", 1)

            if parts[0]:
                new_nodes.append(TextNode(parts[0], text_type_text))

            new_nodes.append(TextNode(alt_text, text_type_link, link_url))

            text_to_split = parts[1] if len(parts) > 1 else ""

        if text_to_split:
            new_nodes.append(TextNode(text_to_split, text_type_text))


    return new_nodes

def extract_markdown_images(text):
    matches = re.findall(r"!\[(.*?)\]\((.*?)\)", text)
    return matches

def extract_markdown_links(text):
    matches = re.findall(r"\[(.*?)\]\((.*?)\)", text)
    return matches
