import customtkinter as ctk
from tkinter import *
from tkinter import messagebox

window = ctk.CTk()

class Apllication():
    

    def __init__(self):
        self.window = window
        self.theme()
        self.windows()
        self.window_login()
        window.mainloop()

            
    
    def theme(self):
        ctk.set_appearance_mode('dark')
        ctk.set_default_color_theme('dark-blue')

    def windows(self):
        window.geometry('700x400')
        window.title('Acompanhamento Fisico')
        window.resizable(False , False)

    
    def window_login(self):
        img = PhotoImage(file = 'imagem/207114.png')
        label_img = ctk.CTkLabel(master=window , image=img , text='',width=200,height=220)
        label_img.place(x=1 , y=80)

        label_tt = ctk.CTkLabel(master=window ,text='Acompanhe sua evolução!',
                                font=('Franklin Gothic Medium Cond',25),text_color='#ffffff').place(x=45,y=15)

        login_frame = ctk.CTkFrame(master=window , width=350 , height=396)
        login_frame.pack(side=RIGHT)


        label = ctk.CTkLabel(master=login_frame , text='Efetue seu login', font = ('Helvetica', 20), text_color= ('white'))
        label.place(x=83 , y =47)



        entry_login = ctk.CTkEntry(master=login_frame , placeholder_text='Nome de usuario',width=300 , 
                                            font=('Roboto',14)).place(x=25 , y=105)
        label1 = ctk.CTkLabel(master=login_frame , text='*Obrigatorio!',text_color='red',font=('Roboto',12)).place(x=25,y=135)

        entry_senha = ctk.CTkEntry(master=login_frame , placeholder_text='Senha',show='*',width=300 , 
                                            font=('Roboto',14)).place(x=25 , y=175)
        label2 = ctk.CTkLabel(master=login_frame , text='*Obrigatorio!',text_color='red',font=('Roboto',12)).place(x=25,y=205)

        checkbox = ctk.CTkCheckBox(master=login_frame , text='Lembrar-me de mim').place(x=25 , y =235)

        def login():
            
            msg = messagebox.showinfo(title='Confirmação de login',message="Login efetuado com sucesso.")
            pass
        login_button = ctk.CTkButton(master=login_frame , text='Login' , width=300,command=login).place(x=25 , y=285)
        
        def window_register():
            login_frame.pack_forget()
            #tela de cadastro
            register_frame = ctk.CTkFrame(master=window , width=350 , height=396)
            register_frame.pack(side=RIGHT)
            label = ctk.CTkLabel(master=register_frame , text='Faça seu cadastro', font = ('Helvetica', 20), text_color= ('white'))
            label.place(x=83 , y =5)

            span = ctk.CTkLabel(master=register_frame, text='Preencha todos os campos corretamente!',
                                font=('Robot0',13),text_color='red').place(x=25 , y=65)

            entry_user = ctk.CTkEntry(master=register_frame , placeholder_text='Nome de usuario',width=300 , 
                                            font=('Roboto',14)).place(x=25 , y=105)
            
            entry_email = ctk.CTkEntry(master=register_frame , placeholder_text='E-mail de usuario',width=300 , 
                                            font=('Roboto',14)).place(x=25 , y=145)
            
            entry_password = ctk.CTkEntry(master=register_frame , placeholder_text='Senha de usuario',width=300 , 
                                            font=('Roboto',14),show='*').place(x=25 , y=185)
            
            entry_cpassword = ctk.CTkEntry(master=register_frame , placeholder_text='Confirmar senha de usuario',width=300 , 
                                            font=('Roboto',14),show='*').place(x=25 , y=225)
            
            checkbox = ctk.CTkCheckBox(master=register_frame , text='Aceito todos os termos e politicas').place(x=25 , y =265)

            def back():
                #removendo o frame de cadastro
                register_frame.pack_forget()
                #devolvendo o frame de login
                login_frame.pack(side=RIGHT)
                
            back_button = ctk.CTkButton(master=register_frame , text='VOLTAR' , width=145,fg_color='gray',hover_color='#202020',command=back).place(x=25 , y=330)
            def save_user():
                msg = messagebox.showinfo(title='Cadastro',message='Usuario Cadastrado com sucesso.')
                pass
            save_button = ctk.CTkButton(master=register_frame , text='CADASTRAR' , width=145,fg_color='green',hover_color='#014B05',command=save_user).place(x=180 , y=330)
            

            
        register_span = ctk.CTkLabel(master=login_frame , text='Não possui uma conta?').place(x=25 , y=325)
        register_button = ctk.CTkButton(master=login_frame , text='Cadastrar' , 
                                        width=150,fg_color='green',hover_color='#2D9334',command=window_register).place(x=175 , y=325)



Apllication()






