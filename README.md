`mdpost` is a command line program for making markdown-based post.

It complements [Gatsby.js](https://www.gatsbyjs.com) markdown workflow.

## Install

```sh
pip install git+https://github.com/KwatME/MDPost.py
```

## Use

Make a post and starting writing in Title/index.md:

```sh
mdpost Title
```

```sh
mdpost "Title with Space" --tag Tag --tag "Tag with Space"
```

Convert a directory with image/ into a post:

```sh
mdpost /path/to/directory
```

If directory/image/ has images, they will be sorted and listed in directory/index.md.
This is powerful because you can simply take bunch of screenshots and automatically make a post with them.

```sh
mdpost test/Kobe\ and\ Jordan/
```

Update frontmatter:

```sh
mdpost path/to/index.md
```

```sh
mdpost test/Kobe\ and\ Jordan/index.md
```

#### Check out [kwatme.com](https://kwatme.com), which is built with [Gatsby.js](https://www.gatsbyjs.com) and [MDPost.py](https://github.com/KwatME/MDPost.py).
