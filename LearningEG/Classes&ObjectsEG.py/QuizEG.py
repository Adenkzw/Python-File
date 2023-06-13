from QuestionFuncEG import Question
#The strings question_prompt
question_prompt = [
    "What colour are Apples?\n(a) Red\n(b) Purple\n(c) Orange\n\n",
    "What colour are Banana?\n(a) Blue\n(b) Yellow\n(c) Green\n\n",
    "What colour are Strawberries?\n(a) Yellow\n(b) Red\n(c) Blue\n\n"
]

questions = [
    Question(question_prompt[0], 'a'),#Objectify the strings with the QuestionFunc (Questions function)
    Question(question_prompt[1], 'b'),#(self, prompt, answer) = Question(prompt, answer)
    Question(question_prompt[2], 'b')
]

def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print('You got ' f'{score}' '/' + str(len(questions)) + ' Correct!')

run_test(questions)