# error handling => hata yönetimi

# Yöntem 1 -> Detaylı gösterim, belirtilen hatalar için özel mesaj.
try:
    x = int(input("x: "))
    y = int(input("y: "))

    print(x / y)
except ZeroDivisionError:
    print("y değeri için 0 girilemez.")
except ValueError:
    print("x ve y değerleri için sayısal değer girmelisiniz.")

# Yöntem 2 -> Belirtilen hatalar için aynı mesaj ama istersek hatanın ne olduğunu öğrenebiliriz.
try:
    x = int(input("x: "))
    y = int(input("y: "))

    print(x / y)
except (ZeroDivisionError, ValueError) as er:
    print("Yanlış değer girdiniz.")
    print(er)

# Yöntem 3 -> Tüm hatalar için aynı mesaj ama hatayı öğrenemeyiz.
try:
    x = int(input("x: "))
    y = int(input("y: "))

    print(x / y)
except:
    print("Yanlış değer girdiniz.")

# Yöntem 4 -> Tüm hatalar için aynı mesaj ve hatayı öğrenemeyiz.
try:
    x = int(input("x: "))
    y = int(input("y: "))

    print(x / y)
except Exception as ex:
    print("Yanlış değer girdiniz.")
    print(ex)


# Doğru bilgi girilene kadar çalışan, doğru bilgi girilince biten kod dizini:
while True:
    try:
        x = int(input("x: "))
        y = int(input("y: "))

        print(x / y)
    except:
        print("Yanlış değer girdiniz.")
    else:
        break
    finally:
        print("try - except sonlandı.")