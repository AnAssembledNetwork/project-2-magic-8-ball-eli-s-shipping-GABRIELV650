from random import randrange
  
def fortune(name, Question):
  answers=("Yes - definitely.", "it is decidely so.", "without a doubt.","Reply hazy",       "try again.", "Ask again later.","Better not tell you now.","My sources say         no.","Outlook not so good!.")
  number=randrange(0,9)
  fortune1 = answers[number]
  # if number ==1:
  #   print("Yes-definitely")
  # elif number ==2:
  #   print("it is decidedly so")
  # elif number ==3:
  #   print("Without a doubt")
  # elif number ==4:
  #   print("Reply hazy, try again")
  # elif number ==5:
  #   print("Very doubtful")
  # elif number ==6:
  #   print("Ask again later")
  # elif number ==7:
  #   print("Better not to tell you now")
  # elif number ==8:
  #   print("My sources say no")
  # else:
  #   print("Outlook not so good")
  first_name=name.find("")
  first_name_index=name[0:first_name]
  return print(f"{name}´Question {Question}\n Magic") 
  print(f"8-Ball Answer : {fortune1} ")
def main():
  name1=input("What Is Your Full Name: ")
  Question_answered=input("What is Your Question You Would Like To Answer: ")
  fortune(name1, Question_answered)


 
         

  





if __name__ == "__main__":
  main()
