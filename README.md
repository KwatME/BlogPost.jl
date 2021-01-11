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
If directory/image/ has images ([number].png), links to these images will be listed in directory/index.md.

```sh
mdpost make /path/to/directory
```

Update frontmatter's time to be now.

```sh
mdpost update path/to/index.md
```
