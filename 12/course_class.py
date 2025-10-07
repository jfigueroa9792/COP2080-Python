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
        student.title()
        if student in self.__students_set:
            print(f"Student {student} is already enrolled in this course")
        else:
            self.__students_set.add(student)
            print (f"Student {student} has been successfully enrolled in the course!")    

    # drop a student, if student not enrolled ignore.    
    def dropStudent(self, student):
        student.title()
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
        self.room_number = room
        self.schedule = schedule
        self.max_seats = max_seats

    def __str__(self):
        return f"{super().__str__()}, Room Number: {self.room_number}, Schedule: {self.schedule}, Max number of Seats: {self.max_seats}"
    
    # overrides parent method to check for seating as well as uniqueness
    def addStudent(self, student):
        if len(self._Course__students_set) < self.max_seats:
            self._Course__students_set.add(student)
            print(f"Student {student} was successfully enrolled in the course and the number of students is:"
                  , len(self._Course__students_set))
        else:
            print(f"Student {student} was unsuccessfully added due to the course being fully enrolled!")
