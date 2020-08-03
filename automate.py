# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'

# %%
from tqdm import tqdm
import glob, os


# %%
file_list = [f for i,f in enumerate(glob.glob("../../datasets/Hotels-50K/images/train/**/*.jpg", recursive=True)) if i <100]
for root, dirs, files in os.walk("../../datasets/Hotels-50K/images/train/"):
    path = root.split(os.sep)
    print((len(path) - 1) * '---', os.path.basename(root))
    for file in files:
        print(len(path) * '---', file)
# file_list = []
# for i, f in tqdm(enumerate(glob.glob("../../datasets/Hotels-50K/images/train/**/*.jpg", recursive=True))):
#     if i > 100:
#         break
#     file_list.append(f)



# %%
for img in file_list:
    bashCommand = "python3 detect.py --source {} "
    bashCommand = bashCommand.format(img)
    print(str(bashCommand))

    # print(bashCommand)
    import subprocess
    process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
    output, error = process.communicate()
    if "bed" in output:
        print("this works")
    print(output)


# %%



