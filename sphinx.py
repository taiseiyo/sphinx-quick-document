#!/usr/bin/env python3
from pyfzf.pyfzf import FzfPrompt
import urllib.request
from bs4 import BeautifulSoup

fzf = FzfPrompt()
sphinx_name_list = ["section", "list",
                    "sourcecode", "table", "image", "link"]


def generate_dict(sphinx_name_list):
    basic_url = "http://tdoc.info/sphinx-reverse-dict/basic/"
    last_url = ".html"
    sphinx_dict = {}
    for name in sphinx_name_list:
        sphinx_dict.update({name: basic_url + name + last_url})
    return sphinx_dict


def url_process(sphinx_dict, name):
    document = ""
    url = urllib.request.Request(sphinx_dict[name])
    with urllib.request.urlopen(url) as res:
        html_body = res.read()

    soup = BeautifulSoup(html_body, "html.parser")
    for line in soup.find_all(text=True):
        document = document + line
    print(document)


def main():
    sphinx_dict = generate_dict(sphinx_name_list)
    name = fzf.prompt(sphinx_name_list)[0]
    url_process(sphinx_dict, name)


main()
