#! /usr/bin/env python3

"""
SSG v09
- Some refactorings to make it easier to understand.
- Easier debugging:   https://github.com/microsoft/debugpy/issues/258
- Also for debugging: import pprint; pprint.pp()
"""

from datetime import date
from   pathlib import Path
from   typing  import Iterator

import shutil
import sys

import cmdline
import engine

import pprint


# -----------------------------------------------------------------------------
def main(input_dir: Path, output_dir: Path) -> None:
    """Reads a markdown file and writes its html conversion."""

    # Get the list of all markdown files
    markdown_dir:           Path           = input_dir/"md"/"peliculas"
    markdown_filepath_iter: Iterator[Path] = markdown_dir.glob("*.md")
    markdown_filepath_list: list[Path]     = sorted(markdown_filepath_iter)

    # Read all MarkDown (md) files and convert their contents to html and metadata
    md_str_list:   list[str]  = [path.read_text() for path in markdown_filepath_list]
    html_str_list: list[str]  = [engine.convert_md_to_html(md_str) for md_str in md_str_list]
    metadata_list: list[dict] = [engine.get_md_metadata(md_str)    for md_str in md_str_list]

    # Fill template with entries (html, metadata)
    template_dir:      Path = input_dir/"html"
    template_filename: str  = "peliculas.html"
    vars_dict:         dict = {"entry_list": zip(html_str_list, metadata_list)}
    html_str:          str  = engine.fill_template(template_dir, template_filename, vars_dict)

    # Write index.html to output dir
    output_dir.mkdir(exist_ok=True)
    (output_dir/"peliculas.html").write_text(html_str)

    # Copy all resource dirs to output_path
    shutil.copytree(input_dir/"css", output_dir/"css", dirs_exist_ok=True)
    shutil.copytree(input_dir/"img", output_dir/"img", dirs_exist_ok=True)
    shutil.copytree(input_dir/"js",  output_dir/"js",  dirs_exist_ok=True)
    
    #############################################################################################################
    # Get the list of all markdown files
    markdown_dir:           Path           = input_dir/"md"/"series"
    markdown_filepath_iter: Iterator[Path] = markdown_dir.glob("*.md")
    markdown_filepath_list: list[Path]     = sorted(markdown_filepath_iter)

    # Read all MarkDown (md) files and convert their contents to html and metadata
    md_str_list:   list[str]  = [path.read_text() for path in markdown_filepath_list]
    html_str_list: list[str]  = [engine.convert_md_to_html(md_str) for md_str in md_str_list]
    metadata_list: list[dict] = [engine.get_md_metadata(md_str)    for md_str in md_str_list]

    # Fill template with entries (html, metadata)
    template_dir:      Path = input_dir/"html"
    template_filename: str  = "series.html"
    vars_dict:         dict = {"entry_list": zip(html_str_list, metadata_list)}
    html_str:          str  = engine.fill_template(template_dir, template_filename, vars_dict)

    # Write index.html to output dir
    output_dir.mkdir(exist_ok=True)
    (output_dir/"series.html").write_text(html_str)

    # Copy all resource dirs to output_path
    shutil.copytree(input_dir/"css", output_dir/"css", dirs_exist_ok=True)
    shutil.copytree(input_dir/"img", output_dir/"img", dirs_exist_ok=True)
    shutil.copytree(input_dir/"js",  output_dir/"js",  dirs_exist_ok=True)

    ###########################################################################################################

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

    #############################################################################################################

        # Get the list of all markdown files
    markdown_dir:           Path           = input_dir/"md"/"equipos"
    markdown_filepath_iter: Iterator[Path] = markdown_dir.glob("*.md")
    markdown_filepath_list: list[Path]     = sorted(markdown_filepath_iter)

    # Read all MarkDown (md) files and convert their contents to html and metadata
    md_str_list:   list[str]  = [path.read_text() for path in markdown_filepath_list]
    html_str_list: list[str]  = [engine.convert_md_to_html(md_str) for md_str in md_str_list]
    metadata_list: list[dict] = [engine.get_md_metadata(md_str)    for md_str in md_str_list]

    # Fill template with entries (html, metadata)
    template_dir:      Path = input_dir/"html"
    template_filename: str  = "equipos.html"
    vars_dict:         dict = {"entry_list": zip(html_str_list, metadata_list)}
    html_str:          str  = engine.fill_template(template_dir, template_filename, vars_dict)

    # Write index.html to output dir
    output_dir.mkdir(exist_ok=True)
    (output_dir/"equipos.html").write_text(html_str)

    # Copy all resource dirs to output_path
    shutil.copytree(input_dir/"css", output_dir/"css", dirs_exist_ok=True)
    shutil.copytree(input_dir/"img", output_dir/"img", dirs_exist_ok=True)
    shutil.copytree(input_dir/"js",  output_dir/"js",  dirs_exist_ok=True)


    # names : list[str] = ["2001 A Space Odyssey","Arrival","Cape Fear","Catch Me If You Can","Jaws","Tenet","The Shining"]

    # for name in names:
    #     template_dir:      Path = input_dir/"html"
    #     template_filename: str  = "blog.html"
    #     var_dict:         dict = {"entry": html_str_list}
    #     html_str:          str  = engine.fill_template(template_dir, template_filename, var_dict)

    # # #     # Write index.html to output dir
        # output_dir.mkdir(exist_ok=True)
        # (output_dir/f"{name}.html").write_text(html_str)


    # titles_dir: Path = input_dir/"md"/"titles.md"
    # tnv: str = Path(titles_dir).read_text()
    # titles_list: list[str] = tnv.split(",")

    # date_dir: Path = input_dir/"md"/"dates.md"
    # dnv: str = Path(date_dir).read_text()
    # dates_list: list[str] = dnv.split(",")

    # aut_dir: Path = input_dir/"md"/"authors.md"
    # anv: str = Path(aut_dir).read_text()
    # authors_list: list[str] = anv.split(",")

    # for title in titles_list:
    #     tmp_dir: Path = input_dir/"html"
    #     template_filename: str  = "blog.html"
    #     var_dict: dict = {"title": title}
    #     title: str = engine.fill_template(tmp_dir,template_filename,var_dict)
    # for date in dates_list:
    #     for author in authors_list:
    #         for title in titles_list:
    #             tmp_dir: Path = input_dir/"html"
    #             template_filename: str  = "blog.html"
    #             var_dict: dict = {"title": title, "autor": author, "date": date}
    #             blog: str = engine.fill_template(tmp_dir,template_filename,var_dict)
    #             output_dir.mkdir(exist_ok=True)
    #             (output_dir/f"{title}.html").write_text(blog)
    

    # casi funciona tiene errores
    # for title in titles_list:
    #     for date in dates_list:
    #         for author in authors_list:
    #             tmp_dir: Path = input_dir/"html"
    #             template_filename: str  = "blog.html"
    #             var_dict: dict = {"title": title,"date": date, "author": author}
    #             blog: str = engine.fill_template(tmp_dir,template_filename,var_dict)
    #             output_dir.mkdir(exist_ok=True)
    #             (output_dir/f"{title}.html").write_text(blog)


    # for title in titles_list:
    #     template_dir: Path = input_dir/"html"
    #     template_filename: str  = "blog.html"
    #     vars_dict:dict = {"entry_list": zip(html_str_list, metadata_list)}
    #     html_str: str  = engine.fill_template(template_dir, template_filename, vars_dict)
                # var_dict: dict = {"title": title,"date": date, "author": author}
                # blog: str = engine.fill_template(tmp_dir,template_filename,var_dict)
        # output_dir.mkdir(exist_ok=True)
        # (output_dir/f"{title}.html").write_text(html_str)
    

    # for title in titles_list:
    #     tmp_dir: Path = input_dir/"html"
    #     template_filename: str  = "blog.html"
    #     var_dict: dict = {"title": title}
    #     blog: str = engine.fill_template(tmp_dir,template_filename,var_dict)
    #     (output_dir/f"{title}.html").write_text(blog)
    #     for date in dates_list:
    #         var_dict: dict = {"date": date}
    #         blog: str = engine.fill_template(tmp_dir,template_filename,var_dict)
    #         (output_dir/f"{title}.html").write_text(blog)
    #         for author in authors_list:
    #             var_dict: dict = {"author": author}
    #             blog: str = engine.fill_template(tmp_dir,template_filename,var_dict)
    #             output_dir.mkdir(exist_ok=True)
    #             (output_dir/f"{title}.html").write_text(blog)

    # for title in titles_list:
    #     tmp_dir: Path = input_dir/"html"
    #     template_filename: str  = "blog.html"
    #     var_dict: dict = {"title": title}
    #     blog: str = engine.fill_template(tmp_dir,template_filename,var_dict)


    # for date in dates_list:
    #     tmp_dir: Path = input_dir/"html"
    #     template_filename: str  = "blog.html"
    #     var_dict: dict = {"date": date}
    #     blog: str = engine.fill_template(tmp_dir,template_filename,var_dict)


    # for author in authors_list:
    #     tmp_dir: Path = input_dir/"html"
    #     template_filename: str  = "blog.html"
    #     var_dict: dict = {"author": author}
    #     blog: str = engine.fill_template(tmp_dir,template_filename,var_dict)
    #     output_dir.mkdir(exist_ok=True)
    #     (output_dir/f"{title}.html").write_text(blog)
        # for date in dates_list:
        #     date_dict: dict = {"date": date}
        #     blog: str = engine.fill_template(tmp_dir,template_filename,date_dict)
        #     for author in authors_list:
        #         aut_dict: dict = {"autor": author}
        #         blog: str = engine.fill_template(tmp_dir,template_filename,aut_dict)
        #         output_dir.mkdir(exist_ok=True)
        #         (output_dir/f"{title}.html").write_text(blog)

    
# -----------------------------------------------------------------------------
if __name__ == "__main__":

    # args: list[str] = sys.argv                       # For command-line
    args: list[str] = [sys.argv[0], "input", "output"] # For easy testing

    input_dir, output_dir = cmdline.parse_args(args)

    main(input_dir, output_dir)

# -----------------------------------------------------------------------------
