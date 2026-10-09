def summarize_file(file_name):
    lines = 0
    words = 0
    with open(file_name, "r", encoding="utf-8") as file:
        for line in file:
            clean = line.strip()
            if clean:
                lines += 1
                words += len(clean.split())
    return lines, words


def main():
    file_name = "sample_input.txt"
    lines, words = summarize_file(file_name)
    print("Lines:", lines)
    print("Words:", words)


if __name__ == "__main__":
    main()
