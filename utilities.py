# OS
from os import path

# Type hinting
from typing import Callable, Dict, List
from neo4j.v1.result import BoltStatementResult

# Database
from neo4j.v1 import GraphDatabase

uri = "bolt://hobby-cfhjihneocolgbkekkgnehbl.dbs.graphenedb.com:24786"
driver = GraphDatabase.driver(uri, auth=("doctrines-admin", "b.boElytalQw6c.UozbGKRdegpIuZq1"))

def run_query(string) -> BoltStatementResult:
    """Perform a query in the database and return the result object."""
    with driver.session() as session:
        with session.begin_transaction() as tx:
            return tx.run(string)


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
            return 'Success'
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
