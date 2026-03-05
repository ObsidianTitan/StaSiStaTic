import unittest

from textnode import *
from Spliter_Delimiter import*

class TestSpliterDelimiter(unittest.TestCase):
    def test_code(self):
        node = TextNode("This is a text with `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        print(f"new_nodes: {new_nodes}")
        for new_node in new_nodes:
            print(f"new_node.text_type: {new_node.text_type}")
            print(f"new_node.text: {new_node.text}")
            print(f"new_node.url: {new_node.url}")
            print(f"new_node: {new_node}")
        self.assertEqual(new_nodes, [
    TextNode("This is a text with ", TextType.TEXT),
    TextNode("code block", TextType.CODE),
    TextNode(" word", TextType.TEXT),
])
    def test_italic(self):
        node = TextNode("This is a text with an _italicized_ word", TextType.TEXT)   
        new_nodes = split_nodes_delimiter([node], "_", TextType.ITALIC)
        self.assertEqual(new_nodes,[
    TextNode("This is a text with an ", TextType.TEXT),
    TextNode("italicized", TextType.ITALIC),
    TextNode(" word", TextType.TEXT),
])
 
if __name__ == "__main__":
    unittest.main()
