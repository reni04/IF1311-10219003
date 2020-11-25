#episode input user

#data yang dimasukan pasti string
data = input("Masukan data : ")

print("data = ", data,",type =", type(data))

#jika kita ingin mengambil int maka 
angka = float(input("Masukan angka:"))
print("angka float = ", angka,",type =", type(angka))

angka = int(input("Masukan angka:"))
print("angka int = ", angka,",type =", type(angka))

print("data = ", angka,",type =", type(angka))

#bagaimana denngan boolean
biner = bool(int(input("Masukan nilai boolean :")))

print("data = ", biner,",type =", type(biner))
