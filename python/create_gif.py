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
        frames.append(frame)
    gif.save(frames, f"{name}.gif", duration=100)

if __name__ == "__main__":
    
    # scatter example
    from random import randint
    nframes = 50
    data = []
    for i in range(nframes):
        x = [randint(0, 100) for _ in range(10)]
        y = [randint(0, 100) for _ in range(10)]
        data.append((x, y))
    create_gif(gif_scatter_plot, data, nframes, "scatter_example")

    # wave plot example
    times = [i for i in range(nframes)]
    create_gif(gif_wave_plot, times, nframes, "wave_example")
