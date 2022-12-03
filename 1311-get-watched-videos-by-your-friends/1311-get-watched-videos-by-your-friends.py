class Solution:
    def watchedVideosByFriends(self, watchedVideos: List[List[str]], friends: List[List[int]], id: int, level: int) -> List[str]:
        queue = deque()
        queue.append(id)
        visited = {id}
        moviesWatched = {}
        
        while queue and level > 0:
            for _ in range(len(queue)):
                curr = queue.popleft()
                for friend in  friends[curr]:
                    if friend not in visited:
                        visited.add(friend)
                        queue.append(friend)
            
            level -= 1
        
        
        
        for friend in queue:
            for movies in watchedVideos[friend]:
                moviesWatched[movies] = 1 + moviesWatched.get(movies, 0)
        
        movie_freq = [(freq, movie) for movie, freq in moviesWatched.items()]
        movie_freq.sort()
        
        return [ movie for _, movie in movie_freq]