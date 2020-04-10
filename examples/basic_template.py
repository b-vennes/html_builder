import sys
import os

# need to add html_builder to python path
html_builder_path = os.path.join(os.getcwd(), '..')
sys.path.append(html_builder_path)

from html_builder.html_builder.html import Html

container = Html('div', 'container')

title = Html('h1')
title.children += ['Test Application']

container.children += [title]

print(container.render())