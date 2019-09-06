# Copy and paste the code below to your Jupyter notebook
- You need Bokeh and Numpy to run the script below in your Jupyter Notebook 
all the helper functions can be found in the python scripts `pfdt.py` and `pf_plot.py`
- You can find the sample data files in `../data` directory

```python
from pfdt import Landmark, Control, Observation, GroundTruth
from pfdt import get_groundtruths_from_file, get_landmarks_from_file, get_observations_from_file
from pf_plot import SimpleMapPlot, SimpleVicinityPlot, VicinityPlot

from time import sleep
import numpy as np 

from bokeh.io import push_notebook, output_notebook
output_notebook()


# -----------------------
# Extract Data from given files
# -----------------------

landmarks = get_landmarks_from_file("../data/map_data.txt")
groundtruths = get_groundtruths_from_file("../data/gt_data.txt")

# If your sensors are perfect these observations per timestep
# are what your going to observe given the particular location of the vehicle at a particular time
total_groundtruth_observations = []
for i in range(1, 2444):
    file_path ='../data/observation/observations_{:06d}.txt'.format(i)
    observations = get_observations_from_file(file_path)
    total_groundtruth_observations.append(observations)


# -----------------------
# Add a little noise given the "perfect" groundtruth observations 
# -----------------------

total_noisy_observations = []
sigma = 0.3

# `current_observations` in the set of observations in a particular time
for current_observations in total_groundtruth_observations:
    
    current_noisy_observations = []
    for i_, observation in enumerate(current_observations):
        x_ = np.random.normal(observation.x, sigma, 1)[0]
        y_ = np.random.normal(observation.y, sigma, 1)[0]
        noisy_observation = Observation(i=i_, x=x_, y=y_)
        current_noisy_observations.append(noisy_observation)
    
    total_noisy_observations.append(current_noisy_observations)


# -----------------------
# Show `simplified` plot from vehicle's perspective
# if sensors were were perfect
# -----------------------

import warnings
warnings.filterwarnings('ignore')

total_points = len(total_groundtruth_observations)
vicinity_plot = SimpleVicinityPlot(total_groundtruth_observations[0])
vicinity_plot.show()

sleep(5)

for i in range(1, total_points):    
    vicinity_plot.update(total_groundtruth_observations[i])
    push_notebook()
    sleep(0.01)


# -----------------------
# Show plot from vehicle's perspective given noisy observations
# the 'ground truth' if sensors were perfect is also plotted
# -----------------------

total_points = len(total_groundtruth_observations)
vicinity_plot = VicinityPlot(total_groundtruth_observations[0], total_noisy_observations[0])
vicinity_plot.show()

sleep(5)

for i in range(1, total_points):    
    vicinity_plot.update(total_groundtruth_observations[i], total_noisy_observations[i])
    push_notebook()
    sleep(0.01)

# -----------------------
# Show `simplified` plot in global coordinates
# -----------------------

total_points = len(groundtruths)
map_plot = SimpleMapPlot(landmarks)
map_plot.show()

sleep(5)

for i in range(total_points):    
    map_plot.update(groundtruths[i])
    push_notebook()
    sleep(0.01)
```
