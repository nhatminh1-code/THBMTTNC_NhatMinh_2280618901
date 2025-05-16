def dao_nguoc_chuoi(chuoi):
    return chuoi[::-1]

input_string = input("Nhập một chuỗi ký tự: ")
reversed_string = dao_nguoc_chuoi(input_string)
print("Chuỗi sau khi đảo ngược:", reversed_string)