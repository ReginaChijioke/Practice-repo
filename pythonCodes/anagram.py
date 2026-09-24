str1 = "Lis ten"
str2 = "Sil ent"
str1 = str1.replace(" ","").upper()
str2 = str2.replace(" ","").upper()

if sorted(str1) == sorted(str2):
    print("True")
else:
    print("False")