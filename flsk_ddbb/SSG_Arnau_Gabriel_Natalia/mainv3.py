#! /usr/bin/env python3

"""
SSG v09
- Some refactorings to make it easier to understand.
- Easier debugging:   https://github.com/microsoft/debugpy/issues/258
- Also for debugging: import pprint; pprint.pp()
"""

from   pathlib import Path
from re import I
from   typing  import Iterator

import shutil
import sys

import cmdline
import engine
import os
import pprint


# -----------------------------------------------------------------------------

def read_md(input_dir: Path) -> list[str]:
    """Reads a markdown file and return a list with strings"""

    # Get the list of all markdown files
    markdown_dir:           Path           = input_dir/"md"
    markdown_filepath_iter: Iterator[Path] = markdown_dir.glob("*.md")
    markdown_filepath_list: list[Path]     = (markdown_filepath_iter)

    # Read all the markdown 
    md_str_list:   list[str]  = [path.read_text() for path in markdown_filepath_list]

    return md_str_list

def create_data(md_str_list: list[str]):
    """convert the md_str_list contents to html and metadata"""

    html_str_list: list[str]  = [engine.convert_md_to_html(md_str) for md_str in md_str_list]
    metadata_list: list[dict] = [engine.get_md_metadata(md_str)    for md_str in md_str_list]

    return html_str_list, metadata_list


def create_index(html_str_list: list[str], metadata_list: list[dict]) -> None:
    """create an html called index.html"""

    # convert the md_str_list contents to html and metadata
    html_str_list: list[str]  = [engine.convert_md_to_html(md_str) for md_str in md_str_list]
    metadata_list: list[dict] = [engine.get_md_metadata(md_str)    for md_str in md_str_list]

    # Fill template with entries (html, metadata)
    template_dir:      Path = input_dir/"html"
    template_filename: str  = "template.html"
    vars_dict:         dict = {"entry_list": zip(html_str_list, metadata_list)}
    html_str:          str  = engine.fill_template(template_dir, template_filename, vars_dict)

    # Write index.html to output dir
    output_dir.mkdir(exist_ok=True)
    (output_dir/"index.html").write_text(html_str)

    # Copy all resource dirs to output_path
    shutil.copytree(input_dir/"css", output_dir/"css", dirs_exist_ok=True)
    shutil.copytree(input_dir/"img", output_dir/"img", dirs_exist_ok=True)
    shutil.copytree(input_dir/"js",  output_dir/"js",  dirs_exist_ok=True)
 

def  create_blog(html_str_list: list[str], metadata_list: list[dict]) -> None:
    """creates an html that is called with the name of the title of each metadata"""

    html_str_list: list[str]  = [engine.convert_md_to_html(md_str) for md_str in md_str_list]
    metadata_list: list[dict] = [engine.get_md_metadata(md_str)    for md_str in md_str_list]


    zip_list: list[tuple[str, dict]] = list(zip(html_str_list, metadata_list))

    for html_str, metadata in zip_list:

        # Fill blog
        template_dir:      Path = input_dir/"html"
        template_filename: str  = "blog.html"
        vardict:            dict = {"entry_metadata":metadata, "entry_html":html_str}
        html_str:          str  = engine.fill_template(template_dir, template_filename, vardict)

        # Write html blog
        output_dir.mkdir(exist_ok=True)
        (output_dir/f"{metadata['title']}.html").write_text(html_str)


# -----------------------------------------------------------------------------
if __name__ == "__main__":

    # args: list[str] = sys.argv                       # For command-line
    args: list[str] = [sys.argv[0], "input", "output"] # For easy testing

    input_dir, output_dir = cmdline.parse_args(args)

    md_str_list: list[str] =read_md(input_dir)

    html_str_list, metadata_list = create_data(md_str_list)

    create_index(html_str_list, metadata_list)

    create_blog(html_str_list, metadata_list)

# -----------------------------------------------------------------------------
