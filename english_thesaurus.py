import json
import pandas as pd
import textwrap

with open("data.json", "r", encoding="utf-8") as f:
    data = json.load(f)

def word_input():
    word = input("Please enter a word to search for: ")
    return word

def word_search(word):
    meanings = []
    
    # Try different cases
    if word in data:
        meanings.extend(data[word])
    if word.lower() in data and word.lower() != word:
        meanings.extend(data[word.lower()])
    if word.title() in data and word.title() != word:
        meanings.extend(data[word.title()])
    
    if meanings:
        result = f"\n{word} meanings are:\n"
        for idx, m in enumerate(meanings, 1):
            wrapped = "\n".join(textwrap.fill(line, width=80) for line in m.splitlines())
            result += f"\n{idx}.\n{wrapped}\n"
        return result
    else:
        return f"Sorry, '{word}' was not found in the dictionary."
    
search_word = word_input()
print(word_search(search_word))