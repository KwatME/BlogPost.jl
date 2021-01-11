from os import listdir, mkdir
from os.path import isdir, join, splitext

from .log import log
from .make_frontmatter import make_frontmatter


def make_post_directory(directory_path, cover_template, **frontmatter):

    md_path = join(directory_path, "index.md")

    md = ""

    if isdir(directory_path):

        image_directory_name = "image"

        image_directory_path = join(directory_path, image_directory_name)

        if isdir(image_directory_path):

            log("Listing {}/[number].png in .md...".format(image_directory_path))

            prefix_ = [
                splitext(name)[0]
                for name in listdir(image_directory_path)
                if name[0] != "."
            ]

            for number in sorted([int(prefix) for prefix in prefix_]):

                md += "\n![]({}/{}.png)\n".format(image_directory_name, number)

    else:

        log("Making {}...".format(directory_path))

        mkdir(directory_path)

    log("Copying {} to {}...".format(cover_template, directory_path))

    with open(md_path, mode="w") as io:

        io.write(make_frontmatter(**frontmatter))

        io.write(md)
