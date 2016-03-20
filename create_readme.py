#!/usr/bin/env python3

import glob


HEADER = '''
# TIL

> Today I Learned

A collection of concise write-ups on small things I learn day to day across a
variety of languages and technologies. These are things that don't really
warrant a full blog post.
'''

FOOTER = '''
## About

I shamelessly stole this idea from
[jbranchaud/til](https://github.com/jbranchaud/til).

## License

&copy; 2016 Jonas Svarvaa

This repository is licensed under the MIT license. See `LICENSE` for
details.
'''

SEP = '\n---\n'


def get_content():
    def categories_list_md(globbed):
        categories = [c.split('/')[0] for c in globbed]
        output = ''
        for c in categories:
            output += '* [{}](#{})\n'.format(c.capitalize(), c)
        return output

    def categories_listing_md(globbed):
        output = ''
        headings = []
        for c in globbed:
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
            output += '- [{}]({})'.format(title, c)
        output += '\n'
        return output

    content_glob = '**/*.md'
    globbed = glob.glob(content_glob)

    output = (
        '\n### Categories\n\n'
        '{categories_list}'
        '{sep}'
        '{categories_listing}'
    ).format(
        sep=SEP,
        categories_list=categories_list_md(globbed),
        categories_listing=categories_listing_md(globbed)
    )
    return output


def main(*args):
    output = (
        '{header}'
        '{sep}'
        '{content}'
        '{sep}'
        '{footer}'
    ).format(header=HEADER, footer=FOOTER, sep=SEP, content=get_content())

    with open('README.md', 'w+') as readme:
        readme.write(output)

if __name__ == '__main__':
    main()
