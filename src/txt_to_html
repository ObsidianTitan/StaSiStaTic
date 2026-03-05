from textnode import *
from htmlnode import HTMLNode, LeafNode

def text_node_to_html_node(text_node):
    if text_node is None:
        raise Exception("TextNode must not be None.")   

    if text_node.text_type is None:
        raise Exception("TextNode must have a text_type.")

    if text_node.text_type == TextType.TEXT:
        return LeafNode(None, text_node.text)

    if text_node.text_type == TextType.BOLD:
        return LeafNode( "b", text_node.text, None)

    if text_node.text_type == TextType.ITALIC:
        return LeafNode( "i", text_node.text, None)

    if text_node.text_type == TextType.CODE:
        return LeafNode( "code", text_node.text, None)

    if text_node.text_type == TextType.LINK:
        if text_node.url is None or text_node.url == "":
            raise Exception("TextType.LINK must have a url.")
        return LeafNode( "a", text_node.text, {"href": text_node.url})

    if text_node.text_type == TextType.IMAGE:
        if text_node.url is None or text_node.url == "":
            raise Exception("TextType.IMAGE must have url.")
        return LeafNode( "img","", {"src": text_node.url, "alt": text_node.text})

    raise Exception(f"Unsupported TextType: {text_node.text_type}")  
