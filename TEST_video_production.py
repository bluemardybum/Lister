from plot_videos import plot_video,alter_DTW_timing
from numpy import genfromtxt
import numpy as np
import os

dir_name = "/dati/openpose_data/output_demo_3d_NO_NOISE/"


for f in os.listdir(dir_name):
    data_3d = os.path.join(dir_name,f, f'{f}.csv')

    seq_data = genfromtxt(data_3d, delimiter='\t', dtype=np.float)
    mask = np.all(np.isnan(seq_data), axis=0)
    print(f'for {f} there are {np.sum(mask)} nan \n{mask}')
    #mask = np.all(np.isnan(seq_data), axis=1)
    filtered_data = np.nan_to_num(seq_data, nan=0.0)

    #filtered_data = seq_data[:, ~mask]
    #print(f' filtered_data shape: {filtered_data.shape}')
    max_val = filtered_data.max()
    min_val = filtered_data.min()

    #norm_seq_data = (filtered_data - min_val)/ (max_val - min_val)
    norm_seq_data = filtered_data
    print(f' norm_seq_data shape: {norm_seq_data.shape}')
    #print(f'{seq_data.shape}')
    #print(f'{norm_seq_data}')

    plot_video(joints=norm_seq_data,
                file_path=os.path.join(dir_name, f),
                video_name=f"{f}.mp4",
                references=None,    
                skip_frames=1,
                sequence_ID=None)
