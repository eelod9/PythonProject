from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

questionBank = []

for key, value in enumerate(question_data):
    text = value["question"]
    answer = value["correct_answer"]
    
    new_question = Question(text, answer)
    questionBank.append(new_question)

print(questionBank[0].text)

    
new_quizBrain = QuizBrain(questionBank)

while(new_quizBrain.still_has_questions()):
    new_quizBrain.next_quesiton()

print(f"Your final score was: {new_quizBrain.score}/{len(new_quizBrain.questList)}")

