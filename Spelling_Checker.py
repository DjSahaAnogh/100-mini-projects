from spellchecker import SpellChecker
def spell_checker():
    word: str = input("Enter the text: ").strip().lower()
    spell = SpellChecker()
    if word in spell:
        print("The word is spelled correctly.")
    else:
        corretion = spell.correction(word)
        suggestions = spell.candidates(word)
        print(f"{word} is spelled incorrectly. Did you mean '{corretion}'?\nSuggestions: {suggestions}")
if __name__ == "__main__":
    spell_checker()