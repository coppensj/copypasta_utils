import gif
import matplotlib.pyplot as plt
import numpy as np

@gif.frame
def gif_wave_plot(t):
    x = np.linspace(0, 2, 1000)
    y = np.sin(2 * np.pi * (x - 0.01 * t))
    plt.figure(figsize=(5, 3), dpi=100)
    plt.plot(x, y, color='red')

@gif.frame
def gif_scatter_plot(data):
    plt.figure(figsize=(5, 3), dpi=100)
    plt.scatter(data[0], data[1])
    plt.xlim((0, 100))
    plt.ylim((0, 100))

def create_gif(plot, data, nframes, name):
    frames = []
    for i in range(nframes):
        frame = plot(data[i])
        frames.append(frame.copy()) #.copy() addition is a temporary fix until PIL is updated
    gif.save(frames, f"{name}.gif", duration=100)

@gif.frame
def gif_scatter_subplots(idx, X, Y, Z):
    fig = plt.figure(figsize=(10,5), dpi=200)
    fig.suptitle(idx, fontsize=20)
    ax0 = fig.add_subplot(1, 2, 1) 
    ax1 = fig.add_subplot(1, 2, 2) 
  
    for x, y in zip(X, Y):
        ax0.scatter(x, y, color='b')
    ax0.scatter(X[-1], Y[-1], color='r')
    ax0.set_xlabel('x', size=20)
    ax0.set_ylabel('y', size=20)
    ax0.set_xlim(0, 100)
    ax0.set_ylim(0, 100)
    
    for y, z in zip(Y, Z):
        ax1.scatter(y, z, color='b')
    ax1.scatter(Y[-1], Z[-1], color='r')
    ax1.set_xlabel('y', size=20)
    ax1.set_ylabel('z', size=20)
    ax1.set_xlim(0, 100)
    ax1.set_ylim(0, 100)

def create_subplot_gif(TX, TY, TZ, nframes):
    frames = []
    for i in range(nframes):
        frame = gif_scatter_subplots(i, TX[0:i+1], TY[0:i+1], TZ[0:i+1])
        frames.append(frame.copy()) #.copy() addition is a temporary fix until PIL is updated
    gif.save(frames, f"subplots_example.gif", duration=100)

if __name__ == "__main__":
    from random import randint
    
    # # Scatter example
    # nframes = 50
    # data = []
    # for i in range(nframes):
    #     x = [randint(0, 100) for _ in range(10)]
    #     y = [randint(0, 100) for _ in range(10)]
    #     data.append((x, y))
    # create_gif(gif_scatter_plot, data, nframes, "scatter_example")

    # # Wave plot example
    # nframes = 50
    # times = [i for i in range(nframes)]
    # create_gif(gif_wave_plot, times, nframes, "wave_example")
    
    # Subplots example
    nframes = 50
    TX = []
    TY = []
    TZ = []
    for i in range(nframes):
        TX.append([randint(0, 100) for _ in range(10)])
        TY.append([randint(0, 100) for _ in range(10)])
        TZ.append([randint(0, 100) for _ in range(10)])
    create_subplot_gif(TX, TY, TZ, nframes)
