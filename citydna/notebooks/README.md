# VISUALIZATION AND ANIMATION
| ![](../docs/gif/simA.gif)      |   ![](../docs/gif/simB.gif)      |
| ----------------------------- |:-------------------------------:|
| ![](../docs/gif/simC.gif)      | ![](../docs/gif/sim0.gif)        |

# Installation and launch

## 1. [Install Miniconda](https://conda.io/docs/user-guide/install/index.html) 
## 2. Create environment
```
$ conda update conda
$ conda create --name rusty-genes 
$ source activate rusty-genes
$ conda install jupyter bokeh numpy 
```

## 3. Prettify with with custom CSS (Optional) 
```
$ cd ~/.jupyter/custom
$ nano custom.css
!copy paste the css file contents from customCSS folder
```

## 4. Launch
```
$ source activate rusty-genes
$ jupyter notebook
```
