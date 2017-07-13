# Complete the function below.
import numpy

def  maxProfit(costPerCut, salePrice, lengths):
    #first find optimal rod lengths dynamically this will maximize our cost 
    #function
    lengths.sort()
    #the longest cut possible is the longest rod in the set.
    max_cut = lengths[-1]
    #matrix to store the max cut length 
    f_nk = np.zeros(max_cut,max_cut)
    #we'll try cutting the logs in diff
    for cut_length in range(0, max_cut):
        for length in lengths:
            if length >
            max(f[n,k], salePrice*totalUniformRods*trial_lenght - totalCuts*f[n-1,k-1])   
    #Now start cutting our valid rods to generate
    #the equal length rods
    totalCuts = 0
    totalUniformRods = 0
    for length in lengths:
        x = length
        while x >= optimal_rod_length:
            x -= optimal_rod_length
            totalCuts += 1
            totalUniformRods += 1
    
    total_profit = salePrice*totalUniformRods*optimal_rod_length - totalCuts*costPerCut
    return total_profit
