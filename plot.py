import matplotlib.pyplot as pyplot
import matplotlib.font_manager
#matplotlib.rcParams['font.family'] = ['sans-serif']
#matplotlib.rcParams['font.sans-serif'] = ['Arial']


def plot(ax,x,y,color='black',fontsize=28, fontweight='bold',xlabel='x',ylabel='y',title='',
labelsize=24,aspectratio=0.8,lw=2,linestyle='-',axlw=2,ticklength=5, tickwidth=2,label='',fontname='DejaVu Sans'):
    

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
    ax.set_xlabel(xlabel,fontsize=fontsize,fontweight=fontweight);
    ax.set_ylabel(ylabel,fontsize=fontsize,fontweight=fontweight);
    ax.set_title(title,fontsize=fontsize,fontweight=fontweight);
    ax.tick_params(which='both',labelsize=labelsize,length=ticklength,width=tickwidth)
    for axis in ['top','bottom','left','right']:
        ax.spines[axis].set_linewidth(axlw)
    ratio=aspectratio
    ax.set_aspect(1/ax.get_data_ratio()*ratio)
