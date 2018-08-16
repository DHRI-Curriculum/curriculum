from parse_toc import tocs

preamble = '''# Summary

* [Overview](README.md)
* [Philosophy](philosophy.md)
'''

sessions_summary = ''

for session_name in tocs:
    fancy_formatting_session_name = session_name.replace('-', ' ').title()

    readme_link = '* [%s](sessions/%s/README.md)\n' % (fancy_formatting_session_name, session_name)
    sessions_summary += readme_link

    for line in tocs[session_name].splitlines():
        summary_formatted_line = '  * ' + line + '\n'
        split_line = summary_formatted_line.split('(')
        summary_corrected_path = split_line[0] + '(' + 'sessions/%s/' % session_name + split_line[1]
        
        sessions_summary += summary_corrected_path

with open('SUMMARY.md', 'w') as out_file:
    out_file.write(preamble + sessions_summary)
