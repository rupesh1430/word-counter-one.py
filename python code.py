#--------------------------------------------------- 
# Ps number : 10 
# Project Title: word counter 
# Student Name: Rupesh kumar sidar 
# Email : rupesh.kumar.sidar@rungta.org
# ERP : RU 26 01065
# Section : BCA 1B 
#----------------------------------------------------
"""
Word Counter & Text Analyzer
----------------------------
Reads text from the user or from a file and reports:
  - number of words, characters, sentences
  - frequency of each word (dictionary)
  - unique words (set)

Counting is case-insensitive and punctuation is removed before counting words.
"""

import string


# ---------------------------------------------------------------- input ----
def read_text_from_user():
    """Return text typed by the user (may be empty)."""
    return input("Enter your text: ").strip()


def read_text_from_file():
    """Return (text, error_message). One of them is None."""
    name = input("Enter file name: ").strip()
    try:
        with open(name, "r", encoding="utf-8") as f:
            return f.read().strip(), None
    except FileNotFoundError:
        return None, f"File '{name}' not found."
    except OSError:
        return None, f"File '{name}' could not be read."


# ------------------------------------------------------------- cleaning ----
def clean_words(text):
    """Lower-case the text, strip punctuation and return a list of words."""
    text = text.lower()
    text = text.replace("'", "")            # don't -> dont
    for ch in string.punctuation:
        text = text.replace(ch, " ")        # 'end.Start' -> 'end Start'
    return text.split()


def count_sentences(text):
    """Count sentences ending with '.', '!' or '?'."""
    text = text.replace("!", ".").replace("?", ".")
    parts = text.split(".")
    return len([p for p in parts if p.strip() != ""])


# ------------------------------------------------------------- analysis ----
def word_frequency(words):
    """Return a dictionary {word: count}."""
    freq = {}
    for w in words:
        freq[w] = freq.get(w, 0) + 1
    return freq


def sorted_by_frequency(freq):
    """Sort by count (high to low), then alphabetically."""
    return sorted(freq.items(), key=lambda item: (-item[1], item[0]))


def analyse(text):
    """Run all calculations and return them in a dictionary."""
    words = clean_words(text)
    return {
        "words": len(words),
        "chars": len(text),                 # with spaces
        "sentences": count_sentences(text),
        "freq": word_frequency(words),
        "unique": set(words),
    }


# -------------------------------------------------------------- reports ----
def show_summary(r):
    print(f"Words: {r['words']} | Characters (with spaces): {r['chars']} "
          f"| Sentences: {r['sentences']} | Unique words: {len(r['unique'])}")


def show_frequency(r, top_n=5):
    ranked = sorted_by_frequency(r["freq"])
    top = " | ".join(f"{w}: {c}" for w, c in ranked[:top_n])
    print("Top words:", top)
    print("\nFull frequency table:")
    for w, c in ranked:
        print(f"  {w:<15} {c}")
    show_unique(r)


def show_unique(r):
    uniq = sorted(r["unique"])
    print(f"Unique words: {len(uniq)} ({', '.join(uniq)})")


# ----------------------------------------------------------------- main ----
def get_text():
    """Ask where the text comes from; return text or None on error."""
    print("\nInput source:  1. Type text   2. Read from file")
    choice = input("Choose 1 or 2: ").strip()

    if choice == "1":
        text = read_text_from_user()
    elif choice == "2":
        text, error = read_text_from_file()
        if error:
            print(error)
            return None
    else:
        print("Invalid choice.")
        return None

    if not text:
        print("No text to analyse.")
        return None
    return text


def main():
    print("=== Word Counter & Text Analyzer ===")
    result = None

    while True:
        print("\nMenu:")
        print("  1. Analyse new text (summary)")
        print("  2. Word frequency")
        print("  3. Unique words")
        print("  4. Exit")
        option = input("Choose an option: ").strip()

        if option == "1":
            text = get_text()
            if text:
                result = analyse(text)
                show_summary(result)
        elif option in ("2", "3"):
            if result is None:
                text = get_text()          # allow going straight to option 2/3
                if text is None:
                    continue
                result = analyse(text)
            if option == "2":
                show_frequency(result)
            else:
                show_unique(result)
        elif option == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please choose 1-4.")


if __name__ == "__main__":
    main()
