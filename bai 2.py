# Phân tích lỗi:
# Toán tử logic bị dùng sai
# Vấn đề: Dùng or thay vì and — chỉ cần một trong hai điều kiện đúng là đủ điều kiện, không đúng với yêu cầu nghiệp vụ.
# -- Sửa lỗi:
print("--- BLOOD DONOR SCREENING SYSTEM ---")
donor_age    = int(float(input("Enter donor's age: ")))
donor_weight = float(input("Enter donor's weight (kg): "))

# Kiểm tra từng điều kiện riêng lẻ
age_ok = donor_age >= 18
weight_ok = donor_weight >= 50

# Hệ thống kiểm tra điều kiện hiến máu
if age_ok and weight_ok:                          # sửa "or" -> "and"
    print("Result: ELIGIBLE. Please proceed to the blood donation room.")
else:
    # Nêu rõ lý do không đủ điều kiện
    reasons = []
    if not age_ok:
        reasons.append(f"tuổi {donor_age} < 18")
    if not weight_ok:
        reasons.append(f"cân nặng {donor_weight} kg < 50 kg")
    print(f"Result: NOT ELIGIBLE. Lý do: {', '.join(reasons)}.")