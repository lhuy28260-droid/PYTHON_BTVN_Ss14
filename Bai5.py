student_records = [
    {
        "student_id": "RA01",
        "name": "Nguyễn Văn Code",
        "current_points": 1500,
        "spent_points": 500,
        "refunded_points": 0,
        "multiplier": 1.0
    },
    {
        "student_id": "RA02",
        "name": "Trần Thị Bug",
        "current_points": 800,
        "spent_points": 1200,
        "refunded_points": 100,
        "multiplier": 1.5
    },
    {
        "student_id": "RA03",
        "name": "Lê Văn Fix",
        "current_points": 300,
        "spent_points": 0,
        "refunded_points": 0,
        "multiplier": 2.0
    }
]

def find_student(records, student_id):
    """Tìm kiếm học viên theo ID, trả về Dictionary (Pointer) hoặc None"""
    for student in records:
        if student["student_id"] == student_id:
            return student
    return None

def get_member_status(points):
    """Phân hạng thành viên dựa trên số dư hiện tại"""
    if points < 500:
        return "Cần tích lũy thêm"
    elif 500 <= points <= 1500:
        return "Thành viên tiềm năng"
    else:
        return "Thành viên ưu tú"

def input_positive_int(prompt_text):
    """[Bẫy 5] Ép người dùng nhập số nguyên dương (> 0)"""
    while True:
        try:
            value = int(input(prompt_text).strip())
            if value > 0:
                return value
            else:
                print("Lỗi: Yêu cầu nhập số nguyên dương hợp lệ!")
        except ValueError:
            print("Lỗi: Yêu cầu nhập số nguyên dương hợp lệ!")

def input_multiplier(prompt_text):
    while True:
        try:
            value = float(input(prompt_text).strip())
            if 1.0 <= value <= 3.0:
                return value
            else:
                print("Hệ số nhân không hợp lệ. Chỉ chấp nhận số từ 1.0 đến 3.0")
        except ValueError:
            print("Hệ số nhân không hợp lệ. Chỉ chấp nhận số từ 1.0 đến 3.0")


def display_statements(records):
    """Chức năng 1: Hiển thị sao kê điểm số"""
    print("\n--- SAO KÊ ĐIỂM SỐ ---")
    if len(records) == 0:
        print("Hệ thống chưa có dữ liệu học viên.")
        return

    for i, student in enumerate(records):
        status = get_member_status(student["current_points"])
        print(f"{i+1}. Mã: {student['student_id']} | Tên: {student['name']} | Hiện có: {student['current_points']} | Đã tiêu: {student['spent_points']} | Hoàn trả: {student['refunded_points']} | Hệ số: x{student['multiplier']} | Trạng thái: {status}")
    print("-" * 30)

def redeem_rewards(records):
    """Chức năng 2: Đổi điểm lấy phần thưởng"""
    print("\n--- ĐỔI ĐIỂM LẤY PHẦN THƯỞNG ---")
    s_id = input("Nhập mã học viên đổi quà: ").strip().upper()
    student = find_student(records, s_id)

    if not student:
        print("Không tìm thấy hồ sơ học viên!")
        return

    points_to_spend = input_positive_int("Nhập số điểm cần tiêu: ")

    if points_to_spend > student["current_points"]:
        print("Số dư điểm không đủ để thực hiện giao dịch!")
        return

    # Thực hiện giao dịch: Trừ ví hiện tại, cộng vào ví đã tiêu
    student["current_points"] -= points_to_spend
    student["spent_points"] += points_to_spend

    print(f">> Giao dịch thành công! '{student['name']}' đã tiêu {points_to_spend} điểm. Số dư còn lại: {student['current_points']} điểm.")

def appeal_score(records):
    """Chức năng 3: Phúc khảo bài thi (Hoàn điểm)"""
    print("--- HOÀN ĐIỂM / PHÚC KHẢO ---")
    s_id = input("Nhập mã học viên cần phúc khảo: ").strip().upper()
    student = find_student(records, s_id)

    if not student:
        print("Không tìm thấy hồ sơ học viên!")
        return

    points_to_refund = input_positive_int("Nhập số điểm cần hoàn: ")

    
    if points_to_refund > student["spent_points"]:
        print("Không thể hoàn số điểm lớn hơn tổng điểm đã tiêu!")
        return

    # Thực hiện hoàn tiền: Trừ số đã tiêu, cộng lại ví hiện hành và ghi nhận vào lịch sử hoàn trả
    student["spent_points"] -= points_to_refund
    student["current_points"] += points_to_refund
    student["refunded_points"] += points_to_refund

    print(f">> Hoàn điểm thành công! '{student['name']}' được cộng lại {points_to_refund} điểm.")

def activate_multiplier(records):
    """Chức năng 4: Kích hoạt hệ số nhân điểm"""
    print("\n--- KÍCH HOẠT HỆ SỐ NHÂN ĐIỂM ---")
    s_id = input("Nhập mã học viên nhận hệ số: ").strip().upper()
    student = find_student(records, s_id)

    if not student:
        print("Không tìm thấy hồ sơ học viên!")
        return

    new_multiplier = input_multiplier("Nhập hệ số nhân mới (1.0 - 3.0): ")
    
    student["multiplier"] = new_multiplier
    print(f">> Đã kích hoạt hệ số x{new_multiplier} cho học viên '{student['name']}'.")

def grade_assignment(records):
    print("--- CHẤM BÀI / THÊM ĐIỂM ---")
    s_id = input("Nhập mã học viên vừa nộp bài: ").strip().upper()
    student = find_student(records, s_id)

    if not student:
        print("Không tìm thấy hồ sơ học viên!")
        return

    base_points = input_positive_int("Nhập số điểm gốc đạt được: ")
    
    # Tính toán điểm thực nhận dựa trên hệ số nhân
    actual_points = int(base_points * student["multiplier"])
    
    # Cộng điểm vào tài khoản
    student["current_points"] += actual_points
    
    print(f">> Hệ số hiện tại của '{student['name']}' là x{student['multiplier']}. Điểm thực nhận: {actual_points}.")
    print(f">> Đã cộng {actual_points} điểm vào tài khoản!")



def main():
    while True:
        print("\n===== HỆ THỐNG NGÂN HÀNG ĐIỂM SỐ RIKKEI ACADEMY =====")
        print("1. Hiển thị sao kê điểm số")
        print("2. Đổi điểm lấy phần thưởng")
        print("3. Phúc khảo bài thi (Hoàn điểm)")
        print("4. Kích hoạt (Hệ số nhân điểm)")
        print("5. Chấm bài (thêm điểm)")
        print("6. Thoát chương trình")
        print("=======================================================")
        
        choice = input("Chọn chức năng (1-6): ").strip()

        if choice == '1':
            display_statements(student_records)
        elif choice == '2':
            redeem_rewards(student_records)
        elif choice == '3':
            appeal_score(student_records)
        elif choice == '4':
            activate_multiplier(student_records)
        elif choice == '5':
            grade_assignment(student_records)
        elif choice == '6':
            print("Chào tạm biệt và kết thúc vòng lặp.")
            break
        else:
            print("Lựa chọn không hợp lệ, vui lòng nhập lại")

if __name__ == "__main__":
    main()