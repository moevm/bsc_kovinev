import os
import re

from tqdm import tqdm

from utils.subprocessor import Subprocessor

start_path = '/home/alien/Desktop/git/bsc_kovinev/models'
original = '/home/alien/Desktop/git/bsc_kovinev/datasets/raw/obj/Cottage.ply'
DISTANCE_FILE = '/home/alien/Desktop/git/bsc_kovinev/benchmark/meshlab/configurations/distance.mlx'
types = ["3DF Zephyr", "Meshroom", "Pix4D", "Agisoft MetaShape"]
models = []


def generate_software(name):
    if "zephyr" in name:
        return types[0]
    if "meshroom" in name:
        return types[1]
    if "pix4d" in name:
        return types[2]
    if "agisoft_metashape" in name:
        return types[3]
    return ""


def generate_name(name):
    if 'extra_snow' in name:
        return "8Extra Snow"
    if 'med_show' in name or 'med_snow' in name:
        return "7Medium Snow"
    if 'med_far' in name:
        return "5Medium Distance"
    if 'extra_far' in name:
        return "6Far Distance"
    if 'extra_dark' in name:
        return "4Extra Dark"
    if 'med_dark' in name:
        return "3Medium Dark"
    if 'original' in name:
        return "0Original"
    if '720x540' in name:
        return "1720x540"
    if '320x240' in name:
        return "2320x240"
    return name


def get_parent(file):
    from pathlib import Path
    return str(Path(file).parent).split('/')[-1]


result = []


def _toFloat(v):
    return float(v.replace(',', '.'))


def callback_distance(input):
    regex = re.compile(r"min : ([\d,]+)\s+max ([\d,]+)\s+mean : ([\d,]+)\s+RMS : ([\d,]+)")
    res = re.findall(regex, input["output"])
    if res:
        result.append({
            "min": _toFloat(res[0][0]),
            "max": _toFloat(res[0][1]),
            "mean": _toFloat(res[0][2]),
            "RMS": _toFloat(res[0][3]),
        })


for dirpath, dnames, fnames in os.walk(start_path):
    for f in fnames:
        if f.endswith(".ply"):
            name = os.path.join(dirpath, f)
            models.append({
                "software": generate_software(name),
                "name": name
            })

models_new = []
for model in tqdm(models):
    result = []
    model_name = model["name"]
    cmd = f"meshlabserver -i {model_name} -i {original} -s {DISTANCE_FILE}"
    Subprocessor().run(cmd, callback_distance)
    models_new.append({
        "software": model["software"],
        "name": model_name,
        "result": result
    })

models = models_new


def generate_head():
    return "| Software\t| Name\t| Max\t| Mean\t| RMS\t|\n|---|---|---|---|---|"


def generate_table(model):
    s = ''
    for m in model:
        s += f"|{m['software']}\t|{m['name'][1:]}\t|"
        for e in m["result"][:1]:
            s += f"{e['max']}\t|{e['mean']}\t|{e['RMS']}\t|"
        s += '\n'
    return s


for type in types:
    models_filtered = list(filter(lambda x: x['software'] == type, models))
    a = []
    for m in models_filtered:
        m["name"] = generate_name(get_parent(m['name']))
        a.append(m)


    print(type)
    print()
    print(generate_head())
    print(generate_table(sorted(a, key=lambda x: x['name'])))
    print()
