import math
class calGPA:
    list = []
    def getSubjects(self):
        subjects =['BANGLA','ENGLISH','MATH','SCIENCE']
        print("Enter all subjects marks :")
        for sub in subjects:
            str = sub +" Mark : "
            mark = int(input(str))
            self.list.append(mark)
    def totalMarks(self):
        total = 0
        for x in self.list:
            total += x
        return total
    def result(self):
        gpa = math.ceil(self.totalMarks()/len(self.list))
        if gpa>=91:
            print("Total Grade : A+")
            print("Average Mark : "+ str(gpa))
        elif gpa<=90 and gpa>=81:
            print("Total Grade : A")
            print("Average Mark : " + str(gpa))
        elif gpa<=80 and gpa>=71:
            print("Total Grade : B")
            print("Average Mark : " + str(gpa))
        elif gpa<=70 and gpa>=61:
            print("Total Grade : C")
            print("Average Mark : " + str(gpa))
        elif gpa<=60 and gpa>=41:
            print("Total Grade : D")
            print("Average Mark : " + str(gpa))
        else:
            print("Total Grade : F")
            print("Average Mark : " + str(gpa))
st1 = calGPA()
st1.getSubjects()
print("----------------------------------")
st1.result()
print("----------------------------------")
print("I use ceil function to Calculate Average Mark")import math
class calGPA:
    list = []
    def getSubjects(self):
        subjects =['BANGLA','ENGLISH','MATH','SCIENCE']
        print("Enter all subjects marks :")
        for sub in subjects:
            str = sub +" Mark : "
            mark = int(input(str))
            self.list.append(mark)
    def totalMarks(self):
        total = 0
        for x in self.list:
            total += x
        return total
    def result(self):
        gpa = math.ceil(self.totalMarks()/len(self.list))
        if gpa>=91:
            print("Total Grade : A+")
            print("Average Mark : "+ str(gpa))
        elif gpa<=90 and gpa>=81:
            print("Total Grade : A")
            print("Average Mark : " + str(gpa))
        elif gpa<=80 and gpa>=71:
            print("Total Grade : B")
            print("Average Mark : " + str(gpa))
        elif gpa<=70 and gpa>=61:
            print("Total Grade : C")
            print("Average Mark : " + str(gpa))
        elif gpa<=60 and gpa>=41:
            print("Total Grade : D")
            print("Average Mark : " + str(gpa))
        else:
            print("Total Grade : F")
            print("Average Mark : " + str(gpa))
st1 = calGPA()
st1.getSubjects()
print("----------------------------------")
st1.result()
print("----------------------------------")
print("I use ceil function to Calculate Average Mark")