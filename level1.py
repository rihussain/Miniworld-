#task1
import random
print("Random Quote Generator")
greetings=["Hello!","konnichiwa!","Greetings!"]
goodbys=["Good Day!","Sayonara!","Bye Bye!","Mata ne!","See you soon!"]

print(random.choice(greetings))

un=input("Enter your noble name MASTER: ")
c=""
quotes = {
    'motivation': [
        {"quote": "Believe you can and you're halfway there.", "author": "Theodore Roosevelt"},
        {"quote": "The future belongs to those who believe in the beauty of their dreams.", "author": "Eleanor Roosevelt"},
        {"quote": "He who conquers himself is the mightiest warrior.", "author": "Confucius"},
        {"quote": "The only limit to our realization of tomorrow will be our doubts of today.", "author": "Franklin D. Roosevelt"},
        {"quote": "Don't watch the clock; do what it does. Keep going.", "author": "Sam Levenson"}
    ],
    'success': [
        {"quote": "Success is not the key to happiness. Happiness is the key to success.", "author": "Albert Schweitzer"},
        {"quote": "Success usually comes to those who are too busy to be looking for it.", "author": "Henry David Thoreau"},
        {"quote": "The road to success and the road to failure are almost exactly the same.", "author": "Colin R. Davis"},
        {"quote": "Success is not in what you have, but who you are.", "author": "Bo Bennett"},
        {"quote": "He will win who knows when to fight and when not to fight.", "author": "Sun Tzu"}
    ],
    'life': [
        {"quote": "The difference between a novice and a master is that a master has failed more times than a novice had tried." , "author": "Ryushi Korogane"},
        {"quote": "The purpose of our lives is to be happy.", "author": "Dalai Lama"},
        {"quote": "Life is really simple, but we insist on making it complicated.", "author": "Confucius"},
        {"quote": "Life is either a daring adventure or nothing at all.", "author": "Helen Keller"}
    ],
    'love': [
        {"quote": "You will never be able to love anybody else until you love yourself.", "author": "Lelouch Lamperouge"},
        {"quote": "Love is composed of a single soul inhabiting two bodies.", "author": "Aristotle"},
        {"quote": "A successful marriage requires falling in love many times, always with the same person.", "author": "Mignon McLaughlin"},
        {"quote": "The best thing to hold onto in life is each other.", "author": "Audrey Hepburn"}
    ]
    }
while(c!="exit"):
    c=input("\nMASTER "+un+" enter the category for the quote(MOTIVATION,SUCCESS,LIFE,LOVE) or MASTER "+un+" can take your humble absence by typing(exit) : ")
    c=c.lower()
    if c in quotes:
        obj = random.choice(quotes[c])
        quote = obj["quote"]
        author = obj["author"]
        gen_q = quote.replace("{name}",un)
        print("\n"+un+"'s generated quote ")
        print("\n"+gen_q)
        print("--" + author)
    elif c!="exit":
        print("\nMaster kindly enter a valid category ")
    if c=="exit":
        break
       
print("\n"+random.choice(goodbys)+" "+un)
    
    
