class Solution:
    def studentGrade(self, marks):
        if marks>=90:
            print("Grade A") 
        elif marks <90 and marks>= 70:
            print("Grade B")
        elif marks <70 and marks >=50:
             print("Grade C")
        elif marks <50 and marks >=35:
            print("Grade D")
        else:
            print("Fail")

solution = Solution()

marks= int(input("Marks : "))
solution.studentGrade(marks)

