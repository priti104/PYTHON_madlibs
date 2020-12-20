print("***Hint: a Verb is an action. A noun is a person/place/thing. An adjective describes a person/place/thing.***")

food_or_silly_word = input("A Food or Silly Word : ")
profession = input("Profession/Job : ")
adjective = input("Adjective : ")
phrase_lyrics_quote = input("Phrase/Lyrics/Quote : ")
animal = input("Animal : ")
verb = input("Verb : ")
place = input("Place : ")
celebrity = input("Celebrity : ")
something_you_would_buy = input("Something you would buy : ")
noun = input("Noun : ") 

madlib = f"Hi my name is {celebrity}, but my friends call me {adjective} {food_or_silly_word}.\n My favorite color is the color of {noun} and my favorite thing to do is {verb}.\n My parents were a {animal} and {profession}, which is why we lived in {place}.\n You probably know me from my TV commercial for {something_you_would_buy}.\n I'm the one who says, '{phrase_lyrics_quote}' at the very end!"

print(madlib)
