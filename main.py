import customtkinter
import tkinter
from plyer import notification
from connection import *
from aledev_lib import *
from contact import *

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

current_user = None

class App(customtkinter.CTk, Contact):

    def add_contact_to_database(self):
        name = self.entry_name_add_contact.get()
        lastname = self.entry_lastname_add_contact.get()
        number = self.entry_number_add_contact.get()
        birthdate = self.entry_birthdate_add_contact.get()

        if name != "" and lastname != "" and number != "" and birthdate != "":
            if Check_Birthday(birthdate):
                AddContact(current_user.id, name, lastname, number, birthdate)
                self.window_add_contact.destroy()
                self.list_contacts()
                notification.notify(
                    title="Contacto agregado",
                    message="El contacto ha sido agregado correctamente",
                    app_icon="img/LogBlanko.ico",
                    timeout=5,
                )
            else:
                print("Invalid birthday")
                notification.notify(
                    title="Error",
                    message="Fecha de nacimiento invalida",
                    app_icon="img/LogBlanko.ico",
                    timeout=5,
                )


    def add_contact(self):
        try:
            self.window_view_contact.withdraw()
            self.window_edit_contact.withdraw()
            self.window_delete_contact.withdraw()
            self.window_add_contact.withdraw()
        except:
            pass

        self.window_add_contact = customtkinter.CTk()
        self.window_add_contact.title("Add Contact - by AleDev")
        self.window_add_contact.geometry(f"{350}x{550}")
        self.window_add_contact.resizable(False, False)

        self.frame_add_contact = customtkinter.CTkFrame(self.window_add_contact, width=300, height=600)
        self.frame_add_contact.pack(pady=10, padx=10, fill="x")

        self.label_title_add_contact = customtkinter.CTkLabel(self.frame_add_contact, text="Add Contact", font=("Arial", 20, "bold"))
        self.label_title_add_contact.pack(pady=10, padx=10, fill="x")

        self.label_name_add_contact = customtkinter.CTkLabel(self.frame_add_contact, text="Name", font=("Arial", 12))
        self.label_name_add_contact.pack(pady=10, padx=10, fill="x")

        self.entry_name_add_contact = customtkinter.CTkEntry(self.frame_add_contact, width=30)
        self.entry_name_add_contact.pack(pady=10, padx=10, fill="x")

        self.label_lastname_add_contact = customtkinter.CTkLabel(self.frame_add_contact, text="Last Name", font=("Arial", 12))
        self.label_lastname_add_contact.pack(pady=10, padx=10, fill="x")

        self.entry_lastname_add_contact = customtkinter.CTkEntry(self.frame_add_contact, width=30)
        self.entry_lastname_add_contact.pack(pady=10, padx=10, fill="x")

        self.label_number_add_contact = customtkinter.CTkLabel(self.frame_add_contact, text="Number", font=("Arial", 12))
        self.label_number_add_contact.pack(pady=10, padx=10, fill="x")

        self.entry_number_add_contact = customtkinter.CTkEntry(self.frame_add_contact, width=30)
        self.entry_number_add_contact.pack(pady=10, padx=10, fill="x")

        self.label_birthdate_add_contact = customtkinter.CTkLabel(self.frame_add_contact, text="Birthdate [Format (day/month/year)]", font=("Arial", 12))
        self.label_birthdate_add_contact.pack(pady=10, padx=10, fill="x")

        self.entry_birthdate_add_contact = customtkinter.CTkEntry(self.frame_add_contact, width=30)
        self.entry_birthdate_add_contact.pack(pady=10, padx=10, fill="x")

        self.button_add_add_contact = customtkinter.CTkButton(self.frame_add_contact, text="Add", width=10, command=self.add_contact_to_database)
        self.button_add_add_contact.pack(pady=10, padx=10, fill="x")

        self.button_cancel_add_contact = customtkinter.CTkButton(self.frame_add_contact, text="Cancel", width=10, command=self.window_add_contact.withdraw)
        self.button_cancel_add_contact.pack(pady=10, padx=10, fill="x")

        # limpiamos los campos de texto
        self.entry_name_add_contact.delete(0, tkinter.END)
        self.entry_lastname_add_contact.delete(0, tkinter.END)
        self.entry_number_add_contact.delete(0, tkinter.END)
        self.entry_birthdate_add_contact.delete(0, tkinter.END)

        self.window_add_contact.mainloop()

    def edit_contact_to_database(self, id):
        print(id)
        name = self.entry_name_edit_contact.get()
        lastname = self.entry_lastname_edit_contact.get()
        number = self.entry_number_edit_contact.get()
        birthdate = self.entry_birthdate_edit_contact.get()

        print(name, lastname, number, birthdate)

        if name != "" and lastname != "" and number != "" and birthdate != "":
            if Check_Birthday(birthdate):
                UpdateContact(id, name, lastname, number, birthdate)
                self.window_edit_contact.destroy()
                notification.notify(
                    title="Success",
                    message="Contacto editado correctamente",
                    app_icon="img/LogBlanko.ico",
                    timeout=5,
                )
            else:
                print("Invalid birthday")
                notification.notify(
                    title="Error",
                    message="Fecha de nacimiento invalida",
                    app_icon="img/LogBlanko.ico",
                    timeout=5,
                )
        else:
            print("Empty fields")
            notification.notify(
                title="Error",
                message="Hay campos vacios",
                app_icon="img/LogBlanko.ico",
                timeout=5,
            )

        self.list_contacts()

    def delete_contact_to_database(self, id):
        DeleteContact(id)
        self.window_delete_contact.destroy()
        self.list_contacts()
        notification.notify(
            title="Success",
            message="Contacto eliminado correctamente",
            app_icon="img/LogBlanko.ico",
            timeout=5,
        )

    def delete_contact(self, id):
        try:
            self.window_view_contact.withdraw()
            self.window_edit_contact.withdraw()
            self.window_delete_contact.withdraw()
            self.window_add_contact.withdraw()
        except:
            pass

        self.window_delete_contact = customtkinter.CTk()
        self.window_delete_contact.title("Delete Contact - by AleDev")
        self.window_delete_contact.geometry(f"{350}x{220}")
        self.window_delete_contact.resizable(False, False)

        self.frame_delete_contact = customtkinter.CTkFrame(self.window_delete_contact, width=300, height=600)
        self.frame_delete_contact.pack(pady=10, padx=10, fill="x")

        self.label_title_delete_contact = customtkinter.CTkLabel(self.frame_delete_contact, text="Delete Contact", font=("Arial", 20, "bold"))
        self.label_title_delete_contact.pack(pady=10, padx=10, fill="x")

        self.label_question_delete_contact = customtkinter.CTkLabel(self.frame_delete_contact, text="Are you sure you want to delete this contact?", font=("Arial", 12))
        self.label_question_delete_contact.pack(pady=10, padx=10, fill="x")

        self.button_yes_delete_contact = customtkinter.CTkButton(self.frame_delete_contact, text="Yes", width=10, command=lambda: self.delete_contact_to_database(id))
        self.button_yes_delete_contact.pack(pady=10, padx=10, fill="x")

        self.button_no_delete_contact = customtkinter.CTkButton(self.frame_delete_contact, text="No", width=10, command=self.window_delete_contact.withdraw)
        self.button_no_delete_contact.pack(pady=10, padx=10, fill="x")

        self.window_delete_contact.mainloop()

    def edit_contact(self, info):
        try:
            self.window_view_contact.withdraw()
            self.window_edit_contact.withdraw()
            self.window_delete_contact.withdraw()
            self.window_add_contact.withdraw()
        except:
            pass

        self.window_edit_contact = customtkinter.CTk()
        self.window_edit_contact.title("Edit Contact - by AleDev")
        self.window_edit_contact.geometry(f"{350}x{550}")
        self.window_edit_contact.resizable(False, False)

        self.frame_edit_contact = customtkinter.CTkFrame(self.window_edit_contact, width=300, height=600)
        self.frame_edit_contact.pack(pady=10, padx=10, fill="x")

        self.label_title_edit_contact = customtkinter.CTkLabel(self.frame_edit_contact, text="Edit Contact", font=("Arial", 20, "bold"))
        self.label_title_edit_contact.pack(pady=10, padx=10, fill="x")

        self.label_name_edit_contact = customtkinter.CTkLabel(self.frame_edit_contact, text="Name", font=("Arial", 12))
        self.label_name_edit_contact.pack(pady=10, padx=10, fill="x")

        self.entry_name_edit_contact = customtkinter.CTkEntry(self.frame_edit_contact, width=30)
        self.entry_name_edit_contact.pack(pady=10, padx=10, fill="x")

        self.label_lastname_edit_contact = customtkinter.CTkLabel(self.frame_edit_contact, text="Last Name", font=("Arial", 12))
        self.label_lastname_edit_contact.pack(pady=10, padx=10, fill="x")

        self.entry_lastname_edit_contact = customtkinter.CTkEntry(self.frame_edit_contact, width=30)
        self.entry_lastname_edit_contact.pack(pady=10, padx=10, fill="x")

        self.label_number_edit_contact = customtkinter.CTkLabel(self.frame_edit_contact, text="Number", font=("Arial", 12))
        self.label_number_edit_contact.pack(pady=10, padx=10, fill="x")

        self.entry_number_edit_contact = customtkinter.CTkEntry(self.frame_edit_contact, width=30)
        self.entry_number_edit_contact.pack(pady=10, padx=10, fill="x")

        self.label_birthdate_edit_contact = customtkinter.CTkLabel(self.frame_edit_contact, text="Birthdate [Format (day/month/year)]", font=("Arial", 12))
        self.label_birthdate_edit_contact.pack(pady=10, padx=10, fill="x")

        self.entry_birthdate_edit_contact = customtkinter.CTkEntry(self.frame_edit_contact, width=30)
        self.entry_birthdate_edit_contact.pack(pady=10, padx=10, fill="x")

        self.button_edit_edit_contact = customtkinter.CTkButton(self.frame_edit_contact, text="Edit", width=10, command=lambda:self.edit_contact_to_database(info[0]))
        self.button_edit_edit_contact.pack(pady=10, padx=10, fill="x")

        self.button_cancel_edit_contact = customtkinter.CTkButton(self.frame_edit_contact, text="Cancel", width=10, command=self.window_edit_contact.withdraw)
        self.button_cancel_edit_contact.pack(pady=10, padx=10, fill="x")

        # limpiamos los campos de texto
        self.entry_name_edit_contact.delete(0, tkinter.END)
        self.entry_lastname_edit_contact.delete(0, tkinter.END)
        self.entry_number_edit_contact.delete(0, tkinter.END)
        self.entry_birthdate_edit_contact.delete(0, tkinter.END)

        # insertamos los datos del contacto
        self.entry_name_edit_contact.insert(0, info[2])
        self.entry_lastname_edit_contact.insert(0, info[3])
        self.entry_number_edit_contact.insert(0, info[4])
        self.entry_birthdate_edit_contact.insert(0, info[5])

        self.window_edit_contact.mainloop()

    def delete_note(self, id):
        DeleteNote(id)
        self.window_view_contact.withdraw()
        notification.notify(
            title="Success",
            message="Nota eliminada correctamente",
            app_icon="img/LogBlanko.ico",
            timeout=5,
        )

    def edit_note_sql(self, id):
        title = self.entry_title_note_edit.get()
        content = self.entry_note_edit_note.get()

        if title == "" or content == "":
            notification.notify(
                title="Error",
                message="No puedes dejar campos vacios",
                app_icon="img/LogBlanko.ico",
                timeout=5,
            )
        else:
            UpdateNoteById(id, title, content)
            self.window_edit_note.withdraw()
            notification.notify(
                title="Success",
                message="Nota editada correctamente",
                app_icon="img/LogBlanko.ico",
                timeout=5,
            )

    def edit_note(self, id):
        try:
            self.window_view_contact.withdraw()
            self.window_edit_contact.withdraw()
            self.window_delete_contact.withdraw()
            self.window_add_contact.withdraw()
            self.window_add_note.withdraw()
        except:
            pass

        self.window_edit_note = customtkinter.CTk()
        self.window_edit_note.title("Edit Note - by AleDev")
        self.window_edit_note.geometry(f"{350}x{370}")
        self.window_edit_note.resizable(False, False)

        self.frame_edit_note = customtkinter.CTkFrame(self.window_edit_note, width=300, height=600)
        self.frame_edit_note.pack(pady=10, padx=10, fill="x")

        self.label_title_edit_note = customtkinter.CTkLabel(self.frame_edit_note, text="Edit Note", font=("Arial", 20, "bold"))
        self.label_title_edit_note.pack(pady=10, padx=10, fill="x")

        self.label_title_note_edit = customtkinter.CTkLabel(self.frame_edit_note, text="Title", font=("Arial", 20, "bold"))
        self.label_title_note_edit.pack(pady=10, padx=10, fill="x")

        self.entry_title_note_edit = customtkinter.CTkEntry(self.frame_edit_note, width=30)
        self.entry_title_note_edit.pack(pady=10, padx=10, fill="x")

        self.label_content_note_edit = customtkinter.CTkLabel(self.frame_edit_note, text="Contente",font=("Arial", 20, "bold"))
        self.label_content_note_edit.pack(pady=10, padx=10, fill="x")

        self.entry_note_edit_note = customtkinter.CTkEntry(self.frame_edit_note, width=30)
        self.entry_note_edit_note.pack(pady=10, padx=10, fill="x")

        self.button_edit_note = customtkinter.CTkButton(self.frame_edit_note, text="Save", width=10, command=lambda:self.edit_note_sql(id))
        self.button_edit_note.pack(pady=10, padx=10, fill="x")

        self.button_cancel_edit_note = customtkinter.CTkButton(self.frame_edit_note, text="Cancel", width=10, command=self.window_edit_note.withdraw)
        self.button_cancel_edit_note.pack(pady=10, padx=10, fill="x")

        info = GetNoteById(id)

        self.entry_title_note_edit.delete(0, tkinter.END)
        self.entry_note_edit_note.delete(0, tkinter.END)

        self.entry_title_note_edit.insert(0, info[1])
        self.entry_note_edit_note.insert(0, info[2])

        self.window_edit_note.mainloop()

    def add_note_SQL(self, id):
        title = self.entry_title_note_add.get()
        content = self.entry_note_add_note.get()

        if title == "" or content == "":
            notification.notify(
                title="Error",
                message="No puedes dejar campos vacios",
                app_icon="img/LogBlanko.ico",
                timeout=5,
            )
        else:
            AddNote(current_user.id, id, title, content)
            # cerramos la ventana
            self.window_add_note.withdraw()
            self.view_contact(id)
            notification.notify(
                title="Success",
                message="Nota agregada correctamente",
                app_icon="img/LogBlanko.ico",
                timeout=5,
            )

    def add_note(self, id):
        try:
            self.window_view_contact.withdraw()
            self.window_edit_contact.withdraw()
            self.window_delete_contact.withdraw()
            self.window_add_contact.withdraw()
        except:
            pass

        self.window_add_note = customtkinter.CTk()
        self.window_add_note.title("Add Note - by AleDev")
        self.window_add_note.geometry(f"{350}x{370}")
        self.window_add_note.resizable(False, False)

        self.frame_add_note = customtkinter.CTkFrame(self.window_add_note, width=300, height=600)
        self.frame_add_note.pack(pady=10, padx=10, fill="x")

        self.label_title_add_note = customtkinter.CTkLabel(self.frame_add_note, text="Add Note", font=("Arial", 20, "bold"))
        self.label_title_add_note.pack(pady=10, padx=10, fill="x")

        self.label_title_note_add = customtkinter.CTkLabel(self.frame_add_note, text="Title", font=("Arial", 20, "bold"))
        self.label_title_note_add.pack(pady=10, padx=10, fill="x")

        self.entry_title_note_add = customtkinter.CTkEntry(self.frame_add_note, width=30)
        self.entry_title_note_add.pack(pady=10, padx=10, fill="x")

        self.label_content_note_add = customtkinter.CTkLabel(self.frame_add_note, text="Contente",font=("Arial", 20, "bold"))
        self.label_content_note_add.pack(pady=10, padx=10, fill="x")

        self.entry_note_add_note = customtkinter.CTkEntry(self.frame_add_note, width=30)
        self.entry_note_add_note.pack(pady=10, padx=10, fill="x")

        self.button_add_add_note = customtkinter.CTkButton(self.frame_add_note, text="Add", width=10, command=lambda:self.add_note_SQL(id))
        self.button_add_add_note.pack(pady=10, padx=10, fill="x")

        self.button_cancel_add_note = customtkinter.CTkButton(self.frame_add_note, text="Cancel", width=10, command=self.window_add_note.withdraw)
        self.button_cancel_add_note.pack(pady=10, padx=10, fill="x")

        self.window_add_note.mainloop()

    def view_contact(self, id):
        info = GetContact(id)

        try:
            self.window_view_contact.withdraw()
            self.window_edit_contact.withdraw()
            self.window_delete_contact.withdraw()
            self.window_add_contact.withdraw()
        except:
            pass

        self.window_view_contact = customtkinter.CTk()
        self.window_view_contact.title("View Contact - by AleDev")
        self.window_view_contact.geometry(f"{350}x{530}")
        self.window_view_contact.resizable(False, False)

        self.tabview = customtkinter.CTkTabview(self.window_view_contact, width=250)
        self.tabview.pack(pady=10, padx=10, fill="x")

        self.tabview.add("Info")
        self.tabview.add("Notes")
        self.tabview.tab("Info")
        self.tabview.tab("Notes")

        self.frame_view_contact = customtkinter.CTkFrame(self.tabview.tab("Info"), width=300, height=600)
        self.frame_view_contact.pack(pady=10, padx=10, fill="x")

        self.label_title_view_contact = customtkinter.CTkLabel(self.frame_view_contact, text="View Contact", font=("Arial", 20, "bold"))
        self.label_title_view_contact.pack(pady=10, padx=10, fill="x")

        self.label_name_view_contact = customtkinter.CTkLabel(self.frame_view_contact, text="Name: " + info[2], font=("Arial", 12))
        self.label_name_view_contact.pack(pady=10, padx=10, fill="x")

        self.label_lastname_view_contact = customtkinter.CTkLabel(self.frame_view_contact, text="Last Name: " + info[3], font=("Arial", 12))
        self.label_lastname_view_contact.pack(pady=10, padx=10, fill="x")

        self.label_number_view_contact = customtkinter.CTkLabel(self.frame_view_contact, text="Number: " + str(info[4]), font=("Arial", 12))
        self.label_number_view_contact.pack(pady=10, padx=10, fill="x")

        self.label_birthdate_view_contact = customtkinter.CTkLabel(self.frame_view_contact, text="Birthdate: " + str(info[5]), font=("Arial", 12))
        self.label_birthdate_view_contact.pack(pady=10, padx=10, fill="x")

        self.button_edit_view_contact = customtkinter.CTkButton(self.frame_view_contact, text="Edit", width=10, command=lambda: self.edit_contact(info))
        self.button_edit_view_contact.pack(pady=10, padx=10, fill="x")

        self.button_add_note_contact = customtkinter.CTkButton(self.frame_view_contact, text="Add note", width=10, command=lambda: self.add_note(info[0]))
        self.button_add_note_contact.pack(pady=10, padx=10, fill="x")

        self.button_delete_view_contact = customtkinter.CTkButton(self.frame_view_contact, text="Delete", width=10, command=lambda: self.delete_contact(info[0]))
        self.button_delete_view_contact.pack(pady=10, padx=10, fill="x")

        self.button_cancel_view_contact = customtkinter.CTkButton(self.frame_view_contact, text="Cancel", width=10, command=self.window_view_contact.withdraw)
        self.button_cancel_view_contact.pack(pady=10, padx=10, fill="x")

        self.frame_notes_view_contact = customtkinter.CTkFrame(self.tabview.tab("Notes"), width=300, height=600)
        self.frame_notes_view_contact.pack(pady=10, padx=10, fill="x")

        self.scrollable_list_notes = customtkinter.CTkScrollableFrame(self.frame_notes_view_contact, width=900, height=470)
        self.scrollable_list_notes.pack(side="top", fill="both", expand=True)

        self.scrollable_frame_list_notes = []

        list = GetNotes(current_user.id, id)

        for note in list:
            self.frame_list_notes = customtkinter.CTkFrame(self.scrollable_list_notes, width=900, height=100, border_color="gray", border_width=1)
            self.frame_list_notes.pack(side="top", fill="x", pady=5)

            self.label_title_list_notes = customtkinter.CTkLabel(self.frame_list_notes, text="Title: " + note[1], font=("Arial", 12))
            self.label_title_list_notes.place(x=10, y=10)

            self.label_content_list_notes = customtkinter.CTkLabel(self.frame_list_notes, text="Content: " + note[2], font=("Arial", 12))
            self.label_content_list_notes.place(x=10, y=40)

            self.button_delete_list_notes = customtkinter.CTkButton(self.frame_list_notes, text="Delete", width=10, command=lambda id=note[0]: self.delete_note(id))
            self.button_delete_list_notes.place(x=10, y=70)

            self.button_edit_list_notes = customtkinter.CTkButton(self.frame_list_notes, text="Edit", width=10, command=lambda id=note[0]: self.edit_note(id))
            self.button_edit_list_notes.place(x=65, y=70)

            self.scrollable_frame_list_notes.append(self.frame_list_notes)

        self.window_view_contact.mainloop()

    def list_contacts(self):
        list = GetContacts(current_user.id)

        for frame in self.scrollable_frame_list_contact:
            frame.destroy()

        for contact in list:
            self.frame_list_contact = customtkinter.CTkFrame(self.scrollable_list_contact, width=900, height=100, border_color="gray", border_width=1)
            self.frame_list_contact.pack(side="top", fill="x", pady=5)

            self.label_name_list_contact = customtkinter.CTkLabel(self.frame_list_contact, text="Name: " + contact[2], font=("Arial", 12))
            self.label_name_list_contact.place(x=10, y=10)

            self.label_lastname_list_contact = customtkinter.CTkLabel(self.frame_list_contact, text="Last Name: " + contact[3], font=("Arial", 12))
            self.label_lastname_list_contact.place(x=10, y=40)

            self.label_number_list_contact = customtkinter.CTkLabel(self.frame_list_contact, text="Number: " + str(contact[4]), font=("Arial", 12))
            self.label_number_list_contact.place(x=10, y=70)

            self.label_birthdate_list_contact = customtkinter.CTkLabel(self.frame_list_contact, text="Birthdate: " + str(contact[5]), font=("Arial", 12))
            self.label_birthdate_list_contact.place(x=10, y=100)

            self.button_view_list_contact = customtkinter.CTkButton(self.frame_list_contact, text="View", width=10, command=lambda id=contact[0]: self.view_contact(id))
            self.button_view_list_contact.place(x=800, y=10)

            self.scrollable_frame_list_contact.append(self.frame_list_contact)

    def logout(self):
        self.ClearLogin()
        self.window_login.deiconify()
        self.window_dashboard.withdraw()

    def list_users(self):

        try:
            self.window_add_contact.withdraw()
            self.window_view_contact.withdraw()
            self.window_delete_contact.withdraw()
            self.window_edit_contact.withdraw()
        except:
            pass

        self.window_list_users = customtkinter.CTk()
        self.window_list_users.title("List Users - by AleDev")
        self.window_list_users.geometry(f"{1200}x{600}")
        self.window_list_users.resizable(False, False)

        self.frame_list_users = customtkinter.CTkFrame(self.window_list_users, width=300, height=600)
        self.frame_list_users.pack(pady=10, padx=10, fill="x")

        self.label_title_list_users = customtkinter.CTkLabel(self.frame_list_users, text="List Users", font=("Arial", 20, "bold"))
        self.label_title_list_users.pack(pady=10, padx=10, fill="x")

        self.scrollable_list_users = customtkinter.CTkScrollableFrame(self.frame_list_users, width=300, height=600)
        self.scrollable_list_users.pack(pady=10, padx=10, fill="x")

        self.scrollable_frame_list_users = []

        self.list_users = GetUsers()

        for user in self.list_users:
            self.frame_list_users = customtkinter.CTkFrame(self.scrollable_list_users, width=300, height=100, border_color="gray", border_width=1)
            self.frame_list_users.pack(side="top", fill="x", pady=5)

            self.label_username_list_users = customtkinter.CTkLabel(self.frame_list_users, text="Email: " + user[1], font=("Arial", 12))
            self.label_username_list_users.place(x=10, y=10)

            self.label_name_list_users = customtkinter.CTkLabel(self.frame_list_users, text="Name: " + user[2], font=("Arial", 12))
            self.label_name_list_users.place(x=10, y=40)

            self.label_lastname_list_users = customtkinter.CTkLabel(self.frame_list_users, text="Last Name: " + user[3], font=("Arial", 12))
            self.label_lastname_list_users.place(x=10, y=70)

            self.scrollable_frame_list_users.append(self.frame_list_users)

        self.window_list_users.mainloop()

    def dashboard(self):
        # create window register y hide login
        self.window_dashboard = customtkinter.CTk()
        self.window_dashboard.title("Dashboard - by AleDev")
        self.window_dashboard.geometry(f"{1200}x{600}")
        self.window_dashboard.resizable(False, False)
        self.withdraw()

        try:
            self.window_login.withdraw()
            self.window_register.withdraw()
        except:
            pass

        # create sidebar frame with widgets
        self.frame_sidebar = customtkinter.CTkFrame(self.window_dashboard, width=200, height=600)
        self.frame_sidebar.place(x=0, y=0)

        # create title label in sidebar
        self.label_title_sidebar = customtkinter.CTkLabel(self.frame_sidebar, text="Contact Manager", font=("Arial", 20, "bold"))
        self.label_title_sidebar.place(x=25, y=20)

        # create add contact button in sidebar
        self.button_add_contact = customtkinter.CTkButton(self.frame_sidebar, text="Add Contact", font=("Arial", 12), command=self.add_contact)
        self.button_add_contact.place(x=30, y=100)

        # create list contacts button in sidebar
        self.button_list_contacts = customtkinter.CTkButton(self.frame_sidebar, text="List Contacts", font=("Arial", 12), command=self.list_contacts)
        self.button_list_contacts.place(x=30, y=150)

        # create button to view all users registered
        self.button_list_users = customtkinter.CTkButton(self.frame_sidebar, text="List Users", font=("Arial", 12), command=self.list_users)
        self.button_list_users.place(x=30, y=200)

        # create logout button in sidebar
        self.button_logout = customtkinter.CTkButton(self.frame_sidebar, text="Logout", font=("Arial", 12), command=self.logout)
        self.button_logout.place(x=30, y=550)

        # create main frame with widgets
        self.frame_main = customtkinter.CTkFrame(self.window_dashboard, width=1000, height=600, fg_color="transparent")
        self.frame_main.place(x=200, y=0)

        # create title label in main
        self.label_title_main = customtkinter.CTkLabel(self.frame_main, text="List Contacts", font=("Arial", 30, "bold"))
        self.label_title_main.place(x=400, y=30)

        # create frame with widgets for list contacts in main
        self.frame_list_contacts = customtkinter.CTkFrame(self.frame_main, width=900, height=470, fg_color="transparent")
        self.frame_list_contacts.place(x=50, y=100)

        # create scrollable frame
        self.scrollable_list_contact = customtkinter.CTkScrollableFrame(self.frame_list_contacts, width=900, height=470)
        self.scrollable_list_contact.pack(side="top", fill="both", expand=True)

        self.scrollable_frame_list_contact = []

        self.list_contacts()

        self.window_dashboard.mainloop()

    def ClearLogin(self):
        #limpiamos los campos de texto del login
        self.textbox_email_login.delete(0, "end")
        self.textbox_password_login.delete(0, "end")

    def ClearRegister(self):
        self.textbox_email_register.delete(0, "end")
        self.textbox_password_register.delete(0, "end")
        self.textbox_password_confirm_register.delete(0, "end")

    def login_user(self):
        email = self.textbox_email_login.get()
        password = self.textbox_password_login.get()

        if len(email) > 0 and len(password) > 0:
            result = LoginSql(email)
            if result != None:
                if check_password(password, result[4]):
                    global current_user
                    current_user = Contact(result[0], result[1], result[2], result[3], result[4])
                    self.dashboard()
                    self.window_login.destroy()
                else:
                    print("Contraseña incorrecta")
                    notification.notify(
                        title="Error",
                        message="Contraseña incorrecta",
                        app_icon="img/LogBlanko.ico",
                        timeout=5,
                    )
                    self.ClearLogin()
            else:
                notification.notify(
                    title="Error",
                    message="Usuario no encontrado",
                    app_icon="img/LogBlanko.ico",
                    timeout=5,
                )
                print("Usuario no encontrado")
                self.ClearLogin()
        else:
            print("No se permiten campos vacios")
            notification.notify(
                title="Error",
                message="No se permiten campos vacios",
                app_icon="img/LogBlanko.ico",
                timeout=5,
            )

    def register_user(self):
        email = self.textbox_email_register.get()
        name = self.textbox_name_register.get()
        lastname = self.textbox_lastname_register.get()
        password = self.textbox_password_register.get()
        password_confirm = self.textbox_password_confirm_register.get()

        if password == password_confirm:
            hashed = hash_password(password)
            if len(name) or len(lastname) > 0:
                result = Register(email, hashed, name, lastname)
                if result:
                    print("Usuario registrado correctamente")
                    notification.notify(
                        title="Registro",
                        message="Usuario registrado correctamente",
                        app_icon="img/LogBlanko.ico",
                        timeout=5,
                    )
                    self.window_login.deiconify()
                    self.window_register.destroy()
                else:
                    print("El usuario ya existe")
                    notification.notify(
                        title="Error",
                        message="El usuario ya existe",
                        app_icon="img/LogBlanko.ico",
                        timeout=5,
                    )
                    self.ClearRegister()
            else:
                print("No se permiten campos vacios")
                notification.notify(
                    title="Error",
                    message="No se permiten campos vacios",
                    app_icon="img/LogBlanko.ico",
                    timeout=5,
                )
                self.ClearRegister()
        else:
            self.ClearRegister()
            print("Las contraseñas no coinciden")
            notification.notify(
                title="Error",
                message="Las contraseñas no coinciden",
                app_icon="img/LogBlanko.ico",
                timeout=5,
            )

    def login(self):
        # create window login y hide register
        self.window_login = customtkinter.CTk()
        self.window_login.title("Login - by AleDev")
        self.window_login.geometry(f"{350}x{350}")
        self.window_login.resizable(False, False)
        self.withdraw()

        try:
            self.window_register.withdraw()
        except:
            pass

        # create widgets
        self.label_title = customtkinter.CTkLabel(self.window_login, text="Login", font=("Arial", 20, "bold"))
        self.label_title.pack(pady=10, padx=10, fill="x")

        self.label_email_login = customtkinter.CTkLabel(self.window_login, text="Email", font=("Arial", 18))
        self.label_email_login.pack(pady=10, padx=10, fill="x")

        self.textbox_email_login = customtkinter.CTkEntry(self.window_login, width=10, font=customtkinter.CTkFont(size=12, weight="bold"))
        self.textbox_email_login.pack(pady=10, padx=10, fill="x")

        self.label_password_login = customtkinter.CTkLabel(self.window_login, text="Password", font=("Arial", 18))
        self.label_password_login.pack(pady=10, padx=10, fill="x")

        self.textbox_password_login = customtkinter.CTkEntry(self.window_login, width=10, font=customtkinter.CTkFont(size=12, weight="bold"), show="*")
        self.textbox_password_login.pack(pady=10, padx=10, fill="x")

        self.button_login_login = customtkinter.CTkButton(self.window_login, text="Login", command=self.login_user)
        self.button_login_login.pack(pady=10, padx=10, fill="x")

        self.button_register_login = customtkinter.CTkButton(self.window_login, text="Register", command=self.register)
        self.button_register_login.pack(pady=10, padx=10, fill="x")

        self.window_login.mainloop()

    def register(self):
        # create window register y hide login
        self.window_register = customtkinter.CTk()
        self.window_register.title("Register - by AleDev")
        self.window_register.geometry(f"{350}x{650}")
        self.window_register.resizable(False, False)
        self.withdraw()

        try:
            self.window_login.withdraw()
        except:
            pass

        # create widgets
        self.label_title_register = customtkinter.CTkLabel(self.window_register, text="Register", font=("Arial", 20, "bold"))
        self.label_title_register.pack(pady=10, padx=10, fill="x")

        self.label_email_register = customtkinter.CTkLabel(self.window_register, text="Email", font=("Arial", 18))
        self.label_email_register.pack(pady=10, padx=10, fill="x")

        self.textbox_email_register = customtkinter.CTkEntry(self.window_register, width=10, font=customtkinter.CTkFont(size=12, weight="bold"))
        self.textbox_email_register.pack(pady=10, padx=10, fill="x")

        self.label_name_register = customtkinter.CTkLabel(self.window_register, text="Name", font=("Arial", 18))
        self.label_name_register.pack(pady=10, padx=10, fill="x")

        self.textbox_name_register = customtkinter.CTkEntry(self.window_register, width=10, font=customtkinter.CTkFont(size=12, weight="bold"))
        self.textbox_name_register.pack(pady=10, padx=10, fill="x")

        self.label_lastname_register = customtkinter.CTkLabel(self.window_register, text="Lastname", font=("Arial", 18))
        self.label_lastname_register.pack(pady=10, padx=10, fill="x")

        self.textbox_lastname_register = customtkinter.CTkEntry(self.window_register, width=10, font=customtkinter.CTkFont(size=12, weight="bold"))
        self.textbox_lastname_register.pack(pady=10, padx=10, fill="x")

        self.label_password_register = customtkinter.CTkLabel(self.window_register, text="Password", font=("Arial", 18))
        self.label_password_register.pack(pady=10, padx=10, fill="x")

        self.textbox_password_register = customtkinter.CTkEntry(self.window_register, width=10, font=customtkinter.CTkFont(size=12, weight="bold"), show="*")
        self.textbox_password_register.pack(pady=10, padx=10, fill="x")

        self.label_password_confirm_register = customtkinter.CTkLabel(self.window_register, text="Confirm Password", font=("Arial", 18))
        self.label_password_confirm_register.pack(pady=10, padx=10, fill="x")

        self.textbox_password_confirm_register = customtkinter.CTkEntry(self.window_register, width=10, font=customtkinter.CTkFont(size=12, weight="bold"), show="*")
        self.textbox_password_confirm_register.pack(pady=10, padx=10, fill="x")

        self.button_register_register = customtkinter.CTkButton(self.window_register, text="Register", command=self.register_user)
        self.button_register_register.pack(pady=10, padx=10, fill="x")

        self.button_login_register = customtkinter.CTkButton(self.window_register, text="Login", command=self.login)
        self.button_login_register.pack(pady=10, padx=10, fill="x")

        self.window_register.mainloop()

    def __init__(self):
        super().__init__()
        self.login()

if __name__ == "__main__":
    app = App()
