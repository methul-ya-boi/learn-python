questionlist = ["where is astreroid belt? ","what is the largest planet? ", "How long does it take for light to reach Earth from the Sun? ", "how long does the moon take to orbit earth? ", "what is the largest moon in our solar system? ", "What is the smallest planet? ", "What is the name of the planet that was once part of the solar system? ", "What planet has a ring? ", "What planet spins the opposite way? ", "What is the name of the storm on jupiter? "]
answerlist = ["between Mars and Jupiter", "Jupiter", "8 minutes", "27 days", "Ganymede", "Mercury", "Pluto", "Saturn", "Venus", "The Great Red Spot"]
points = 0
print("please use capitals only for names")
print("")
question = -1
answer = -1

for questions in range(10):
    question = question + 1
    questionindex = questionlist[question]
    userinput = input(questionindex)
    answer = answer + 1
    answerindex = answerlist[answer]
    if userinput == answerindex:
        print("correct")
        points = points + 1
    else:
        print("incorrect")
strpoints = str(points)
print("you got "+strpoints+" points!")