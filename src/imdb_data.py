from pathlib import Path

import pandas as pd


LABELS = {
    "neg": 0,
    "pos": 1,
}


def iter_review_files(dataset_dir: Path, split: str):
    split_dir = dataset_dir / split
    for label_name, label_value in LABELS.items():
        label_dir = split_dir / label_name
        for path in sorted(label_dir.glob("*.txt")):
            yield split, label_name, label_value, path


def load_reviews(dataset_dir: str | Path) -> pd.DataFrame:
    dataset_path = Path(dataset_dir)
    rows = []

    for split in ("train", "test"):
        for split_name, label_name, label_value, path in iter_review_files(dataset_path, split):
            rows.append(
                {
                    "split": split_name,
                    "label": label_name,
                    "target": label_value,
                    "review": path.read_text(encoding="utf-8"),
                    "file": str(path),
                }
            )

    return pd.DataFrame(rows)


def count_reviews(dataset_dir: str | Path) -> dict[str, dict[str, int]]:
    dataset_path = Path(dataset_dir)
    counts: dict[str, dict[str, int]] = {}

    for split in ("train", "test"):
        counts[split] = {}
        for label_name in LABELS:
            counts[split][label_name] = len(list((dataset_path / split / label_name).glob("*.txt")))

    return counts
