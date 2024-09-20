score = 0
print("Time for a quiz game!")

print("Question 1: Which of these planets has no Rings?")
print("a) Uranus")
print("b) Neptune")
print("c) Saturn ")
print("d) Jupiter")
answer1 = input("Enter your answer: ")
if answer1.lower() == "neptune":
    score = score + 1

print("Question 2: What year was the moon landing?")
print("a) 1969")
print("b) 1978")
print("c) 1946")
print("d) 1999")
answer2 = input("Enter your answer: ")
if answer2.lower() == "1969":
    score = score + 1

print("Question 3: What element(s) are diamonds made of? ")
print("a) carbon")
print("b) diamond")
print("c) chromium + silver")
print("d) platinum + oxygen")
answer3 = input("Enter your answer: ")
if answer3.lower() == "carbon":
    score = score + 1 

print("Question 3: What fameous structure is visible from space")
print("a) The Great Wall Of China")
print("b) The Burj Khalifa ")
print("c) The Coloseum")
print("d) The Pyramids of Giza")
answer4 = input("Enter your answer: ")
if answer4.lower() == "the great wall of china":
    score = score + 1 


#Calculating score
print("You got " + str(score) + "/5 questions right")
percent = score/5
final = percent * 100
print("You got a " + str(final) + "%")



