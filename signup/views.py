from django.shortcuts import render
import mysql.connector as sql

fn = ''
ln = ''
s = ''
em = ''
pwd = ''

def signaction(request):
    global fn, ln, s, em, pwd

    message = ""
    email_error = "" 

    if request.method == "POST":
        m = sql.connect(host="localhost", user="root", passwd="Nomysql#123", database="squapl")
        cursor = m.cursor()
        d = request.POST

        for key, value in d.items():
            if key == "first_name":
                fn = value
            if key == "last_name":
                ln = value
            if key == "sex":
                s = value
            if key == "email":
                em = value

            if key == "password":
                pwd = value

        # Check if the email is provided
        if not em:
            email_error = "Email is required"
        else:
            # Check if the email already exists in the database
            cursor.execute("SELECT * FROM users WHERE email = %s", (em,))
            existing_user = cursor.fetchone()

            if existing_user:
                email_error = "Email is already in use. Choose a different email."
            else:
                # Proceed with the database insertion
                c = "INSERT INTO users VALUES('{}', '{}', '{}', '{}', '{}')".format(fn, ln, s, em, pwd)
                cursor.execute(c)
                m.commit()

                # Set the success message
                message = "Signup successful!"

    return render(request, 'signup_page.html', {'message': message, 'email_error': email_error})
