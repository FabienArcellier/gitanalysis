## Motivation

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

You can run the application with the following command

```bash
gitanalysis changelog
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

A short snippet describing the license (MIT, Apache, etc.)
