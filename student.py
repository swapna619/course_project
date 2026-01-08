import sys

def calculate_grade(avg):
    if 90 <= avg <= 100:
        return "S"
    elif 80 <= avg < 90:
        return "A"
    elif 65 <= avg < 80:
        return "B"
    elif 50 <= avg < 65:
        return "C"
    elif 40 <= avg < 50:
        return "D"
    else:
        return "F"

def main():
    if len(sys.argv) != 7:
        print("Usage: python student.py <name> <dept> <sem> <m1> <m2> <m3>")
        sys.exit(1)

    name = sys.argv[1]
    department = sys.argv[2]
    semester = sys.argv[3]
    m1 = int(sys.argv[4])
    m2 = int(sys.argv[5])
    m3 = int(sys.argv[6])

    avg = (m1 + m2 + m3) / 3
    grade = calculate_grade(avg)

    print("===== STUDENT DETAILS =====")
    print(f"Name       : {name}")
    print(f"Department : {department}")
    print(f"Semester   : {semester}")
    print(f"Average    : {avg:.2f}")
    print(f"Grade      : {grade}")

if __name__ == "__main__":
    main()
