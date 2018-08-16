import os

sessions = os.listdir('./sessions')

def get_readmes(folder='./sessions'):
    "Get contents of README files and place them as values in a dictionary. The session names are the keys."
    readmes = {}

    for session in sessions:
        with open('%s/%s/README.md' % (folder, session), 'r') as readme_file:
            readme_text = readme_file.read()
            readmes[session] = readme_text

    return readmes


def extract_toc(readme):
    "Given README contents, extract TOC."
    sectioned_readme = readme.split('-----')
    table_of_contents = sectioned_readme[1].strip()    

    toc_with_only_links = ''
    for line in table_of_contents.splitlines():
        if len(line) > 0 and line[0] == '[':
            toc_with_only_links += line
            toc_with_only_links += '\n'
    
    return toc_with_only_links.strip()

readmes = get_readmes()

tocs = {}

for readme in readmes:
    # tocs[readme] = extract_toc(readmes[readme])
    toc = extract_toc(readmes[readme])

    tocs[readme] = toc
