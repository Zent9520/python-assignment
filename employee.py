employ = [
    {
      "id": 1,
      "name": "Nguyen Van Chung",
      "position": "Inter",
      "skill" : ("Python","C")#kiểu tuple
    },
    {
        "id": 2,
        "name": "Le Thi Lanh",
        "position": "Dev",
        "skill": ("C#","C+")
    },
    {
        "id": 3,
        "name": "Tran Van Duy",
        "position": "Director",
        "skill": ("Soft Skill","React","JavaScript")
    }
]


#Chuyển dict về list
list1 = list(employ)



# Hàm thêm mới nhân viên
def new_employ():
    em_id = int(input("Nhập id: "))
    namee = str(input("Nhập tên: "))
    position = input("Nhập vị trí: ")
    skill = input("Nhập kĩ năng (cách nhau bằng dấu phẩy): ")

    # Lưu skill dưới dạng set
    skillss = {s.strip() for s in skill.split(",")}

    new_emp = {
        "id": em_id,
        "name": namee,
        "position": position,
        "skill": skillss   
    }
    list1.append(new_emp)
    print(" Đã thêm:", new_emp)


# Hàm lấy dữ liệu theo id
def get_id(em_id):
    try:
        for emp in list1:
            if emp["id"] == em_id:
                print("Nhân viên tìm được:", emp)
                return emp
        raise ValueError(f"Không tìm thấy ID: {em_id}")
    except Exception as e:   #exeption là bắt tất cả lỗi 
        print(e)
        
    
    


# Hàm cập nhật kỹ năng nhân viên cũ
def update_skill(em_id):
    emp = get_id(em_id)
    if not emp:
        print(" Không tìm thấy nhân viên")
        return
    
    # Ép tuple -> set (tạm thời để update)
    current_skills = set(emp["skill"])
    
    skill_input = input("Nhập kỹ năng mới (cách nhau bằng dấu phẩy): ")
    new_skills = {s.strip() for s in skill_input.split(",")}
    
    current_skills.update(new_skills)
    
    # Chuyển lại tuple khi lưu
    emp["skill"] = tuple(current_skills)
    
    print(f" Kỹ năng mới của {emp['name']}: {emp['skill']}")

