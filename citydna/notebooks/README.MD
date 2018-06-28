# PLOT PLAYGROUND
- A collection of jupyter notebooks where I play with interactive widgets paired with
visualization libraries such as bokeh and plotly

# Get Started

1. Install Miniconda 
2. Create environment

```
$ conda update conda
$ conda create --name plot-playground 
$ source activate plot-playground
```
3. Install Dependencies
```
$ conda install -c conda-forge ipywidgets
$ conda install jupyter bokeh plotly numpy scipy pandas matplotlib seaborn  
$ conda install -c menpo ffmpeg 
```

4. Prettify with with custom CSS (Optional) 

A. Custom CSS
```
$ cd ~/.jupyter/custom
$ nano custom.css
!copy paste the following from customCSS folder
```

B. Alternatively use Jupyter Themes
```
$ pip install cython
$ pip install --upgrade pip
$ pip install jupyterthemes
$ pip install --upgrade jupyterthemes
$ jt -t onedork -tf latosans -tfs 15 -lineh 170 -ofs 14
```

5. Launch
```
$ jupyter notebook
```
