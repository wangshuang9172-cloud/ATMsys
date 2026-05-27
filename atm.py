import customtkinter as ctk
#全局样式设置
ctk.set_appearance_mode('System')
ctk.set_default_color_theme('blue')
class ATMClient(ctk.CTk)
    def __init__(self):
        # 初始化主窗口
        app = ctk.CTk()
        app.title('ATM')
        app.geometry('500x500')
        app.resizable(False, False)

#3.添加注册，登录，取款

