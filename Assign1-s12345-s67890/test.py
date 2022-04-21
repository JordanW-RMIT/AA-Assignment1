from dictionary.hashtable_dictionary import HashTableDictionary
from dictionary.word_frequency import WordFrequency

word1 = WordFrequency("Apple", 100)
word3 = WordFrequency("Ant", 300)
word2 = WordFrequency("App", 200)
word4 = WordFrequency("And", 1000)
word5 = WordFrequency("Adult", 500)

list = [word1, word2, word3, word4, word5]
dict = HashTableDictionary()
dict.build_dictionary(list)

print("---------------")

new_list = dict.autocomplete("B")

print(new_list[0].word)
print(new_list[1].word)
print(new_list[2].word)