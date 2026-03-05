from block_markdown import *
from textnode import *
from txt_to_txtnodes import *
from txt_to_html import *


def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    
    block_children = []
    for block in blocks:
        block_children.append(block_to_html_node(block))

    return ParentNode("div", block_children)           

def block_to_html_node(block):
    t = block_to_block_type(block)

    if t == BlockType.HEADING:
       level = count_heading_level(block)
       text = block[level +1:]
       return ParentNode(f"h{level}", text_to_children(text))

    if t == BlockType.PARAGRAPH:
        text = " ".join(block.splitlines())
        return ParentNode("p", text_to_children(text))

    if t == BlockType.CODE:
        code_text = strip_code_fences(block)
        code_leaf = LeafNode("code", code_text)
        return ParentNode("pre",[code_leaf])

    if t == BlockType.QUOTE:
        text = strip_quote_markers(block)
        return ParentNode("blockquote", text_to_children(text))


    if t == BlockType.UNORDERED_LIST:
        items = strip_ul_items(block)
        li_nodes = [ParentNode("li", text_to_children(item)) for item in items]
        return ParentNode("ul", li_nodes)

    if t == BlockType.ORDERED_LIST:
        items = strip_ol_items(block)
        li_nodes = [ParentNode("li", text_to_children(item)) for item in items] 
        return ParentNode("ol", li_nodes)
      
    raise ValueError(f"Unknown block type: {t}")

def text_to_children(text):
    textnodes = text_to_textnodes(text)
    return [text_node_to_html_node(tn) for tn in textnodes]   

def count_heading_level(block):
    i = 0
    while i < len(block) and block[i] == "#":
        i += 1
    return i

def strip_code_fences(block):
    lines = block.splitlines()
    inner = lines[1:-1]
    return "\n".join(inner) + "\n"
    
def strip_quote_markers(block):
    lines = block.splitlines()
    cleaned = []
    for line in lines:
        if line.startswith("> "):
            cleaned.append(line[2:])
        elif line.startswith(">"):
            cleaned.append(line[1:])
        else:
            cleaned.append(line)
    return " ".join(cleaned)

def strip_ul_items(block):
    lines = block.splitlines()
    items = []
    for line in lines:
        items.append(line[2:])
    return items

def strip_ol_items(block):
    lines = block.splitlines()
    items = []
    for line in lines:
        parts = line.split(". ", 1)
        items.append(parts[1])
    return items
