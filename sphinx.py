#!/usr/bin/env python3
from pyfzf.pyfzf import FzfPrompt
import urllib.request
from bs4 import BeautifulSoup

fzf = FzfPrompt()

basic_url = "http://tdoc.info/sphinx-reverse-dict/basic/"
last_url = ".html"
sphinx_name_list = ["section", "list", "sourcecode", "table", "image", "link"]


def generate_dict(sphinx_name_list):
    sphinx_dict = {}
    for name in sphinx_name_list:
        sphinx_dict.update({name: basic_url + name + last_url})
    return sphinx_dict


sphinx_dict = generate_dict(sphinx_name_list)
name = fzf.prompt(sphinx_name_list)[0]


def url_process():
    document = ""
    url = urllib.request.Request(sphinx_dict[name])
    with urllib.request.urlopen(url) as res:
        html_body = res.read()

    soup = BeautifulSoup(html_body, "html.parser")
    for line in soup.find_all(text=True):
        document = document + line
    print(document)


def main():
    url_process()


main()
