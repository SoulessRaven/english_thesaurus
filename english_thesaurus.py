import json
import textwrap
import threading

from difflib import get_close_matches as gcmatcher

class InputTimeoutException(Exception):
    pass

with open("data.json", "r", encoding="utf-8") as f:
    data = json.load(f)

# function to collect a user input with a timeout feature
def timeout_input(prompt, timeout=60):
    user_input = [None]
    
    def ask():
        user_input[0] = input(prompt).strip()
    
    thread = threading.Thread(target=ask)
    thread.start()
    thread.join(timeout)

    if thread.is_alive():
        raise InputTimeoutException
    else:
        return user_input[0]

# function that takes user input compares to it to a list of dict.keys and returns 3 most likely.
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

# function to search for the word (dict.key) in the dict and return all values
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
        try:
            search_word = timeout_input("Please enter a word to search for (or type '/exit' to quit): ", timeout=60)
            if search_word == "/exit":
                print("Goodbye!")
                break
        except InputTimeoutException:
            print("\nNo input detected. Exiting due to inactivity.")
            break

        search_word = fuzzy_word(search_word)
        print(word_search(search_word))