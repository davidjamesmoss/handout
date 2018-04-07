import os
import base64
from markdown.treeprocessors import Treeprocessor
from markdown.extensions import Extension
from markdown.util import etree


class InlineImageProcessor(Treeprocessor):
    def run(self, doc):
        for image in doc.findall('.//img'):
            filepath = '/app/src/{}'.format(image.get('src'))
            fname, fext = os.path.splitext(filepath)

            try:
                with open(filepath, 'r') as fp:
                    b64 = base64.b64encode(fp.read())
            except IOError:
                continue

            figure = etree.Element('figure')
            new_image = etree.Element('img')
            new_image.set('src', 'data:image/{};base64,{}'.format(fext[1:], b64))
            figure.insert(0, new_image)

            alt = image.get('alt')
            if alt:
                caption = etree.Element('figcaption')
                caption.text = alt
                figure.insert(1, caption)

            image.clear()
            image.append(figure)


class InlineImageExtension(Extension):
    def extendMarkdown(self, md, md_globals):
        img_ext = InlineImageProcessor(md)
        md.treeprocessors.add('imgext', img_ext, '>inline')
