def calculate_final_price(price, discount, shipping_fee):
    # Tính toán theo đúng công thức
    total = price - (price * discount) + shipping_fee
    
    # [FIX LỖI 2]: Thay print() bằng return để trả kết quả về cho hệ thống tính toán tiếp
    return total

# [FIX LỖI 1]: Truyền tham số đúng thứ tự: (Giá gốc, Tỉ lệ giảm, Phí ship)
# Đơn hàng mua áo thun: Giá 100000, giảm giá 10% (0.1), phí ship 15000
order_total = calculate_final_price(100000, 0.1, 15000)

# Hệ thống cộng thêm 5000 VNĐ phí đóng gói vào tổng tiền đơn hàng
final_payment = order_total + 5000

# In kết quả cuối cùng ra màn hình
print(f"Khách hàng cần thanh toán: {final_payment}")