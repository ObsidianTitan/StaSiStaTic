import unittest

from htmlnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_link(self):
        node = LeafNode("a","Let's learn!", {"href": "https://www.freecodecamp.org"})
        self.assertEqual(node.to_html(),'<a href="https://www.freecodecamp.org">Let\'s learn!</a>')

    def test_leaf_3(self):
        node = LeafNode("p", "This is a paragraph")
        self.assertEqual(node.to_html(), "<p>This is a paragraph</p>")

    def test_leaf_raw_text(self):
        node = LeafNode(None, "Hi")
        self.assertEqual(node.to_html(), "Hi")

    def test_leaf_value_required(self):
        node = LeafNode("p", None)
        with self.assertRaises(ValueError):
            node.to_html()


if __name__ == "__main__":
    unittest.main()

