# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'

# %%
from tqdm import tqdm
import glob, os

def detect(imgs, return_list):
    found_ids = []
    for img in imgs:
        bashCommand = "python3 detect.py --source {} "
        bashCommand = bashCommand.format(img[1])
        # print(str(bashCommand))
        
        import subprocess
        process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
        output, error = process.communicate()
        for r in rare:
            if r in str(output):
                return_list.append(img[0])
    # print(output)

if __name__ == '__main__':
    import json
    imgs = []
    with open("./response_1595959017442.json") as f:
        data = json.load(f)
    base = "../../datasets/Hotels-50K/images/train/"
    for f in data['images']:
        if f["dataset_id"] == 9:
            path = f['file_name'].split("_", 1)[1].replace("_GREY_SEG", "").replace("_", "/").replace("travel/website",'travel_website')
            imgs.append((f['id'], base+path))


    rare = ['sink', "refridgerator", "microwave", "closet"]


    
    from multiprocessing import Process
    import multiprocessing
    manager = multiprocessing.Manager()
    return_list = manager.list()
    jobs = []
    n = 10 
    import numpy
    chunks = list(numpy.array_split(numpy.array(imgs),10))

    print("Starting Threads...")
    for i in range(n):
        p = Process(target=detect, args=(chunks[0],return_list))
        jobs.append(p)
        p.start()

    print("Joining Threads")
    for proc in jobs:
        proc.join()
    print("Done")
    sorted(list(set(list(return_list))))
    with open("ids.txt", "w") as f:
        for id in return_list:
            f.write(str(id)+'\n')
