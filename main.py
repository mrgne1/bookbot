alphabet = set("abcdefghijklmnopqrstuvwxyz")

def main(path):
    report = create_report(path)
    print_report(report)

def create_report(path):
    text = read_text(path)
    word_count = count_words(text)
    text_histogram = string_histogram(text)

    return {"path": path, "text": text, "word_count": word_count, "text_histogram": text_histogram}

def print_report(report):
    print(f"--- Begin report of {report['path']} ---")
    
    print(f"{report['word_count']} words found in the document")
    print()

    character_counts = list(report["text_histogram"].items())
    character_counts.sort(reverse=True, key=lambda x: x[1])
    for char, count in character_counts:
        if char in alphabet:
            print(f"The '{char}' character was found {count} times")
    
    print("--- End report ---")
    
def read_text(path):
    with open(path) as f:
        text = f.read()
    return text

def count_words(text):
    return len(text.split())

def string_histogram(text):
    hist = {}
    for c in text.lower():
        hist[c] = hist.get(c, 0) + 1
    return hist

if __name__ == "__main__":
    path = "books/frankenstein.txt"
    main(path)