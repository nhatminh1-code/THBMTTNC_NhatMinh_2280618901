print("Nhap cac dong van ban (nhap 'done' de ket thuc):")
lines = []
while True:
    line = input()
    if line.lower() == 'done':
        break
    lines.append(line.upper())
print("\nCac dong van ban sau khi chuyen doi:")
for line in lines:
    print(line.upper())