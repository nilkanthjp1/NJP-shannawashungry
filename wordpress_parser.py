import json
import string
from markdownify import markdownify as md
from bs4 import BeautifulSoup

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
---
${content}
{% capture ingredients %}
${ingredients}
{% endcapture %}
{% capture method %}
${method}
{% endcapture %}
''')

with open('data.json') as data:    
    data = json.load(data)
    #for post in data['posts']:
    for post in data['posts']:
        post['tags'] = ''.join(tagsTemplate.substitute(i) for i in post['tags'])
        post['images'] = ''.join(imagesTemplate.format(slug=i['slug'], url=test(i['url'])) for i in post['attachments'])
        post['content'] = BeautifulSoup(post['content'], 'html.parser').encode('utf-8').strip()
        post['ingredients'] = BeautifulSoup(post['custom_fields']['ingredients'][0], 'html.parser').encode('utf-8').strip()
        post['method'] = BeautifulSoup(post['custom_fields']['method'][0], 'html.parser').encode('utf-8').strip()
        post['title'] = BeautifulSoup(post['title'].encode('utf-8').strip(), "html.parser")
        post['tags'] = str(post['tags'])
        post['slug'] = str(post['slug'])
        post['date'] = str(post['date'])
        markdown = markdownTemplate.substitute(post)
        filename = 'src/_posts/' + post['date'].split(' ')[0] + '-' + post['slug'] + '.markdown'
        print filename
        target = open(filename, 'w')
        target.write(markdown)
        target.close()