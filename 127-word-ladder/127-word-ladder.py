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
        
        counter = 1
        queue.append(beginWord)
        while queue:
            for i in range(len(queue)):
                word = queue.popleft()
                if word == endWord:
                    return counter 
                if word in visited:
                    continue
                    
                w = list(word)
                for i in range(len(w)):
                    temp = w[i]
                    w[i] = '*'
                    nextWords = graph["".join(w)]
                    queue.extend(nextWords)
                    w[i] = temp
                visited.add(word)
                
            counter += 1
        
        return 0
                    
                
                