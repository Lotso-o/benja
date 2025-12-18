import bcrypt

incoming_pasword = input("ingrese su contraseña: ").encode("UTF-8")
salt = bcrypt.gensalt(rounds=12)

hashed_pasword = bcrypt.hashpw(password=incoming_pasword,salt=salt)

print("contraseña hasheada",hashed_pasword)

confirm_pasword = input("ingresa nuevamente la contraseña").encode("UTF-8")
if bcrypt.checkpw(confirm_pasword, hashed_pasword ):
    print
else:
    print("contraseña incorrecta")


