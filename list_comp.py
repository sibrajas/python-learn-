numbers=[1.1,1.2,-1.4,-3,2]
newlist=[int(number) for number in numbers if number>0]
print newlist
sentence="The fox jumped over the wall" #first the is in capitals
words=[]
words=sentence.split()
lens=[len(word) for word in words if word != "the"]
print words
#print word for word in words if word != "the"
print lens
sentence = "the quick brown fox jumps over the lazy dog"
words = sentence.split()
word_lengths = [len(word) for word in words if word != "the"]
print word_lengths
