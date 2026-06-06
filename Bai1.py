products = {
    "LAP001": {"name": "Laptop Dell", "price": 15000},
    "LAP002": {"name": "Laptop HP", "price": 12000}
}

# 1. Lấy danh sách mã sản phẩm (Sử dụng keys() thay vì value())
product_codes = products.keys()

# 2. Cập nhật giá Laptop Dell 
products["LAP001"].update({"price": 16000})

# 3. Xóa hoàn toàn Laptop HP 
del products["LAP002"]

print(f"Danh sách mã sản phẩm: {product_codes}")
print(f"Thông tin Laptop Dell sau cập nhật: {products['LAP001']}")
print(f"Kho hàng sau khi xóa: {products}")