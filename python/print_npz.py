import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

def print_npz(ipath, opath, name, VMIN, VMAX):
    data = dict(np.load(ipath))
    for arr in data:
        num = [int(s) for s in arr.split('_') if s.isdigit()]
        if(num):
            savepath = f"{opath}/{num[0]:06d}_{name}.png"
        else:
            savepath = f"{opath}/{num}_{name}.png"
        print(savepath)
        plt.imsave(savepath, data[arr], cmap='gray', vmin=VMIN, vmax=VMAX)


def print_npz_and_hist(ipath, opath, name, VMIN, VMAX):
    data = np.load(INFILE)
    for d in data:
        print(name + "_" + d + ".png")
        fig, (img, hist) = plt.subplots(nrows=1, ncols=2)
        a = data[d]
        
        hist.set_xlim(VMIN, VMAX)
        sns.distplot(a[np.nonzero(a)].flatten(), ax=hist, norm_hist=True)
        sns.despine(ax=hist)
        # hist.set_ylim(0, 0.1)
        # hist.axvline(x=2885, ls='--', c='k')
        # hist.axvline(x=2942, ls='--', c='k')

        img.imshow(a, cmap='gray', vmin=VMIN, vmax=VMAX)
        
        fig.tight_layout()
        fig.set_size_inches(w=11, h=5)
        plt.savefig(opath + name + "_" + d + ".png")
        plt.close()
