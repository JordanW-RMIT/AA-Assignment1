from dictionary.word_frequency import WordFrequency
from dictionary.base_dictionary import BaseDictionary
from typing import List


# ------------------------------------------------------------------------
# This class is required TO BE IMPLEMENTED. List-based dictionary implementation.
#
# __author__ = 'Son Hoang Dau'
# __copyright__ = 'Copyright 2022, RMIT University'
# ------------------------------------------------------------------------

class ListDictionary(BaseDictionary):

    def build_dictionary(self, words_frequencies: List[WordFrequency]):
        """
        construct the data structure to store nodes
        @param words_frequencies: list of (word, frequency) to be stored
        """
        self.words_frequencies = words_frequencies

    def search(self, word: str) -> int:
        """
        search for a word
        @param word: the word to be searched
        @return: frequency > 0 if found and 0 if NOT found
        """
        return_value = 0

        for word_obj in self.words_frequencies:
            if word_obj.word == word:
                return_value = word_obj.frequency
        
        return return_value

    def add_word_frequency(self, word_frequency: WordFrequency) -> bool:
        """
        add a word and its frequency to the dictionary
        @param word_frequency: (word, frequency) to be added
        :return: True whether succeeded, False when word is already in the dictionary
        """

        return_value = False
        exists = False

        for word in self.words_frequencies:
            if word.word == word_frequency.word:
                exists = True
        
        if not exists:
            self.words_frequencies.append(word_frequency)
            return_value = True

        return return_value

    def delete_word(self, word: str) -> bool:
        """
        delete a word from the dictionary
        @param word: word to be deleted
        @return: whether succeeded, e.g. return False when point not found
        """
        return_value = False
        exists = False
        index = 0

        for i in range(len(self.words_frequencies)):
            if self.words_frequencies[i].word==word:
                exists = True
                index = i

        if exists:
            del self.words_frequencies[index]
            return_value = True
        return return_value

    def autocomplete(self, prefix_word: str) -> List[WordFrequency]:
        """
        return a list of 3 most-frequent words in the dictionary that have 'prefix_word' as a prefix
        @param prefix_word: word to be autocompleted
        @return: a list (could be empty) of (at most) 3 most-frequent words with prefix 'prefix_word'
        """
        
        # List to hold words that contain the prefix
        prefix_list = []
        for word in self.words_frequencies:
            if word.word.startswith(prefix_word):
                prefix_list.append(word)

        benchmarkList = []
        if len(prefix_list) > 0:

            benchmarkFrequency = prefix_list[0].frequency
            lowestFrequencyIndex = 0
            for word in prefix_list:

                if len(benchmarkList) < 3:

                    benchmarkList.append(word)

                    if word.frequency < benchmarkFrequency:
                        benchmarkFrequency = word.frequency

                        lowestFrequencyIndex = benchmarkList.index(word)


                elif word.frequency > benchmarkFrequency:

                    del benchmarkList[lowestFrequencyIndex]

                    benchmarkList.append(word)
                    benchmarkFrequency = word.frequency

                    lowestFrequencyIndex = benchmarkList.index(word)

                    for i in benchmarkList:
                        if i.frequency < benchmarkFrequency:
                            benchmarkFrequency = i.frequency

                            lowestFrequencyIndex = benchmarkList.index(i)

        benchmarkList.sort(key = lambda x: x.frequency, reverse=True)

        return benchmarkList

    def getWordIndex(self, word):
        index = -1
        for i in range(len(self.words_frequencies)):
            if self.words_frequencies[i]==word:
                index = i
        return index
