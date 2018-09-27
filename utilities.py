# OS
from os import path

# Type hinting
from typing import Callable, Dict, List

def save_table(filename: str, table: str,
               caption: str = '', label: str = '') -> str:
    """
    Write the content of a table to a specified filename. Caption and label can
    be added if needed.
    """
    with open(filename, 'w') as file:
        if caption:
            caption = "\\caption{%s}\n" % caption
        if label:
            label = "\\label{%s}\n" % label
        cont = (
            "\\begin{table}\n"
            "\\centering\n"
        ) + table + caption + label + (
            "\\end{table}"
        )
        try:
            file.write(cont)
            return print('Printed the following table to %s:\n\%s' % (filename, cont))
        except OSError:
            raise


def print_figure_inclusion(filename: str, caption: str = '',
                           label: str = '') -> str:
    """
    Create a sting for including a figure in LaTeX format. Label and caption
    can be given.
    """
    img_figure = path.splitext(path.basename(filename))[0] + '.pdf'
    if caption:
        caption = "\\caption{%s}\n" % caption
    if label:
        label = "\\label{%s}\n" % label
    cont = (
        "\\begin{figure}\n"
        "\\centering\n"
        "\\includegraphics[width=\\linewidth]{data/figures/%s}\n" % img_figure
    )  + caption + label + (
        "\\end{figure}"
    )
    print(cont)


def build_matrix(authors, docfunc):
    matrix = {}
    for author in authors:
        matrix[author] = []
        values = docfunc(author)
        for name in authors:
            if name in values:
                matrix[author].append(values[name])
            else:
                matrix[author].append(0)
    return matrix

def log_progress(sequence, every=None, size=None, name='Items'):
    from ipywidgets import IntProgress, HTML, VBox
    from IPython.display import display

    is_iterator = False
    if size is None:
        try:
            size = len(sequence)
        except TypeError:
            is_iterator = True
    if size is not None:
        if every is None:
            if size <= 200:
                every = 1
            else:
                every = int(size / 200)     # every 0.5%
    else:
        assert every is not None, 'sequence is iterator, set every'

    if is_iterator:
        progress = IntProgress(min=0, max=1, value=1)
        progress.bar_style = 'info'
    else:
        progress = IntProgress(min=0, max=size, value=0)
    label = HTML()
    box = VBox(children=[label, progress])
    display(box)

    index = 0
    try:
        for index, record in enumerate(sequence, 1):
            if index == 1 or index % every == 0:
                if is_iterator:
                    label.value = '{name}: {index} / ?'.format(
                        name=name,
                        index=index
                    )
                else:
                    progress.value = index
                    label.value = u'{name}: {index} / {size}'.format(
                        name=name,
                        index=index,
                        size=size
                    )
            yield record
    except:
        progress.bar_style = 'danger'
        raise
    else:
        progress.bar_style = 'success'
        progress.value = index
        label.value = "{name}: {index}".format(
            name=name,
            index=str(index or '?')
        )
