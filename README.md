# Good Health and Well-being

[![Codacy Badge](https://api.codacy.com/project/badge/Grade/c87d1094207d46758618a055c5793f9d)](https://app.codacy.com/gh/BuildForSDG/Team-179-Backend?utm_source=github.com&utm_medium=referral&utm_content=BuildForSDG/Team-179-Backend&utm_campaign=Badge_Grade_Settings)

<!-- TODO: setting up codacy test coverage -->

## About

Aims to ensure health and well-being for all, by focusing on mental health.Mental health includes our emotional, psychological, and social well-being. It affects how we think, feel, act and helps determine how we handle stress, relate to others, and make choices.

## Why

The stigma and scrutiny that comes with being associated with mental illness is one of the rising cause of this illness. People who may have noticed a difference in behavioural attitude desist from evaluating further just because of this stigma.This project aims at creating a forum that addresses that by:

- Addressing social and geographical isolation experienced by forum members
- Creating social connection for forum members
- Provide information and practical advice for forum members

## Usage

How would someone use what you have built, include URLs to the deployed app, service e.t.c when you have it setup

## Setup

This is a simple python starter repo template for setting up your project. The setup contains:

- install: poetry via pip. poetry is a dependecy manager.

- poetry: configuration in pyproject.toml

- flake8: for linting and formatting

You should have **Python 3.5+** and **git** installed.

1. Clone the repo you've created from the template herein and change into the directory

    ``
    git clone Team-179-Backend
    ``

2. Change into repo directory

    ``
    cd Team-179-Backend
    ``

3. Install poetry, a dependecy manager for python.

    On windows, you will need powershell to install it:

    ``
    (Invoke-WebRequest -Uri https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py -UseBasicParsing).Content | python
    ``

    After that you will need to restart the shell to make it operational.

    &nbsp;

    On linux and other posix systems (mac included):

    ``curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python``

    &nbsp;

    To check that it is correctly installed, you can check the version:
    ``poetry --version``

    May be the latest stable version is not installed with the installation script, to update poetry, you can run:

    ``poetry self update``

4. With poetry installed, you should install project dependecies by running:

    ``poetry install``

    This will install pytest for running tests and flake8, linter for your project.

### To Note

`src/app.py` is the entry to the project and source code should go into the `src` folder.

All tests should be written in the `tests` folder. tests/test_src.py is a sample test file that shows how tests should like. Feel free to delete it.

#### Hints

- Lint: `poetry run flake8`
- Run tests using the command: `poetry run pytest`
- Install dependencies:
  `poetry add <dependency>`
- Install dev dependencies:
  `poetry add --dev <dev-dependency>`
- Run your project:
  `poetry run app`

## Authors

- [Urban Ishimwe](https://github.com/urbanishimwe)
- [Charles Muchogo](https://github.com/muchogoc)
- [Jerry Shikanga](https://github.com/jerryshikanga)
- [Kenneth Irungu](https://github.com/ken1800)
- [Raymond Oluoch](https://github.com/rOluochKe)

## Contributing

If this project sounds interesting to you and you'd like to contribute, thank you!
First, you can send a mail to buildforsdg@andela.com to indicate your interest, why you'd like to support and what forms of support you can bring to the table, but here are areas we think we'd need the most help in this project :

1. Feedback on our roadmap and feature list. This app is about promoting mental health
2. Opt-in and try using your staging app at staging.project-name.com and report any bugs
3. area three (e.g here is the zoom link to our end-of sprint webinar, join and provide feedback as a stakeholder if you can)

## Acknowledgements

[Smith-Merry J, Goggin G, Campbell A, McKenzie K, Ridout B, Baylosis C. Social connection and online engagement: insights from interviews with users of a mental health online forum. JMIR Ment Health. 2019 Mar 26;6(3):e11084. doi: 10.2196/11084.](https://mental.jmir.org/2019/3/e11084/)

## LICENSE

MIT
