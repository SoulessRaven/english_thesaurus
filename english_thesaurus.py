import json
import textwrap
from difflib import get_close_matches as gcmatcher

with open("data.json", "r", encoding="utf-8") as f:
    data = json.load(f)

def word_input():
    word = input("Please enter a word to search for (or type '/exit' to quit): ").strip()
    return word

def fuzzy_word(word):
    matches = gcmatcher(word, data.keys(), n=3, cutoff=0.7)
    if matches:
        print("\nDid you mean:")
        for idx, guess in enumerate(matches, 1):
            print(f"{idx}. {guess}")
        print("0. None of these")
        
        while True:
            try:
                choice = int(input("Enter the number of the correct word (0-3): "))
                if choice == 0:
                    return word
                elif 1 <= choice <= len(matches):
                    return matches[choice - 1]
                else:
                    print("Invalid choice. Please select a number between 0 and 3.")
            except ValueError:
                print("Please enter a valid number.")
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
    
if __name__ == "__main__":
    while True:
        search_word = word_input()
        if search_word == "/exit":
            print("Goodbye!")
            break
        search_word = fuzzy_word(search_word)
        print(word_search(search_word))