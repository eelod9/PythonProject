class QuizBrain:
    def __init__(self,question_list):
        self.questNum = 0
        self.questList = question_list
        self.score = 0
    
    def still_has_questions(self):
        return self.questNum < len(self.questList)
        

    def next_quesiton(self):
        current_question = self.questList[self.questNum]
        self.questNum += 1 
        user_answer = input(f"Q.{self.questNum}: {current_question.text} (True or False):")
        self.check_answer(user_answer, current_question.answer)
    
    def check_answer(self, user_answer, correct_answer):
        if(user_answer.lower() == correct_answer.lower()):
            self.score += 1
            print(f"correct! current score: {self.score}")
        else:
            print(f"Incorrect current score: {self.score} ")
    