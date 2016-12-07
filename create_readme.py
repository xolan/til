#!/usr/bin/env python3

import glob


HEADER = ''
with open('template_header.md', 'r') as f:
    HEADER = f.read()
FOOTER = ''
with open('template_footer.md', 'r') as f:
    FOOTER = f.read()
SEP = '\n---\n'

def get_content():
    def categories_list_md(globbed):
        categories = sorted(list(set([c.split('/')[0] for c in globbed])))
        output = ''
        for c in categories:
            output += '* [{}](#{})\n'.format(c.capitalize(), c)
        return output

    def categories_listing_md(globbed):
        output = ''
        headings = []
        for c in sorted(globbed):
            title = c
            with open(c, 'r') as entry:
                content = entry.read()
                for line in content.split('\n'):
                    if line.startswith('#'):
                        title = line[1:].lstrip()
                        break
            heading = c.split('/')[0].capitalize()
            if heading not in headings:
                output += '\n### {}\n\n'.format(heading)
                headings.append(heading)
            output += '- [{}]({})\n'.format(title, c)
        output += '\n'
        return output

    content_glob = '**/*.md'
    globbed = glob.glob(content_glob)

    categories_list = categories_list_md(globbed)
    categories_listing = categories_listing_md(globbed)

    output = (
        '\n### Categories\n\n'
        '{categories_list}'
        '{sep}'
        '{categories_listing}'
    ).format(
        sep=SEP,
        categories_list=categories_list,
        categories_listing=categories_listing
    )
    return (output, categories_list, categories_listing)


def main(*args):
    content = get_content()
    output = (
        '{header}'
        '{sep}'
        '{content}'
        '{sep}'
        '{footer}'
    ).format(header=HEADER.format(til_count=len(content[2])), footer=FOOTER, sep=SEP, content=content[0])

    with open('README.md', 'w+') as readme:
        readme.write(output)

if __name__ == '__main__':
    main()
