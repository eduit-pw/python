import argparse
def argumenty(argv):
    p = argparse.ArgumentParser()
    p.add_argument("--limit", default=10)
    return p.parse_args(argv)
