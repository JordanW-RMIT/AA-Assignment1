from dictionary.base_dictionary import BaseDictionary
from dictionary.word_frequency import WordFrequency
from dictionary.node import Node
from typing import List


# ------------------------------------------------------------------------
# This class is required to be implemented. Ternary Search Tree implementation.
#
# __author__ = 'Son Hoang Dau'
# __copyright__ = 'Copyright 2022, RMIT University'
# ------------------------------------------------------------------------


class TernarySearchTreeDictionary(BaseDictionary):

    def __init__(self):
        self.root = None


    def build_dictionary(self, words_frequencies: List[WordFrequency]):
        """
        construct the data structure to store nodes
        @param words_frequencies: list of (word, frequency) to be stored
        """
        for word in words_frequencies:
            _ = self.add_word_frequency(word)


    def search(self, word: str) -> int:
        """
        search for a word
        @param word: the word to be searched
        @return: frequency > 0 if found and 0 if NOT found
        """
        curr_node = self.traverse(self.root, word[0])
        for i in range(len(word) -1):
            if curr_node.letter == word[i]:
                if curr_node.middle != None:
                    if curr_node.middle.letter == word[i+1]:
                        curr_node = curr_node.middle
                    else:
                        curr_node = self.traverse(curr_node.middle, word[i+1])
                else:
                    return 0
            else:
                curr_node = self.traverse(curr_node, word[i])

            if curr_node != None:
                if curr_node.letter == None:
                    return 0
        if curr_node.end_word:
            return curr_node.frequency
        else:
            return 0


    def add_word_frequency(self, word_frequency: WordFrequency) -> bool:
        """
        add a word and its frequency to the dictionary
        @param word_frequency: (word, frequency) to be added
        :return: True whether succeeded, False when word is already in the dictionary
        """
        curr_node = None
        word = word_frequency.word
        frequency = word_frequency.frequency

        # If statement finds the start node of the word starting with the second letter
        curr_node = self.traverse(self.root, word[0])

        if self.root == None or (curr_node != None and curr_node.letter == None) or curr_node == None:
            if self.root == None:
                self.root = Node(letter=word[0])
                curr_node = self.root
            else:
                curr_node.letter = word[0]
            # If nothing exists at given node then the word is added on each middle pointer
            for i in range(1, len(word)):
                letter = word[i]
                if i == len(word) -1:
                    curr_node.middle = Node(letter=letter, frequency=frequency, end_word=True)
                else:
                    curr_node.middle = Node(letter=letter)
                    curr_node = curr_node.middle
        else:
            if curr_node.middle == None:
                curr_node.middle = Node()
            curr_node = curr_node.middle
            for i in range(1, len(word)):
                # temp variable to hold current letter
                letter = word[i]
                # Call traverse function to check where next node should be placed if at all
                if curr_node.letter != None:
                    next_node = self.traverse(curr_node, letter)
                else:
                    next_node = curr_node
                # next_node will be None if the letter given was not already in the tree at the specified position
                if next_node.letter == None:
                    curr_node = next_node
                    for j in range(i, len(word)):
                        if j == len(word) -1:
                            curr_node.letter = word[j]
                            curr_node.frequency = frequency
                            curr_node.end_word = True
                            return True
                        else:
                            curr_node.letter = word[j]
                            curr_node.middle = Node()
                            curr_node = curr_node.middle
                else:
                    if i == len(word) -1:
                        if next_node.end_word == True:
                            return False
                        else:
                            next_node.end_word = True
                            next_node.frequency = frequency
                    else:
                        if next_node.middle == None:
                            next_node.middle = Node()
                        curr_node = next_node.middle
            

        return True


    # Function to traverse the TST to find where the start node of a word will be
    def traverse(self, curr_node, letter):
        # Base case, if the node reached is empty
        if curr_node == None or curr_node.letter == None:
            return curr_node
            # Base case 2, if node reached is equal to letter
        elif letter == curr_node.letter:
            return curr_node
        # elif curr_node.middle != None and letter == curr_node.middle.letter:
        #     return curr_node.middle
        # Check if letter is greater than node letter and recursively call traverse
        elif letter > curr_node.letter:
            if curr_node.right == None: curr_node.right = Node()
            return self.traverse(curr_node.right, letter)
        # Check if letter is less than node letter
        elif letter < curr_node.letter:
            if curr_node.left == None: curr_node.left = Node()
            return self.traverse(curr_node.left, letter)

    # Function to traverse the TST to find the node before a given letter node
    def traverse_before(self, curr_node, letter, last_node=None):
        # Base case, if the node reached is empty
        if curr_node == None or curr_node.letter == None:
            return last_node
            # Base case 2, if node reached is equal to letter
        elif letter == curr_node.letter:
            return last_node
        elif letter == curr_node.middle.letter:
            return curr_node
        # Check if letter is greater than node letter and recursively call traverse
        elif letter > curr_node.letter:
            if curr_node.right == None: curr_node.right = Node()
            return self.traverse_before(curr_node.right, letter, curr_node)
        # Check if letter is less than node letter
        elif letter < curr_node.letter:
            if curr_node.left == None: curr_node.left = Node()
            return self.traverse_before(curr_node.left, letter, curr_node)


    def delete_word(self, word: str) -> bool:
        """
        delete a word from the dictionary
        @param word: word to be deleted
        @return: whether succeeded, e.g. return False when point not found
        """
        curr_node = self.traverse(self.root, word[0])
        node_list = [curr_node]
        for i in range(len(word) -1):
            if curr_node.letter == word[i]:
                if curr_node.middle != None:
                    if curr_node.middle.letter == word[i+1]:
                        curr_node = curr_node.middle
                    else:
                        node_list.append(curr_node.middle)
                        curr_node = self.traverse(curr_node.middle, word[i+1])
            else:
                curr_node = self.traverse(curr_node, word[i])

            if curr_node != None:
                if curr_node.letter == None:
                    return False
                else:
                    node_list.append(curr_node)


        curr_node = node_list[len(node_list)-1]
        if curr_node.left == None and curr_node.middle == None and curr_node.right == None:
            last_node = node_list[len(node_list)-2]
            if last_node.left == curr_node:
                last_node.left = None
            elif last_node.middle == curr_node:
                last_node.middle = None
            elif last_node.right == curr_node:
                last_node.right = None

            for i in range(len(node_list) -2, -1, -1):
                curr_node = node_list[i]
                if curr_node.left == None and curr_node.middle == None and curr_node.right == None and curr_node.end_word != True:
                    # Checks to see if node is the first node in word, if so finds the node before
                    if i == 0:
                        last_node = self.traverse_before(self.root, curr_node.letter)
                    else:
                        last_node = node_list[i-1]

                    # Checks each pointer and sets the one that points to the node to be deleted to None
                    if last_node.left == curr_node:
                        last_node.left = None
                    elif last_node.middle == curr_node:
                        last_node.middle = None
                    elif last_node.right == curr_node:
                        last_node.right = None
                else:
                    return True
            return True

        else:
            curr_node.end_word = False
            curr_node.frequency = None
            return True






    def find_words(self, curr_node, prefix, word_list=None, root_node=True):


        if curr_node.left != None and not root_node:
            # Check if left node is an end of word
            if curr_node.left.end_word and curr_node.left.letter != None:
                # Take one letter of prefix if is a left node
                word_list.append(WordFrequency(prefix[:-1] + curr_node.left.letter, curr_node.left.frequency))
                # Call find words on left node to search through its nodes
                word_list = self.find_words(curr_node.left, prefix[:-1] + curr_node.left.letter, word_list, False)
            # If node is not an end of word but still exists then search through its children
            elif curr_node.left.letter != None:
                word_list = self.find_words(curr_node.left, prefix[:-1] + curr_node.left.letter, word_list, False)

        
        if curr_node.middle != None:
            # Check if middle node is an end of word
            if curr_node.middle.end_word and curr_node.middle.letter != None:
                word_list.append(WordFrequency(prefix + curr_node.middle.letter, curr_node.middle.frequency))
                # Call find words on middle node to search through its nodes
                word_list = self.find_words(curr_node.middle, prefix + curr_node.middle.letter, word_list, False)
            # If node is not an end of word but still exists then search through its children
            elif curr_node.middle.letter != None:
                word_list = self.find_words(curr_node.middle, prefix + curr_node.middle.letter, word_list, False)

        
        if curr_node.right != None and not root_node:
            # Check if right node is an end of word
            if curr_node.right.end_word and curr_node.right.letter != None:
                # Take one letter of prefix if is a right node
                word_list.append(WordFrequency(prefix[:-1] + curr_node.right.letter, curr_node.right.frequency))
                # Call find words on right node to search through its nodes
                word_list = self.find_words(curr_node.right, prefix[:-1] + curr_node.right.letter, word_list, False)
            # If node is not an end of word but still exists then search through its children
            elif curr_node.right.letter != None:
                word_list = self.find_words(curr_node.right, prefix[:-1] + curr_node.right.letter, word_list, False)
        
        # Returns all the words found and their frequencies
        return word_list

    

    def autocomplete(self, word: str) -> List[WordFrequency]:
        """
        return a list of 3 most-frequent words in the dictionary that have 'word' as a prefix
        @param word: word to be autocompleted
        @return: a list (could be empty) of (at most) 3 most-frequent words with prefix 'word'
        """
        # Get final node of prefix
        curr_node = self.root
        for letter in word:
            # Each time a traverse is made it will be from the previous letter
            if curr_node.middle.letter == letter:
                curr_node = curr_node.middle
            elif letter == curr_node.letter:
                curr_node = self.traverse(curr_node.middle, letter)
            else:
                curr_node = self.traverse(curr_node, letter)
            # If the node is not found return a list with no items
            if curr_node.letter == None:
                return []

        prefix_list = self.find_words(curr_node, word, word_list=[])
        # If the root node is also an end of word add this word to the list
        if curr_node.end_word:
            prefix_list.append(WordFrequency(word, curr_node.frequency))

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