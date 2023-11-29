from read_excel import read_excel
from write_to_canvas import *

CPSC_121_COURSE_CODE_CANVAS = 123413
TERM = "2023W1"

print("CPSC 121 Lab Grade Automation Script by Aprameya Aithal\n")

def update_grades_for_lab():
    for i in range(len(sections)):
        section_name = section_names.split(" ")[i]
        section = sections[i]
        student_grades = read_excel(section_name, lab_no=lab_no)
        update_grades(lab, section, student_grades)



if __name__ == "__main__":
    load_course(CPSC_121_COURSE_CODE_CANVAS) # Loads CPSC 121 course from Canvas API - must run first!
    welcome_user()

    global section_names
    section_names = input("Enter section names separated by spaces (eg: L1C L13 L14): ")
    global sections
    sections = [get_lab_section(section_name, TERM) for section_name in section_names.split(" ")]    

    global lab_no
    lab_no = int(input("Enter lab number (eg: Enter 2 for Lab 02): "))
    lab_no_spoof = None # Set to test a specific lab number
    if lab_no_spoof is not None:
        lab_no = lab_no_spoof

    print("The following Lab Assignment's grades will be updated:")
    lab = get_lab_assignment(lab_no, TERM)
    print(lab)

    print("The following Sections' grades will be updated:")
    for section in sections:
        print(section)
    print()


    if input("\nConfirm? (Y/n)") in ["Yes", "Y", "Ya", "Of course"]:
        update_grades_for_lab()
    else:
        print("Cancelled")


