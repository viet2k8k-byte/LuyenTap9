n = input("Nhập một số bất kỳ: ")
total = 0
for ch in n:
    if ch.isdigit():
        total += int(ch)
print(f"Tổng các chữ số là : {total}")