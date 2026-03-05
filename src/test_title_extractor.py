from title_extractor import extract_title
import unittest

class TestTitleExtractor(unittest.TestCase):
    def TestHeader(self):
        header = "# Introduction"
        title = self.assertEqual(extract_title(header), "Introduction")




if __name__ == "__main__":
    unittest.main()
        
