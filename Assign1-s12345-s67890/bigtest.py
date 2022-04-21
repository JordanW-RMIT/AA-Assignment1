import sys
from dictionary.node import Node
from dictionary.word_frequency import WordFrequency
from dictionary.base_dictionary import BaseDictionary
from dictionary.list_dictionary import ListDictionary
from dictionary.hashtable_dictionary import HashTableDictionary
from dictionary.ternarysearchtree_dictionary import TernarySearchTreeDictionary
import time

dictType = "tst"

agent: BaseDictionary = None
if dictType == 'list':
    agent = ListDictionary()
elif dictType == 'hashtable':
    agent = HashTableDictionary()
elif dictType == 'tst':
        agent = TernarySearchTreeDictionary()

data_filename = "sampleData200k.txt"
words_frequencies_from_file = []
try:
    data_file = open(data_filename, 'r')
    for line in data_file:
        values = line.split()
        word = values[0]
        frequency = int(values[1])
        word_frequency = WordFrequency(word, frequency)  # each line contains a word and its frequency
        words_frequencies_from_file.append(word_frequency)
    data_file.close()
    agent.build_dictionary(words_frequencies_from_file)
except FileNotFoundError as e:
    print("Data file doesn't exist.")

print("----------------")
avgTime = []

for i in range(0,100):
    start_time = time.time()

    new_list = agent.autocomplete("hell")

    end_time = time.time()

    avgTime.append(end_time-start_time)

print(sum(avgTime)/len(avgTime))

print("----------------")

print(new_list[0].word + ": " + str(new_list[0].frequency))
print(new_list[1].word + ": " + str(new_list[1].frequency))
print(new_list[2].word + ": " + str(new_list[2].frequency))