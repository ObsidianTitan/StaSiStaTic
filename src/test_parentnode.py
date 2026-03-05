import unittest

from htmlnode import ParentNode, LeafNode

class TestParentNode(unittest.TestCase):
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span><b>grandchild</b></span></div>",)
 
    def test_to_html_with_nested_parents(self):
        child = LeafNode("b", "child")
        inner = ParentNode("span", [child])
        outer = ParentNode("div", [inner, LeafNode("b", "inner")])
        self.assertEqual(
            outer.to_html(),
            "<div><span><b>child</b></span><b>inner</b></div>",
        )

    def test_to_html_with_multiple_children(self):
        parent = ParentNode(
            "p",
            [
                LeafNode("b", "Bold"),
                LeafNode(None, "Normal"),
                LeafNode("i", "Italic"),
            ],
        )
        self.assertEqual(parent.to_html(), "<p><b>Bold</b>Normal<i>Italic</i></p>")

    def test_to_html_with_no_children(self):
        parent = ParentNode("div", None)
        with self.assertRaises(ValueError):
            parent.to_html()


if __name__ == "__main__":
    unittest.main()
    
