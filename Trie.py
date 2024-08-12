
########################################################
########################################################
########################################################
# Trie, with basic insert and search
class TrieNode:
    def __init__(self):
        # Stores children nodes and whether node is the end of a word
        self.children = {}
        self.isEnd = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str):
        cur = self.root
        # Insert character by character into trie
        for c in word:
            # if character path does not exist, create it
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.isEnd = True

    def search(self, word: str):
        cur = self.root
        # Search character by character in trie
        for c in word:
            # if character path does not exist, return False
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return cur.isEnd

    def startsWith(self, prefix: str):
        # Same as search, except there is no isEnd condition at final return
        cur = self.root
        for c in prefix:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return True


########################################################
########################################################
########################################################
# Trie, with a smart prefix-suffix combination search for words
class TrieNode(object):
    def __init__(self):
        self.children = {}
        self.end_of_word = False
        self.word = None

    def fill_stats(self, suffix =""):
        for char in self.children:
                new_suffix = suffix + char
                self.children[char].fill_stats(new_suffix)
        if self.end_of_word:
                self.word = suffix

    def search(self, prefix):
        if len(prefix) == 0:
                if self.end_of_word:
                        return self.word
                else:
                        return -1
        s = prefix[0]

        if s in self.children:
                return self.children[s].search(prefix[1:])
        else:
                return -1


    def add_word(self, word):
        if len(word) == 0:
                self.end_of_word = True
                return
        w = word[0]
        if w in self.children:
                child = self.children[w]
        else:
                child = TrieNode()
                self.children[w] = child
        child.add_word(word[1:])


root = TrieNode()

class WordFilter(object):
    def __init__(self, words):
        """
        :type words: List[str]
        """
        self.words = words
        for word in words:
                for i in range(len(word)+1):
                        concat_word = word[i:] + "{" + word
                        root.add_word(concat_word)
        root.fill_stats()

    def f(self, pref, suff):
        """
        :type pref: str
        :type suff: str
        :rtype: int
        """
        word = root.search(suff + "{" + pref)
        # print("search word: ", word)
        if word == -1:
                return -1
        word = word.split("{")[1]
        idx = self.words.index(word)
        print(idx)
        return idx





# Your WordFilter object will be instantiated and called as such:
words = ["x", "apeeeee", "apple"]
words = ["abbba","abba"]

# pref, suff = ["a", "e"]
pref, suff = ["ab","ba"]
obj = WordFilter(words)
param_1 = obj.f(pref,suff)

# print(root.children)
# print(root.children["{"].children["x"].complete_word)