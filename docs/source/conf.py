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

html_theme = 'sphinxawesome_theme'
html_logo = '../Logo.jpg'

html_theme_options = {
    'light_css_variables': {
        'color-brand-primary': '#DC3545',
        'color-brand-content': '#DC3545',
    },
    'style_nav_header_background': '#DC3545',
    'sidebarbgcolor': '#DC3545',
    'sidebartextcolor': 'white',
    #Toc options
    'titles_only': True,
    'sticky_navigation': True,
 }

html_context = {
  'display_github': True,
  'github_user': 'PCN',
  'github_repo': 'user manual',
}

html_css_files = [
    'css/custom.css',
]

# -- Options for EPUB output
epub_show_urls = 'footnote' 
