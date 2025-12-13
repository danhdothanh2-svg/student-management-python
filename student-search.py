def find_student_by_name(students):
    keyword = input("Nhập tên sinh viên cần tìm: ").strip().lower()

    found_students = []

    for student in students:
        if keyword in student["name"].lower():
            found_students.append(student)

    if not found_students:
        print("❌ Không tìm thấy sinh viên nào phù hợp.")
    else:
        print(f"✅ Tìm thấy {len(found_students)} sinh viên:")
        for sv in found_students:
            print(f"Mã SV: {sv['student_id']}")
            print(f"Họ tên: {sv['name']}")
            print(f"Tuổi: {sv['age']}")
            print(f"Ngành: {sv['major']}")
