student_records = [
    {
        "student_id": "SV001",
        "name": "Nguyễn Văn A",
        "math": 8.5,
        "physics": 7.0,
        "chemistry": 9.0
    },
    {
        "student_id": "SV002",
        "name": "Trần Thị B",
        "math": 4.0,
        "physics": 5.5,
        "chemistry": 5.0
    },
    {
        "student_id": "SV003",
        "name": "Lê Văn C",
        "math": 9.5,
        "physics": 9.0,
        "chemistry": 8.5
    }
]


def get_average(student):
    return (student["math"] + student["physics"] + student["chemistry"]) / 3

def get_rank(avg_score):
    
    if avg_score >= 8.0:
        return "Giỏi"
    elif avg_score >= 6.5:
        return "Khá"
    elif avg_score >= 5.0:
        return "Trung bình"
    else:
        return "Yếu"

def find_student(records, student_id):
    
    for student in records:
        if student["student_id"] == student_id:
            return student
    return None

def validate_score():

    while True:
        score_input = input("Nhập điểm mới: ").strip()
        try:
            score = float(score_input)
            if 0 <= score <= 10:
                return score
            else:
                print("Điểm số không hợp lệ. Vui lòng nhập từ 0 đến 10!")
        except ValueError:
            print("Điểm số không hợp lệ. Vui lòng nhập số!")



def display_grades(records):
    """Chức năng 1: Xem bảng điểm và học lực"""
    print("\n--- BẢNG ĐIỂM SINH VIÊN ---")
    if len(records) == 0:
        print("Hệ thống chưa có dữ liệu sinh viên.")
        return

    for index, student in enumerate(records):
        avg = get_average(student)
        rank = get_rank(avg)
        print(f"{index + 1}. [{student['student_id']}] {student['name']} | Toán: {student['math']} | Lý: {student['physics']} | Hóa: {student['chemistry']} | ĐTB: {avg:.2f} - {rank}")
    print("-" * 30)

def update_student_score(records):
    
    print("\n--- CẬP NHẬT ĐIỂM THI ---")
    
    s_id = input("Nhập mã sinh viên cần cập nhật: ").strip().upper()
    found_student = find_student(records, s_id)

    if not found_student:
        print(f"Không tìm thấy sinh viên mang mã {s_id} trong hệ thống!")
        return

    
    while True:
        subject_choice = input("Chọn môn học (1-Toán, 2-Lý, 3-Hóa): ").strip()
        if subject_choice in ['1', '2', '3']:
            break
        print("Lựa chọn không hợp lệ, vui lòng chọn 1, 2 hoặc 3.")

    
    subject_map = {'1': ('math', 'Toán'), '2': ('physics', 'Lý'), '3': ('chemistry', 'Hóa')}
    dict_key, subject_name = subject_map[subject_choice]

   
    new_score = validate_score()

    # Cập nhật trực tiếp vào Pointer
    found_student[dict_key] = new_score
    print(f">> Đã cập nhật điểm {subject_name} của sinh viên '{found_student['name']}' thành {new_score}.")

def generate_report(records):
    print("\n--- BÁO CÁO HỌC VỤ ---")
    total_students = len(records)
    
    if total_students == 0:
        print("Hệ thống chưa có dữ liệu sinh viên.")
        return

    pass_count = 0
    for student in records:
        if get_average(student) >= 5.0:
            pass_count += 1
            
    fail_count = total_students - pass_count
    
    # Tính tỷ lệ phần trăm
    pass_pct = (pass_count / total_students) * 100
    fail_pct = (fail_count / total_students) * 100

    print(f"Tổng số sinh viên: {total_students}")
    print(f"Số lượng qua môn (ĐTB >= 5.0): {pass_count} sinh viên (Chiếm {pass_pct:.2f}%)")
    print(f"Số lượng trượt (ĐTB < 5.0): {fail_count} sinh viên (Chiếm {fail_pct:.2f}%)")
    print("-" * 30)

def find_valedictorian(records):
    """Chức năng 4: Tìm sinh viên Thủ khoa (Max ĐTB)"""
    print("\n--- VINH DANH THỦ KHOA ---")
    if len(records) == 0:
        print("Hệ thống chưa có dữ liệu sinh viên.")
        return

    valedictorian = None
    max_avg = -1.0

    # Thuật toán tìm Max cơ bản
    for student in records:
        current_avg = get_average(student)
        if current_avg > max_avg:
            max_avg = current_avg
            valedictorian = student

    print(f"Sinh viên: {valedictorian['name']} (Mã: {valedictorian['student_id']})")
    print(f"Điểm Trung Bình: {max_avg:.2f}")
    print("Chúc mừng sinh viên đã đạt thành tích xuất sắc nhất khóa!")
    print("-" * 30)


def main():
    while True:
        print("\n===== HỆ THỐNG QUẢN LÝ ĐIỂM THI RIKKEI UNIVERSITY =====")
        print("1. Xem bảng điểm và học lực")
        print("2. Cập nhật điểm thi sinh viên")
        print("3. Báo cáo thống kê (Đỗ/Trượt)")
        print("4. Tìm sinh viên Thủ khoa")
        print("5. Thoát chương trình")
        print("=======================================================")
        
        choice = input("Chọn chức năng (1-5): ").strip()

        if choice == '1':
            display_grades(student_records)
        elif choice == '2':
            update_student_score(student_records)
        elif choice == '3':
            generate_report(student_records)
        elif choice == '4':
            find_valedictorian(student_records)
        elif choice == '5':
            print("Cảm ơn bạn đã sử dụng hệ thống!")
            break
        else:
            print("Lựa chọn không hợp lệ, vui lòng nhập từ 1 đến 5!")

if __name__ == "__main__":
    main()