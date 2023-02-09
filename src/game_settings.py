from configparser import ConfigParser
from re import match
from os import listdir


def configwrite(file: str, section: str, config: dict):
    configx = ConfigParser(strict=False)
    configx.optionxform = str
    configx.read(file)
    for i in configx[section].keys():
        try:
            configx[section][i] = config[i]
        except KeyError:
            pass
    with open(file, 'w') as f:
        configx.write(f, space_around_delimiters=False)


def overwatch(ow2path: str):
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
    configwrite(ow2path, "Render.13", render)


def fortnite(fortpath: str):
    configwrite(fortpath,
                "ScalabilityGroups",
                {'sg.ResolutionQuality': '80',
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
                 })
    configwrite(fortpath, "PerformanceMode", {'MeshQuality': '2'})


def val(valpath: str, valkey: str):
    # Getting the Key

    key = ''

    configx = ConfigParser(strict=False)
    configx.optionxform = str
    configx.read(valkey)
    for i in configx["UserInfo"].keys():
        key = configx["UserInfo"][i]

    # Finding the Files

    valpath = valpath[:len(valpath)-1]
    for f in listdir(valpath):
        if match(key, f):
            config = valpath + f + r'\Windows\GameUserSettings.ini'

    # Setting the Config

    configwrite(config,
                "ScalabilityGroups",
                {'sg.ResolutionQuality': '80',
                 'sg.ViewDistanceQuality': '0',
                 'sg.AntiAliasingQuality': '0',
                 'sg.ShadowQuality': '0',
                 'sg.PostProcessQuality': '0',
                 'sg.TextureQuality': '0',
                 'sg.EffectsQuality': '0',
                 'sg.FoliageQuality': '0',
                 'sg.ShadingQuality': '0'
                 })


def apex(apexpath: str):
    config, lines = {}, ["VideoConfig\n{"]
    videoconfig = {"setting.cl_gib_allow": "0",
                   "setting.cl_particle_fallback_base": "-1",
                   "setting.cl_particle_fallback_multiplier": "-1",
                   "setting.cl_ragdoll_maxcount": "0",
                   "setting.cl_ragdoll_self_collision": "1",
                   "setting.mat_forceaniso": "0",
                   "setting.mat_mip_linear": "0",
                   "setting.stream_memory": "2000000000",
                   "setting.mat_picmip": "4",
                   "setting.particle_cpu_level": "0",
                   "setting.r_createmodeldecals": "0",
                   "setting.r_decals": "0",
                   "setting.r_lod_switch_scale": "0.600000",
                   "setting.shadow_enable": "0",
                   "setting.shadow_depth_dimen_min": "0",
                   "setting.shadow_depth_upres_factor_max": "0",
                   "setting.shadow_maxdynamic": "4",
                   "setting.ssao_enabled": "0",
                   "setting.ssao_downsample": "3",
                   "setting.dvs_enable": "0",
                   "setting.nowindowborder": "0",
                   "setting.fullscreen": "1",
                   "setting.volumetric_lighting": "0",
                   "setting.volumetric_fog": "0",
                   "setting.mat_vsync_mode": "0",
                   "setting.mat_backbuffer_count": "1",
                   "setting.mat_antialias_mode": "0",
                   "setting.csm_enabled": "0",
                   "setting.csm_coverage": "0",
                   "setting.csm_cascade_res": "512",
                   "setting.fadeDistScale": "1.000000",
                   "setting.dvs_supersample_enable": "0",
                   "setting.new_shadow_settings": "1",
                   "setting.gamma": "0.7",
                   "setting.configversion": "7"}

    with open(apexpath, encoding="ascii") as f:
        lines = [line.strip() for line in f.readlines()]

    for line in lines:
        if line in ('\"VideoConfig\"', '{', '}'):
            continue
        key, value = [i.strip('"') for i in line.split("\t\t", 1)]
        config[key] = value

    for key in videoconfig:
        try:
            config[key] = videoconfig[key]
        except KeyError:
            pass

    for key, value in config.items():
        lines.append(f'\t"{key}"\t\t"{value}"')
    lines.append("}")
    with open(apexpath, "w", encoding="ascii") as f:
        f.write("\n".join(lines))
