import os
import sys

# -- Project information -----------------------------------------------------
project = 'rr_sb_sysytem_docs'
copyright = '2025, Rapyuta Robotics'
author = 'Rapyuta Robotics'

# -- General configuration ---------------------------------------------------
extensions = []

templates_path = ['_templates']
exclude_patterns = []

# -- Custom roles for reStructuredText ---------------------------------------
rst_prolog = """
.. role:: red
"""

# -- Options for HTML output -------------------------------------------------
html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
html_css_files = ['custom.css']
extensions = ['sphinx.ext.autosectionlabel']


html_logo = "_static/rapyuta_logo.png"  # or .svg

# Optional: Show only the logo (no project name text)
html_theme_options = {
    "logo_only": True,
    "display_version": False
}
