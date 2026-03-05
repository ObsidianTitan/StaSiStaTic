import os
from markdown_to_html_node import markdown_to_html_node
from title_extractor import extract_title

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    with open(template_path, "r") as f:
        temp = f.read()

    def walk(src_dir, dst_dir):
        os.makedirs(dst_dir, exist_ok = True)

        for entry in os.listdir(src_dir):
            src_path = os.path.join(src_dir, entry)
            dst_path = os.path.join(dst_dir, entry)
            
            if os.path.isdir(src_path):
                walk(src_path, dst_path)
                continue               
       
            if not entry.endswith(".md"):
                continue

            with open(src_path, "r") as f:
                markdown = f.read()
        
            html_file = markdown_to_html_node(markdown).to_html()
            page_title = extract_title(markdown)

            full_html = temp.replace("{{ Title }}", page_title).replace("{{ Content }}", html_file)              

            dst_html = os.path.splitext(dst_path)[0] + ".html"
            os.makedirs(os.path.dirname(dst_html), exist_ok = True)
 
            with open(dst_html, "w") as f:
                f.write(full_html)
      
    walk(dir_path_content, dest_dir_path)        
