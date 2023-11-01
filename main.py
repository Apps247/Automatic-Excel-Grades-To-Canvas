from read_excel import read_excel
from write_to_canvas import *

CPSC_121_COURSE_CODE_CANVAS = 123413
TERM = "2023W1"

print("CPSC 121 Lab Grade Automation Script by Aprameya Aithal\n")

if __name__ == "__main__":
    section_name = input("Enter section name (eg: L12): ")
    lab_no = int(input("Enter lab number (eg: Enter 2 for Lab 02): "))
    lab_no_spoof = None # Set to test a specific lab number
    if lab_no_spoof is not None:
        lab_no = lab_no_spoof

    student_grades = read_excel(section_name, lab_no=lab_no)
    welcome_user()
    load_course(CPSC_121_COURSE_CODE_CANVAS)
    section = get_lab_section(section_name, TERM)
    lab = get_lab_assignment(lab_no, TERM)
    print(lab)
    print(section)

    # for student in get_students(section):
    #     print(student.user['name'])
    if input("Confirm? (Y/n)") in ["Yes", "Y", "Ya", "Of course"]:
        update_grades(lab, section, student_grades)
    else:
        print("Cancelled")

