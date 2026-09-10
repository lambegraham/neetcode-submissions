class TrieNode():
    def __init__(self):
        self.children = {}
        self.word = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.word = True
        
    def search(self, word: str) -> bool:
        def dfs(j, root):
            curr = root

            for i in range(j, len(word)): #loop through word given in dfs()
                c = word[i] #letter
                if c == '.':
                    for child in curr.children.values():
                        if dfs(i+1, child):
                            return True #word found
                    return False #word not found

                else:
                    if c not in curr.children:
                        return False
                    curr = curr.children[c] #adv
            return curr.word
            
        return dfs(0, self.root) #begin searching from 0