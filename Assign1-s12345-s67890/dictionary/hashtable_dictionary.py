from dictionary.base_dictionary import BaseDictionary
from dictionary.word_frequency import WordFrequency
from typing import List


# ------------------------------------------------------------------------
# This class is required TO BE IMPLEMENTED. Hash-table-based dictionary.
#
# __author__ = 'Son Hoang Dau'
# __copyright__ = 'Copyright 2022, RMIT University'
# ------------------------------------------------------------------------

class HashTableDictionary(BaseDictionary):

    def build_dictionary(self, words_frequencies: List[WordFrequency]):
        """
        construct the data structure to store nodes
        @param words_frequencies: list of (word, frequency) to be stored
        """
        self.words_frequencies = {}

        for word in words_frequencies:
            self.words_frequencies[word.word] = word.frequency

    def search(self, word: str) -> int:
        """
        search for a word
        @param word: the word to be searched
        @return: frequency > 0 if found and 0 if NOT found
        """
        return_value = 0

        try:
            return_value = self.words_frequencies[word]
        except:
            return_value = 0

        return return_value

    def add_word_frequency(self, word_frequency: WordFrequency) -> bool:
        """
        add a word and its frequency to the dictionary
        @param word_frequency: (word, frequency) to be added
        :return: True whether succeeded, False when word is already in the dictionary
        """

        return_value = False

        try:
            self.words_frequencies[word_frequency.word] = word_frequency.frequency
            return_value = True
        except:
            return_value = False

        return return_value

    def delete_word(self, word: str) -> bool:
        """
        delete a word from the dictionary
        @param word: word to be deleted
        @return: whether succeeded, e.g. return False when point not found
        """
        return_value = False

        try:
            del self.words_frequencies[word]
            return_value = True
        except:
            return_value = False

        return return_value

    def autocomplete(self, word: str) -> List[WordFrequency]:
        """
        return a list of 3 most-frequent words in the dictionary that have 'word' as a prefix
        @param word: word to be autocompleted
        @return: a list (could be empty) of (at most) 3 most-frequent words with prefix 'word'
        """
        prefix_list = []
        for key in self.words_frequencies.keys():
            if key.startswith(word):
                prefix_list.append(key)

        benchmarkList = []
        if len(prefix_list) > 0:

            benchmarkFrequency = self.words_frequencies[prefix_list[0]]

            lowestFrequencyIndex = 0
            for word in prefix_list:

                if len(benchmarkList) < 3:

                    benchmarkList.append(word)

                    if self.words_frequencies[word] < benchmarkFrequency:
                        benchmarkFrequency = self.words_frequencies[prefix_list[0]]

                        lowestFrequencyIndex = benchmarkList.index(word)


                elif self.words_frequencies[word] > benchmarkFrequency:

                    benchmarkList[lowestFrequencyIndex] = word

                    benchmarkFrequency = self.words_frequencies[word]

                    lowestFrequencyIndex = benchmarkList.index(word)

                    for key in benchmarkList:
                        if self.words_frequencies[key] < benchmarkFrequency:
                            benchmarkFrequency = self.words_frequencies[key]

                            lowestFrequencyIndex = benchmarkList.index(key)


        benchmarkList.sort(key = lambda x: self.words_frequencies[x], reverse=True)

        return_list = []
        for i in range(len(benchmarkList)):
            return_list.append(WordFrequency(benchmarkList[i], self.words_frequencies[benchmarkList[i]]))

        return return_list
