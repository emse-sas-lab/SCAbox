# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys
sys.path.insert(0, os.path.abspath('.'))
sys.path.append("../../") # to locate scabox module


#add_module_names = False

# -- Project information -----------------------------------------------------
master_doc = 'index'
project = 'SCAbox'
copyright = '2022, EMSE'
author = 'Joseph Gravellier, Sami Dahoux, Jean-Max Dutertre'

# The full version, including alpha/beta/rc tags
release = '0.0.1'


# -----------------------------------------------------------------------------
# General configuration
# -----------------------------------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
'sphinx.ext.autodoc',
'sphinx.ext.autosummary',
'sphinx.ext.intersphinx',
#'numpydoc',
#'myst_nb',
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

exclude_dirs = []
default_role = "autolink"
add_function_parentheses = False

# -----------------------------------------------------------------------------
# HTML output
# -----------------------------------------------------------------------------

html_theme = 'pydata_sphinx_theme'
html_logo = ""
html_favicon = "media/img/scabox_logo.ico"

html_title = project
html_static_path = []
html_last_updated_fmt = '%b %d, %Y'

html_additional_pages = {}
html_use_modindex = True
html_domain_indices = False
html_copy_source = False
html_file_suffix = '.html'
htmlhelp_basename = 'scabox'


