#!/usr/bin/env python3
"""Create LaTeX documents."""

import argparse
import os

parser = argparse.ArgumentParser(
    prog="create-latex",
    description="Create LaTeX documents."
)

parser.add_argument(
    "docname",
    metavar="name",
    help="The name of the document to create."
)

parser.add_argument(
    "-n", "--new",
    help="Create as a new project",
    action="store_true"
)

args = parser.parse_args()

os.system("cp ~/Documents/dev/latex-templates/document.tex {}.tex".format(args.docname))
if args.new:
    os.system("cp ~/Documents/dev/latex-templates/preamble.tex .")
