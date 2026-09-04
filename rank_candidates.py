```python
#!/usr/bin/env python3

import argparse


def main():
    parser = argparse.ArgumentParser(
        description="Rank candidates by interview score.",
        epilog='Example: python3 rank_candidates.py "Alice Johnson:92" "Bob Smith:87"',
    )

    parser.add_argument(
        "candidates",
        nargs="+",
        help='Candidates in the format "Name:Score"',
    )

    args = parser.parse_args()

    candidates = []

    for entry in args.candidates:
        if ":" not in entry:
            parser.error(
                f'Invalid input: "{entry}"\n'
                '  Expected format: "Name:Score"\n'
                '  Example: "Alice Johnson:92"'
            )

        name, score_text = entry.rsplit(":", 1)
        name = name.strip()
        score_text = score_text.strip()

        if not name:
            parser.error(
                f'Invalid input: "{entry}"\n'
                "  The candidate name cannot be empty.\n"
                '  Example: "Alice Johnson:92"'
            )

        try:
            score = float(score_text)
        except ValueError:
            parser.error(
                f'Invalid score for candidate "{name}": "{score_text}"\n'
                "  The score must be a number.\n"
                '  Example: "Bob Smith:87" or "Bob Smith:87.5"'
            )

        candidates.append((name, score))

    candidates.sort(key=lambda x: x[1], reverse=True)

    print("Candidate Rankings")
    print("------------------")

    for rank, (name, score) in enumerate(candidates, start=1):
        print(f"{rank:>2}. {name:<25} {score:g}")


if __name__ == "__main__":
    main()
```
