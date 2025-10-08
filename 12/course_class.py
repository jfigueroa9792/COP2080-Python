class Course:
    # initializing the class Course, enforcing the student variable into a set for uniqueness
    def __init__(self, course, students: set):
        self.__course_name = course 
        if isinstance(students, set): self.__students_set = students
        else: self.__students_set = set(students)
    

    def __str__(self):
        return f"Course name: {self.__course_name}, Students in the course: {self.__students_set}"
        
    # add a student, if student already enrolled ignore.
    def addStudent(self, student: str): 
        student = student.capitalize()
        if student in self.__students_set:
            print(f"Student {student} is already enrolled in this course")
        else:
            self.__students_set.add(student)
            print (f"Student {student} has been successfully enrolled in the course!")    

    # drop a student, if student not enrolled ignore.    
    def dropStudent(self, student: str):
        student = student.capitalize()
        if student in self.__students_set: 
            self.__students_set.remove(student)
            print(f"Student {student} has been dropped from the course!")
        else: print(f"Student {student} is not enrolled in the course")

    # getters
    def getCourseName(self):
        return self.__course_name
    def getStudents(self):
        return print(self.__students_set)
    def getNumOfStudents(self):
        return print(f"The number of students in the class are: {len(self.__students_set)}")

# child class from Course
class InPersonCourse(Course):
    def __init__(self, course, students, room, schedule, max_seats):
        super().__init__(course, students)
        self.__room_number = room
        self.__schedule = schedule
        self.__max_seats = max_seats

    def __str__(self):
        return f"{super().__str__()}, Room Number: {self.__room_number}, Schedule: {self.__schedule}, Max number of Seats: {self.__max_seats}"
    
    # overrides parent method to check for seating as well as uniqueness
    def addStudent(self, student: str):
        student = student.capitalize()
        if student in self._Course__students_set:
            print(f"Student {student} is already enrolled in the course!")
            return
        elif len(self._Course__students_set) >= self.__max_seats:
            print(f"Student {student} was unsuccessfuly enrolled due to the course being full!")
            return
        
        self._Course__students_set.add(student)
        print(f"Student {student} was successfully enrolled in the course and the number of students is:", len(self._Course__students_set))
                
    # getters
    def getRoomNum(self):
        return self.__room_number  
    def getMaxSeats(self):
        return self.__max_seats
    def getSchedule(self):
        return self.__schedule  



### Testing ###
'''
history = InPersonCourse("History", {"Michael", "Drew", "Hannah", "Juan"}, 1032, "MWF 11am - 11:50am", 5)

print(history.__str__())
history.addStudent("Michael")
history.addStudent("Steve")
history.addStudent("steve")
history.addStudent("Michelle")
history.dropStudent("Juan")
history.getCourseName()
history.getMaxSeats()
history.getSchedule()
history.getRoomNum()
'''