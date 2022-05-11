import os


def root():
    r"""get main directory ."""

    return os.path.abspath(r'..\..\..\..')


def resources_path():
    r"""get resources directory ."""

    return root() + r'\resources'
