from time import sleep 
from numpy import cos, sin, pi, sqrt, linspace
from random import shuffle, randrange, uniform
import csv
from city_plot import City, CityPlot

def simulate(city_filename, output_filename, sleep=0.1):
    cities = read_cities_csv(city_filename)
    x1, x2, y1, y2 = min_max(cities) # get x and y ranges
    plot = CityPlot(cities, (x1 - 1.0, x2 + 1.0), (y1 - 1.0, y2 + 1.0)) # Add margins to ranges
    simulation_animation(plot, output_filename, t=sleep)
    

# iteration number_of_cities champion_fitness, challenger_fitness, champion_dna, challenger_dna
def yield_from_csv(name):
    cities = []
    with open(name, newline='') as csv_file:
        reader = csv.reader(csv_file, delimiter=',', quotechar='|')
        i, n, f1, f2 = 0, 0, 0.0, 0.0
        for r in reader:
            i, n, f1, f2 = int(r[0]), int(r[1]), float(r[2]), float(r[3])
            champion = [int(i) for i in r[4:(4 + n)]]
            challenger = [int(i) for i in r[(4 + n):]]
            # print("# ",i, "champion score:", f1, "challenger score:", f2)
            yield (champion, challenger)
        print("FINAL", "champion score:", f1, "challenger score:", f2)
        

def simulation_animation(plot, filename, t=0.1):
    plot.show()
    for r in yield_from_csv(filename):
        champion, challenger = r
        plot.update(champion, challenger)
        sleep(t)
    print("done!")

 
def random_animation(plot, n = 50, t = 0.1):
    plot.show()
    c = len(plot.x1)
    order1 = [i for i in range(0, c)]
    order2 = [i for i in range(0, c)]
    
    for x in range(n):
        sleep(t)
        shuffle(order1)
        shuffle(order2)
        plot.update(order1, order2)
        
    print("done!")

    
def read_cities_csv(name):
    cities = []
    with open(name, newline='') as csv_file:
        reader = csv.reader(csv_file, delimiter=',', quotechar='|')
        for row in reader:
            _i, _x, _y = int(row[0]), float(row[1]), float(row[2])
            city = City(i=_i, x =_x, y=_y)
            cities.append(city)
            
    return cities


def write_cities_csv(cities, name="city.csv"):
    with open(name, 'w', newline='') as csv_file:
        writer = csv.writer(csv_file, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        for city in cities:
            writer.writerow([city.i, city.x, city.y])

    
def random_cities(n, X1, X2, Y1, Y2):
    cities = []
    for i_ in range(n):
        x_, y_ = uniform(X1, X2), uniform(Y1, Y2)
        city = City(i = i_, x = x_, y = y_)
        cities.append(city)
        
    return cities


def wavey_random_cities(NUMBER_OF_CITIES, a, b_noise=0.0, k_noise=0.0):
    # a cos( wt + k ) + b  
    index = [i for i in range(NUMBER_OF_CITIES)]
    shuffle(index);
    xs, ys, cities = [], [], []
    t = linspace(-pi, pi, NUMBER_OF_CITIES + 1)
    
    for i in range(NUMBER_OF_CITIES):
        x = t[i] + uniform(-k_noise, k_noise)
        y = a * sin (x) + uniform(-b_noise, b_noise)
        xs.append(x)
        ys.append(y)
        
    for j in range(NUMBER_OF_CITIES):
        i = index[j]
        city = City(i = j, x = xs[i], y = ys[i])
        cities.append(city)
        
    return cities


def circley_random_cities(NUMBER_OF_CITIES, d=5.0, noise=0.1, theta_noise=0.1):

    index = [i for i in range(NUMBER_OF_CITIES)]
    shuffle(index);
    xs, ys, cities = [], [], []
    thetas = linspace(-pi, pi, NUMBER_OF_CITIES + 1)
    
    for i in range(NUMBER_OF_CITIES):
        theta = thetas[i] + uniform(-theta_noise, theta_noise)
        noisy_d = d + uniform(-noise, noise)
        x = noisy_d * cos(theta) 
        y = noisy_d * sin(theta)
        xs.append(x)
        ys.append(y)
        
    for j in range(NUMBER_OF_CITIES):
        i = index[j]
        city = City(i = j, x = xs[i], y = ys[i])
        cities.append(city)

    return cities


def min_max(cities):
    n = 1000000000.0
    minx, maxx, miny, maxy = n, -n, n, -n
    for city in cities:
        if city.x < minx: 
            minx = city.x
        if city.x > maxx:
            maxx = city.x
        if city.y < miny:
            miny = city.y
        if city.y > maxy:
            maxy = city.y
        
    return (minx, maxx, miny, maxy)