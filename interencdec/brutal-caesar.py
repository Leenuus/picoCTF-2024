#!/usr/bin/env python

from sys import argv, stderr
from colorama import Fore


def main():
    for s in argv[1:]:
        print("-" * 10 + s + "-" * 10, file=stderr)
        for offset in range(26):
            d = {}
            for letter in range(26):
                d[chr(letter + ord("a"))] = chr((offset + letter) % 26 + ord("a"))
                d[chr(letter + ord("A"))] = chr((offset + letter) % 26 + ord("A"))

            res = []
            for c in s:
                res.append(d.get(c, c))
            res = "".join(res)
            red = Fore.RED if "picoCTF" in res else ""
            reset = Fore.RESET if "picoCTF" in res else ""
            print(f"{red}Result: {res}{reset}")
        print("-" * 10 + "-" * 10, file=stderr)
        print()


if __name__ == "__main__":
    main()
