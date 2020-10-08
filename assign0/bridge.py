f = open("answers.txt", "r")
lines = f.readlines()

question=0
for line in lines:
    print("KEEPER: Stop! Who would cross the Bridge of Death must answer me these questions three, 'ere the other "
          "side he see.")
    name = input("KEEPER: What is your name? ").strip()
    quest = input("KEEPER: What is your quest? ").strip()
    answer = input("KEEPER: What is "+lines[question].split('?')[0]+"?")
    question+=1
    if answer[-1] == '?':
        print("KEEPER: Auuuuuuuugh!")
        break
    elif answer.upper() in lines[question-1].split('?')[1].upper():
        print("KEEPER: Right. Off you go.")
    else:
        print(name.upper()+": Auuuuuuuugh!")



