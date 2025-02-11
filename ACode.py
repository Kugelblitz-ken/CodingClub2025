print("\t\t\t\tWELCOME")
print("\t\t\t   1.Penentu Grade \n\t\t\t   2.Penentu Dewasa")
a=input("\t\tPilih pilih sistem yang anda inginkan  : ")
if a =="1":
    print ("\n\n\t\t Selamat datang di penentu grade!")
    Nilai=int(input("\t\t\tMasukkan nilai anda  : "))
    if Nilai >=90:
        grade="A"
    elif Nilai >=70:
        grade="B"
    elif Nilai >=50:
        grade="C"
    else:
        grade="Tidak Lulus"
    print("\t\tnilai kamu adalah ",Nilai,"dan grade kamu adalah "+grade+"")
elif a =="2":
    print ("\n\n\t\t Selamat datang di penentu dewasa!")
    umur=int(input("\t\t\tMasukkan umur anda  : "))
    if umur >=18:
        status="dewasa"
    else:
        status="Remaja"
    print("\t\tUmur kamu adalah",umur,"dan status kamu adalah "+status+"")
else:
    print("system not found")