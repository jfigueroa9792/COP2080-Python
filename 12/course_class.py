class Course:
    '''
    course_name (private)
    list of students (private)
    
    addStudent(self, student) shouldn't enroll the same student twice

    getCourseName
    getStudents
    getNumberOfStudents

    dropStudent(self, student) should provide a message with a dropped student name; should check if the student is enrolled


    __str__ info about the course
    '''

class InPersonCourse(Course):
    ''' 
    room_number (private)
    schedule (MWF 11am - 11:50am) string (private)
    max_seats (private)

    Override addStudent method (check if there are available seats); print corresponding message
    Override __str__

    '''