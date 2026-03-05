import os
from markdown_to_html_node import markdown_to_html_node
from title_extractor import extract_title

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page {from_path} to {dest_path} using {template_path}")
    
    with open(from_path, "r") as f:
        markdown = f.read()

    with open(template_path, "r") as f:
        temp = f.read()
         
    html_str = markdown_to_html_node(markdown).to_html()
    page_title = extract_title(markdown)

    full_html = temp.replace("{{ Title }}", page_title).replace("{{ Content }}", html_str)

    parent = os.path.dirname(dest_path)
    if parent:
        os.makedirs(parent, exist_ok=True)    

    with open(dest_path, "w") as f:
        f.write(full_html)

    
