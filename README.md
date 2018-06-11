[![Binder](https://mybinder.org/badge.svg)](https://mybinder.org/v2/gh/stenskjaer/notebooks/master)

# Doctrinal notebooks

This repository provides a set of notebooks used to investigate doctrines
concerning intellectual self-knowledge in my PhD dissertation on that subject in
Latin medieval commentaries on Aristotle's *De anima*. 
The notebooks can be read in static form here, but there are also interactive
versions of them available **[LINK MISSING]**

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

In the following sections I will outline the content of each of the included
notebooks, present the main structure of the content of the database, and give
some sparse examples for how to interact with the database. 

## Database structure and content

A Neo4j database is a graph database, where *nodes* (also called *vertices*) are
put into relation with each other by *edges*. Nodes and edges can be of
different types and contains any number of key-value pairs for data structure
and registration.

The database contains the following relevant node types:

- `Doctrine`: Singular points of doctrine.
- `Question`: Individual questions in a particular question commentary.
- `QuestionType`: Different types of questions and can be found in question
  commentaries. A question on the possibility of having a science of the soul
  could be represented with a `QuestionType`.
- `Text`: Individual texts.
- `Author`: Individual authors of texts, including commentators.

The database contains the following relevant edge types:

- `WROTE`: An `Author` wrote a `Text`.
- `CONTAINS`: A `Text` contains a `Question` or a `Question` contains a
  `Doctrine`
- `INSTANCE_OF`: A `Question` is an instance of a `QuestionType`.
- `ATTACKS`: A `Doctrine` attacks another `Doctrine`.
- `USES`: A `Doctrine` uses another `Doctrine`.
- `SUPPORTS`: A `Doctrine` supports another `Doctrine`.

This results in this reduced database schema.
![Illustration of the reduced graph schema](/graphics/graph-schema.png "Graph
schema illustration")

