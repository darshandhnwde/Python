# Classes and Object

class Student:

    def __init__(self,name,major,gpa,is_detention) -> None:
        self.name = name
        self.major = major
        self.gpa = gpa
        self.is_detention = is_detention

Student1 = Student("Darshan","AI",4,False)
print(Student1.name)
print(Student1.gpa)
print(Student1.major)
print(Student1.is_detention) 

#Building a Multiple Choice Quiz 

class Question :
    def __init__(self,prompt,answer) -> None:
        self.prompt = prompt
        self.answer = answer

question_prompts = [
    "what color are apple ?\n(a)Red&Green\n(b)orange \n(c)purple\n(d)white\n\n",
    "capital of Germany ?\n(a)moscow\n(b)berlin\n(c)lisban\n(d)rome\n\n",
    "the country has most population ?\n(a)usa\n(b)china\n(c)russia\n(d)india\n"
]
question = [
    Question(question_prompts[0], "a"),
    Question(question_prompts[1], "b"),
    Question(question_prompts[2], "d"),
]

def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print("You got " + str(score) + "/" + str(len(questions)) + " correct")

run_test(question) 

# Object Function

class Person :
    def __init__(self ,name ,gender,age) -> None:
        self.name = name
        self.gender = gender
        self.age = age

    def eligible_for_vote(self):
        if self.age >= 18:
            return True
        else:
            return False

person1 = Person("Akash KDM","Male",20)
person2 = Person("Kelly DL","Female",17)

print(person1.eligible_for_vote())
print(person2.eligible_for_vote())

