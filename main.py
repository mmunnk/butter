import os, customtkinter, tkinter, configparser, re
from stat import S_IREAD, S_IRGRP, S_IROTH, S_IWUSR
from PIL import Image, ImageTk

# Paths

homedir = os.path.expanduser('~')
apexpath = homedir + r'\Saved Games\Respawn\Apex\local\videoconfig.txt'

valpath = homedir + r'\AppData\Local\VALORANT\Saved\Config\\'
valkey = homedir + r'\AppData\Local\VALORANT\Saved\Config\Windows\RiotLocalMachine.ini'
config = ''

fortpath = homedir + r'\AppData\Local\FortniteGame\Saved\Config\WindowsClient\GameUserSettings.ini'


# Checking if the Paths Exist

installed = []

if os.path.exists(apexpath) == True:
    installed.append('Apex')

if os.path.exists(valkey) == True:
    installed.append('Valorant')

if os.path.exists(fortpath) == True:
    installed.append('Fortnite')

if os.path.exists(homedir + '\OneDrive\Documents\Overwatch\Settings\Settings_v0.ini'):
    ow2path = homedir + '\OneDrive\Documents\Overwatch\Settings\Settings_v0.ini'
    installed.append('Overwatch 2')
elif os.path.exists(homedir + '\Documents\Overwatch\Settings\Settings_v0.ini'):
    ow2path = ow2path = homedir + '\Documents\Overwatch\Settings\Settings_v0.ini'

# Replace Line Function

def replace_line(file_name, line_num, text):
    with open(file_name) as f:
        lines = f.readlines()
    lines[line_num - 1] = text + '\n'

    with open(file_name, 'w') as f:
        for line in lines:
            f.write(line)


# Game Scripts

def overwatch():
    render = {'AADetail': '"0"',
'AnisotropicFiltering': '"0"',
'DirectionalShadowDetail': '"1"',
'DynamicRenderScale': '"0"',
'EffectsQuality': '"1"',
'FrameRateCap': '"0"',
'GFXPresetLevel': '"1"',
'HighQualityUpsample': '"0"',
'LightQuality': '"0"',
'LocalFogDetail': '"3"',
'LocalReflections': '"0"',
'MaxAnisotropy': '"1"',
'MaxEffectsAnisotropy': '"1"',
'MaxExtraQualityAnisotropy': '"1"',
'MaxWorldScale': '"100.000000"',
'MinWorldScale': '"75.000000"',
'ModelQuality': '"1"',
'ReflexMode': '"1"',
'RefractionDetail': '"0"',
'RenderBrightness': '"0.080000"',
'ShaderQuality': '"1"',
'ShowFPSCounter': '"1"',
'SimpleDirectionalShadows': '"1"',
'SoundQuality': '"1"',
'SSAODetail': '"0"',
'SSLRDetailLevel': '"0"',
'TextureDetail': '"1"',
'UseCustomFrameRates': '"1"',
'UseCustomWorldScale': '"1"',
'VerticalSyncEnabled': '"0"',
'WindowedFullscreen': '"0"',
'WindowMode': '"0"'
    }

    skipped = 0
    os.chmod(ow2path, S_IWUSR | S_IREAD)

    configx = configparser.ConfigParser(strict=False)
    configx.optionxform = str
    configx.read(ow2path)
    for i in configx["Render.13"].keys():
        try: configx["Render.13"][i] = render[i]

        except KeyError:
            skipped = i
    with open(ow2path, 'w') as f:
        configx.write(f, space_around_delimiters=False)


def fortnite():

    # Setting the Config

    scalabilitygroups = {'sg.ResolutionQuality': '80',
               'sg.ViewDistanceQuality': '1',
               'sg.AntiAliasingQuality': '0',
               'sg.ShadowQuality': '0',
               'sg.PostProcessQuality': '0',
               'sg.TextureQuality': '0',
               'sg.EffectsQuality': '0',
               'sg.FoliageQuality': '0',
               'sg.ShadingQuality': '0',
               'sg.GlobalIlluminationQuality': '0',
               'sg.ReflectionQuality': '0'
                }

    performancemode = {'MeshQuality': '2'}

    os.chmod(fortpath, S_IWUSR | S_IREAD)

    # Changing the Config

    configx = configparser.ConfigParser(strict=False)
    configx.optionxform = str
    configx.read(fortpath)
    for i in configx["ScalabilityGroups"].keys():
        configx["ScalabilityGroups"][i] = scalabilitygroups[i]
    with open(fortpath, 'w') as f:
        configx.write(f, space_around_delimiters=False)

    configx = configparser.ConfigParser(strict=False)
    configx.optionxform = str
    configx.read(fortpath)
    for i in configx["PerformanceMode"].keys():
        configx["PerformanceMode"][i] = performancemode[i]
    with open(fortpath, 'w') as f:
        configx.write(f, space_around_delimiters=False)

    # Making read Only

    os.chmod(fortpath, S_IREAD | S_IRGRP | S_IROTH)


def val():
    global valpath
    global config

    # Getting the Key

    key = ''

    configx = configparser.ConfigParser(strict=False)
    configx.optionxform = str
    configx.read(valkey)
    for i in configx["UserInfo"].keys():
        key = configx["UserInfo"][i]

    # Finding the Files

    valpath = valpath[:len(valpath)-1]
    for f in os.listdir(valpath):
        if re.match(key, f):
            config = valpath + f + r'\Windows\GameUserSettings.ini'

    os.chmod(config, S_IWUSR | S_IREAD)

    # Setting the Config

    scalabilitygroups = {'sg.ResolutionQuality': '80',
               'sg.ViewDistanceQuality': '0',
               'sg.AntiAliasingQuality': '0',
               'sg.ShadowQuality': '0',
               'sg.PostProcessQuality': '0',
               'sg.TextureQuality': '0',
               'sg.EffectsQuality': '0',
               'sg.FoliageQuality': '0',
               'sg.ShadingQuality': '0'
               }

    # Changing the Config

    configx = configparser.ConfigParser(strict=False)
    configx.optionxform = str
    configx.read(config)
    for i in configx["ScalabilityGroups"].keys():
        configx["ScalabilityGroups"][i] = scalabilitygroups[i]
    with open(config, 'w') as f:
        configx.write(f, space_around_delimiters=False)

    # Making Read Only

    os.chmod(config, S_IREAD | S_IRGRP | S_IROTH)


def apex():
    # Opening, Reading, Saving

    os.chmod(apexpath, S_IWUSR | S_IREAD)

    with open(apexpath, 'r') as f:
        lines = f.readlines()
        saveline1 = lines[27 - 1]
        saveline2 = lines[28 - 1]

    # Replacing

    with open(apexpath, 'w') as f:
        f.write(r'''"VideoConfig"
{
    "setting.cl_gib_allow"		"0"
    "setting.cl_particle_fallback_base"		"-1"
    "setting.cl_particle_fallback_multiplier"		"-1"
    "setting.cl_ragdoll_maxcount"		"0"
    "setting.cl_ragdoll_self_collision"		"1"
    "setting.mat_forceaniso"		"0"
    "setting.mat_mip_linear"		"0"
    "setting.stream_memory"		"2000000000"
    "setting.mat_picmip"		"4"
    "setting.particle_cpu_level"		"0"
    "setting.r_createmodeldecals"		"0"
    "setting.r_decals"		"0"
    "setting.r_lod_switch_scale"		"0.600000"
    "setting.shadow_enable"		"0"
    "setting.shadow_depth_dimen_min"		"0"
    "setting.shadow_depth_upres_factor_max"		"0"
    "setting.shadow_maxdynamic"		"4"
    "setting.ssao_enabled"		"0"
    "setting.ssao_downsample"		"3"
    "setting.dvs_enable"		"0"
    "setting.dvs_gpuframetime_min"		"15000"
    "setting.dvs_gpuframetime_max"		"16500"
    "setting.nowindowborder"		"0"
    "setting.fullscreen"		"1"
    "setting.defaultres"		"1920"
    "setting.defaultresheight"		"1080"
    "setting.volumetric_lighting"		"0"
    "setting.volumetric_fog"		"0"
    "setting.mat_vsync_mode"		"0"
    "setting.mat_backbuffer_count"		"1"
    "setting.mat_antialias_mode"		"0"
    "setting.csm_enabled"		"0"
    "setting.csm_coverage"		"0"
    "setting.csm_cascade_res"		"512"
    "setting.fadeDistScale"		"1.000000"
    "setting.dvs_supersample_enable"		"0"
    "setting.new_shadow_settings"		"1"
    "setting.gamma"		"0.7"
    "setting.configversion"		"7"
}''')

    # Correcting

    lines = open(apexpath, 'r').readlines()
    lines[27 - 1] = saveline1
    out = open(apexpath, 'w')
    out.writelines(lines)
    out.close()

    lines = open(apexpath, 'r').readlines()
    lines[28 - 1] = saveline2
    out = open(apexpath, 'w')
    out.writelines(lines)
    out.close()

    # Making Read-Only

    os.chmod(apexpath, S_IREAD | S_IRGRP | S_IROTH)

# GUI

customtkinter.set_appearance_mode('dark')
customtkinter.set_default_color_theme('dark-blue')

root = customtkinter.CTk()
root.title('butter.exe')
root.geometry('450x350')

ico = Image.open('assets/logo.png')
photo = ImageTk.PhotoImage(ico)
root.wm_iconphoto(False, photo)

# Frames

frame = customtkinter.CTkFrame(master=root, width=300, height=50, corner_radius=10)
frame.pack(pady=10, padx=20, fill="x")

frame2 = customtkinter.CTkFrame(master=root, width=300, height=400, corner_radius=10)
frame2.pack(pady=10, padx=20, fill="both", expand=True)

# Window

def optimise():
    if chosen[(len(chosen))-1] == 'Apex':
        apex()
    elif chosen[(len(chosen))-1] == 'Valorant':
        val()
    elif chosen[(len(chosen))-1] == 'Fortnite':
        fortnite()
    elif chosen[(len(chosen))-1] == 'Overwatch 2':
        overwatch()

# Define

chosen = []

def optionmenu_callback(choice):
    chosen.append(choice)


# Image

my_image = customtkinter.CTkImage(Image.open(r"assets\butter.png"),
                                  size=(250,60))

button1 = customtkinter.CTkButton(frame, text='',image=my_image, fg_color='#F8D038', hover_color='#F8D038', border_color='#e5e5e5', anchor=tkinter.CENTER)
button1.pack(padx=20, pady=60, anchor=tkinter.CENTER)

# Dropdown

selected = customtkinter.StringVar(value='Select Game')

combobox = customtkinter.CTkComboBox(master=frame2,values=installed,command=optionmenu_callback,variable=selected)
combobox.pack(padx=20, pady=10)

# Button

button = customtkinter.CTkButton(master=frame2, text="Optimise", fg_color='#3F3F3F', hover_color='#2B2B2B',command=optimise)
button.pack(padx=20, pady=10)

# Run

root.mainloop()
