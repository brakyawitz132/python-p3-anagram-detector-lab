# your code goes here!
class Anagram:
    def __init__(self, word):
        self.word = word

    def match(self,list):
        match_list = []
        for word in list:
             if sorted(self.word) == sorted(word):
                 match_list.append(word)
        return match_list
