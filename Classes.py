class Faculty:
    faculties = []

    def __init__(self, name):
        self.name = name
        self.faculties.append(self)


class Level:
    levels = []

    def __init__(self, level_number):
        self.level_number = level_number
        self.levels.append(self)


class Department:
    departments = []

    def __init__(self, department_name):
        self.department_name = department_name
        self.departments.append(self)


class FacultyMember:
    faculty_members = []

    def __init__(self, name, faculty, availability):
        self.name = name
        self.faculty = faculty
        self.availability = availability
        self.faculty_members.append(self)


class Course:
    courses = []

    def __init__(self, code, title, duration, faculty, department, year_level, instructor):
        self.code = code
        self.title = title
        self.duration = duration
        self.faculty = faculty
        self.department = department
        self.year_level = year_level
        self.instructor = instructor
        self.courses.append(self)


class Classroom:
    classrooms = []

    def __init__(self, room_number, capacity, faculty):
        self.room_number = room_number
        self.capacity = capacity
        self.faculty = faculty
        self.classrooms.append(self)


class Timeslot:
    timeslots=[]

    def __init__(self, day, start_time, end_time):
        self.day = day
        self.start_time = start_time
        self.end_time = end_time
        self.timeslots.append(self)



