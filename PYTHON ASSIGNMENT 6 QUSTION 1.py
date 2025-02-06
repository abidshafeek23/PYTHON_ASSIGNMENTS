class Course:
    def __init__(self, course_code, course_name, credit_hours):
        self.course_code = course_code
        self.course_name = course_name
        self.credit_hours = credit_hours

    def __str__(self):
        return f"Course Code: {self.course_code}, Course Name: {self.course_name}, Credit Hours: {self.credit_hours}"

class CoreCourse(Course):
    def __init__(self, course_code, course_name, credit_hours, required_for_major):
        super().__init__(course_code, course_name, credit_hours)
        self.required_for_major = required_for_major

    def __str__(self):
        return super().__str__() + f", Required for Major: {self.required_for_major}"

class ElectiveCourse(Course):
    def __init__(self, course_code, course_name, credit_hours, elective_type):
        super().__init__(course_code, course_name, credit_hours)
        self.elective_type = elective_type

    def __str__(self):
        return super().__str__() + f", Elective Type: {self.elective_type}"

if __name__ == '__main__':
    core_course = CoreCourse("CS101", "Introduction to Computer Science", 3, True)
    print(core_course)

    elective_course = ElectiveCourse("ARTS101", "Introduction to Art", 2, "Liberal arts")
    print(elective_course)
