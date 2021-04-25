`mdpost` is a command line program for making a post.

It complements [Gatsby.js](https://www.gatsbyjs.com) markdown workflow.

## Install

```sh
python3 -m pip install git+https://github.com/KwatME/MDPost.py
```

## Use

### Make a post

Make a post and start adding content to Title/index.md:

```sh
mdpost Title
```

Add some tags to the frontmatter:

```sh
mdpost "Title with Space" --tag Tag --tag "Tag with Space"
```

Copy some files to the post directory:

```sh
mdpost "Title with Space" --copy path/to/file --copy test/cover_template.key
```

### Convert a directory into a post

```sh
mdpost /path/to/directory
```

If directory/image/ exists, the images will be sorted and listed in directory/index.md.
You can simply take bunch of screenshots and automatically make a post with them.

```sh
mdpost test/Kobe\ and\ Jordan/
```

### Update frontmatter

```sh
mdpost path/to/index.md
```

```sh
mdpost test/Kobe\ and\ Jordan/index.md
```

---

Check out [kwatme.com](https://kwatme.com), which is built with [Gatsby.js](https://www.gatsbyjs.com) and [MDPost.py](https://github.com/KwatME/MDPost.py).
