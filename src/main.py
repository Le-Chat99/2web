from textnode import TextNode
import os
import shutil
from copystatic import *
from generatepage import *

dir_path_static = "./static"
dir_path_public = "./public"

def main():
    #print("Deleting public directory...")
    #if os.path.exists(dir_path_public):
    #    shutil.rmtree(dir_path_public)

    #print("Copying static files to public directory...")
    #copy_files_recursive(dir_path_static, dir_path_public)
    
    generate_page('~/2web/content/index.md', '~/2web/template.html', '~/2web/public/index.html')

main()