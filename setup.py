from setuptools import (
    setup,
)

n = "mdpost"

setup(
    name=n,
    version="0.2.0",
    python_requires=">=3.6",
    install_requires=(
        "click",
        "pyyaml",
    ),
    packages=(n,),
    entry_points={
        "console_scripts": (
            "{0}={1}.{2}:{2}".format(
                n.lower(),
                n,
                "cli",
            ),
        )
    },
)
