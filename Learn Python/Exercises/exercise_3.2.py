#us is a short form of user score. Its the score that the user enters. 
us = float(input("Enter your score here: "))
if us < 0.0:
    print("error")
elif us > 1.0:
    print("error")
elif 0.9 <= us < 1.0:
    print("A")
elif 0.8 <= us < 0.9:
    print("B")
elif 0.7 <= us < 0.8:
    print("C")
elif 0.6 <= us < 0.7:
    print("D")
elif 0.5 <= us < 0.6:
    print("E")