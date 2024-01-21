from django.shortcuts import render
import mysql.connector as sql

em = ''
pwd = ''

def loginaction(request):
    global em, pwd
    if request.method == "POST":
        m = sql.connect(host="localhost", user="root", passwd="Mysql#123", database="squapl")
        cursor = m.cursor()
        d = request.POST
        for key, value in d.items():
            if key == "email":
                em = value
            if key == "password":
                pwd = value

        c = "SELECT * FROM users WHERE email='{}' and password='{}'".format(em, pwd)  # Added table name 'users'
        cursor.execute(c)
        t = tuple(cursor.fetchall())
        if not t:
            return render(request, "error.html")
        else:
            # Corrected the render function to redirect to a URL
            return render(request, "squapl.html") 
        
    return render(request, 'login_page.html')
