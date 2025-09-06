from employee import list1, new_employ, get_id, update_skill,update_employee_skill
#Gọi thực thi các câu lệnh trong employee.py
#in danh sách dữ liệu
print("Danh sách dữ liệu:")
for e in list1:
    print(e)


#thêm nhân viên
print("Thêm nhân viên mới")
new_employ()


#tìm kiếm theo id
print("Tìm kiếm theo id")
emp = get_id(6)
print("Kết quả:", emp)


#cập nhật skill
print("Cập nhật kỹ năng cho id=2:")
update_skill(2)

print("\nCập nhật kỹ năng cho id=2 (bằng hàm mới):")
update_employee_skill(2, "Python")