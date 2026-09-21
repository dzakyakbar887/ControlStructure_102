nilai = input ("berapa skor anda?")
if int(nilai) >= 90:
    print("excellent")
elif int(nilai) >= 80:
    print("good")
elif int(nilai) >= 70:
    print("fair")
elif int(nilai) >= 60:
    print("poor")
else:
    print("fail")