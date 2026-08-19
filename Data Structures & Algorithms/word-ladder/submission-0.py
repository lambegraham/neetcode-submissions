class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        
        #build adj wildcard
        wildCards = defaultdict(list)
        wordList.append(beginWord) #append starting word to our wordlist

        for word in wordList:
            for j in range(len(word)):
                pattern = word[:j] + "*" + word[j + 1:]
                wildCards[pattern].append(word) #*ot = {hot} .. etc
        
        #bfs
        visited = set([beginWord])
        q = deque([(beginWord)])
        res = 1 #since we start at 1
        while q:
            for _ in range(len(q)):
                word = q.popleft()
                if word == endWord:
                    return res                
                #else rebuild pattern 
                for j in range(len(word)):
                    pattern = word[:j] + "*" + word[j + 1:] #build pattern
                    for neiWord in wildCards[pattern]: #check for words in this pattern
                        if neiWord in visited:
                            continue
                        visited.add(neiWord)
                        q.append(neiWord)
            res +=1
        return 0