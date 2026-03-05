from Spliter_Delimiter import *
from extractor import *
from htmlnode import *
from textnode import *
from txt_to_html import *

def text_to_textnodes(text):
    nodes = [TextNode(text, TextType.TEXT)]
    img_nodes = split_nodes_image(nodes)
    link_nodes = split_nodes_link(img_nodes)
    bold_nodes = split_nodes_delimiter(link_nodes, "**", TextType.BOLD)
    italic_nodes = split_nodes_delimiter(bold_nodes, "_", TextType.ITALIC)
    code_nodes = split_nodes_delimiter(italic_nodes, "`", TextType.CODE)
    
    return code_nodes
