import unittest
from block_markdown import markdown_to_blocks, block_to_block_type, BlockType

class TestBlockMarkdown(unittest.TestCase):
    def test_markdown_to_blocks(self):
        md = """
This is a **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
             "This is a **bolded** paragraph",
             "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
             "- This is a list\n- with items",
            ],
        )

    def test_heading(self):
        md = "### Hello world"
        self.assertEqual(block_to_block_type(md), BlockType.HEADING)

    def test_extra_hash(self):
        md = "####### Hello world"
        self.assertEqual(block_to_block_type(md), BlockType.PARAGRAPH)

    def test_paragraph(self):
        md = "This is a normal paragraph."
        self.assertEqual(block_to_block_type(md), BlockType.PARAGRAPH)

    def test_code_block(self):
        md = "```\nprint('hi')\n```"
        self.assertEqual(block_to_block_type(md), BlockType.CODE)

    def test_extra_backtick(self):
        md = "````\nprint('secret')\n````"
        self.assertEqual(block_to_block_type(md), BlockType.PARAGRAPH)

    def test_quote_block(self):
        md = "> quote line 1\n> quote line 2"
        self.assertEqual(block_to_block_type(md), BlockType.QUOTE)
    
    def test_unordered_test(self):
        md = "- item 1\n- item 2\n- item3"
        self.assertEqual(block_to_block_type(md), BlockType.UNORDERED_LIST)

    def test_ordered_test(self):
        md = "1. item1\n2. item 2\n3. item 3"
        self.assertEqual(block_to_block_type(md), BlockType.ORDERED_LIST)

    def test_not_ordered_if_wrong_start(self):
        md = "2. item 1\n3. item 2"
        self.assertEqual(block_to_block_type(md), BlockType.PARAGRAPH)

    def test_not_ordered_if_skips_number(self):
        md = "1. item 1\n3. item 2"
        self.assertEqual(block_to_block_type(md), BlockType.PARAGRAPH) 

    def test_not_unordered_if_missing_space(self):
        md = "-item 1\n-item 2"
        self.assertEqual(block_to_block_type(md), BlockType.PARAGRAPH)
 
    def test_not_quote_if_one_line_missing(self):
        md = ">quote line 1\nnot quote line 2"
        self.assertEqual(block_to_block_type(md), BlockType.PARAGRAPH)

if __name__ == "__main__":
    unittest.main()
