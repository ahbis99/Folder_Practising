# Seçeceğiniz herhangi bir şiiri bilgisayarına .txt dosyası olarak kaydedin. Şiirin kaç dizeden oluştuğunu hesaplayın.
with open("siir.txt","r",encoding="utf8") as file:
    siir = file.readlines()
    bosluk = 0
    for i in siir:
        if i == "\n":
            bosluk +=1
dize= bosluk+1
print(f"Dize sayısı:{dize}")
# Yeni bir dosyaya her şiirdeki her dizenin ilk kelimesini yazdırın.
ilk_kelimeler = []
with open("siir.txt","r",encoding="utf8") as file:
    for i in range(1,10):
        line = file.readline()
        splitted = line.split(" ")
        if splitted[0] != "\n":
            ilk_kelimeler.append(splitted[0])
with open("ilk_kelimeler.txt","w") as f:
    for i in ilk_kelimeler:
        f.write(f"{i}\n")
