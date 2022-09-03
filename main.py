import time, sys
def loading():
    print ("Loading...")
    for i in range(0, 100):
        time.sleep(0.1)
        sys.stdout.write(u"\u001b[1000D" + str(i + 1) + "%")
        sys.stdout.flush()
    print
    
loading()

print ("\n\n✧ Loading Complete...!")

blue = "\033[0;34m"
purple = "\033[0;35m"


score = 0
def correct():
  print("\n\033[0;33mGood job! you've earned a point.")
  global score
  score = score + 1
  print ("Points:", score)

def incorrect(): 
  print("\n\033[0;33mwrong unfortunately! better luck next time.")
  print("Points:", score)

def question(q, a):
  print(q)
  answer = input ("\n\033[0;34mAnswer: ")
  if answer == a:
    correct()
  else:
   incorrect()


question ("\n\n\033[0;34mWho in Stranger Things Said this 'Mornings are for coffee and contemplation.'?\n\033[0;35m(a). Jim Hopper\n(b). Eddie Munson\n(c). Robin Buckley", 'a' )

question ("\n\033[0;34mWho in Stranger Things Said 'Sometimes I think it’s just scary to open up like that. To say how you really feel. Especially to people you care about the most. Because, what if they don’t like the truth?'?\n\033[0;35m(a). Chrissy Cunningham\n(b). Nancy Wheeler\n(c). Will Byers", 'c')

question ("\n\033[0;34mWho in Stranger Things said ' It's forced confirmity. Thats whats killing the kids! Thats the real monster.'?\n\033[0;35m(a). Jonathan Byers\n(b). Steve Harrington\n(c). Eddie Munson", 'c')

question ("\n\033[0;34mWho in stranger things said 'You Shouldn't Like Things Because People Tell You You're Supposed To.'?\n\033[0;35m(a). Jonathan Byers\n(b). Joyce Byers\n(c). Max Mayfield", 'a')

question ("\n\033[0;34mWho in Stranger Things said 'We Ask for Forgiveness, Not Permission.'?\n\033[0;35m(a). Jim Hopper\n(b). Nancy Wheeler\n(c). Argyle", 'b')

question ("\n\033[0;34mWho in Stranger Things said 'If we’re both going crazy, then we’ll go crazy together, right?'?\n\033[0;35m(a). Mike Wheeler\n(b). Steve Harrington\n(c). Nancy Wheeler", 'a')

question ("\n\033[0;34mWho in Stranger Things said 'This Is Not Yours To Fix Alone. You Act Like You’re All Alone Out There in the World, but You’re Not. You’re Not Alone.'?\n\033[0;35m(a). Nancy Wheeler\n(b). Joyce Byers\n(c). Dr Sam Owens", 'b')

question ("\n\033[0;34mWho in Stranger Things said 'People don’t spend their lives trying to look at what’s behind the curtain. They like the curtain. It provides them stability, comfort, and definition.'?\n\033[0;35m(a). Dr Brenner\n(b). Dmitri Antonov\n(c). Murray Bauman", 'c')

question ("\n\033[0;34mWho in Stranger Things said 'You know what this half-baked plan of yours sounds like to me? Child endangerment.'?\n\033[0;35m(a). Erica Sinclair\n(b). Dustin Henderson\n(c). Robin Buckley", 'a')

question ("\n\033[0;34mWho in Stranger Things said 'Yeah, the real world sucks, deal with it like the rest of us.'?\n\033[0;35m(a). Jim Hopper\n(b). Jonathan Byers\n(c). Eddie Munson", 'b')


print ("\n\n\033[0;37m.｡.:*✧End Of Quiz.｡.:*✧")