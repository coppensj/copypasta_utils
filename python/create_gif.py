import gif
import matplotlib.pyplot as plt

@gif.frame
def gif_scatter_plot(data):
    plt.figure(figsize=(5, 3), dpi=100)
    plt.scatter(data[0], data[1])
    plt.xlim((0, 100))
    plt.ylim((0, 100))

def create_gif(data, plot, nframes):
    frames = []
    for i in range(nframes):
        frame = plot(data[i])
        frames.append(frame)
    gif.save(frames, "example.gif", duration=100)

if __name__ == "__main__":
    from random import randint

    nframes = 50
    data = []
    for i in range(nframes):
        x = [randint(0, 100) for _ in range(10)]
        y = [randint(0, 100) for _ in range(10)]
        data.append((x, y))

    create_gif(data, gif_scatter_plot, nframes)
