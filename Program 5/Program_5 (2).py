#  CS 101
#  Program 5
#  Gregory Gagnon
#  gagnong@umkc.edu
#
#  PROBLEM: 

#  Using provided sunspot data, remove the random noise to provide a 
#  smoothed data set for analysis of 11-year sunspot cycles. Graph the smoothed
#  data to provide a visual representation of the sunspot activity for the 
#  period of time the data covers.
#
#  ALGORITHM:
#
#  1) Create a function that formats the raw data from dailysunpots.txt into
#     monthly.txt:
#     a) Open file 
#     b) With a for loop, read the txt file line-by-line.
#         i) If sunspot count is not 999:
#            1) Split line into strings, retaining date and sunspot count.
#            2) Create dictionary full of each year/mon values. Split on month.
#        ii) Average values from each dictionary month's dictionary
#       iii) Formatted properly, write each month's dictionary average to a line
#            in a new file called monthly.txt
#
#  2) Create a function that “smooths” the data from monthly.txt:
#     a. Open file
#     b. With a for loop, read the txt file line-by-line
#         i. Copy into dictionary of values
#     c. For all values with six months before and after, calculate smoothed 
#        value: (.5 * first value + .5 * last value + sum of other values )/ 12)
#     d. Save each calculated, smoothed value into a line of new file called 
#        smooth.txt
# 
#  3) Create a function that graphs the data from smooth.txt:
#     a. Using pylab, graph the monthly data from smooth.txt
#
#
#  ERROR HANDLING: inputs sanitized. 
#
#  OTHER COMMENTS:
#  Sunspot cycles will reach peak next in 2012 and 2023.
#
#
#
##############################################################

import pylab

# Creates Dictionary of valid daily sunspot counts (those that != 999)
def CreateDailyDict(reader):
    daily_dict = {}
    for line in reader:
        date = line[0:8]
        spots = line[19:22]
        if spots != "999":
            daily_dict[date] = spots
    return daily_dict

# Creates Dictionary of monthly sunspot averages
def MonthlyAvgDict(daily_dict : dict): 
    monthly_dict = {}
    avg_dict = {}
    for entry in daily_dict.items():
        year_month_int = int(entry[0][0:6])
        sunspots_int = int(entry[1])
        
        # Creates new month's entry, or adds sunspots and days for averaging later
        if year_month_int not in monthly_dict:    
            #[sunspots,total days to avg]
            monthly_dict[year_month_int] = [sunspots_int,1] 
        else:
            #[add to sunspot total, add 1 to days to avg]
            monthly_dict[year_month_int] = monthly_dict[year_month_int][0] + sunspots_int, monthly_dict[year_month_int][1] + 1 

    # averages total sunspots for number of days in each month recorded
    for month in monthly_dict.items():
        avg_dict[month[0]] = month[1][0]/month[1][1] 
    
    return avg_dict

#Smooths averages according to data noise removal specs 
def SmoothAvg(monthly):
    monthly_dict = {}
    smooth_dict = {}
    smooth_list = []
    
    for line in monthly:
        monthly_dict[int(line[0:6])] = float(line[7:-1])
    
    #y = numbered key to find 6 months before/after
    y = 1
    for x in sorted(monthly_dict.items()):
        smooth_dict[y] = list(x)
        y += 1
    # smoothing data according to averaging specs
    for y in smooth_dict:
        if y-6 in smooth_dict and y+6 in smooth_dict:            
            smooth_fl = (smooth_dict[y-6][1] * 0.5 + smooth_dict[y+6][1] * 0.5 + smooth_dict[y-5][1] + smooth_dict[y-4][1] + smooth_dict[y-3][1] + smooth_dict[y-2][1] + smooth_dict[y-1][1] + smooth_dict[y][1] + smooth_dict[y+1][1] + smooth_dict[y+2][1] + smooth_dict[y+3][1] + smooth_dict[y+4][1] + smooth_dict[y+5][1]) / 12
        
            smooth_list.append((smooth_dict[y][0], smooth_fl))
                
    return smooth_list

# Open file to read
while True:
    file_str = input("what is the filename? ")
    try:
        data_file = open(file_str, "r")
        break
    except IOError:
        print("Oops, no file found. Be sure to include .txt")
        print()

# Open file to write            
monthly_file = open("monthly.txt", "w")

# Compile daily data, find monthly averages
daily_dict = CreateDailyDict(data_file)
monthly_avg_dict = MonthlyAvgDict(daily_dict)

data_file.close()

# Sort Monthly Averages from Dictionary and write to monthly.txt
for entry in sorted(monthly_avg_dict.items()):
    line_str = str(entry[0]) + " " + str(entry[1]) + "\n"
    monthly_file.write(line_str)
    
monthly_file.close()

# Open file to read monthly data and write smoothed data.           
smooth_file = open("smooth.txt", "w")
mon_avg_file = open("monthly.txt", "r")

#Smooth Function
smooth_list = SmoothAvg(mon_avg_file)

# Write smoothed data to smooth.txt
for entry in smooth_list:
    line_str = str(entry[0]) + " " + str(entry[1]) + "\n"
    smooth_file.write(line_str)

smooth_file.close()

# Open smooth.txt to graph
graph_file = open("smooth.txt", "r")
graph_list = []

for line in graph_file:
    date = int(line[0:6])
    spots = float(line[7:-1])
    graph_list.append((date,spots))

# Graph values
x_list = []
y_list = []

for x,y in graph_list:
    x_list.append(x)
    y_list.append(y)
    
pylab.plot(x_list,y_list)
pylab.show()

#The next cycles peaks will be in ~2012 and ~2023