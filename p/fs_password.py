def password():
    user = input("User-nya = ")
    passw = input("Password-nya = ")

    username_from_db = "user"
    password_from_db = "admin"

    if user == username_from_db:
        if passw == password_from_db:
            print("Username dan password cocok")
        else:
            print("Password salah")
    else:
        print("User tidak terdaftar")
