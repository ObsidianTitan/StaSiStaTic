from enum import Enum
import re

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"

def block_to_block_type(markdown):
   lines = markdown.split("\n")

   if re.match(r"^#{1,6}(?!#) .+", markdown):
       return BlockType.HEADING

   if markdown.startswith("```\n") and markdown.endswith("```"):
       return BlockType.CODE

   if all(line.startswith(">") for line in lines):
       return BlockType.QUOTE
        
   if all(line.startswith("- ") for line in lines):
       return BlockType.UNORDERED_LIST

   is_ordered = True
   for i,line in enumerate(lines, start = 1):
       if not line.startswith(f"{i}. "):
           is_ordered = False
           break
   if is_ordered:
       return BlockType.ORDERED_LIST

   return BlockType.PARAGRAPH
 

def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")
   
    stripped = [] 
    for b in blocks:
        b = b.strip()
        if b:
           stripped.append(b)
    return stripped
