from question_model import Question
from data import question_data

questionBank = []

for key, value in enumerate(question_data):
    text = value["text"]
    answer = value["answer"]
    print(text)
    new_question = Question(text, answer)
    questionBank.append(new_question)

print(questionBank)