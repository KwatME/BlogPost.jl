from click import Path, argument, command, group, option

from .log import log
from .make_post_directory import make_post_directory
from .update_frontmatter import update_frontmatter


@group()
def cli():
    """
    `mdpost` is a command line program for making markdown-based post.

    https://github.com/KwatME/MDPost.py
    """


@command()
@argument("title", nargs=1)
@option("--cover-template", type=Path(exists=True))
@option("--cover", default="cover.jpeg")
@option("--tag", multiple=True)
def make(title, cover, tag, cover_template):
    """
    Make a post
    """

    directory_path = title

    log('Making "{}/"...'.format(directory_path))

    make_post_directory(
        directory_path, cover_template, title=title, cover=cover, tags=list(tag)
    )


@command()
@argument("md_path", type=Path(exists=True))
def update(md_path):
    """
    Update frontmatter's time
    """

    log("Updating {}...".format(md_path))

    update_frontmatter(md_path)


cli.add_command(make)

cli.add_command(update)

if __name__ == "__main__":

    cli()
