
students = [
    {
        "student_id": "RA001",
        "name": "Nguyễn Văn A",
        "math_score": 8.5,
        "english_score": 7.0
    },
    {
        "student_id": "RA002",
        "name": "Trần Thị B",
        "math_score": 9.0,
        "english_score": 9.5
    }
]



def validate_score(score_input):
    """
    [Helper] Kiểm tra dữ liệu điểm đầu vào.
    Trả về True nếu là số hợp lệ từ 0 đến 10, ngược lại trả về False.
    """
    try:
        score = float(score_input)
        if 0 <= score <= 10:
            return True
        return False
    except ValueError:
        return False


def find_student_by_id(student_list, student_id):
    """
    [Helper] Tìm kiếm học viên trong danh sách dựa trên ID.
    Trả về chính Dictionary của học viên nếu thấy (Pointer), ngược lại trả về None.
    """
    for student in student_list:
        if student["student_id"] == student_id:
            return student
    return None


def get_rank(average_score):
    """
    [Helper] Nhận điểm trung bình và phân loại học lực chuẩn doanh nghiệp.
    """
    if average_score >= 8.0:
        return "Giỏi"
    elif average_score >= 6.5:
        return "Khá"
    elif average_score >= 5.0:
        return "Trung bình"
    else:
        return "Yếu"



def display_students(student_list):
    print("\n--- DANH SÁCH HỌC VIÊN ---")
    
    # Kiểm soát ranh giới bãi dữ liệu trống
    if len(student_list) == 0:
        print("Danh sách học viên hiện đang trống.")
        return

    for index, student in enumerate(student_list):
        print(f"{index + 1}. Mã: {student['student_id']} | Tên: {student['name']} | Toán: {student['math_score']} | Anh: {student['english_score']}")


def add_student(student_list):
    while True:
        student_id = input("Nhập Mã Học Viên: ").strip().upper()
        if not student_id:
            print("Mã học viên không được để trống!")
            continue
            
        # Gọi Helper kiểm tra trùng lặp
        if find_student_by_id(student_list, student_id):
            print("Mã học viên đã tồn tại, vui lòng nhập mã khác!")
        else:
            break # Mã hợp lệ và chưa tồn tại, thoát vòng lặp kiểm tra

    while True:
        name = input("Nhập Tên Học Viên: ").strip().title()
        if not name:
            print("Tên học viên không được để trống!")
        else:
            break

    while True:
        math_input = input("Nhập Điểm Toán: ").strip()
        if validate_score(math_input):
            math_score = float(math_input)
            break
        else:
            print("Điểm không hợp lệ, phải là số từ 0 đến 10")

    while True:
        english_input = input("Nhập Điểm Anh: ").strip()
        if validate_score(english_input):
            english_score = float(english_input)
            break
        else:
            print("Điểm không hợp lệ, phải là số từ 0 đến 10")

    new_student = {
        "student_id": student_id,
        "name": name,
        "math_score": math_score,
        "english_score": english_score
    }
    student_list.append(new_student)
    print("Thêm học viên thành công!")


def update_score(student_list):
    search_id = input("Nhập mã học viên cần cập nhật: ").strip().upper()
    
    found_student = find_student_by_id(student_list, search_id)
    
    if not found_student:
        print(f"Không tìm thấy học viên mang mã {search_id}!")
        return #  đẩy về Menu chính

    print(f"Tìm thấy học viên: {found_student['name']}")
    

    while True:
        math_input = input("Nhập Điểm Toán mới: ").strip()
        if validate_score(math_input):
            found_student["math_score"] = float(math_input)
            break
        else:
            print("Điểm không hợp lệ, phải là số từ 0 đến 10")

    while True:
        english_input = input("Nhập Điểm Anh mới: ").strip()
        if validate_score(english_input):
            found_student["english_score"] = float(english_input)
            break
        else:
            print("Điểm không hợp lệ, phải là số từ 0 đến 10")
            
    print("Cập nhật điểm thành công!")


def evaluate_students(student_list):
    if len(student_list) == 0:
        print("Danh sách học viên hiện đang trống.")
        return

    for student in student_list:
        
        average_score = (student["math_score"] + student["english_score"]) / 2
        
        
        rank = get_rank(average_score)
        
        print(f"Mã: {student['student_id']} | Tên: {student['name']} | ĐTB: {average_score:.2f} | Xếp loại: {rank}")


def main():
    while True:
        print("\n===== HỆ THỐNG QUẢN LÝ ĐIỂM THI RIKKEI ACADEMY =====")
        print("1. Hiển thị danh sách học viên")
        print("2. Thêm học viên mới")
        print("3. Cập nhật điểm thi theo mã học viên")
        print("4. Đánh giá học lực của toàn bộ học viên")
        print("5. Thoát chương trình")
        print("====================================================")
        
        choice = input("Mời bạn chọn chức năng (1-5): ").strip()

        
        if choice not in ['1', '2', '3', '4', '5']:
            print("Lựa chọn không hợp lệ, vui lòng nhập lại!")
            continue

        if choice == '1':
            display_students(students)
        elif choice == '2':
            add_student(students)
        elif choice == '3':
            update_score(students)
        elif choice == '4':
            evaluate_students(students)
        elif choice == '5':
            print("Cảm ơn bạn đã sử dụng hệ thống!")
            break 


if __name__ == "__main__":
    main()