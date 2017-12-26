import json
import string
from markdownify import markdownify as md
from bs4 import BeautifulSoup
import textwrap

def test(url):
    return url.split('/uploads')[1]

tagsTemplate = string.Template('''
  - name: ${title}
    slug: ${slug}''')

imagesTemplate = '''
  - url: {url}
    title: {slug}'''

markdownTemplate = string.Template('''---
layout: post
title:  "${title}"
date:   ${date}
categories: recipe
permalink: /:categories/:slug.html
slug: ${slug}
author: Shanna Patel
tags: ${tags}
images: ${images}
ingredients: >
  ${ingredients}
method: >
${method}
---
${content}
''')

with open('assets/data/data.json') as data:    
    data = json.load(data)
    #for post in data['posts']:
    for post in data['posts']:
        post['tags'] = ''.join(tagsTemplate.substitute(i) for i in post['tags'])
        post['images'] = ''.join(imagesTemplate.format(slug=i['slug'], url=test(i['url'])) for i in post['attachments'])
        post['content'] = BeautifulSoup(post['content'], 'html.parser')
        post['ingredients'] = BeautifulSoup(post['custom_fields']['ingredients'][0].replace('\n', '\n  '), 'html.parser')
        post['method'] = textwrap.indent(post['custom_fields']['method'][0].replace('\t', ''), '  ')
        post['title'] = BeautifulSoup(post['title'], "html.parser")
        post['tags'] = str(post['tags'])
        post['slug'] = str(post['slug'])
        post['date'] = str(post['date'])
        markdown = markdownTemplate.substitute(post)
        filename = '_posts/' + post['date'].split(' ')[0] + '-' + post['slug'] + '.markdown'
        print(filename)
        target = open(filename, 'w')
        target.write(markdown)
        target.close()