from bokeh.io import push_notebook, show, output_notebook
from bokeh.plotting import figure
from bokeh.io import push_notebook, show, output_notebook
from bokeh.models import ColumnDataSource
import collections

City = collections.namedtuple('City', 'i x y')

BACKGROUND_COLOR = "#222f3e"
LEGEND_TEXT_COLOR = "#a29bfe"

def plot_city_paths(plot, champion, contender):
    
    line_square = plot.line('x', 'y', source=champion, legend=" CHAMPION PATH ", line_color="#a29bfe", line_alpha=1.0)
    line_circle = plot.line('x', 'y', source=contender, legend = " CONTENDER PATH ", line_color="#a29bfe", line_dash="10 2", line_alpha=1.0)
    
    plot.square('x', 'y', source=champion, legend=" CHAMPION PATH ",
        size=8, fill_color="#e84393", line_color="#fd79a8", fill_alpha=1.0, line_width=1)
    
    plot.circle('x', 'y', source=contender,  legend=" CONTENDER PATH ", 
        size=8, fill_color="#e84393", line_color="#fd79a8", fill_alpha=1.0, line_width=1)

    return line_square, line_circle

def stylize_plot(plot):
    #plot.legend.background_fill_color = "navy"
    plot.axis.major_tick_line_color = None
    plot.axis.major_label_standoff = 0
    plot.grid.grid_line_color = None
    plot.background_fill_color = BACKGROUND_COLOR
    plot.outline_line_color = BACKGROUND_COLOR
    plot.border_fill_color = BACKGROUND_COLOR
    plot.legend.label_text_color = LEGEND_TEXT_COLOR
    plot.legend.background_fill_alpha = 0.0
    plot.legend.label_text_alpha = 1.0
    plot.legend.label_text_font = "courier"
    plot.legend.orientation = "horizontal"
    plot.legend.location = "top_center"

def preliminary_city_figure(xr, yr):
    x = xr[1] + xr[1] - xr[0]
    return figure(x_range=[xr[0], x], y_range=[yr[0], yr[1] + 1.0],
        plot_height=500, plot_width=900, x_axis_location=None, y_axis_location=None, tools="")

def extract_data(cities, x):
    y = [city.y for city in cities]
    x1 = [city.x for city in cities]
    x2 = [city.x + x for city in cities]
    return x1, x2, y 

def change_path(order, source, x, y):
    source.data['x'] = [x[i] for i in order]
    source.data['y'] = [y[i] for i in order]       
    
class CityPlot:
            
    def __init__(self, cities, xr, yr):
        
        self.x1, self.x2, self.y = extract_data(cities, xr[1] - xr[0])
        
        self.plot = preliminary_city_figure(xr, yr)
                
        champion = ColumnDataSource({'x': self.x1, 'y': self.y})
        contender = ColumnDataSource({'x': self.x2, 'y': self.y})
        self.line_square, self.line_circle = plot_city_paths(self.plot, champion, contender)
        
        stylize_plot(self.plot)
        
    def update(self, order1, order2):
        change_path(order1, self.line_square.data_source, self.x1, self.y);
        change_path(order2, self.line_circle.data_source, self.x2, self.y);
        push_notebook();
        
    def show(self):
        output_notebook()
        show(self.plot, notebook_handle=True)