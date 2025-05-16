so_gio_lam = float(input("Nhập số giờ làm việc trong tuần: "))
muc_luong_theo_gio = float(input("Nhập mức lương theo giờ: "))
thue_suat = float(input("Nhập thuế suất (ví dụ: 0.1 cho 10%): "))
tong_luong = so_gio_lam * muc_luong_theo_gio
thue = tong_luong * thue_suat
luong_thuc_nhan = tong_luong - thue
print("Tổng lương trước thuế:", tong_luong)
print("Thuế:", thue)
print("Lương thực nhận:", luong_thuc_nhan)
# Yêu cầu người dùng nhập số giờ làm việc, mức lương theo giờ và thuế suất
# Tính tổng lương trước thuế
# Tính thuế
# Tính lương thực nhận
# In kết quả