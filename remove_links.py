import os
import shutil



session_directories = os.walk('sessions')


markdown_file_paths = []

for directory_map in session_directories:
    directory_location = directory_map[0]
    directory_contents = directory_map[2]

    for file_or_directory in directory_contents:
        if file_or_directory[-3:] == '.md':
            markdown_file_paths.append(directory_location + '/' + file_or_directory)

            
# Remove previous and next links from markdown files
for path in markdown_file_paths:
    with open(path, 'r') as markdown_file_read, open(path+'.clean', 'w') as markdown_file_write:
        lines = markdown_file_read.readlines()

        no_links = [line for line in lines if '[<<<' not in line and ' >>>]' not in line]

        out_text = ''.join(no_links)

        out_text_no_trailing = out_text.lstrip().rstrip()

        markdown_file_write.write(out_text_no_trailing)



for path in markdown_file_paths:
    shutil.move(path+'.clean', path)

