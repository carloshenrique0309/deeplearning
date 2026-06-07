from pathlib import Path

from src.imdb_data import count_reviews

DATA_DIR = Path("data/raw/aclImdb")

def main() -> None:
    if not DATA_DIR.exists():
        raise FileNotFoundError(
            f"Dataset nao encontrado em {DATA_DIR}. "
            "Extraia o arquivo aclImdb_v1.tar.gz para data/raw/."
        )

    counts = count_reviews(DATA_DIR)
    print("Resumo do dataset IMDb:")
    for split, labels in counts.items():
        print(f"- {split}:")
        for label, total in labels.items():
            print(f"  - {label}: {total}")


if __name__ == "__main__":
    main()
