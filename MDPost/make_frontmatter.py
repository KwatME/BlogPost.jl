from datetime import datetime

from yaml import dump


def make_frontmatter(**kwargs):

    frontmatter = ""

    separator = "---\n"

    frontmatter += separator

    frontmatter += dump(
        {
            **kwargs,
            "time": datetime.now(),
        },
        default_flow_style=None,
    )

    frontmatter += separator

    return frontmatter
