import sys

grade_book = [
    {"id": "SV01", "name": "Nguyễn Văn A", "info": (8.5, 7.0)},
    {"id": "SV02", "name": "Trần Thị B", "info": (6.0, 9.0)}
]


def display_grades(book):
    
    if len(book) == 0:
        print("Danh sách lớp hiện đang trống.")
        return
        
    print("\n--- BẢNG ĐIỂM HỌC SINH ---")
    print(f"{'Mã SV':<6} | {'Tên Học Sinh':<18} | {'Điểm Toán':<9} | {'Điểm Anh':<8} | {'ĐTB'}")
    print("-" * 65)
    
    for student in book:
        st_id = student["id"]
        st_name = student["name"]
        
        math_score, english_score = student["info"]
        
        avg_score = (math_score + english_score) / 2
        
        print(f"{st_id:<6} | {st_name:<18} | {math_score:<9} | {english_score:<8} | {avg_score:.2f}")
    print("-" * 65)

def add_student(book):
    
    st_id = input("Nhập mã học sinh mới: ").strip().upper()
    
    for student in book:
        if student["id"] == st_id:
            print(f"Lỗi: Mã học sinh {st_id} đã tồn tại! Vui lòng nhập mã khác.")
            return
            
    st_name = input("Nhập tên học sinh: ").strip().title()
    
    try:
        math_score = float(input("Nhập điểm Toán: ").strip())
        english_score = float(input("Nhập điểm Anh: ").strip())
        
        if not (0 <= math_score <= 10 and 0 <= english_score <= 10):
            print("Điểm số phải nằm trong khoảng từ 0 đến 10.")
            return
            
        new_student = {
            "id": st_id,
            "name": st_name,
            "info": (math_score, english_score) # TẠO TUPLE MỚI
        }
        book.append(new_student)
        print(f"Thành công: Đã thêm học sinh {st_id} vào hệ thống!")
        
    except ValueError:
        print(" Điểm số phải là một con số hợp lệ!")

def update_scores(book):
    
    st_id = input("Nhập mã học sinh cần cập nhật: ").strip().upper()
    
    target_student = None
    for student in book:
        if student["id"] == st_id:
            target_student = student
            break
            
    if target_student is None:
        print(f" Không tìm thấy hồ sơ mang mã {st_id}.")
        return
        
    try:
        new_math = float(input("Nhập điểm Toán mới: ").strip())
        new_english = float(input("Nhập điểm Anh mới: ").strip())
        
        if not (0 <= new_math <= 10 and 0 <= new_english <= 10):
            print("[!] Lỗi: Điểm số phải nằm trong khoảng từ 0 đến 10.")
            return
            
        target_student["info"] = (new_math, new_english)
        print(f"Thành công: Đã cập nhật điểm cho học sinh {st_id}!")
        
    except ValueError:
        print(" Điểm số phải là một con số hợp lệ!")

def delete_student(book):
    
    st_id = input("Nhập mã học sinh cần xóa: ").strip().upper()
    
    target_index = -1
    for i in range(len(book)):
        if book[i]["id"] == st_id:
            target_index = i
            break
            
    if target_index != -1:
        del book[target_index]
        print(f"Thành công: Đã xóa hồ sơ học sinh {st_id} khỏi hệ thống!")
    else:
        print(f" Không tìm thấy hồ sơ mang mã {st_id} để xóa.")


def main():
    while True:
        print("\n=== HỆ THỐNG QUẢN LÝ ĐIỂM SỐ ===")
        print("1. Xem bảng điểm học sinh")
        print("2. Thêm hồ sơ học sinh mới")
        print("3. Cập nhật điểm số")
        print("4. Xóa hồ sơ học sinh")
        print("5. Thoát chương trình")
        print("================================")
        
        choice = input("Chọn chức năng (1-5): ").strip()
        
        if choice == '1':
            display_grades(grade_book)
        elif choice == '2':
            add_student(grade_book)
        elif choice == '3':
            update_scores(grade_book)
        elif choice == '4':
            delete_student(grade_book)
        elif choice == '5':
            print("Cảm ơn bạn đã sử dụng hệ thống. Hẹn gặp lại!")
            break
        else:
            print("[!] Lựa chọn không hợp lệ, vui lòng nhập lại.")

if __name__ == "__main__":
    main()