# -*- coding: utf-8 -*-
"""
Created on 2024-05-26 16:43:21

@author: Boris Jobs, Chairman of FrameX Inc.

Our mission is as same as xAi's, 'Understand the Universe'.

AI that benefits all humanity is all you need.
"""

import torch
import _wode_functions as cz

def show_heatmaps(matrices, xlabel, ylabel, titles=None, figsize=(2.5, 2.5),
                  cmap='Reds'):
    """显示矩阵热图"""
    cz.use_svg_display()
    num_rows, num_cols = matrices.shape[0], matrices.shape[1]
    fig, axes = cz.plt.subplots(num_rows, num_cols, figsize=figsize,
                                 sharex=True, sharey=True, squeeze=False)
    for i, (row_axes, row_matrices) in enumerate(zip(axes, matrices)):
        for j, (ax, matrix) in enumerate(zip(row_axes, row_matrices)):
            pcm = ax.imshow(matrix.detach().numpy(), cmap=cmap)
            if i == num_rows - 1:
                ax.set_xlabel(xlabel)
            if j == 0:
                ax.set_ylabel(ylabel)
            if titles:
                ax.set_title(titles[j])
    fig.colorbar(pcm, ax=axes, shrink=0.6);

if __name__ == '__main__':
    attention_weights = torch.eye(10).reshape((1, 1, 10, 10))
    show_heatmaps(attention_weights, xlabel='Keys', ylabel='Queries')