product_prices = {
    "SP01": 250000,
    "SP02": 350000,
    "SP03": 150000
}
cart = {}

def hien_thi_gio_hang():
    
    if len(cart) == 0:
        print("Giỏ hàng đang trống.")
        return # Thoát hàm sớm nếu giỏ rỗng
        
    print("\n--- CHI TIẾT GIỎ HÀNG ---")
    for p_code, qty in cart.items():
        unit_price = product_prices[p_code]
        total_price = qty * unit_price
        print(f"Mã SP: {p_code} | Số lượng: {qty} | Đơn giá: {unit_price:,}đ | Thành tiền: {total_price:,}đ")

def them_san_pham():
    
    p_code = input("Nhập mã sản phẩm cần thêm: ").strip().upper()
    
    if p_code not in product_prices:
        print("Lỗi: Sản phẩm không tồn tại trong hệ thống!")
        return
        
    qty_str = input("Nhập số lượng muốn mua: ").strip()
    if not qty_str.isdigit() or int(qty_str) <= 0:
        print("Lỗi: Số lượng không hợp lệ!")
        return
        
    qty = int(qty_str)
    # Cộng dồn số lượng bằng .get()
    cart[p_code] = cart.get(p_code, 0) + qty
    print(f"=> Đã thêm thành công {qty} sản phẩm {p_code} vào giỏ hàng!")

def cap_nhat_so_luong():
    
    if len(cart) == 0:
        print("Giỏ hàng đang trống, không thể cập nhật.")
        return
        
    p_code = input("Nhập mã sản phẩm cần cập nhật: ").strip().upper()
    if p_code not in cart:
        print("Lỗi: Sản phẩm không có trong giỏ hàng!")
        return
        
    new_qty_str = input("Nhập số lượng mới: ").strip()
    if not new_qty_str.isdigit() or int(new_qty_str) <= 0:
        print(" Lỗi: Số lượng không hợp lệ!")
        return
        
    cart[p_code] = int(new_qty_str)
    print(f"=> Đã cập nhật số lượng của {p_code} thành {new_qty_str}!")

def xoa_san_pham():
    if len(cart) == 0:
        print(" Giỏ hàng đang trống, không thể xóa.")
        return
        
    p_code = input("Nhập mã sản phẩm cần xóa: ").strip().upper()
    if p_code not in cart:
        print(" Lỗi: Sản phẩm không có trong giỏ hàng!")
        return
        
    del cart[p_code]
    print(f"=> Đã xóa sản phẩm {p_code} khỏi giỏ hàng!")

def thanh_toan():
    if len(cart) == 0:
        print("Giỏ hàng đang trống, không có gì để thanh toán.")
        return
        
    print("\n===== HÓA ĐƠN THANH TOÁN =====")
    total_bill = 0
    for p_code, qty in cart.items():
        unit_price = product_prices[p_code]
        total_price = qty * unit_price
        total_bill += total_price
        print(f"- {p_code}: {qty} x {unit_price:,}đ = {total_price:,}đ")
        
    print("-" * 30)
    print(f"TỔNG CỘNG: {total_bill:,} VNĐ")
    print("==============================")
    
    cart.clear() # Xóa sạch giỏ hàng sau khi tính tiền xong
    print("=> Thanh toán thành công! Cảm ơn quý khách.")



def main():
    while True:
        print("="*40)
        print("        HỆ THỐNG QUẢN LÝ GIỎ HÀNG")
        print("="*40)
        print("1. Hiển thị giỏ hàng")
        print("2. Thêm sản phẩm vào giỏ")
        print("3. Cập nhật số lượng sản phẩm")
        print("4. Xóa sản phẩm khỏi giỏ")
        print("5. Thanh toán")
        print("6. Thoát chương trình")
        print("-" * 40)
        
        choice = input("Nhập lựa chọn của bạn (1-6): ").strip()
        
        
        if choice == '1':
            hien_thi_gio_hang()
        elif choice == '2':
            them_san_pham()
        elif choice == '3':
            cap_nhat_so_luong()
        elif choice == '4':
            xoa_san_pham()
        elif choice == '5':
            thanh_toan()
        elif choice == '6':
            print("Thoát chương trình. Hẹn gặp lại!")
            break
        else:
            print("Lựa chọn không hợp lệ, vui lòng nhập lại!")


main()