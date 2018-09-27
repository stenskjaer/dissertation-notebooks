[![Binder](https://mybinder.org/badge.svg)](https://mybinder.org/v2/gh/stenskjaer/notebooks/master)

# Doctrinal notebooks

This repository provides a set of notebooks used to investigate doctrines
concerning intellectual self-knowledge in my PhD dissertation on that subject in
Latin medieval commentaries on Aristotle's *De anima*. 

The notebooks can be read in static form here, but there are also interactive
versions of them available by clicking the badge "launch binder" above or
[following this link](https://mybinder.org/v2/gh/stenskjaer/notebooks/master).

The notebooks are [Jupyter notebooks](https://jupyter.org/), which means that
regular running prose is interspersed with calculations in the [Python
programming language](https://python.org). This lets me think aloud and document
what I do as the investigations go along. It is therefore possible to validate
my process of thought and the details of any calculations, and in the
interactive versions of the notebooks it is also possible to investigate the
content of the database further. Any results presented in the main analyses of
my dissertation from the use of the database should therefore be reproducible.

The data provided in these analyses is stored in a [Neo4j
database](https://neo4j.com/).

## Database structure and content

A Neo4j database is a graph database, where *nodes* (also called *vertices*) are
put into relation with each other by *edges*. Nodes and edges can be of
different types and contains any number of key-value pairs for data structure
and registration.

The database contains the following relevant node types:

- `Doctrine`: Singular points of doctrine.
- `Instance`: Single instance of a doctrine.
- `Question`: Individual questions in a particular question commentary (similar
  to a chapter).
- `Text`: Individual texts.
- `Author`: Individual authors of texts, including commentators.

The database contains the following relevant edge types:

- `WROTE`: An `Author` wrote a `Text`.
- `CONTAINS`: A `Text` contains a `Question` or a `Question` contains a
  `Doctrine`
- `HAS`: A `Question` has an `Instance` of a `Doctrine`.
- `OF`: An `Instance` is an instance of a `Doctrine`.
- `ATTACKS`: A `Doctrine` attacks another `Doctrine`.
- `USES`: A `Doctrine` uses another `Doctrine`.
- `SUPPORTS`: A `Doctrine` supports another `Doctrine`.

This results in the reduced database schema.
![Illustration of the reduced graph schema](/graphics/db-schema.pdf "Graph
schema illustration")

Properties on nodes:
- `Doctrine`: 
  - `uuid`: ID of the doctrine.
  - `description`: The identifying headline of the doctrine. This is what is
    used as the title in the appendix of the dissertation.
  - `note`: A description of the node. This is used as the description in the
    dissertation. 
- `Instance`:
  - `uuid`: ID of the instance.
  - `type`: Indication of the instance type. These are one of: `["Negative
    ratio", "Positive ratio", "Refutation"]`.
- `Question`:
  - `uuid`: ID of the question.
  - `title`: Question title in the commentary.
  - `number`: The question number in the commentary. This is no used often.
- `Text`
  - `uuid`: ID of the text.
  - `title`: The title of the text.
- `Author`:
  - `uuid`: ID of the author.
  - `name`: The author name.

These nodes make up the substance of the registrations. For some calculations it
has been relevant to filter the material according to which chapter of my
dissertation it is treated in, and I therefore also apply the node type
`DissertationPart`. The database contains two examples of that node, referring
to chapter two and three of my dissertation, with a relationship of type
`INCLUDES` to each doctrine `Instance`.

## Using the notebooks

It is possible to read the static version of the notebooks by visiting them in
the repository.

It is also possible to visit an interactive version of the notebook by following
the 
[binder link](https://mybinder.org/v2/gh/stenskjaer/notebooks/master) at the top
of this README. This will open up the notebooks for interactive use and
experimentation. As the database is read-only, it will not be possible to make
any changes in the registrations of the database, but merely to inspect and
experiment with the registrations directly.

