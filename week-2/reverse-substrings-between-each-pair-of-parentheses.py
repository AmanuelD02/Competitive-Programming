# https://leetcode.com/problems/reverse-substrings-between-each-pair-of-parentheses/

from collections import deque
class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        queue = deque()
        opening = '('
        closing = ')'
        for letter in s:
            if letter == closing:
                current = stack.pop()
                while(current != opening):
                    queue.append(current)
                    current = stack.pop()
                while len(queue) >0:
                    stack.append(queue.popleft())
            else:
                stack.append(letter)
        return ''.join(stack)
        