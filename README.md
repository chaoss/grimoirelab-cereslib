# Ceres [![Build Status](https://github.com/chaoss/grimoirelab-cereslib/workflows/tests/badge.svg)](https://github.com/chaoss/grimoirelab-cereslib/actions?query=workflow:tests+branch:main+event:push) [![Coverage Status](https://coveralls.io/repos/github/chaoss/grimoirelab-cereslib/badge.svg?branch=main)](https://coveralls.io/github/chaoss/grimoirelab-cereslib?branch=main) [![PyPI version](https://badge.fury.io/py/cereslib.svg)](https://badge.fury.io/py/cereslib)

Ceres is a library that aims at dealing with data in general,
and software development data in particular.

The initial goal of Ceres is to parse information in several ways
from the [Perceval](https://github.com/grimoirelab/perceval) tool
in the [GrimoireLab project](https://github.com/grimoirelab).

However, the more code is added to this project, the more generic
methods are found to be useful in other areas of analysis.

The following are the areas of analysis that Ceres can help at:

## Eventize

The 'eventizer' helps to split information coming from Perceval.
In short, Perceval produces JSON documents and those can be consumed
by Ceres and by the 'eventizing' side of the library.

By 'eventizing', this means the process to parse a full Perceval JSON
document and produce a Pandas DataFrame with certain amount of information.

As an example, a commit contains information about the commit itself, and
the files that were 'touched' at some point. Depending on the granularity
of the analysis Ceres will work in the following way:

* Granularity = 1: This is the first level and produces 1 to 1 relationship
  with the main items in the original data source. For example 1 commit would 
  be just 1 row in the resultant dataframe. This would be a similar case for
  a code review process in Gerrit or in Bugzilla for tickets.
* Granularity = 2: This is the second level and depends on the data source
  how in depth this goes. In the specific case of commits, this would return
  n rows in the dataframe. And there will be as many rows as files where 
  'touched' in the original data source.


## Format

The format part of the library contains some utils that are useful for
some basic formatting actions such as having a whole column in the Pandas
dataframe with the same string format.

Another example would be the use of the format utils to cast from string
to date using datetuils and applying the method to a whole column of a 
given dataframe.

## Filter

The filter utility basically removes rows based on certain values in
certain cells of a dataframe.

## Data Enrich

This is the utility most context-related together with the eventizing
actions. This will add or modify one or more columns in several ways.

There are several examples such as taking care of the surrogates enabling
UTF8, adding new columns based on some actions on others, adding the gender
of the name provided in another column, and others.


# How can you help here?

This project is still quite new, and the development is really slow, so
any extra hand would be really awesome, even giving directions, pieces
of advice or feature requests :).

And of course, using the software would be great!

# Where to start?

The examples folder contains some of the clients I've used for some
analysis such as the gender analysis or to produce dataframes that help
to understand the areas of the code where developers are working.

Those are probably a good place to have a look at.

## Requirements

 * Python >= 3.9

You will also need some other libraries for running the tool, you can find the
whole list of dependencies in [pyproject.toml](pyproject.toml) file.

## Installation

There are several ways to install Cereslib on your system: packages or source 
code using Poetry or pip.

### PyPI

Cereslib can be installed using pip, a tool for installing Python packages. 
To do it, run the next command:
```
$ pip install cereslib
```

### Source code

To install from the source code you will need to clone the repository first:
```
$ git clone https://github.com/chaoss/grimoirelab-cereslib
$ cd grimoirelab-cereslib
```

Then use pip or Poetry to install the package along with its dependencies.

#### Pip
To install the package from local directory run the following command:
```
$ pip install .
```
In case you are a developer, you should install cereslib in editable mode:
```
$ pip install -e .
```

#### Poetry
We use [poetry](https://python-poetry.org/) for dependency management and 
packaging. You can install it following its [documentation](https://python-poetry.org/docs/#installation).
Once you have installed it, you can install cereslib and the dependencies in 
a project isolated environment using:
```
$ poetry install
```
To spaw a new shell within the virtual environment use:
```
$ poetry shell
```

## License

Licensed under GNU General Public License (GPL), version 3 or later.
