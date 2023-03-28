import mysql.connector
from mysql.connector import errorcode

def CheckDatabase():
    status = False

    try:
        cnx = mysql.connector.connect(user='root', password='', host='localhost', database='contact_manager')
        #print("[MYSQL] Connected to database Successfully!")
        status = True
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("[MYSQL] Something is wrong with your user name or password")
            status = False
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("[MYSQL] Database does not exist")
            status = False
        else:
            print(err)
    else:
        cnx.close()

    return status

def LoginSql(email):

    if CheckDatabase():
        cnx = mysql.connector.connect(user='root', password='', host='localhost', database='contact_manager')
        cursor = cnx.cursor()
        query = ("SELECT * FROM user_accounts WHERE email = %s")
        cursor.execute(query, (email,))
        result = cursor.fetchone()
        cursor.close()
        cnx.close()
        return result
    else:
        print("[MYSQL] Error connecting to database")
        return None

def Register(email, password, name, lastname):
    if CheckDatabase():
        cnx = mysql.connector.connect(user='root', password='', host='localhost', database='contact_manager')
        cursor = cnx.cursor()
        query = ("SELECT * FROM user_accounts WHERE email = %s")
        queryInsert = ("INSERT INTO user_accounts(email, name, lastname, password) VALUES(%s, %s, %s, %s)")
        cursor.execute(query, (email,))
        result = cursor.fetchone()

        if result == None:
            cursor.execute(queryInsert, (email, name, lastname, password))
            cnx.commit()
            status = True
        else:
            status = False
        cursor.close()
        cnx.close()
        return status
    else:
        print("[MYSQL] Error connecting to database")
        return False

def AddContact(id, name, lastname, number, birthdate):
    if CheckDatabase():
        cnx = mysql.connector.connect(user='root', password='', host='localhost', database='contact_manager')
        cursor = cnx.cursor()
        query = ("INSERT INTO contacts(id_owner, name, lastname, number, birthday) VALUES(%s, %s, %s, %s, %s)")
        cursor.execute(query, (id, name, lastname, number, birthdate))
        cnx.commit()
        cursor.close()
        cnx.close()
    else:
        print("[MYSQL] Error connecting to database")

def GetContacts(id):
    if CheckDatabase():
        cnx = mysql.connector.connect(user='root', password='', host='localhost', database='contact_manager')
        cursor = cnx.cursor()
        query = ("SELECT * FROM contacts WHERE id_owner = %s ORDER BY name ASC")
        cursor.execute(query, (id,))
        result = cursor.fetchall()
        cursor.close()
        cnx.close()
        return result
    else:
        print("[MYSQL] Error connecting to database")
        return None

def GetContact(id):
    if CheckDatabase():
        cnx = mysql.connector.connect(user='root', password='', host='localhost', database='contact_manager')
        cursor = cnx.cursor()
        query = ("SELECT * FROM contacts WHERE id = %s")
        cursor.execute(query, (id,))
        result = cursor.fetchone()
        cursor.close()
        cnx.close()
        return result
    else:
        print("[MYSQL] Error connecting to database")
        return None

def UpdateContact(id, name, lastname, number, birthdate):
    if CheckDatabase():
        cnx = mysql.connector.connect(user='root', password='', host='localhost', database='contact_manager')
        cursor = cnx.cursor()
        query = ("UPDATE contacts SET name = %s, lastname = %s, number = %s, birthday = %s WHERE id = %s")
        cursor.execute(query, (name, lastname, number, birthdate, id))
        cnx.commit()
        cursor.close()
        cnx.close()
    else:
        print("[MYSQL] Error connecting to database")

def DeleteContact(id):
    if CheckDatabase():
        cnx = mysql.connector.connect(user='root', password='', host='localhost', database='contact_manager')
        cursor = cnx.cursor()
        query = ("DELETE FROM contacts WHERE id = %s")
        cursor.execute(query, (id,))
        cnx.commit()
        cursor.close()
        cnx.close()
    else:
        print("[MYSQL] Error connecting to database")

def GetUsers():
    if CheckDatabase():
        cnx = mysql.connector.connect(user='root', password='', host='localhost', database='contact_manager')
        cursor = cnx.cursor()
        query = ("SELECT * FROM user_accounts")
        cursor.execute(query)
        result = cursor.fetchall()
        cursor.close()
        cnx.close()
        return result
    else:
        print("[MYSQL] Error connecting to database")
        return None

def GetNotes(id_owner, id_contact):
    if CheckDatabase():
        cnx = mysql.connector.connect(user='root', password='', host='localhost', database='contact_manager')
        cursor = cnx.cursor()
        query = ("SELECT * FROM notes_contact WHERE id_owner = %s AND id_contact = %s")
        cursor.execute(query, (id_owner, id_contact))
        result = cursor.fetchall()
        cursor.close()
        cnx.close()
        return result
    else:
        print("[MYSQL] Error connecting to database")
        return None

def AddNote(id_owner, id_contact, title, content):
    if CheckDatabase():
        cnx = mysql.connector.connect(user='root', password='', host='localhost', database='contact_manager')
        cursor = cnx.cursor()
        query = ("INSERT INTO notes_contact(id_owner, id_contact, title, content) VALUES(%s, %s, %s, %s)")
        cursor.execute(query, (id_owner, id_contact, title, content))
        cnx.commit()
        cursor.close()
        cnx.close()
    else:
        print("[MYSQL] Error connecting to database")

def DeleteNote(id):
    if CheckDatabase():
        cnx = mysql.connector.connect(user='root', password='', host='localhost', database='contact_manager')
        cursor = cnx.cursor()
        query = ("DELETE FROM notes_contact WHERE id = %s")
        cursor.execute(query, (id,))
        cnx.commit()
        cursor.close()
        cnx.close()
    else:
        print("[MYSQL] Error connecting to database")

def GetNoteById(id):
    if CheckDatabase():
        cnx = mysql.connector.connect(user='root', password='', host='localhost', database='contact_manager')
        cursor = cnx.cursor()
        query = ("SELECT * FROM notes_contact WHERE id = %s")
        cursor.execute(query, (id,))
        result = cursor.fetchone()
        cursor.close()
        cnx.close()
        return result
    else:
        print("[MYSQL] Error connecting to database")
        return None

def UpdateNoteById(id, title, content):
    if CheckDatabase():
        cnx = mysql.connector.connect(user='root', password='', host='localhost', database='contact_manager')
        cursor = cnx.cursor()
        query = ("UPDATE notes_contact SET title = %s, content = %s WHERE id = %s")
        cursor.execute(query, (title, content, id))
        cnx.commit()
        cursor.close()
        cnx.close()
    else:
        print("[MYSQL] Error connecting to database")