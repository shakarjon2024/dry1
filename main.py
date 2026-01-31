# 1 - misol
def faktorial(n):
    natija = 1
    for i in range(1, n +1 ):
        natija *= i
    return  natija

print(faktorial(8))


# 2 - misol
def juft_yigindi(a, b):
    yigindi = 0
    for i in range(a, b + 1):
        if i % 2 == 0:
            yigindi += i
        return yigindi

print(juft_yigindi(4, 5))



# 3 - misol
def orta_arifmetik(royxat):
    eng_kichik = min(royxat)
    eng_katta = max(royxat)
    return (eng_kichik + eng_katta) / 2

sonlar = [1, 2, 3, 4, 5, 6, 7]
natija = orta_arifmetik(sonlar)
print(natija)




# 4 - misol
def umumiy_element(a, b):
    roy1 = a
    roy2 = b
    return (roy1 + roy2)

royxat1 = [1, 2, 3, 4, 5]
royxat2 = [6, 7, 8, 9]
natija = umumiy_element(royxat1, royxat2)
print(natija)
