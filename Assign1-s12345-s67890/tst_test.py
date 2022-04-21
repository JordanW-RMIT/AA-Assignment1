from dictionary.ternarysearchtree_dictionary import TernarySearchTreeDictionary
from dictionary.word_frequency import WordFrequency
from dictionary.node import Node

word1 = WordFrequency("cut", 10)
word2 = WordFrequency("app", 20)
word3 = WordFrequency("cute", 50)
word4 = WordFrequency("farm", 40)
word5 = WordFrequency("cup", 30)
word6 = WordFrequency("hello", 60)
list = [word1, word2, word3, word4, word5, word6]
tst = TernarySearchTreeDictionary()
tst.build_dictionary(list)

temp = tst.autocomplete("cut")

for word in temp:
    print(word.word + ": " + str(word.frequency))