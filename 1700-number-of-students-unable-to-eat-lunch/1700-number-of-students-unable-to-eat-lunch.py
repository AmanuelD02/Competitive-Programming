class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        sandwiches.reverse()
        students = deque(students)
        while sandwiches:
            FLAG = True
            for i in range(len(students)):
                if sandwiches[-1] == students[0]:
                    sandwiches.pop()
                    students.popleft()
                    FLAG = False
                else:
                    students.append(students.popleft())
            if FLAG:
                return len(students)
        return 0
                