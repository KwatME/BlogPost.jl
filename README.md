`mdpost` is a command line program for making markdown-based post.

It complements [Gatsby.js](https://www.gatsbyjs.com) markdown workflow.

## Install

```sh
pip install git+https://github.com/KwatME/MDPost.py
```

## Use

Make a post and starting writing in Title/index.md.

```sh
mdpost make Title
```

```sh
mdpost make "Anoher Title" --tag Tag --tag "Another Tag"
```

```sh
mdpost make "Yet Anoher Title" --tag Tag --tag "Another Tag" --cover path/to/cover.jpeg
```

Convert an existing directory into a post directory.
If directory/image/ has images (named [0-9+].png), this will sort and add them to the directory/index.md.
This is powerful because you can simply take bunch of screenshots and automatically make a post with them.

```sh
mdpost make /path/to/directory
```

Update frontmatter's time to be now.

```sh
mdpost update path/to/index.md
```
