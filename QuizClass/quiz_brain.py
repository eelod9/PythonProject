class QuizBrain:
    def __init__(self,question_list):
        self.questNum = 0
        self.questList = question_list

    def next_quesiton(self):
        current_question = self.questList[self.questNum]
        input(f"{current_question.text}")