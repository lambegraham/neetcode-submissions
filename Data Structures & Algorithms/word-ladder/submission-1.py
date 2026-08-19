class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        nei = defaultdict(list)
        wordList.append(beginWord)

        for word in wordList:
            for j in range(len(word)):
                pattern = word[:j] + "*" + word[j+1:]
                nei[pattern].append(word) #*ot= {..}
        
        q = deque([(beginWord)])
        visited = set([beginWord])
        res = 1 #since we take 1 word to get there

        while q:
            for j in range(len(q)):
                word = q.popleft()
                if word == endWord:
                    return res

                for j in range(len(word)):
                    pattern = word[:j] + "*" + word[j+1:]
                    
                    for neiWord in nei[pattern]:
                        if neiWord in visited:
                            continue
                        visited.add(neiWord)
                        q.append(neiWord)
            res += 1
        return 0