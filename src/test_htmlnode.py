import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html_none(self):
        node = HTMLNode("p", "Hello", None, None)
        self.assertEqual(node.props_to_html(), "")

    def test_props_to_html_empty(self):
        node = HTMLNode("p", "This is a paragraph", None, {})
        self.assertEqual(node.props_to_html(), "")

    def test_props_to_html_multiple(self):
        props = {"href": "https://www.google.com", "target": "_blank"}
        node = HTMLNode("a", "Google", None, props)
        self.assertEqual(node.props_to_html(), ' href="https://www.google.com" target="_blank"')

if __name__  == "__main__":
    unittest.main()
