from textnode import TextNode, TextType
from extractor import extract_markdown_images, extract_markdown_links


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    sep_nodes = []

    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            sep_nodes.append(old_node)
            continue

        parts = old_node.text.split(delimiter)

        if len(parts) % 2 == 0:
            raise Exception("The closing delimiter is not found.")

        for idx, part in enumerate(parts):
            if part == "":
                continue

            if idx % 2 == 0:
                sep_nodes.append(TextNode(part, TextType.TEXT))
            else:
                sep_nodes.append(TextNode(part, text_type))

    return sep_nodes


def split_nodes_image(old_nodes):
    new_nodes = []

    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue

        if old_node.text == "":
            continue

        matches = extract_markdown_images(old_node.text)
        if not matches:
            new_nodes.append(old_node)
            continue

        remaining = old_node.text

        for alt, url in matches:
            marker = f"![{alt}]({url})"
            before, after = remaining.split(marker, 1)

            if before != "":
                new_nodes.append(TextNode(before, TextType.TEXT))

            new_nodes.append(TextNode(alt, TextType.IMAGE, url))
            remaining = after

        if remaining != "":
            new_nodes.append(TextNode(remaining, TextType.TEXT))

    return new_nodes


def split_nodes_link(old_nodes):
    new_nodes = []

    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue

        if old_node.text == "":
            continue

        matches = extract_markdown_links(old_node.text)
        if not matches:
            new_nodes.append(old_node)
            continue

        remaining = old_node.text

        for anchor, url in matches:
            marker = f"[{anchor}]({url})"
            before, after = remaining.split(marker, 1)

            if before != "":
                new_nodes.append(TextNode(before, TextType.TEXT))

            new_nodes.append(TextNode(anchor, TextType.LINK, url))
            remaining = after

        if remaining != "":
            new_nodes.append(TextNode(remaining, TextType.TEXT))

    return new_nodes
