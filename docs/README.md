# Producing Code Documentation Using Sphinx
This is a short demonstration of using sphinx to document code

In Visual Studio Code open the folder that holds your code folder

Create an environment as previously
```sh
python -m venv .env
```

Install sphinx::
```sh
python -m pip install sphinx
```

In VSCode open a terminal and create a folder "docs" and change to that folder::
```sh
mkdir docs
cd docs
```
Run sphinx setup
```sh
sphinx-quickstart 
```
In the source folder you edit conf.py to uncomment the lines
```python
import os
import sys
sys.path.insert(0, os.path.abspath('../../{folder name for your code}'))
```
and add the extension 'sphinx.ext.autodoc' and 'sphinx.ext.napoleon'

In vscode check you are in the docs folder and run
```sh
make html
```

Check the output by going to the same docs folder in windows explorer and then open buid\html\index.html


This is your first output.  Look in the index.rst file to see how this has been translated.  Note none of your code comments are there.


For further reference on restructured text see

https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html

https://docs.anaconda.com/restructuredtext/detailed/

Autodoc
-------

To see how autodoc generates documentation add the following lines after the toctree block in the index.rst file
```rst
.. automodule:: requests
   :members:
```
Run the make command again and look at the output - you should see documentation for requests module

Try replacing "requests" with the name of one of your modules (in the folder you pointed to in the conf.py file.
so for example if you use Michael's mygui.py example and put it in the folder you specified in conf.py try::
```rst
.. automodule:: mygui
   :members:
   :private-members:
   :special-members:
```

The documentation for autodoc is here

https://eikonomega.medium.com/getting-started-with-sphinx-autodoc-part-1-2cebbbca5365

https://www.sphinx-doc.org/en/master/usage/extensions/autodoc.html

http://www.pythondoc.com/sphinx/ext/autodoc.html


Creating a pdf with rinohtype
-----------------------------

Install rinohtype
```sh
python -m pip install rinohtype
````
Edit the conf.py file to include the extension::
```python
'rinoh.frontend.sphinx'
```
and add the definition at the end of the file
```python
# Rinohtype configuration----------------------------------------------------------
rinoh_documents = [dict(doc='index', # top-level file (index.rst)
target='manual')] # output file (manual.pdf)
```

Make the pdf
```sh
make rinoh
```
To explore rinohtype see

https://www.mos6581.org/rinohtype/master/intro.html

https://www.mos6581.org/rinohtype/master/manual.pdf

(note issues with Python 3.10 and rinohtype)

Creating a pdf with LaTeX
-------------------------

To create a pdf install mktex if you do not already have LaTeX installed

Run
```sh
make latex
````   
Cd to build\latex and find the tex file with the name you gave the project {project name}.tex and run::
```sh
pdflatex {project name}.tex
```    
This will create {project name}.pdf in the same folder
 
 