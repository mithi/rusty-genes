# PFDT 
# Particle Filter Datastructures for lack of better term

from collections import namedtuple
import csv

Landmark = namedtuple('Landmark', 'i x y')

# speed in m/s , turnrate in rad/s
Control = namedtuple('Control', 'speed turnrate')

# Observed landmark position the x and y distance in m relative to the vehicle
# x - right is positive, y - forward is positive
Observation = namedtuple('Observation', 'i x y')

# Global x and y positions in m, 
# theta  is global vehicle yaw (rad)
GroundTruth = namedtuple('GroundTruth', 'i x y theta')


def get_groundtruths_from_file(filename):
    groundtruths = []
    with open(filename, newline='') as file:
        reader = csv.reader(file, delimiter=' ', quotechar='|')
        x, y, theta, i_ = 0.0, 0.0, 0.0, 0
        for r in reader:
            x_, y_, theta_= float(r[0]), float(r[1]), float(r[2])
            groundtruth = GroundTruth(i=i_, x=x_, y=y_, theta=theta_)
            groundtruths.append(groundtruth)
            i_+=1
        return groundtruths
    

def get_landmarks_from_file(filename):
    landmarks = []
    with open(filename, newline='') as file:
        reader = csv.reader(file, delimiter='\t', quotechar='|')
        x, y, i = 0.0, 0.0, 0
        for r in reader:
            x_, y_, i_ = float(r[0]), float(r[1]), int(r[2])
            landmark = Landmark(i=i_, x=x_, y=y_)
            landmarks.append(landmark)
        return landmarks


def get_observations_from_file(filename):
    observations = []
    with open(filename, newline='') as file:
        reader = csv.reader(file, delimiter=' ', quotechar='|')
        x, y, i_ = 0.0, 0.0, 0
        for r in reader:
            x_, y_ = float(r[0]), float(r[1])
            observation = Observation(i=i_, x=x_, y=y_)
            observations.append(observation)
            i_+=1
        return observations