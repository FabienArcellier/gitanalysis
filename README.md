## Gitanalysis

[![Build Status](https://travis-ci.org/FabienArcellier/gitanalysis.svg?branch=master)](https://travis-ci.org/FabienArcellier/gitanalysis)

transform a formatted log from git as csv file

git log - `git log --all --numstat --date=short --pretty=format:'--%h--%ad--%aN' --no-renames`

```
--b092e02--2018-10-24--Fabien Arcellier
1       1       slidesearch/indexer/application/cli/daemon.py

--44ced73--2018-10-22--Fabien Arcellier
5       1       slidesearch/indexer/lib/workers/documentscrawler.py

--bb6f57d--2018-10-22--Fabien Arcellier
3       2       slidesearch/indexer/lib/workers/documentscrawler.py
```

changelog expose on stdout as csv file

```
shorthash,author,date,insertions,deletions,filename
c166c30,Fabien Arcellier,2015-08-13,1,9,src/AppBundle/Controller/DefaultController.php
c166c30,Fabien Arcellier,2015-08-13,0,5,src/AppBundle/Resources/views/default/home.html.twig
c166c30,Fabien Arcellier,2015-08-13,1,1,src/AppBundle/Resources/views/default/slides.html.twig
2fc1fdf,Fabien Arcellier,2015-08-01,4,0,README.md
2fc1fdf,Fabien Arcellier,2015-08-01,7,0,app/.htaccess
2fc1fdf,Fabien Arcellier,2015-08-01,9,0,app/AppCache.php
2fc1fdf,Fabien Arcellier,2015-08-01,36,0,app/AppKernel.php
2fc1fdf,Fabien Arcellier,2015-08-01,13,0,app/Resources/views/base.html.twig
```

## The latest version

You can find the latest version to ...

```bash
pip install gitanalysis
```

## Usage

```
Usage: gitanalysis [OPTIONS] COMMAND [ARGS]...

Options:
  --help  Show this message and exit.

Commands:
  changelog         export a csv changelog from git log
  effort_by_author  export a csv that list the count of days spent by...
```

### Changelog

```
Usage: gitanalysis [OPTIONS] COMMAND [ARGS]...

Options:
  --help  Show this message and exit.

Commands:
  changelog         export a csv changelog from git log
  effort_by_author  export a csv that list the number of days an author has...
```

You can run the application with the following command

```bash
gitanalysis changelog
```

or with

```bash
gitanalysis changelog < gitlog.txt
```

or with

```bash
git log --pretty=format:'-%h;%an;%ad' --numstat | gitanalysis changelog
```

#### date_format option

By default, the exported format is compatible with Excel.
You may want to use your own date format.

The following example allow to export date using ISO9001 format.

```
gitanalysis changelog --date_format %Y-%m-%dT%H:%m%sZ
```

* [supported format](https://docs.python.org/3/library/datetime.html#strftime-and-strptime-behavior)

### effort_by_author

```
Usage: gitanalysis effort_by_author [OPTIONS]

  export a csv that list the number of days an author has commit code

Options:
  --use-git  force the usage of git on the current directory
  --help     Show this message and exit.
```

You can run the application with the following command

```bash
gitanalysis effort_by_author
```

or with

```bash
gitanalysis effort_by_author < gitlog.txt
```

```
author,effort(days)
Fabien Arcellier,85
...
```

## Developper guideline

### Install development environment

Use make to instanciate a python virtual environment in ./venv and install the
python dependencies.

```bash
make install_requirements_dev
```

### Activate the python environment

When you setup the requirements, a `venv` directory on python 3 is created.
To activate the venv, you have to execute :

```bash
make venv
source venv/bin/activate
```

### Run the linter and the unit tests

Before commit or send a pull request, you have to execute `pylint` to check the syntax
of your code and run the unit tests to validate the behavior.

```bash
make lint
make tests
```

## Contributors

* Fabien Arcellier

## License

MIT License

Copyright (c) 2018 Fabien Arcellier

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.