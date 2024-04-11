from time import sleep

import os
# Clearing the Screen

print ("      ~ WHO AM I? ~         ")
sleep(1)
print ("(Bible Character Quiz Game) \n")

sleep(2) 
playing = input("Do you want to start guessing who's who in the Bible?\nType 'yes' to proceed: ")
if playing.lower() != "yes":
   quit()
sleep(1)
os.system('cls')

#-----------------NAME INPUT--------------------
name = input("\nPlease type your name: ")
sleep(1)  
os.system('cls')

print("\nGet ready with your Bible knowledge! \n")
sleep(2)
os.system('cls')

print("Welcome to EASY level " + name + ".""\n 10 questions :)\n")
sleep(1) 
print(name + ", you have to guess 8 or more characters to proceed to the INTERMEDIATE LEVEL")
playing = input("Type 'ok' if you understand: ")
if playing.lower() != "ok":
    quit()
os.system('cls')

'''
------------------------------EASY LEVEL Q&A------------------------------
-------------------------------10 QUESTIONS-------------------------------
'''
sleep(1)
score1 = 0
#1
answer = input("\nWho's the first man that God created? ")
if answer.lower() == "adam":
  print ("Correct!")
  score1 += 1  
else:
  print("The correct answer is 'Adam'")
  sleep(2)
os.system('cls')
#2  
answer = input("\nWho did God ask to make an ark? ")
if answer.lower() == "noah":
  print ("Correct!")
  score1 += 1  
else:
  print("The correct answer is 'Noah'")
  sleep(2)
os.system('cls')
#3  
answer = input("\nWho's known as the 'Father of Many Nations'? ")
if answer.lower() == "abraham":
  print ("Correct!")
  score1 += 1  
else:
  print("The correct answer is 'Abraham'")
  sleep(2)
os.system('cls')
#4  
answer = input("\nWho did God use to part the Red sea? ")
if answer.lower() == "moses":
  print ("Correct!")
  score1 += 1  
else:
  print("The correct answer is 'Moses'")
  sleep(2)
os.system('cls')
#5  
answer = input("\nWho got swallowed by a whale and stayed at it's belly for 3 days? ")
if answer.lower() == "jonah":
  print ("Correct!")
  score1 += 1  
else:
  print("The correct answer is 'Jonah'") 
  sleep(2)
os.system('cls')
#6  
answer = input("\nWho did God send to bring salvation to earth? ")
if answer.lower() == "jesus":
  print ("Correct!")
  score1 += 1  
else:
  print("The correct answer is 'Jesus'") 
  sleep(2)
os.system('cls')
#7  
answer = input("\nWho in the 12 apostles betrayed Jesus? ")
if answer.lower() == "judah":
  print ("Correct!")
  score1 += 1  
else:
  print("The correct answer is 'Judah'")  
  sleep(2)
os.system('cls')
#8  
answer = input("\nWho's the father of 12 tribes? ")
if answer.lower() == "israel":
  print ("Correct!")
  score1 += 1  
else:
  print("The correct answer is 'Israel'")  
  sleep(2)
os.system('cls')
#9    
answer = input("\nWho defeated a giant named 'Goliath'? ")
if answer.lower() == "david":
  print ("Correct!")
  score1 += 1  
else:
  print("The correct answer is 'David'")
  sleep(2)
os.system('cls')
#10  
answer = input("\nWho did God gifted with wisdom and wealth which later on had 700 wives and 300 concubines? ")
if answer.lower() == "solomon":
  print ("Correct!")
  score1 += 1  
else:
  print("The correct answer is 'Solomon'")
  sleep(2)
os.system('cls')

#---------------------------EASY LEVEL SCORE--------------------------------
sleep(1)
print("\n"+ name + ", you've guessed " + str(score1) + " correct characters out of 10.")
sleep(2)
if (score1) >= 8:
  os.system('cls')
  print ("\nWelcome to INTERMEDIATE level " + name + ".""\n 15 questions ;)\n") 
  sleep(1)
else:
  print ("Don't forget to read the Bible!")
  sleep(2)
  quit()
os.system('cls')

print(name + ", you have to guess 12 or more characters to proceed to the ADVANCED LEVEL")
playing = input("Type 'ok' if you understand: ")
if playing.lower() != "ok":
    quit()
os.system('cls')

'''
---------------------------INTERMEDIATE LEVEL Q&A---------------------------
-------------------------------15 QUESTIONS---------------------------------
'''
score2 = 0
sleep(1)

#1
answer = input("\nWho's the first king of Israel? ")
if answer.lower() == "saul":
  print ("Correct!")
  score2 += 1  
else:
  print("The correct answer is 'Saul'")
  sleep(2)
os.system('cls')
#2  
answer = input("\nWho was thrown into the lion's den? ")
if answer.lower() == "daniel":
  print ("Correct!")
  score2 += 1  
else:
  print("The correct answer is 'Daniel'")
  sleep(2)
os.system('cls')
#3
answer = input("\nWho pretended to be his brother and stole his brother's inheritance right? ")
if answer.lower() == "jacob":
  print ("Correct!")
  score2 += 1  
else:
  print("The correct answer is 'Jacob'")
  sleep(2)
os.system('cls')
#4
answer = input("\nWho is Moses' brother which assisted him in leading Isrealites? ")
if answer.lower() == "aaron":
  print ("Correct!")
  score2 += 1  
else:
  print("The correct answer is 'Aaron'") 
  sleep(2)
os.system('cls')
#5   
answer = input("\nWho protected the two spies sent by Joshua to Jericho? ")
if answer.lower() == "rahab":
  print ("Correct!")
  score2 += 1  
else:
  print("The correct answer is 'Rahab'")
  sleep(2)
os.system('cls')
#6   
answer = input("\nWho is the prophet of God that was fed by ravens? ")
if answer.lower() == "elijah":
  print ("Correct!")
  score2 += 1  
else:
  print("The correct answer is 'Elijah'")   
  sleep(2)
os.system('cls')
#7
answer = input("\nWho led the Israelites into Canaan and conquered Jericho? ")
if answer.lower() == "joshua":
  print ("Correct!")
  score2 += 1  
else:
  print("The correct answer is 'Joshua'")
  sleep(2)
os.system('cls')
#8
answer = input("\nWho led the 300 warriors? ")
if answer.lower() == "gideon":
  print ("Correct!")
  score2 += 1  
else:
  print("The correct answer is 'Gideon'")
  sleep(2)
os.system('cls')
#9
answer = input("\nWho was sold as a slave by his brothers who later on became the interpretator of the dreams of the pharoh of Egypt? ")
if answer.lower() == "joseph":
  print ("Correct!")
  score2 += 1  
else:
  print("The correct answer is 'Joseph'")
  sleep(2)
os.system('cls')
#10
answer = input("\nWho had a great strength which comes from his long hair? ")
if answer.lower() == "samson":
  print ("Correct!")
  score2 += 1  
else:
  print("The correct answer is 'Samson'")
  sleep(2)
os.system('cls')
#11
answer = input("\nWho is the prophet that anoints both Saul and David as king? ")
if answer.lower() == "samuel":
  print ("Correct!")
  score2 += 1  
else:
  print("The correct answer is 'Samuel'")
  sleep(2)
os.system('cls')
#12
answer = input("\nWho is a shepard that murdered his younger brother out of jealousy? ")
if answer.lower() == "cain":
  print ("Correct!")
  score2 += 1  
else:
  print("The correct answer is 'Cain'")
  sleep(2)
os.system('cls')
#13
answer = input("\nWho is the Philistine beauty that deceived Samson to reveal the source of his strength? ")
if answer.lower() == "delilah":
  print ("Correct!")
  score2 += 1  
else:
  print("The correct answer is 'Delilah'")
  sleep(2)
os.system('cls')
#14
answer = input("\nWho traded his birthright to his younger brother for some soup? ")
if answer.lower() == "esau":
  print ("Correct!")
  score2 += 1  
else:
  print("The correct answer is 'Esau'")
  sleep(2)
os.system('cls')
#15 
answer = input("\nWho got pregnant at the late age of 99 years old? ")
if answer.lower() == "sarah":
  print ("Correct!")
  score2 += 1  
else:
  print("The correct answer is 'Sarah'")
  sleep(2)
os.system('cls')

#-----------------------INTERMEDIATE LEVEL SCORE----------------------------------
sleep(1)
print("\n"+name+", you've guessed " + str(score2) + " correct characters out of 15")
sleep(2)
if (score2) >= 12:
  print("\nWelcome to ADVANCED level "+ name + ".""\n 20 questions 0_0)") 
  sleep(1)
else:
  print("Don't forget to read the Bible!") 
  sleep(2)
  quit()

print("\nThis will be the final round.\nContinue to showcase your knowledge in Bible.")
playing = input("Type 'ok' if you understand: ")
if playing.lower() != "ok":
    quit()
os.system('cls')

'''
-------------------------ADVANCED LEVEL Q&A------------------------------
---------------------------20 QUESTIONS----------------------------------
'''

score3 = 0
sleep(1)

#1
answer = input("\nWho was originally married to Uriah but charmed David while she was taking a bath? ")
if answer.lower() == "bathsheba":
  print ("Correct!")
  score3 += 1  
else:
  print("The correct answer is 'Bathsheba'")
  sleep(2)
os.system('cls')
#2  
answer = input("\nWho was was intoxicated by his two daughters for him to impregnate them? ")
if answer.lower() == "lot":
  print ("Correct!")
  score3 += 1  
else:
  print("The correct answer is 'Lot'")
  sleep(2)
os.system('cls')
#3
answer = input("\nWho became the new queen of Persia and saved her nation from being exiled? ")
if answer.lower() == "esther":
  print ("Correct!")
  score3 += 1  
else:
  print("The correct answer is 'Esther'")
  sleep(2)
os.system('cls')
#4
answer = input("\n(answer format: ____ & ____)\nWho are the daughters of Laban that got married to Jacob? ")
if answer.lower() == "leah & rachel":
  print ("Correct!")
  score3 += 1
elif answer.lower() == "rachel & leah":  
  print ("Correct!")
  score3 += 1
else:
  print("The correct answer is 'Rachel & Leah'") 
  sleep(2)
os.system('cls')
#5   
answer = input("\nWho was a prophetess and also the only female judge? ")
if answer.lower() == "deborah":
  print ("Correct!")
  score3 += 1  
else:
  print("The correct answer is 'Deborah'")
  sleep(2)
os.system('cls')
#6   
answer = input("\nWho is the daughter-in-law of Naomi that got married to Boaz? ")
if answer.lower() == "ruth":
  print ("Correct!")
  score3 += 1  
else:
  print("The correct answer is 'Ruth'")   
  sleep(2)
os.system('cls')
#7
answer = input("\nWho is the only daughter of Jacob that was raped by Shechem? ")
if answer.lower() == "dina":
  print ("Correct!")
  score3 += 1  
else:
  print("The correct answer is 'Dina'")
  sleep(2)
os.system('cls')
#8
answer = input("\nWho's the 12th son of Jacob that was framed by Joseph as a robber? ")
if answer.lower() == "benjamin":
  print ("Correct!")
  score3 += 1  
else:
  print("The correct answer is 'Benjamin'")
  sleep(2)
os.system('cls')
#9
answer = input("\nWho's known as the 'weeping prophet'? ")
if answer.lower() == "jeremiah":
  print ("Correct!")
  score3 += 1  
else:
  print("The correct answer is 'Jeremiah'")
  sleep(2)
os.system('cls')
#10
answer = input("\nWho got accused to be drunk as she was praying and weeping to God by a priest in the temple? ")
if answer.lower() == "hannah":
  print ("Correct!")
  score3 += 1  
else:
  print("The correct answer is 'Hannah'")
  sleep(2)
os.system('cls')
#11
answer = input("\nWho lives the longest years? ")
if answer.lower() == "methuselah":
  print ("Correct!")
  score3 += 1  
else:
  print("The correct answer is 'Methuselah'")
  sleep(2)
os.system('cls')
#12
answer = input("\nWho fell to the ground from the third story window as he was sinking into a deep sleep while Paul was talking? ")
if answer.lower() == "eutychus":
  print ("Correct!")
  score3 += 1  
else:
  print("The correct answer is 'Eutychus'")
  sleep(2)
os.system('cls')
#13
answer = input("\nWho is the priest and judge that took supervision over samuel? ")
if answer.lower() == "eli":
  print ("Correct!")
  score3 += 1  
else:
  print("The correct answer is 'Eli'")
  sleep(2)
os.system('cls')
#14
answer = input("\nWho received the double portion power of Elijah? ")
if answer.lower() == "elisha":
  print ("Correct!")
  score3 += 1  
else:
  print("The correct answer is 'Elisha'")
  sleep(2)
os.system('cls')
#15 
answer = input("\nWho would not die before he had seen the Lord Messiah as revealed to him by the Holy Spirit? ")
if answer.lower() == "simeon":
  print ("Correct!")
  score3 += 1  
else:
  print("The correct answer is 'Simeon'")
  sleep(2)
os.system('cls')
#16
answer = input("\nWho prepared a special gallows to be used for the excution of Mordecai, but later on was hanged by that same gallows? ")
if answer.lower() == "haman":
  print ("Correct!")
  score3 += 1  
else:
  print("The correct answer is 'Haman'")
  sleep(2)
os.system('cls')
#17
answer = input("\nWho's the high priest at the time of trial and crucifixion of Jesus Christ? ")
if answer.lower() == "caiaphas":
  print ("Correct!")
  score3 += 1  
else:
  print("The correct answer is 'Caiaphas'")
  sleep(2)
os.system('cls')
#18
answer = input("\nWho got a vision from God and sent two servants and a soldier to bring Peter to him? ")
if answer.lower() == "cornelius":
  print ("Correct!")
  score3 += 1  
else:
  print("The correct answer is 'Cornelius'")
  sleep(2)
os.system('cls')
#19
answer = input("\nWho despised David in her heart when she saw him leaping and dancing before the Lord? ")
if answer.lower() == "michal":
  print ("Correct!")
  score3 += 1  
else:
  print("The correct answer is 'Michal'")
  sleep(2)
os.system('cls')
#20
answer = input("\n(answer format: ____ & ____)\nWho are the two couple who lied to Peter about the money of their sold field that fell down and died? ")
if answer.lower() == "ananias & sapphira":
  print ("Correct!")
  score3 += 1  
elif answer.lower() == "sapphira & ananias":
  print ("Correct!")
  score3 += 1  
else:
  print("The correct answer is 'Ananias & Sapphira'")
  sleep(2)
os.system('cls')

#---------------------------ADVANCED LEVEL SCORE------------------------------
sleep(1)
print("\n" + name + ", you've guessed " + str(score3) + " correct characters out of 20.")
fscore = score1 + score2 + score3
print("Total guesses of "+ name + " is " + str(fscore) + " out of 45 questions.\n")
sleep(3)
if (score3) >= 18:
  print ("Continue to read the Bible and learn more.")
  sleep(2)
else:
  print ("Don't forget to read the Bible!")
  sleep(2)
  quit()
