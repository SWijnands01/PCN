# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'PCN'
copyright = '2022, SWijnands'
author = 'SWijnands'

release = '0.1'
version = '0.1.0'

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output

html_theme = 'sphinx_rtd_theme'
html_logo = 'logo.jpg'

html_theme_options = {
    'style_nav_header_background': 'black',
}

html_context = {
  'display_github': True,
  'github_user': 'PCN',
  'github_repo': 'user manual',
}

# -- Options for EPUB output
epub_show_urls = 'footnote' 
