class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        st = [(indices[x], s[x]) for x in range(len(indices)) ]
        st.sort()
        return "".join([x[1] for x in st ])