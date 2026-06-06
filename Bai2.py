orders = [
    {"order_id": "ORD001", "items": ["Áo thun", "Quần Jean"]},
    {"order_id": "ORD002", "items": ["Váy", "Áo Khoác"]}
]

items_1 = orders[0]["items"]


orders[1]["items"].append("Giày")


orders[1]["items"].remove("Váy")

print(f"Danh sách sản phẩm của đơn hàng ORD001: {items_1}")
print(f"Chi tiết hệ thống đơn hàng sau cập nhật:{orders}")