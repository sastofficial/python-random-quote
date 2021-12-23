import random
def first():
   #print("Keep it logically awesome.")

  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()
  last = 8
  rnd = random.randint(1, last)
  print(quotes[rnd])

if __name__== "__main__":
  first()
