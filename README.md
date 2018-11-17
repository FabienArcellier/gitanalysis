## Gitanalysis

[![Build Status](https://travis-ci.org/FabienArcellier/gitanalysis.svg?branch=master)](https://travis-ci.org/FabienArcellier/gitanalysis)

transform a formatted log from git as csv file

git log - `git log --pretty=format:'-%h;%an;%ad' --numstat`

```
-79e6be4;Fabien Arcellier;Mon Jul 23 13:37:45 2018 +0200
2       2       .env.dist
1       1       VERSION.in
2       2       app/config/parameters.php
4       4       src/AppBundle/Resources/config/services.yml
2       2       src/Slidesearch/Infrastructures/SlidesearchStorage/IndexHandler.php
-985d57e;Fabien Arcellier;Mon Jul 23 16:00:56 2018 +0200
-80e5be4;Fabien Arcellier;Mon Jul 23 13:37:45 2018 +0200
2       2       .env.dist
1       1       VERSION.in
2       2       app/config/parameters.php
4       4       src/AppBundle/Resources/config/services.yml
2       2       src/Slidesearch/Infrastructures/SlidesearchStorage/IndexHandler.php
```

changelog expose on stdout as csv file

```
shorthash,author,date,insertions,deletions,filename
c166c30,Fabien Arcellier,2015-08-13 07:10:38,1,9,src/AppBundle/Controller/DefaultController.php
c166c30,Fabien Arcellier,2015-08-13 07:10:38,0,5,src/AppBundle/Resources/views/default/home.html.twig
c166c30,Fabien Arcellier,2015-08-13 07:10:38,1,1,src/AppBundle/Resources/views/default/slides.html.twig
2fc1fdf,Fabien Arcellier,2015-08-01 12:59:28,4,0,README.md
2fc1fdf,Fabien Arcellier,2015-08-01 12:59:28,7,0,app/.htaccess
2fc1fdf,Fabien Arcellier,2015-08-01 12:59:28,9,0,app/AppCache.php
2fc1fdf,Fabien Arcellier,2015-08-01 12:59:28,36,0,app/AppKernel.php
2fc1fdf,Fabien Arcellier,2015-08-01 12:59:28,13,0,app/Resources/views/base.html.twig
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
  changelog  export a csv change from git log
```

### Changelog

```
Usage: gitanalysis changelog [OPTIONS]

  export a csv change from git log

Options:
  --use-git           force the usage of git on the current directory
  --date_format TEXT  date format - ref : https://docs.python.org/3/library/da
                      tetime.html#strftime-and-strptime-behavior
  --help              Show this message and exit.
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