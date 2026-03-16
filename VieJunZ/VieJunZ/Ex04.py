s = input("Nhập chuỗi: ")

hoa = 0
thuong = 0
so = 0
dac_biet = 0
khoang_trang = 0
nguyen_am = 0
phu_am = 0

nguyen_am_ds = "aeiouAEIOU"

for ch in s:
    if ch.isupper():
        hoa += 1
    elif ch.islower():
        thuong += 1

    if ch.isdigit():
        so += 1
    elif ch == " ":
        khoang_trang += 1
    elif not ch.isalpha() and not ch.isdigit():
        dac_biet += 1

    if ch.isalpha():
        if ch in nguyen_am_ds:
            nguyen_am += 1
        else:
            phu_am += 1

print(f"Chữ hoa: {hoa}")
print(f"Chữ thường: {thuong}")
print(f"Chữ số: {so}")
print(f"Ký tự đặc biệt: {dac_biet}")
print(f"Khoảng trắng: {khoang_trang}")
print(f"Nguyên âm: {nguyen_am}")
print(f"Phụ âm: {phu_am}")

