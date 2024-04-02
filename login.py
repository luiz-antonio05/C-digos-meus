import flet as ft
import os
import time
import threading
import json

with open('users.json', 'r', encoding="utf8") as f:
    data = json.load(f)
    USERS = data["users"]

def main(page: ft.page):
    page.title = 'Login Screen'
    page.window_width = 600
    page.window_height = 600
    page.window_resizable = False
    page.padding = 100
    page.theme_mode = 'dark'
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    def btn_click(event):
        username = name_input.value
        password = pass_input.value

        index_search = -1
        for index, user in enumerate(USERS):
            if user["username"] == username:
                #print("Usuario ", index)
                #print(user["username"])
                #print(user["password"])
                index_search = index



        if index_search != -1:
            if USERS[index_search]["password"] == password:
                dlg = ft.AlertDialog(
                    title=ft.Text('Bem vindo ' + name_input.value))
                page.dialog = dlg
                dlg.open = True
                page.update()
                time.sleep(2)
                open_documents_folder()
            else:
                dlg = ft.AlertDialog(
                    title=ft.Text('Senha incorreta.'),
                    content=ft.Text('Digite a senha correta!'))
                page.dialog= dlg
                dlg.open = True
                page.update()

        else:
            dlg = ft.AlertDialog(
                title=ft.Text('Usuário não encontrado, Tente novamente.'),
                content=ft.Text('Credenciais inválidas'))
            page.dialog= dlg
            dlg.open = True
            page.update()

    def open_documents_folder():
        documents_folder = os.path.join('C:\\Users\\luiz.antonio\\Desktop')
        if os.path.exists(documents_folder):
            os.startfile("{}".format(documents_folder))

    
    page.appbar = ft.AppBar(title=ft.Text('Login Screen'), center_title=True)
    name_input = ft.TextField(
        label='Nome', autofocus=True, hint_text='Digite seu nome')
    pass_input = ft.TextField(
        label='Senha', password=True, can_reveal_password=True)
    submit_btn = ft.ElevatedButton(
        text='Enviar', width=600, on_click=btn_click)
    page.add(name_input, pass_input, submit_btn)
    page.update()

ft.app(target=main)
