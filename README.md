# Word Counter & Text Analyzer

| | |
|---|---|
| **Student** | Rupesh Kumar Sidar |
| **ERP No.** | RU 01065 |
| **College** | Rungta International Skills University |
| **Language** | Python 3 |
| **Concepts** | Strings, Dictionaries, Sets, Frequency Analysis |

## 1. Project Overview

Word Counter & Text Analyzer is a console-based Python 3 program. It analyses a piece of text, typed by the user or read from a text file, and reports the number of words, characters and sentences, the frequency of each word, and the list of unique words.

**Rule used:** counting is case-insensitive, and punctuation is removed before counting words.

## 2. Objectives

- Read text from the user or from a file.
- Clean the text using string methods (`lower`, `split`, `strip`, `replace`).
- Count word frequency using a **dictionary**.
- Find unique words using a **set**.
- Show results sorted by frequency.
- Handle invalid input (empty text, missing file, wrong menu choice) with clear messages.

## 3. Features

- Input from the keyboard or from a `.txt` file
- Word count, character count (with spaces) and sentence count
- Word frequency table, sorted by count (high to low), then alphabetically
- Unique words list (set), sorted alphabetically
- Menu-driven program that can be used repeatedly until Exit
- Friendly error messages for invalid input

## 4. Requirements

- Python 3.x (no external libraries needed; only the built-in `string` module is used)
- Any terminal: VS Code terminal, Command Prompt, PowerShell or Linux/macOS shell

## 5. How to Run

1. Keep `one.py` (and `sample.txt` if you want to test file input) in the same folder.
2. Open a terminal in that folder and run:

```bash
python one.py
```

## 6. Input / Output Details

**Menu**

```
1. Analyse new text (summary)
2. Word frequency
3. Unique words
4. Exit
```

**Input**

| Step | Input |
|---|---|
| Menu | Option number `1` to `4` |
| Input source | `1` = type text, `2` = read from a file |
| Text | Any text (words, numbers, punctuation) |
| File name | Name of a `.txt` file in the same folder, for example `sample.txt` |

**Output**

| Option | Output |
|---|---|
| 1 | `Words: n \| Characters (with spaces): n \| Sentences: n \| Unique words: n` |
| 2 | `Top words: word: count \| ...`, a full frequency table, and the unique words |
| 3 | `Unique words: n (word1, word2, ...)` |

**Error messages**

| Situation | Message |
|---|---|
| Empty text | `No text to analyse.` |
| File does not exist | `File 'notes.txt' not found.` |
| Wrong source or menu choice | `Invalid choice.` / `Invalid option. Please choose 1-4.` |

## 7. Logic

1. **Clean:** `lower()` makes the text lower case, `replace()` removes apostrophes and turns other punctuation into spaces, and `split()` gives the list of words.
2. **Sentences:** `!` and `?` are replaced by `.`, the text is split on `.`, and non-empty parts are counted.
3. **Frequency:** a dictionary stores `{word: count}`.
4. **Unique words:** a `set` of the cleaned words.
5. **Sorting:** `sorted()` with the key `(-count, word)`.

## 8. Test Cases (all pass)

| # | Input | Output |
|---|---|---|
| 1 | `Python is easy. Python is fun.` | Words: 6 \| Characters (with spaces): 30 \| Sentences: 2 |
| 2 | `Hello` | Words: 1 \| Characters: 5 \| Sentences: 1 \| Unique words: 1 |
| 3a | *(empty text)* | No text to analyse. |
| 3b | File `notes.txt` (does not exist) | File 'notes.txt' not found. |
| 4 | `The cat saw the dog. The dog ran.` with option 2 | Top words: the: 3 \| dog: 2 \| ... Unique words: 5 (cat, dog, ran, saw, the) |
| 5 | File `sample.txt` | Words: 19 \| Characters (with spaces): 99 \| Sentences: 5 \| Unique words: 12 |

Screenshots of the input and output of every test case are in `Test_Case_Screenshots.pdf`.

## 9. Project Structure

```
.
├── one.py                       # complete project code (single file)
├── README.md                    # project documentation
├── sample.txt                   # supporting file for file-input testing
├── Test_Case_Screenshots.pdf    # input/output screenshots of every test case
└── Python_Report.pdf            # project report
```

## 10. Author

**Rupesh Kumar Sidar** | ERP RU 01065
Rungta International Skills University
