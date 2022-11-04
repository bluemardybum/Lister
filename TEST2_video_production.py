from plot_videos import plot_video,alter_DTW_timing
from numpy import genfromtxt
import numpy as np
import os

dir_name = "/dati/openpose_data/output_demo_3d/"

for f in os.listdir(dir_name):
    data_3d = os.path.join(dir_name,f, f'{f}.csv')

    print(f'{data_3d}')
    #seq_data = genfromtxt(data_3d, delimiter='\t', dtype=np.float)
    seq_data = genfromtxt(data_3d, delimiter=' ', dtype=np.float)

    seq_splitted = np.array(np.split(seq_data, 151))
    seq_splitted = seq_splitted.transpose()

    plot_video(joints=seq_splitted,
                file_path=dir_name,
                video_name=f"{f}.mp4",
                references=None,    
                skip_frames=1,
                sequence_ID=None)
