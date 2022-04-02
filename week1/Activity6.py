# exercise 2

class Name:
    def __init__(self, firstName, surName, title, otherNames):
        self.firstName = firstName
        self.surName = surName
        self.title = title
        self.otherName = otherNames
    def formalName(self):
        return f"{self.title} {self.firstName[0]}. {self.surName}"

class DistanceStudent:
    def __init__(self, name, currentModule):
        self.name = name
        self.currentModule = currentModule

    def studentInfo(self):
      return f"{self.name.formalName()} currently studying the {self.currentModule} module"

jason = Name("Jason", "Greenhold", "Mr", "S")
student = DistanceStudent(jason, "Advanced Programming")
print(student.studentInfo())
