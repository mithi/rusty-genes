
# City Generation and Algorithm Visualization Animation
- **IMPORTANT**: When running the simulation: use `debug_level = 1` to generate output `csv` file compatible with the helper scripts that you can use for algorithm visualization.

# Requirements
- Python
- Jupyter notebook or Jupyter lab
- Bokeh
- Numpy

```
$ jupyter notebook
```

You can copy the following sample codes to Jupyter notebooks
which uses `city_plot.py` and `helpers.py` in this directory.

# Sample codes for your jupyter notebook
You can try the following examples on a Jupyter Notebook


## Example 1: City Generation
- This example generates semi-random city configurations,
and saves them to files, reads those city files and plots thoses cities
- This doesn't run genetic algorithms but you might want to use it to generate
your own city configuration

```python

from helpers import write_cities_csv, read_cities_csv, random_cities, circley_random_cities, wavey_random_cities, min_max
from city_plot import CityPlot, City

def city_filename(i):
    return "../citydna/data/cities/cities" + str(i) + ".csv"

def plot_cities_from_file(cities, i):
    cities = read_cities_csv(city_filename(i))
    x1, x2, y1, y2 = min_max(cities) # get x and y ranges
    plot = CityPlot(cities, (x1 - 1.0, x2 + 1.0), (y1 - 1.0, y2 + 1.0)) # Add margins to ranges
    plot.show()


n = 20
# -----------------------------------------------
# Generate semi-random cities
# Write the cities to respective csv files
# n is the number of cities to write
# -----------------------------------------------

x1, x2, y1, y2 = 0.0, 20.0, -6.0, 6.0,
cities = random_cities(n, x1, x2, y1, y2)
write_cities_csv(cities, city_filename('X'))

# -----------------------------------------------

cities = circley_random_cities(NUMBER_OF_CITIES=n, d=5.0, noise=1.0, theta_noise=0.2)
write_cities_csv(cities, city_filename('Y'))

# -----------------------------------------------

a, b_noise, k_noise = 3.0, 1.0, 0.2
cities = wavey_random_cities(n, a, b_noise, k_noise)
write_cities_csv(cities, city_filename('Z'))

# -----------------------------------------------

plot_cities_from_file(cities, 'X')
plot_cities_from_file(cities, 'Y')
plot_cities_from_file(cities, 'Z')

```

## Example 2
- Given you have random cities such as those located on `../data/cities`
and you have produces the respective outputs on `../data/output/`
by running `cargo run ./specs.csv ./cities.csv > ./output.csv`
You can use the following code to see the history of the genetic algorithm
(visualization of the search)

```python
from helpers import simulate
simulate("../citydna/data/cities/cities0.csv", "../citydna/data/output/output0.csv", sleep=0.0)
simulate("../citydna/data/cities/citiesA.csv", "../data/output/outputA.csv", sleep=0.15)
simulate("../citydna/data/cities/citiesB.csv", "../data/output/outputB.csv", sleep=0.2)
simulate("../citydna/data/cities/citiesC.csv", "../data/output/outputC.csv", sleep=0.15)
```

## Example 3
- This does random animation for generated random cities, this is used only
to test the city generation and animation, it has nothing to do with
genetic algorithms. But you might be interested in it.
```python
from helpers import random_animation, random_cities, circley_random_cities, wavey_random_cities
from city_plot import CityPlot
from numpy import pi

NUMBER_OF_CITIES = 10
X1, X2, Y1, Y2 = 0.0, 20.0, -6.0, 6.0
cities = random_cities(NUMBER_OF_CITIES, X1, X2, Y1, Y2)
plot = CityPlot(cities, (X1, X2), (Y1, Y2))
random_animation(plot, n=10, t=0.1)

cities = circley_random_cities(NUMBER_OF_CITIES=12, d=5.0, noise=1.0, theta_noise=0.2)
x = 5.0 + 0.0 + 1.0 # d + noise + 1.0
plot = CityPlot(cities, (-x, x), (-x, x))
random_animation(plot, n=20, t= 0.1)

NUMBER_OF_CITIES = 25
a, b_noise, k_noise = 4.0, 1.0, 0.2
y = a + b_noise + 1.0
x = pi + k_noise

cities = wavey_random_cities(NUMBER_OF_CITIES, a, b_noise, k_noise)
plot = CityPlot(cities, (-x, x), (-y, y))
random_animation(plot, n=20, t= 0.1)
```


