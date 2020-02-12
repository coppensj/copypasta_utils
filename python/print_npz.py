import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

def load_npz_data(ipath):
    return dict(np.load(ipath))

def print_npz(data, opath, name, VMIN, VMAX):
    for arr in data:
        num = [int(s) for s in arr.split('_') if s.isdigit()]
        if(num):
            savepath = f"{opath}/{num[0]:06d}_{name}.png"
        else:
            savepath = f"{opath}/{num}_{name}.png"
        print(savepath)
        plt.imsave(savepath, data[arr], cmap='gray', vmin=VMIN, vmax=VMAX)

