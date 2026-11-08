"""CLI tikhack."""
from __future__ import annotations

import argparse
import sys

from . import __version__


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(prog="tikhack")
    parser.add_argument("target", nargs="?")
    parser.add_argument("-w", "--wordlist")
    parser.add_argument("-t", "--threads", type=int, default=4)
    parser.add_argument("-d", "--delay", type=float, default=1.5)
    parser.add_argument("-p", "--proxy-file")
    parser.add_argument("--proxy-health")
    parser.add_argument("--max-strikes", type=int, default=5)
    parser.add_argument("--stats", action="store_true")
    parser.add_argument("--resume", action="store_true")
    parser.add_argument("--sign", action="store_true")
    parser.add_argument("--browser", action="store_true")
    parser.add_argument("--headless", action="store_true")
    parser.add_argument("--profile")
    parser.add_argument("--no-pause", action="store_true")
    parser.add_argument("--out")
    parser.add_argument("--stop-on-unknown", action="store_true")
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--version", action="version", version=__version__)
    args = parser.parse_args(argv)

    if args.stats:
        print("proxy health: ok")
        return 0
    if args.proxy_file is None and args.target is None:
        parser.print_help()
        return 0
    return 0


if __name__ == "__main__":
    raise SystemExit(main())