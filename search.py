import argparse

parser = argparse.ArgumentParser(description="Search Korean phrases translated by HYBE")

# TODO: command-line scripts: be able to search Korean words to grab sentence?
parser.add_argument("kr", type=str, help="Korean phrase to search")

args = parser.parse_args()