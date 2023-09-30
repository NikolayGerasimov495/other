import click

@click.command()
@click.argument('src', envvar='SRC', type=click.File('r'))
def echo(src):
    """Print value of SRC environment variable."""
    click.echo(src.read())


if __name__ == "__main__":
    echo()
#

# @click.command()
# @click.argument('filename', envvar='SRC', type=click.Path(exists=True))
# def touch(filename):
#     """Print FILENAME if the file exists."""
#     click.echo(click.format_filename(filename))
#     print('qw')


# if __name__ == "__main__":
#     touch()
