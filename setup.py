from setuptools import setup

na = "md_post"

setup(
    name=na,
    version="0.3.0",
    python_requires=">=3.6",
    install_requires=["click", "pyyaml"],
    packages=[na],
    entry_points={
        "console_scripts": ["{0}={0}.{1}:{1}".format(na, "cli")],
    },
)
