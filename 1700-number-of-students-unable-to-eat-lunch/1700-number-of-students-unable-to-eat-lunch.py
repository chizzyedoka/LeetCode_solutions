class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        students = deque(students)
        sandwishes = deque(sandwiches)
        while len(students)!=0 and sandwishes[0] in students:
            if students[0] == sandwishes[0]:
                students.popleft()
                sandwishes.popleft()
            else:
                students.append(students.popleft())
        return 0 if len(students) == 0 else len(students)