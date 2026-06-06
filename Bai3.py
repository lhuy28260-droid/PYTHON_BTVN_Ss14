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
    """Kiểm tra điểm số đầu vào có phải là số từ 0 đến 10 hay không"""
    try:
        score = float(score_input)
        if 0 <= score <= 10:
            return True
        return False
    except ValueError:
        return False

def find_student_by_id(student_list, student_id):
    """Tìm kiếm học viên theo ID, trả về Dictionary nếu có, ngược lại trả về None"""
    for student in student_list:
        if student["student_id"] == student_id:
            return student
    return None

def get_rank(average_score):
    """Trả về chuỗi xếp loại dựa trên điểm trung bình"""
    if average_score >= 8.0:
        return "Giỏi"
    elif average_score >= 6.5:
        return "Khá"
    elif average_score >= 5.0:
        return "Trung bình"
    else:
        return "Yếu"


def display_students(student_list):
    """Chức năng 1: Hiển thị danh sách học viên"""
    print("\n--- DANH SÁCH HỌC VIÊN ---")
    if len(student_list) == 0:
        print("Danh sách học viên hiện đang trống.")
        return

    for i, student in enumerate(student_list):
        print(f"{i+1}. Mã: {student['student_id']} | Tên: {student['name']} | Toán: {student['math_score']} | Anh: {student['english_score']}")

def add_student(student_list):
    """Chức năng 2: Thêm học viên mới"""
    print("\n--- THÊM HỌC VIÊN MỚI ---")
    
    # [Bẫy 1]: Kiểm tra trùng mã
    while True:
        s_id = input("Mã Học Viên: ").strip().upper()
        if find_student_by_id(student_list, s_id):
            print("Mã học viên đã tồn tại, vui lòng nhập mã khác!")
        else:
            break

    # [Bẫy 4]: Kiểm tra tên rỗng và chuẩn hóa
    while True:
        name = input("Tên Học viên: ").strip().title()
        if not name:
            print("Tên học viên không được để trống!")
        else:
            break

    # [Bẫy 2]: Kiểm tra điểm Toán
    while True:
        math_input = input("Nhập Điểm Toán: ").strip()
        if validate_score(math_input):
            math_score = float(math_input)
            break
        else:
            print("Điểm không hợp lệ, phải là số từ 0 đến 10")

    # [Bẫy 2]: Kiểm tra điểm Anh
    while True:
        eng_input = input("Nhập Điểm Anh: ").strip()
        if validate_score(eng_input):
            eng_score = float(eng_input)
            break
        else:
            print("Điểm không hợp lệ, phải là số từ 0 đến 10")

    # Lưu dữ liệu
    new_student = {
        "student_id": s_id,
        "name": name,
        "math_score": math_score,
        "english_score": eng_score
    }
    student_list.append(new_student)
    print("Thêm học viên thành công!")

def update_score(student_list):
    """Chức năng 3: Cập nhật điểm thi"""
    print("\n--- CẬP NHẬT ĐIỂM THI ---")
    s_id = input("Nhập mã học viên cần cập nhật: ").strip().upper()
    
    # Tái sử dụng hàm phụ trợ để tìm kiếm
    found_student = find_student_by_id(student_list, s_id)
    
    if not found_student:
        print(f"Không tìm thấy học viên mang mã {s_id}!")
        return

    print(f"Đang cập nhật điểm cho HV: {found_student['name']}")
    
    # Tái sử dụng hàm phụ trợ để nhập điểm Toán mới
    while True:
        math_input = input("Nhập Điểm Toán mới: ").strip()
        if validate_score(math_input):
            found_student["math_score"] = float(math_input)
            break
        else:
            print("Điểm không hợp lệ, phải là số từ 0 đến 10")

    # Tái sử dụng hàm phụ trợ để nhập điểm Anh mới
    while True:
        eng_input = input("Nhập Điểm Anh mới: ").strip()
        if validate_score(eng_input):
            found_student["english_score"] = float(eng_input)
            break
        else:
            print("Điểm không hợp lệ, phải là số từ 0 đến 10")
            
    print("Cập nhật điểm thành công!")

def evaluate_students(student_list):
    """Chức năng 4: Đánh giá học lực"""
    print("\n--- ĐÁNH GIÁ HỌC LỰC ---")
    if len(student_list) == 0:
        print("Danh sách học viên hiện đang trống.")
        return

    for student in student_list:
        avg_score = (student["math_score"] + student["english_score"]) / 2
        rank = get_rank(avg_score)
        print(f"Mã: {student['student_id']} | Tên: {student['name']} | ĐTB: {avg_score:.2f} | Xếp loại: {rank}")


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