import json
from difflib import get_close_matches

def load_knowlege_base(filepath: str) -> dict:
    try:
        with open(filepath, 'r') as file:
            data: dict = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        data = {"questions": []}  # Initialize with an empty list if file doesn't exist or is empty/corrupted
    return data

def save_knowledge_base(filepath: str, data: dict):
    with open(filepath, 'w') as file:
        json.dump(data, file, indent=2)

def find_best_matches(user_question: str, questions: list[str]) -> str | None:
    matches: list = get_close_matches(user_question, questions, n=1, cutoff=0.6)
    return matches[0] if matches else None

def get_answer_for_question(question: str, knowledge_base: dict) -> str | None:
    for q in knowledge_base["questions"]:
        if q["question"] == question:
            return q["answer"]
    return None

def chatbot():
    knowledge_base_file = 'knowledge_base.json'
    knowledge_base: dict = load_knowlege_base(knowledge_base_file)

    while True:
        user_input: str = input('You: ')
        if user_input.lower() == 'quit':
            break

        best_match: str | None = find_best_matches(user_input, [q['question'] for q in knowledge_base["questions"]])

        if best_match:
            answer: str | None = get_answer_for_question(best_match, knowledge_base)
            if answer:
                print(f'Bot: {answer}')
            else:
                print('Bot: I don\'t know the answer. Can you teach me?')
                new_answer: str = input('Type the answer or "skip" to skip: ')
                if new_answer.strip().lower() != 'skip':
                    knowledge_base["questions"].append({"question": user_input, "answer": new_answer})
                    save_knowledge_base(knowledge_base_file, knowledge_base)
                    print("Bot: Thank you! I learned a new response!")
        else:
            print('Bot: I don\'t know the answer. Can you teach me?')
            new_answer: str = input('Type the answer or "skip" to skip: ')
            if new_answer.strip().lower() != 'skip':
                knowledge_base["questions"].append({"question": user_input, "answer": new_answer})
                save_knowledge_base(knowledge_base_file, knowledge_base)
                print("Bot: Thank you! I learned a new response!")

if __name__ == '__main__':
    chatbot()
