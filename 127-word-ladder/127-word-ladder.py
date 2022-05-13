class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        graph = defaultdict(set)
        queue, visited = deque(), set()
        
        for word in wordList:
            w = list(word)
            for i in range(len(w)):
                temp = w[i]
                w[i] = '*'
                graph["".join(w)].add(word)
                w[i] = temp
        
        counter = 0
        queue.append(beginWord)
        while queue:
            for i in range(len(queue)):
                word = queue.popleft()
                if word == endWord:
                    return counter + 1
                if word in visited:
                    continue
                w = list(word)
                for i in range(len(w)):
                    temp = w[i]
                    w[i] = '*'
                    nextWords = graph["".join(w)]
                    if nextWords:
                        for ww in nextWords:
                            if ww not in visited:
                                queue.append(ww)
                    w[i] = temp
                visited.add(word)
            counter += 1
        
        return 0
                    
                
                