from data import question_data
from question_model import Question
import quiz_brain

for key, value in enumerate(question_data):
    text = value["text"]
    answer = value["answer"]
    print(text)
    questionBank =+ Question(text, answer)