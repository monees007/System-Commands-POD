import codecs
import os

import markdown

for filename in os.listdir('markdowns'):
    f = os.path.join(filename)
    # checking if it is a file
    if os.path.isfile(os.path.join('markdowns', filename)) and f[-3:] == '.md':
        markdown.markdownFromFile(
            input=f'markdowns/{f}',
            output=f'templates/{f}.html',
            encoding='utf8',)
        with open(f'templates/{f}.html', 'r', encoding='utf8') as op:
            content = op.read()
            op.close()
        head = "{% extends 'base.html' %}\n\n{% block content %}\n"
        foot = "\n{% endblock %}"
    
        with codecs.open(f'templates/{f}.html', 'w', 'utf-8-sig') as op:
            op.write(head + content + foot)
            op.close()
