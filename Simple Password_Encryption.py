print('--------Simple Password Encryption---------')
print('Nama  : Alfianri Manihuruk')
print('NIM   : 120450088')
print('Matkul: Pemograman Berbasis Fungsi')
print('-------------------------------------------')



def encrypt(pwd):
  splitpass = list(pwd)

  asciipass = list()
  for char in splitpass:
    asciichar = ord(char)
    asciipass.append(asciichar)

  encryptedpass = ""
  for num in asciipass:
    firstval = num//26 + 80
    secondval = num%26 + 80
    if firstval > secondval:
      thirdval = '-'
    else:
      thirdval = '+'

    encryptedpass = encryptedpass + chr(firstval) + chr(secondval) + thirdval


  return encryptedpass

def decrypt(pwd):
  splitpass = [pwd[i:i+3] for i in range(0, len(pwd), 3)]

  asciipass = list()
  for word in splitpass:
    firstval = ord(word[0]) - 80
    secval = ord(word[1]) - 80
    val = 26 * firstval + secval
    asciipass.append(val)

  password = ''
  for i in asciipass:
    char = chr(i)
    password = password + char

  return password
a=encrypt('anakanakcerdas2020')
b=decrypt('Sc-TV-Sc-TS+T[-Sc-TQ+TV-T[-Sf-Sc-T\-Sc-Qh-Qf-Qh-Qf-TS+Sg-Se-Sg-')
print(a)
