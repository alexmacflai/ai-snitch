#!/usr/bin/env python3
"""Generate external creative stimuli; no files or network access required."""
import argparse
import secrets
import string


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--count', type=int, default=1)
    parser.add_argument('--length', type=int, default=64)
    args = parser.parse_args()
    if not 1 <= args.count <= 100 or not 16 <= args.length <= 256:
        parser.error('count must be 1–100 and length 16–256')
    alphabet = string.ascii_letters + string.digits
    for _ in range(args.count):
        print(''.join(secrets.choice(alphabet) for _ in range(args.length)))


if __name__ == '__main__':
    main()
