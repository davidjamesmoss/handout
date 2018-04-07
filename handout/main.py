# -*- coding: utf-8 -*-
import os
import codecs
import jinja2
import markdown
from inline_image_extension import InlineImageExtension

pages = []
files = sorted(os.listdir('/app/src/'))
env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(['/app/handout', ]),
    autoescape=True,
)

for f in files:
    if f.endswith('.md'):
        fp = codecs.open('/app/src/{}'.format(f), mode='r', encoding='utf-8')

        md = markdown.Markdown(
            output_format='html5',
            extensions=[
                'markdown.extensions.meta',
                'markdown.extensions.extra',
                'markdown.extensions.toc',
                'markdown.extensions.nl2br',
                InlineImageExtension()
            ]
        )

        html = md.convert(fp.read())
        title = md.Meta.get('title')
        slug = md.Meta.get('slug')

        pages.append({
            'title': title[0] if title else f,
            'slug': slug[0] if slug else 'untitled',
            'body': html,
        })

        md.reset()

html_output = env.get_template('template.html').render({'pages': pages})
output_file = codecs.open('/app/output.html', 'w', encoding='utf-8', errors='xmlcharrefreplace')
output_file.write(html_output)
