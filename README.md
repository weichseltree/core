# Basis for python-based research projects. 


## Clean Notebooks

In order to keep notebooks in this project small and clean, there is a script to remove output data from the .ipynb files. To enable this filter, add this entry to your `.git/config`.

```
[filter "clean_notebook"]
    clean = /home/<path to git folder>/package/clean_notebook.py
```
