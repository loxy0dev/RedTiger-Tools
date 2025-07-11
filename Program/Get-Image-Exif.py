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
    import piexif
    import exifread
    import base64
    import os
    import tkinter
    from PIL import Image
    from tkinter import filedialog
except Exception as e:
   ErrorModule(e)

Title("Get Image Exif")

try:
    def ChooseImageFile():
        try:
            print(f"{BEFORE + current_time_hour() + AFTER} {INPUT} Enter the path to the image -> {reset}")
            image_file_types = [("Image files", "*.png;*.jpg;*.jpeg;*.gif;*.bmp;*.tiff"), ("All files", "*.*")]

            if sys.platform.startswith("win"):
                root = tkinter.Tk()
                root.iconbitmap(os.path.join(tool_path, "Img", "RedTiger_icon.ico"))
                root.withdraw()
                root.attributes('-topmost', True)
                file = filedialog.askopenfilename(parent=root, title=f"{name_tool} {version_tool} - Choose an image file", filetypes=image_file_types)
            elif sys.platform.startswith("linux"):
                file = filedialog.askopenfilename(title=f"{name_tool} {version_tool} - Choose an image file", filetypes=image_file_types)
            print(f"{BEFORE + current_time_hour() + AFTER} {INFO} File path: {white + file}")
            return file
        except:
            return input(f"{BEFORE + current_time_hour() + AFTER} {INPUT} Enter the path to the image -> {reset}")

    def CleanValue(value):
        if isinstance(value, bytes):
            try:
                return value.decode('utf-8', errors='replace')
            except:
                return base64.b64encode(value).decode('utf-8')
        elif isinstance(value, (list, tuple)):
            return ', '.join(str(v) for v in value)
        elif isinstance(value, dict):
            return {k: CleanValue(v) for k, v in value.items()}
        else:
            return value
        
    def GetAllExif(image_path):
        exif_data = {}

        try:
            exif_dict = piexif.load(image_path)
            for ifd in exif_dict:
                if isinstance(exif_dict[ifd], dict):
                    for tag in exif_dict[ifd]:
                        tag_name = piexif.TAGS[ifd].get(tag, {"name": tag})["name"]
                        raw_value = exif_dict[ifd][tag]
                        exif_data[f"{tag_name}"] = CleanValue(raw_value)
        except:
            pass

        try:
            with open(image_path, 'rb') as f:
                tags = exifread.process_file(f, details=True)
                for tag in tags:
                    label = tag.split()[-1]
                    if label not in exif_data:
                        exif_data[label] = CleanValue(str(tags[tag]))
        except:
            pass
        
        try:
            with Image.open(image_path) as img:
                width, height = img.size
                depth = len(img.getbands())
                exif_data['Dimension'] = f"{width}x{height}"
                exif_data['Width'] = width
                exif_data['Height'] = height
                exif_data['Depth'] = depth
        except Exception as e:
            exif_data["Image Error"] = str(e)

        try:
            exif_dict = piexif.load(image_path)
            for ifd in exif_dict:
                if isinstance(exif_dict[ifd], dict):
                    for tag in exif_dict[ifd]:
                        tag_name = piexif.TAGS[ifd].get(tag, {"name": tag})["name"]
                        raw_value = exif_dict[ifd][tag]
                        exif_data[f"{tag_name}"] = CleanValue(raw_value)
        except Exception as e:
            exif_data["PIEXIF_ERROR"] = str(e)

        try:
            file_stats = os.stat(image_path)
            exif_data['Name'] = os.path.basename(image_path)
            exif_data['Type'] = os.path.splitext(image_path)[1]
            exif_data['Creation date'] = time.ctime(file_stats.st_ctime)
            exif_data['Date modified'] = time.ctime(file_stats.st_mtime)
            exif_data['Attributes'] = oct(file_stats.st_mode)
            exif_data['Availability'] = 'Available' if os.access(image_path, os.R_OK) else 'Not available'
            exif_data['Offline Status'] = 'Online' if os.path.exists(image_path) else 'Offline'
        except Exception as e:
            exif_data["File Stats Error"] = str(e)
            
        if exif_data:
            max_key_length = max(len(k) for k in exif_data.keys())

            print(f"\n{white}────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────")
            for key, value in sorted(exif_data.items(), key=lambda x: x[0].lower()):
                print(f" {INFO_ADD} {key.ljust(max_key_length)} : {white + str(value)}")
                time.sleep(0.01)
            print(f"{white}────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────\n")
        else:
            print(f"{BEFORE + current_time_hour() + AFTER} {ERROR} No information found.")

    Slow(osint_banner)
    image_path = ChooseImageFile()
    print(f"{BEFORE + current_time_hour() + AFTER} {WAIT} Searching for information in the roots of the image...")
    GetAllExif(image_path)
    Continue()
    Reset()
except Exception as e:
    Error(e)