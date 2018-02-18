import click
from .pymeetups import PyMeetups


@click.command()
def main():
    PyMeetups().populate_texttable()
    return 0


if __name__ == "__main__":
    import sys
    sys.exit(main())