from yaml import FullLoader, load

from .make_frontmatter import make_frontmatter


def update_frontmatter(md_path):

    separator = "---\n"

    frontmatter_line_ = []

    md_line_ = []

    with open(md_path) as io:

        in_frontmatter = False

        for line in io:

            if line == separator:

                in_frontmatter = not in_frontmatter

                continue

            if in_frontmatter:

                frontmatter_line_.append(line)

            else:

                md_line_.append(line)

    with open(md_path, mode="w") as io:

        io.write(
            make_frontmatter(**load("".join(frontmatter_line_), Loader=FullLoader))
        )

        io.write("".join(md_line_))
