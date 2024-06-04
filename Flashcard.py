class question:
    def __init__(self, question, options, answer):
            self.question = question
            self.options= options
            self.answer= answer
      
    def flashcard(self):
        print(self.question)
        for idx, option in enumerate(self.options, 1):      #This allows for a better way of reading the question
            print(f"{idx}. {option}")
    
        while True:
            ans = input("What is the answer (1-3): ")
            if ans.isdigit() and 1 <= int(ans) <= 3:
                if self.options[int(ans)-1] == self.answer:
                    print("you are right")
                    break
                else:
                    print("you are wrong")
            else:
                print("invalid entry")
q1 = question("What is the capital of France?", ["Paris", "Berlin", "London"], "Paris")
q1.flashcard()

q2 = question("What is does CPU mean?", ["Central proccessing unit", "Central poverty unit", "Central process unti"], "Central proccessing unit")
q2.flashcard()