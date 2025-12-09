import gensim.downloader as api
import random
import spacy

print("Loading Glove model... (this might take a minute)")
model = api.load("glove-wiki-gigaword-100")

nlp = spacy.load("en_core_web_sm")

def is_valid_noun(word):
    if len(word) < 4 or not word.isalpha():
        return False
    
    doc = nlp(word)
    return doc[0].pos_ in ["NOUN", "PROPN"]

def get_game_round():
    vocab_keys = list(model.key_to_index.keys())
    
    basis_word = ""
    while True:
        candidate = random.choice(vocab_keys)
        if is_valid_noun(candidate):
            basis_word = candidate
            break
            
    similar_entries = model.most_similar(basis_word, topn=3)
    game_words = [word for word, score in similar_entries]
    
    intruder = ""
    while True:
        candidate = random.choice(vocab_keys)
        
        if model.similarity(basis_word, candidate) < 0.1:
            
            test_list = game_words + [candidate]
            if model.doesnt_match(test_list) == candidate:
                intruder = candidate
                break
    
    game_words.append(intruder)
    
    random.shuffle(game_words)
    
    return basis_word, game_words, intruder

def play_game():
    print("\n--- 4-Word-Game (Odd One Out) ---")
    print("Generating a new puzzle...")
    
    basis_word, options, correct_intruder = get_game_round()
    
    print(f"\nWords: {options}")
    print("(Type the word that does not belong)")
    
    user_guess = input("Your choice: ").strip().lower()
    
    if user_guess == correct_intruder:
        print(f"\nCorrect! '{correct_intruder}' is the odd one out.")
    else:
        print(f"\nNot quite. The odd one out was '{correct_intruder}'.")
        print(f"(The hidden theme was based on: '{basis_word}')")

    print("\nSortierung nach Ähnlichkeit zum Basiswort:")
    
    scored_words = []
    for word in options:
        sim = model.similarity(basis_word, word)
        scored_words.append((word, sim))
        
    scored_words.sort(key=lambda x: x[1], reverse=True)
    
    for word, score in scored_words:
        print(f"{word} -> {score:.2f}")

if __name__ == "__main__":
    while True:
        play_game()
        again = input("\nPlay again? (y/n): ")
        if again.lower() != 'y':
            break
