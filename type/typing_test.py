import time
import random

def get_words():
    # Add a list of words to be used in the typing test
    words = ["python", "programming", "challenge", "speed", "typing", "test", "practice", "keyboard"]
    return words

def calculate_wpm(start_time, end_time, typed_words):
    total_time = end_time - start_time
    words_per_minute = (len(typed_words) / total_time) * 60
    return words_per_minute

def main():
    words = get_words()
    random.shuffle(words)
    
    print("Welcome to the Speed Typing Test!")
    print("Type the following words:")
    
    for word in words:
        print(word)
        input("Press Enter to continue...")
        start_time = time.time()
        typed_word = input("Type the word: ")
        end_time = time.time()
        
        if typed_word == word:
            print("Correct!")
        else:
            print("Incorrect!")
        
        wpm = calculate_wpm(start_time, end_time, typed_word)
        print(f"Words per minute: {wpm:.2f}\n")
    
    print("Test completed!")

if __name__ == "__main__":
    main()
