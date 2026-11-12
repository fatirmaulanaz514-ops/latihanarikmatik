#operator 
#Operator Aritmatika

a = 5
b = 3
C = 8
a = 7
b = 6
C = 4
penjumlahan = a + b + C
print(f"Hasil penjumlahan {a} + {b} + {C} = {penjumlahan} ")
sisabagi = a % b
print(f"sisa bagi {a} mod {b} = {sisabagi}")
perkalian = C * a
print(f"Hasil perkalian {C} * {a} = {perkalian}")
pembagian = b / C
print(f"hasil pembagian {b} / {C} = {pembagian}")
pengurangan = a - b
print(f"hasil pengurangan {a} - {b} = {pengurangan}")
perpangkatan = a ** b
print(f"hasil perpangkatan {a} ** {b} = {perpangkatan}")
pembagianbulat = a // b
print(f"pemabagian bulat {a} // {b} = {pembagianbulat}")

# Operator Assigment

a += 2
b -= 3
C *= 7
print(a)
print(b)
print(C)

# Operator Perbandingan
perbandingan = a >= b #144 >=2 true 

x = 5
y = 7
banding = x <= y

print(x != y)
print(perbandingan)

# Operator logika And
print("===Operator Logika====")
opAnd = a >= b and x <= y and x !=y #false
opOR = perbandingan or banding or x != y #true
opNot = not opAnd
print(opAnd)
print(opOR)
print(opNot)
