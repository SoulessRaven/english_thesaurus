# 📖 English Thesaurus

A lightweight, easy-to-use command-line English thesaurus built with Python.

This application allows you to search for words and retrieve multiple definitions, cleanly formatted for easy reading.  
It supports case-insensitive search and multi-meaning words, with a simple loop to allow repeated lookups.

---

## 🚀 Features

- 📚 **Multiple definitions per word** (structured from a JSON dictionary).
- 🔍 **Case-insensitive search** (handles "cat", "Cat", "CAT", etc.).
- 📜 **Clean text formatting** with word wrapping (easy to read in the terminal).
- 🚱 **UTF-8 safe** (handles international characters correctly).
- 🔁 **Continuous search loop** until you type `exit`.

---

## 🛠 Requirements

- Python 3.7+ (standard library only — no external packages required).

---

## 💻 How to Run

### Clone the repository:

```bash
git clone https://github.com/SoulessRaven/english_thesaurus.git
cd english_thesaurus
```

### Run the app:

```bash
python english_thesaurus.py
```

### Search for words!

- Enter a word (e.g., `cat`, `dog`, `book`).
- The app will print all available meanings.
- Type `exit` to close the app.

---

## 📂 Project Structure

```
english_thesaurus/
├── data.json              # Dictionary data (word: [definitions])
├── english_thesaurus.py   # Main program file
└── README.md              # Project documentation (this file)
```

---

## 📋 Notes

- All words and definitions are sourced from a custom `data.json` file.
- You can extend or modify `data.json` to add new words or update meanings easily.
- If both `"cat"` and `"Cat"` exist in the data, the app intelligently merges them during search.

---

## 📜 Example Usage

```text
Please enter a word to search for (or type 'exit' to quit): cat

cat meanings are:

1.
The word "cat" refers to a small domesticated carnivorous mammal...

2.
The word 'cat' refers to a small domesticated mammal belonging to the species *Felis catus*...

3.
A "cat" is a small, typically agile domesticated mammal of the species Felis catus...

...etc.

Please enter a word to search for (or type 'exit' to quit): exit
Goodbye! 👋
```

---

## 🧑‍💻 Future Improvements

- Fuzzy matching for typos (e.g., suggesting "cat" if user types "cta").
- A simple graphical user interface (GUI) version using Tkinter.
- Ability to add new words through the app itself.

---

# 🎯

Thanks for checking out **English Thesaurus**!  
Feel free to fork the repo, suggest improvements, or use it as a foundation for your own dictionary apps.

