import os

TEXT = "Cursor blinks at three\na thousand log lines scroll past\njust one wrong letter"


def main():
    assert 1 <= len(TEXT) <= 200, "gate: entry must be 1-200 chars"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
