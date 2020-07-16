def plt_setup(width=8, height=6, borders='lb', fontsize=9):
    font = {
        'family' : 'Roboto',
        'weight' : 'light',
        'size'   : int(fontsize)
    }
    matplotlib.rc('font', **font)

    plt.figure(figsize=(float(width), float(height)))

    ax = plt.subplot(111)

    for b in ['left', 'right', 'top', 'bottom']:
        if b[0] in borders:
            ax.spines[b].set_visible(True)
            ax.spines[b].set_linewidth(.6)
        else:
            ax.spines[b].set_visible(False)

    ax.get_xaxis().tick_bottom()
    ax.get_yaxis().tick_left()
