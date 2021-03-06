from __future__ import print_function

import argparse
import sys

BLACKLIST = [
    b'BEGIN RSA PRIVATE KEY',
    b'BEGIN DSA PRIVATE KEY',
    b'BEGIN EC PRIVATE KEY',
    b'BEGIN OPENSSH PRIVATE KEY',
    b'print ',
]


def detect_private_key(argv=None):
    parser = argparse.ArgumentParser()
    parser.add_argument('filenames', nargs='*', help='Filenames to check')
    args = parser.parse_args(argv)

    private_key_files = []

    for filename in args.filenames:
        with open(filename, 'rb') as f:
            content = f.read()
            if any(line in content for line in BLACKLIST):
                private_key_files.append((filename, line))

    if private_key_files:
        for private_key_file in private_key_files:
            print('Print statement found! File:{0}, line:{1}'.format(*private_key_file))
        return 1
    else:
        return 0


if __name__ == '__main__':
    sys.exit(detect_private_key())
