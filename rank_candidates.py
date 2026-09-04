#!/usr/bin/env python3

import argparse


def main():
    parser = argparse.ArgumentParser(
        description="Rank candidates by interview score."
    )
    parser.add_argument(
        "candidates",
        nargs="+",
        help='Candidates in the format "Name:Score"'
    )

    args = parser.parse_args()

    candidates = []

    for entry in args.candidates:
        try:
            name, score = entry.rsplit(":", 1)
            candidates.append((name.strip(), float(score)))
        except ValueError:
            parser.error(
                f'Invalid candidate "{entry}". Use the format "Name:Score".'
            )

    candidates.sort(key=lambda x: x[1], reverse=True)

    print("Candidate Rankings")
    print("------------------")

    for rank, (name, score) in enumerate(candidates, start=1):
        print(f"{rank:>2}. {name:<25} {score:g}")


if __name__ == "__main__":
    main()
