import matplotlib.pyplot as plt
import matplotlib.font_manager
from matplotlib import rc
# rc('font',**{'family':'sans-serif','sans-serif':'Arial'})
# # plt.rcParams['font.family'] = ['sans-serif']
# # plt.rcParams['font.sans-serif'] = ['Arial']
# # rc('font',**{'family':'sans-serif','sans-serif':['Helvetica']})

def plot(ax,x,y,color='black',fontsize=28, fontweight='bold',xlabel='x',ylabel='y',title='',
labelsize=24,aspectratio=0.8,lw=2,linestyle='-',axlw=2,ticklength=5, tickwidth=2,label='',fontname='DejaVu Sans'):
    
    """
    Plots x vs y with predtermined default settings using matplotlib. Plots points connected by a line.
    
    Params
    ax : matplotlib axes object
    x  : x data to be plotted
    y  : y data to be plotted 
    color : color of line
    fontsize   : fontsize of all text not including tick labels
    fontweight : weather or not to bold text
    xlabel : x axis label
    ylabel : y axis label
    title  : plot title
    labelsize  : size of the tick labels
    aspectratio: aspect ratio of the plot, speficied by the plotted data
    linestyle : linestyle of histogram lines
    axlw : line width of axes
    ticklength : length of ticks on axis
    tickwidth : width of ticks on axis
    alpha : transparency of plot
    label : label for plotted data for purposes of referencing in a legend.
    
    returns : Does not return anything.
    
    """

    handle=ax.plot(x,y,color=color,lw=lw,linestyle=linestyle,label=label)
    ax.set_xlabel(xlabel,fontname=fontname,fontsize=fontsize,fontweight=fontweight);
    ax.set_ylabel(ylabel,fontname=fontname,fontsize=fontsize,fontweight=fontweight);
    ax.set_title(title,fontname=fontname,fontsize=fontsize,fontweight=fontweight);

    for axis in ['top','bottom','left','right']:
        ax.spines[axis].set_linewidth(axlw)
        
    for label in ax.get_xticklabels():
        label.set_fontproperties(fontname)
        label.set_fontweight(fontweight)

    for label in ax.get_yticklabels():
        label.set_fontproperties(fontname)
        label.set_fontweight(fontweight)
    
    ratio=aspectratio
    ax.tick_params(which='both',labelsize=labelsize,length=ticklength,width=tickwidth)
    ax.set_aspect(1/ax.get_data_ratio()*ratio)
    return handle

def scatter(ax,x,y,fontsize=28, fontweight='bold',xlabel='x',ylabel='y',title='',
labelsize=24,aspectratio=0.8,lw=2,linestyle='-',axlw=2,
facecolor='#1f77b4',edgecolor='#1f77b4',s=30,ticklength=5, tickwidth=2,label='',fontname='DejaVuSans'):
    
    """
    Plots x vs y with predtermined default settings using matplotlib. Plots points as a scatter plot.
    
    Params
    
    ax : matplotlib axes object
    x  : x data to be plotted
    y  : y data to be plotted  
    fontsize   : fontsize of all text not including tick labels
    fontweight : weather or not to bold text
    xlabel : x axis label
    ylabel : y axis label
    title  : plot title
    labelsize  : size of the tick labels
    aspectratio: aspect ratio of the plot, speficied by the plotted data
    linestyle : linestyle of histogram lines
    axlw : line width of axes
    facecolor      : color of the fill of the markers plotted
    edgecolor  : color of the edge of the markers plotted. Usually black of the same clor as facecolor.
    ticklength : length of ticks on axis
    tickwidth : width of ticks on axis
    alpha : transparency of plot
    label : label for plotted data for purposes of referencing in a legend.
    
    returns : Does not return anything.
    """


    handle=ax.scatter(x,y,lw=lw,facecolor=facecolor,edgecolor=edgecolor,label=label,s=s)
    ax.set_xlabel(xlabel,fontname='DejaVuSans',fontsize=fontsize,fontweight=fontweight);
    ax.set_ylabel(ylabel,fontname='DejaVuSans',fontsize=fontsize,fontweight=fontweight);
    ax.set_title(title,fontname='DejaVuSans',fontsize=fontsize,fontweight=fontweight);

    for axis in ['top','bottom','left','right']:
        ax.spines[axis].set_linewidth(axlw)
    
    for label in ax.get_xticklabels():
        label.set_fontproperties(fontname)
        label.set_fontweight(fontweight)

    for label in ax.get_yticklabels():
        label.set_fontproperties(fontname)
        label.set_fontweight(fontweight)

    ax.tick_params(which='both',labelsize=labelsize,length=ticklength,width=tickwidth)
    
    ratio=aspectratio
    ax.set_aspect(1/ax.get_data_ratio()*ratio)
    return handle


def hist(ax,y,bins=20,color='#1f77b4',edgecolor='black',fontsize=24, fontweight='bold',xlabel='x',ylabel='y',title='',
labelsize=22,aspectratio=0.8,lw=2,linestyle='-',axlw=2,ticklength=5, tickwidth=2,alpha=1,label=''):
    
    """
    Plots y as a histogram of values.
    
    Params
    ax : matplotlib axes object
    x  : x data to be plotted
    y  : y data to be plotted
    color      : color to fill in the histogram bars
    edgecolor  : color of the edges of the histogram bars
    fontsize   : fontsize of all text not including tick labels
    fontweight : weather or not to bold text
    xlabel : x axis label
    ylabel : y axis label
    title  : plot title
    labelsize  : size of the tick labels
    aspectratio: aspect ratio of the plot, speficied by the plotted data
    linestyle : linestyle of histogram lines
    axlw : line width of axes
    ticklength : length of ticks on axis
    tickwidth: line width of ticks on axes
    alpha : transparency of plot
    label : label for plotted data for purposes of referencing in a legend.
    
    returns : Does not return anything.
    """

    ax.hist(y,bins=bins,color=color,lw=lw,linestyle=linestyle,edgecolor='black',alpha=alpha,label=label)
    ax.set_xlabel(xlabel,fontsize=fontsize,fontweight=fontweight);
    ax.set_ylabel(ylabel,fontsize=fontsize,fontweight=fontweight);
    ax.set_title(title,fontsize=fontsize,fontweight=fontweight);
    ax.tick_params(which='both',labelsize=labelsize,length=ticklength,width=tickwidth)
    for axis in ['top','bottom','left','right']:
        ax.spines[axis].set_linewidth(axlw)
    ratio=aspectratio
    ax.set_aspect(1/ax.get_data_ratio()*ratio)

def set(ax,color='#1f77b4',edgecolor='black',fontsize=24, fontweight='bold',xlabel='x',ylabel='y',title='',
labelsize=22,aspectratio=0.8,lw=2,linestyle='-',axlw=2,ticklength=5, tickwidth=2):
    
    """
    Sets the style parameters of an ax object.
    
    Params
    ax : matplotlib axes object
    x  : x data to be plotted
    y  : y data to be plotted
    edgecolor  : color of the edges of the histogram bars
    fontsize   : fontsize of all text not including tick labels
    fontweight : weather or not to bold text
    xlabel : x axis label
    ylabel : y axis label
    title  : plot title
    labelsize  : size of the tick labels
    aspectratio: aspect ratio of the plot, speficied by the plotted data
    linestyle : linestyle of histogram lines
    axlw : line width of axes
    ticklength : length of ticks on axis
    tickwidth: line width of ticks on axes
    
    returns : nothing
    
    """
    ax.set_xlabel(xlabel,fontsize=fontsize,fontweight=fontweight);
    ax.set_ylabel(ylabel,fontsize=fontsize,fontweight=fontweight);
    ax.set_title(title,fontsize=fontsize,fontweight=fontweight);
    ax.tick_params(which='both',labelsize=labelsize,length=ticklength,width=tickwidth)
    for axis in ['top','bottom','left','right']:
        ax.spines[axis].set_linewidth(axlw)
    ratio=aspectratio
    ax.set_aspect(1/ax.get_data_ratio()*ratio)
