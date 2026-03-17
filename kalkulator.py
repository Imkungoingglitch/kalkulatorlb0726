x = input("masukkan angka dan opr: ")
x += "+" 
stack = []
num = ""
opr = "+"

for i in x:
    if i.isdigit():
        num += i
    elif i in "+-*/":
        val = int(num)
        if opr == "+":
            stack.append(val)
        elif opr == "-":
            stack.append(-val) 
        elif opr == "*":

            last_val = stack.pop()
            stack.append(last_val * val)
        elif opr == "/":

            last_val = stack.pop()
            stack.append(int(last_val / val))
        
        num = ""
        opr = i

print(f"Isi Stack: {stack}")
print(f"Hasil Akhir: {sum(stack)}")x = input("masukkan angka dan opr: ")
x += "+" 
stack = []
num = ""
opr = "+"

for i in x:
    if i.isdigit():
        num += i
    elif i in "+-*/":
        val = int(num)
        if opr == "+":
            stack.append(val)
        elif opr == "-":
            stack.append(-val) 
        elif opr == "*":

            last_val = stack.pop()
            stack.append(last_val * val)
        elif opr == "/":

            last_val = stack.pop()
            stack.append(int(last_val / val))
        
        num = ""
        opr = i

print(f"Isi Stack: {stack}")
print(f"Hasil Akhir: {sum(stack)}")     