from click import secho


def log(message):

    secho(message, fg="bright_green", bold=True)
