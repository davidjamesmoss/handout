# Handout: Distributable web documents

Handout is a simple static site generator for making multi-page, single-file documentation sites, to distribute via email, messaging apps or network share.

![Screenshot](https://raw.github.com/davidjamesmoss/handout/master/screenshot.png)

Handout is bare-bones and limited in scope, however it might come in handy if it meets your requirements.

### How it works
Handout takes a directory of Markdown files and images as input, and outputs a single HTML file. Each of the documents is combined into a faux-paginated microsite and the images are embedded as data URLs.

### Creating a handout site

Add your Markdown files in `src`. There is a file called `01 homepage.md` to get you started.

The name of your files does not matter, provided they end in `.md`. Prefix the filenames with numbers to set the order the pages appear in.

At the top of the file is some metadata:

    Title: Welcome to Handout
    Slug: homepage

The title is used in the navigation menu and for the window title. Slug is the name of the URL fragment that identifies the page (eg. `output.html#homepage`).

Add images by referencing them as normal and put the file in the `src` directory. The alt text will be turned into a caption placed underneath the image. Images are not resized, so check that they’re a suitable size for embedding.

    ![This image is embedded in the page](book.png)

You can link to other pages within your document using the slug:

    Go to [this page](#another-page) for more information.

To add a table of contents built from the headings on your page, add `[TOC]` anywhere in your document.

To build your website (and assuming you have Docker installed), run:

    $ docker build -t handout .
    $ docker run -v $(pwd):/app/ handout

The HTML output will be written to `output.html` which you can rename as required.

### Customising the template
A basic template is provided in `handout/template.html` which you can customise as you wish. The templating language used is Jinja2.
