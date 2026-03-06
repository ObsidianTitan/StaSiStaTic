import os
import shutil
import sys
from recur_pg_gen import generate_pages_recursive

def copy_static(source_dir, dest_dir):
    if os.path.exists(dest_dir):
        shutil.rmtree(dest_dir)

    os.mkdir(dest_dir)
    
    _copy_dir_contents(source_dir, dest_dir)

def _copy_dir_contents(source_dir, dest_dir):    
    for item in os.listdir(source_dir):
        src_path = os.path.join(source_dir, item)
        dest_path = os.path.join(dest_dir, item)
        print(f" * {src_path} -> {dest_path}")
        if os.path.isfile(src_path):
            shutil.copy(src_path, dest_path)

        else:
            os.mkdir(dest_path)
            _copy_dir_contents(src_path, dest_path)        

def main():
    basepath = sys.argv[1] if len(sys.argv) > 1 else "/"
    copy_static("static", "docs")
    generate_pages_recursive("content", "template.html", "docs", basepath)

if __name__ == "__main__":
    main()
