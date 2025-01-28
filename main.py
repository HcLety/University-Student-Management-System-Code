import json

class Student:
    def __init__(self, student_id, name, age, major):
        """
        Initializes a student object with their ID, name, age, and major.

        :param student_id: The unique ID for the student.
        :param name: The name of the student.
        :param age: The age of the student.
        :param major: The major the student is enrolled in.
        """
        self.student_id = student_id
        self.name = name
        self.age = age
        self.major = major
        self.courses = []

    def add_course(self, course):
        """
        Adds a course to the student's list of courses.

        :param course: The course to be added.
        """
        self.courses.append(course)

    def remove_course(self, course):
        """
        Removes a course from the student's list of courses.

        :param course: The course to be removed.
        """
        if course in self.courses:
            self.courses.remove(course)
        else:
            print(f"{course} is not in the student's courses.")

    def get_courses(self):
        """
        Returns the list of courses the student is enrolled in.

        :return: A list of course names.
        """
        return self.courses

    def __str__(self):
        """
        String representation of the student object.
        """
        return f"{self.name} (ID: {self.student_id}), Age: {self.age}, Major: {self.major}, Courses: {', '.join(self.courses)}"


class Course:
    def __init__(self, course_code, course_name, instructor, credits):
        """
        Initializes a course object with its course code, name, instructor, and credits.

        :param course_code: The code of the course (e.g., CS101).
        :param course_name: The name of the course (e.g., Introduction to Computer Science).
        :param instructor: The name of the instructor.
        :param credits: The number of credits for the course.
        """
        self.course_code = course_code
        self.course_name = course_name
        self.instructor = instructor
        self.credits = credits

    def __str__(self):
        """
        String representation of the course object.
        """
        return f"{self.course_name} (Code: {self.course_code}), Instructor: {self.instructor}, Credits: {self.credits}"


class University:
    def __init__(self):
        """
        Initializes a university object with an empty database of students and courses.
        """
        self.students = []
        self.courses = []

    def add_student(self, student):
        """
        Adds a student to the university.

        :param student: The student object to be added.
        """
        self.students.append(student)

    def remove_student(self, student_id):
        """
        Removes a student from the university by their ID.

        :param student_id: The ID of the student to be removed.
        """
        student = self.get_student_by_id(student_id)
        if student:
            self.students.remove(student)
            print(f"Student {student.name} has been removed.")
        else:
            print("Student not found.")

    def add_course(self, course):
        """
        Adds a course to the university.

        :param course: The course object to be added.
        """
        self.courses.append(course)

    def get_student_by_id(self, student_id):
        """
        Gets a student by their ID.

        :param student_id: The ID of the student.
        :return: The student object if found, otherwise None.
        """
        for student in self.students:
            if student.student_id == student_id:
                return student
        return None

    def get_course_by_code(self, course_code):
        """
        Gets a course by its code.

        :param course_code: The course code.
        :return: The course object if found, otherwise None.
        """
        for course in self.courses:
            if course.course_code == course_code:
                return course
        return None

    def save_to_file(self, filename="university_data.json"):
        """
        Saves the university data (students and courses) to a JSON file.

        :param filename: The filename to save the data to.
        """
        data = {
            "students": [vars(student) for student in self.students],
            "courses": [vars(course) for course in self.courses]
        }
        with open(filename, 'w') as f:
            json.dump(data, f, indent=4)

    def load_from_file(self, filename="university_data.json"):
        """
        Loads the university data (students and courses) from a JSON file.

        :param filename: The filename to load the data from.
        """
        try:
            with open(filename, 'r') as f:
                data = json.load(f)
                self.students = [Student(**student) for student in data["students"]]
                self.courses = [Course(**course) for course in data["courses"]]
        except FileNotFoundError:
            print("No data file found, starting with an empty database.")


# Create a university instance
university = University()

# Add courses
course1 = Course("CS101", "Introduction to Computer Science", "Dr. Smith", 3)
course2 = Course("MATH101", "Calculus I", "Prof. Johnson", 4)
university.add_course(course1)
university.add_course(course2)

# Add students
student1 = Student(1, "Alice Johnson", 20, "Computer Science")
student2 = Student(2, "Bob Brown", 22, "Mathematics")
university.add_student(student1)
university.add_student(student2)

# Enroll students in courses
student1.add_course(course1.course_name)
student2.add_course(course2.course_name)

# Print student information
print(student1)
print(student2)

# Save to file
university.save_to_file()

# Load from file (testing persistence)
new_university = University()
new_university.load_from_file()

# Print students after loading
for student in new_university.students:
    print(student)
