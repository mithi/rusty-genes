from bokeh.plotting import figure
from bokeh.io import push_notebook, show, output_notebook
from bokeh.models import ColumnDataSource

BACKGROUND_COLOR = "#222f3e"
LEGEND_TEXT_COLOR = "#a29bfe"
ROBOT_LINE_COLOR = "#833471"
ROBOT_FILL_COLOR = "#9980FA"
LANDMARK_COLOR = "#fd79a8"
SENSED_COLOR = "#17c0eb"


def stylize_plot(plot):
    #plot.legend.background_fill_color = "navy"
    plot.axis.major_tick_line_color = None
    plot.axis.major_label_standoff = 0
    plot.grid.grid_line_color = None
    plot.background_fill_color = BACKGROUND_COLOR
    plot.outline_line_color = BACKGROUND_COLOR
    plot.border_fill_color = BACKGROUND_COLOR
    plot.legend.label_text_color = LEGEND_TEXT_COLOR
    plot.legend.label_text_font_size = '8pt'
    plot.legend.background_fill_alpha = 0.0
    plot.legend.label_text_alpha = 1.0
    plot.legend.label_text_font = "courier"
    plot.legend.orientation = "vertical"
    plot.legend.location = "bottom_right"

    
def map_figure(x1=-60, x2=310, y1=-110, y2=60, w=900, h=600):
    return figure(x_range=[x1, x2], y_range=[y1, y2],
        plot_height=h, plot_width=w, 
        x_axis_location=None, y_axis_location=None, tools="")


def extract_landmarks(landmarks):
    x = [landmark.x for landmark in landmarks]
    y = [landmark.y for landmark in landmarks]
    return x, y


def extract_observations(observations):
    x = [observation.x for observation in observations]
    y = [observation.y for observation in observations]
    return x, y


def plot_landmarks(plot, landmarks):
    landmark_x, landmark_y = extract_landmarks(landmarks)
    landmark_source = ColumnDataSource({'x': landmark_x, 'y': landmark_y} )
    plot.circle('x', 'y', legend="LANDMARKS", source=landmark_source,
        size=9, line_color=LANDMARK_COLOR, fill_alpha=0.0, line_width=1)


def plot_initial_robot(plot, robot_source):
    
    robot_triangle = plot.triangle('x', 'y', legend = "GROUND TRUTH LOCATION", source = robot_source,
        size=30, fill_color=ROBOT_FILL_COLOR, line_color=ROBOT_LINE_COLOR, fill_alpha=1.0, line_width=1,
        angle='theta')

    robot_cross = plot.cross('x', 'y', legend="GROUND TRUTH LOCATION", source=robot_source,
        size=12, line_color=ROBOT_LINE_COLOR, angle='theta', fill_alpha=0.0, line_width=1)

    robot_range = plot.circle('x', 'y', legend="OBSERVATION RANGE", source=robot_source,
        radius=50, line_color=ROBOT_LINE_COLOR, line_dash="10 5", fill_alpha=0.0, line_width=1)

    return (robot_range, robot_triangle, robot_cross)


def plot_robot(source, x, y, theta):
    source.data['x'] = [x]
    source.data['y'] = [y]
    source.data['theta'] = [theta] 


def plot_fixed_vehicle(plot):
    robot_source = ColumnDataSource(data = { 'x' : [0], 'y' : [0], 'theta' : [-3.14 / 2] })
    plot.triangle('x', 'y', size=30, fill_color=ROBOT_FILL_COLOR, legend="vehicle's perspective",
        line_color=ROBOT_LINE_COLOR, fill_alpha =1.0, line_width=1,
        angle = 'theta', source=robot_source)
    plot.cross('x', 'y', source=robot_source,
        size=12, line_color=ROBOT_LINE_COLOR, angle = 'theta', fill_alpha=0.0, line_width=1)
    plot.circle('x', 'y', source=robot_source,
        radius=52, line_color=ROBOT_LINE_COLOR, fill_alpha=0.0, line_width=1, line_dash="10 5")


class SimpleMapPlot: 
    def __init__(self, landmarks):
        
        self.plot = map_figure(x1=-60, x2=300, y1=-110, y2=50, h=400, w=900)
        plot_landmarks(self.plot, landmarks)    
        self.robot_source = ColumnDataSource(data = { 'x' : [0], 'y' : [0], 'theta' : [0] })
        self.robot_range, self.robot_triangle, self.robot_cross = plot_initial_robot(self.plot, self.robot_source)
        stylize_plot(self.plot)
    
    def update(self, g):
        theta = g.theta - 3.14 / 2 # -g.theta - 1.1 #FIX
        plot_robot(self.robot_triangle.data_source, g.x, g.y, theta)
        plot_robot(self.robot_cross.data_source, g.x, g.y, theta)
        plot_robot(self.robot_range.data_source, g.x, g.y, theta)
    
    def show(self):
        show(self.plot, notebook_handle=True)


class VicinityPlot: 
    def __init__(self, observations, noisy_observations):
        self.plot = map_figure(x1=-70, x2=70, y1=-70, y2=70, h=350, w=350)
        plot_fixed_vehicle(self.plot)

        observation_x, observation_y = extract_observations(noisy_observations)
        observation_source = ColumnDataSource({'x': observation_x, 'y': observation_y} )
        self.noisy_observation_circles = self.plot.circle('x', 'y', source=observation_source,
            size=9, line_color=SENSED_COLOR, fill_color=SENSED_COLOR, fill_alpha=0.25, line_width=3, alpha=0.25,
            legend="noisy observation")

        observation_x, observation_y = extract_observations(observations)
        observation_source = ColumnDataSource({'x': observation_x, 'y': observation_y} )
        self.observation_circles = self.plot.circle('x', 'y', source=observation_source,
            size=9, line_color=LANDMARK_COLOR, fill_alpha=0.0, line_width=1, alpha=1.0, legend="ground truth")
        
        stylize_plot(self.plot)  
            
    def update(self, observations, noisy_observations):
        observation_x, observation_y = extract_observations(noisy_observations)
        self.noisy_observation_circles.data_source.data['x'] = observation_x
        self.noisy_observation_circles.data_source.data['y'] = observation_y

        observation_x, observation_y = extract_observations(observations)
        self.observation_circles.data_source.data['x'] = observation_x
        self.observation_circles.data_source.data['y'] = observation_y
        
    def show(self):
        show(self.plot, notebook_handle=True)


class SimpleVicinityPlot: 
    def __init__(self, observations):
        self.plot = map_figure(x1=-70, x2=70, y1=-70, y2=70, h=350, w=350)
        plot_fixed_vehicle(self.plot)
        observation_x, observation_y = extract_observations(observations)
        observation_source = ColumnDataSource({'x': observation_x, 'y': observation_y} )
        self.observation_circles = self.plot.circle('x', 'y', source=observation_source,
            size=9, line_color=LANDMARK_COLOR, fill_alpha=0.0, line_width=1, alpha=1.0, legend="ground truth")
        stylize_plot(self.plot)  
        
    def update(self, observations):
        observation_x, observation_y = extract_observations(observations)
        self.observation_circles.data_source.data['x'] = observation_x
        self.observation_circles.data_source.data['y'] = observation_y
        
    def show(self):
        show(self.plot, notebook_handle=True)