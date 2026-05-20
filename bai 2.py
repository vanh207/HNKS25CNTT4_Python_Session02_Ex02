""" 
    Phân tích lỗi: 
    - Luồng thuộc thi:
    Cho người dùng nhập tuổi và nhập cân nậng
    sau đó check điều kiện nếu tuổi >= 18 hoặc cân nặng phải lớn hơn hoặc bằng 50
    thì in đủ điều kiện để đi hến máu
    -- Lỗi:
        + điều lỗi xảy ra khi dùng toán tử OR thì khi một người có cân nặng nhẹ nhưng tuổi hợp lý
        thì vẫn sẽ được 
        ==> Từ đó gây ra lỗi
    phân biệt and và or
        + And: khi đúng khi mà  chỉ khi cả 2 đúng
        + Or: đúng khi 1 trong 2 đúng
    sửa lỗi
"""

print("---  BLOOD  DONOR SCREENING SYSTEM ---")
donor_age = int(input("Enter donor's age: "))
donor_weight = float(input("Enter donor's weight (kg): "))

if donor_age >= 18 and donor_weight >= 50:
    print("Result: ELIGIBLE. Please proceed to the blood donation room")
else:
    print("Result: NOT ELIGIBLE. Thank you for your interest")

