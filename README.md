# NLP Text Analyzer 📊

A basic Natural Language Processing (NLP) tool developed in Python to perform comprehensive textual analysis on given documents. The program processes text corpora to extract grammatical statistics, token frequencies, and character-level data, outputting the results in a strictly aligned format.

## 📝 Project Overview

This project focuses on providing computers with the ability to process data encoded in natural language using rule-based and statistical approaches. It reads an input text file, processes the content, and writes the calculated statistics to an output file. 

### Key Statistics Calculated:
- **Tokenization & Word Count:** Parses the text into words by removing punctuations and splitting by white-spaces.
- **Sentence Count:** Identifies sentences based on specific end-of-sentence characters (`.`, `!`, `?`, `...`).
- **Averages:** Calculates the average number of words per sentence.
- **Character Metrics:** Counts total characters (including/excluding white-spaces and punctuations).
- **Frequency Analysis:** Identifies the shortest and longest words, along with the specific frequencies of all words used in the text (sorted in descending order with alphabetical tie-breakers).

## 🚀 Features

- **Custom Text Parsing:** Built from scratch without heavy external NLP libraries.
- **Strict Formatting:** Outputs data with precise spacing (e.g., `{:24}` alignment) and decimal limits (e.g., `:.4f` for frequencies).
- **Case-Insensitive Processing:** Converts all text to lowercase using the `en_US` locale to ensure accurate frequency counting regardless of original casing.

## 🛠️ Installation & Usage

1. **Clone the repository:**

```bash
git clone [https://github.com/Afra-Topcu/nlp-text-analyzer.git](https://github.com/Afra-Topcu/nlp-text-analyzer.git)
```

2. **Run the script:**
The script is designed to run on Python 3.9.18 and requires both an input and an output file path as command-line arguments:

```bash
python text_analyzer.py input.txt output.txt
```

## 📊 Example Output

The generated `output.txt` will follow this exact structure:

```text
Statistics about input.txt :
#Words                  : 509
#Sentences              : 21
#Words/#Sentences       : 24.24
#Characters             : 3011
#Characters (Just Words): 2411
The Shortest Word       : a                        (0.0177)
The Longest Word        : bacteria-elimination     (0.0020)
Words and Frequencies   :
the                     : 0.0963
and                     : 0.0452
of                      : 0.0432
```

---

*Developed as a Computer Engineering student at Hacettepe University.*