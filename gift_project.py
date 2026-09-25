import numpy as np
import imageio.v3 as iio
from PIL import Image

filenames = ['team-pic1.png', 'team-pic2.png', 'supernovas.png']
images = []

for filename in filenames:
    frame = iio.imread(filename)

    if frame.ndim == 2:
        frame = np.stack([frame] * 3, axis=-1)
    elif frame.shape[-1] == 4:
        frame = frame[..., :3]
    elif frame.shape[-1] == 1:
        frame = frame[..., 0]

    frame = Image.fromarray(frame).convert('RGB')

    if not images:
        target_size = frame.size
    else:
        frame = frame.resize(target_size)

    images.append(np.asarray(frame))

iio.imwrite('team.gif', images, duration=500, loop=0)