import markdown

for i in range(1, 9):
    markdown.markdownFromFile(
        input=f'markdowns/Week{i}.md',
        output=f'htmls/Week{i}.html',
        encoding='utf8',
    )
    with open(f'htmls/Week{i}.html', 'r', encoding="utf8") as op:
        content = op.read()
        op.close()
    head = "{% extends 'base.html' %}\n\n{% block content %}\n"
    foot = "\n{% endblock %}"

    with open(f'htmls/Week{i}.html', 'w') as op:
        op.write(head + content + foot)
        op.close()
