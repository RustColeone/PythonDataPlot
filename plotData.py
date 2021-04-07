import numpy as np
from scipy import optimize
import matplotlib.pyplot as plt

import sys, getopt

def plotFile(fileName, delimiter, saveFile, xRange, yRange, hTick, vTick):
    #Edit this here
    title0, title1, title2, title3 = np.loadtxt(fileName, delimiter=delimiter, dtype='str', unpack=False, max_rows=1)
    data1, ddata1, data2, ddata2 = np.loadtxt(fileName, delimiter=delimiter, unpack=True, skiprows=1)

    # Create our figure
    fig1 = plt.figure()

    # Add a subplot in the {1,1,1} position, that is, add just one plot in what could be an array of plots.
    ax1 = fig1.add_subplot(111)

    # errorbar(x,y,yneg,ypos,xneg,xpos) plots y vs x and makes error bars for both the x and
    # y directions. yneg and ypos set the size of the top and bottom half of the error bars 
    # respectively, while xneg and xpos do the same for error bars in the x direction.
    errorBar = False
    if(errorBar):
        ax1.errorbar(data1, data2, ddata2, fmt='k.', label = '{} Data'.format(title2), capsize = 5, ecolor = 'blue')
    else:
        ax1.plot(data1, data2, 'x')

    # Set the title and axis labels for our plot
    ax1.set_title('{} Data'.format(fileName[:-4]))
    ax1.set_xlabel(title0)
    ax1.set_ylabel(title2)

    # Create a second set of axes for the top and right hand sides of the plot, then locate them as above
    ax1.yaxis.set_ticks_position('both')
    ax1.xaxis.set_ticks_position('both')


    # Tick mark locations are specified by the command set_major_locator() and set_minor_locator() commands,
    # which take arguments MultipleLocator(), NullLocator(), or MaxNLocator()

    ax1.xaxis.set_major_locator(plt.MultipleLocator(hTick))
    ax1.xaxis.set_minor_locator(plt.MultipleLocator(hTick/2))

    ax1.yaxis.set_major_locator(plt.MultipleLocator(vTick))
    ax1.yaxis.set_minor_locator(plt.MultipleLocator(vTick/2))

    # Tick mark labels can be set by the command set_major_formatter() and set_minor_formatter() commands, 
    # which take arguments FormatStrFormatter(), NullFormatter(), 
    ax1.xaxis.set_major_formatter(plt.FormatStrFormatter('%g')) 
    ax1.yaxis.set_minor_formatter(plt.NullFormatter())


    # To set parameters of the ticks like size, direction, color, etc.
    ax1.tick_params(which = 'major', direction = 'in', length = 6, width = 1, color = 'grey')
    ax1.tick_params(which = 'minor', direction = 'in', length = 3, width = 1, color = 'black') 

    # To add an annotation, first create the text you want as a string, and then use the "text" command as follows:
    #textfit1 = 'This is an annotation. Equations are \n available using LaTeX environment: \n $\int_{a}^{b} x^2 dx$'
    #ax1.text(0.1, .65, textfit1, transform=ax1.transAxes, fontsize=9, verticalalignment='top')

    # Create a legend to distinguish between data sets. bbox_to_anchor sets the (x,y) position of the corner of the legend
    #ax1.legend(bbox_to_anchor=(0.43, 0.98))

    # Set the upper and lower limits of the axes
    if(xRange[0] == xRange[1]):
        maxX = max(data1)
        minX = min(data1)
        maxdX = max(ddata1)
        rangeX = maxX - minX
        xRange[0] = minX - maxdX - rangeX * 0.05
        xRange[1] = maxX + maxdX + rangeX * 0.05
    if(yRange[0] == yRange[1]):
        maxY = max(data2)
        minY = min(data2)
        maxdY = max(ddata2)
        rangeY = maxY - minY
        yRange[0] = minY - maxdY - rangeY * 0.05
        yRange[1] = maxY + maxdY + rangeY * 0.05
    ax1.set_xlim(xRange)
    ax1.set_ylim(yRange)

    ax1.set_aspect(1.0/ax1.get_data_ratio(), adjustable='box')

    # Save the figure to the same folder if saveFile is not an empty string
    if(saveFile != ""):
        plt.savefig(saveFile)

    plt.show()
    return

def main(argv):
    inputfile = "exampleData.csv"
    outputFile = "exampleData"
    xRange = [0,0]
    yRange = [0,0]
    hTick = 10
    vTick = 5
    delimiter = ","
    argumentList = sys.argv[1:]
    options = "hi:o:d:x:y:X:Y:H:V:"
    long_options = ["help", "input", "output", "delimiter", "x-min", "y-min", "x-max", "y-max", "horizontal-tick", "vertical-tick"]

    try:
        # Parsing argument
        plot = True
        arguments, argv1 = getopt.getopt(argumentList, options, long_options)
        print(arguments)
        for currentArgument, currentValue in arguments:
            if currentArgument in ("-h", "--Help"):
                print ("usage example: plot.py -i <inputfile> -o <outputfile>")
                print ("usage full   : Usage: plotData.py -i <inputFile.csv> -o <outputFile.xxx> -d <delimiter> -x <x-min> -X <X-max> -y <y-min> -Y <Y-max> -H <Horizontal-Tick> -V <Vertical-Tick>")
                plot = False

            elif currentArgument in ("-i", "--input"):
                inputfile = currentValue

            elif currentArgument in ("-o", "--output"):
                outputFile = currentValue

            elif currentArgument in ("-d", "--delimiter"):
                delimiter = currentValue
            
            elif currentArgument in ("-x", "--x-min"):
                xRange[0] = float(currentValue)

            elif currentArgument in ("-X", "--x-max"):
                xRange[1] = float(currentValue)

            elif currentArgument in ("-y", "--y-min"):
                yRange[0] = float(currentValue)

            elif currentArgument in ("-Y", "--y-max"):
                yRange[1] = float(currentValue)

            elif currentArgument in ("-H", "--horizontal-tick"):
                hTick = float(currentValue)
            
            elif currentArgument in ("-V", "--vertical-tick"):
                vTick = float(currentValue)
        if(plot):
            plotFile(inputfile, delimiter, outputFile, xRange, yRange, hTick, vTick)

    except getopt.error as err:
        # output error, and return with an error code
        print (str(err))
        print ("Usage: plotData.py -i <inputFile.csv> -o <outputFile.xxx> -d <delimiter> -x <x-min> -X <X-max> -y <y-min> -Y <Y-max> -H <Horizontal-Tick> -V <Vertical-Tick>")

if __name__ == "__main__":
   main(sys.argv[1:])

