class Student:
    def__init__(self,name,marks):
        self.name = name
        self.marks = marks
        
    def avarage(self):
        tot=0
        for m in self.marks:
            tot+=m
            avg=tot/len(m)
        return avg
        
s=Student("Harry",[100, 93, 97, 95])
print(f"Student : {s.name} got Avarage : {s.avg} marks")