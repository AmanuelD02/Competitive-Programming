class Codec:
    def __init__(self):
        self.cache = {}
        
    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        coded = str(hash(longUrl))[1:13]
        self.cache[coded] = longUrl
        return coded

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        return self.cache[shortUrl]
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))