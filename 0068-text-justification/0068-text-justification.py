class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        result = []
        
        curr_word_length, curr_words = 0 ,  []
        for word in words:
            if len(word) + curr_word_length + len(curr_words) > maxWidth:
                # ADD LINE TO result
                left = maxWidth - curr_word_length
                for i in range(left):
                    curr_words[i % (max(1, len(curr_words) - 1))] += ' '
                result.append("".join(curr_words))
                
                curr_word_length = 0
                curr_words = []
            
            curr_word_length += (len(word))
            curr_words.append(word)
        
        
        return result + [" ".join(curr_words).ljust(maxWidth)]