from setuptools import setup

name = "MDPost"

setup(
    name=name,
    version="0.1.0",
    python_requires=">=3.6",
    install_requires=("click", "pyyaml"),
    packages=(name,),
    entry_points={
        "console_scripts": ("{0}={1}.{2}:{2}".format(name.lower(), name, "cli"),)
    },
)
