import json
import random
import sys

GREEN = "\033[92m" 
RED = "\033[91m"    
RESET = "\033[0m"   

def load_vocab(file_path):
    """Load vocabulary from a JSON file."""
    with open(file_path, 'r', encoding='utf-8') as f:
        return json.load(f)

def save_scores(vocab_data, file_path):
    """Save updated vocabulary data back to the JSON file."""
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(vocab_data, f, ensure_ascii=False, indent=4)

def update_score(word, correct):
    if correct:
        word['score'] += 1  
    else:
        word['score'] = max(0, word['score'] - 1)  

def quiz_word(word, vocab_data, file_path):
    """Prompt the user to answer a word and update the score."""
    print("\n")  
    print(word['czech'])  
    user_answer = input()  

        
    if user_answer.strip().lower() == 'exit':
        print("Exiting the quiz.")
        return False 

    correct = user_answer.strip().lower() == word['german'].strip().lower()
    update_score(word, correct)
    
    if correct:
        print(f"{GREEN}Correct!{RESET}")
    else:
        print(f"{RED}Incorrect!{RESET}")
        print({word['german']})
    

    save_scores(vocab_data, file_path)
    
    return True  

def quiz_lesson(vocab_data, lesson_id, page_id, file_path):
    """Conduct a quiz for all words on a specified page of a lesson."""
    words = vocab_data[lesson_id][page_id]
    random.shuffle(words)  
    for word in words:
        if not quiz_word(word, vocab_data, file_path):  
            break

def quiz_specific_page(vocab_data, lesson_id, page_id, file_path):
    """Quiz for a specific lesson and page."""
    if lesson_id in vocab_data and page_id in vocab_data[lesson_id]:
        quiz_lesson(vocab_data, lesson_id, page_id, file_path)
    else:
        print(f"No vocabulary found for lesson {lesson_id} on page {page_id}.")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: run.py <vocab.json> <lesson_id> [page_id]")
        sys.exit(1)

    vocab_file = sys.argv[1]
    lesson_id = sys.argv[2]
    page_id = sys.argv[3] if len(sys.argv) > 3 else None

    vocab_data = load_vocab(vocab_file)

    if page_id:
        quiz_specific_page(vocab_data, lesson_id, page_id, vocab_file)
    else:
        for page in vocab_data[lesson_id]:
            quiz_lesson(vocab_data, lesson_id, page, vocab_file)