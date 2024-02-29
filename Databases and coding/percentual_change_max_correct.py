import numpy as np
import pandas as pd
from scipy import stats
import modules as md

def compare_mean_max(x,y):
    b = ((y * 100)/x)-100
    b = np.around(b,3)
    print(b)



#comparing mean vs max
#creating arrays containing the means of the precases
enterqueue_mean_pre_72_lifeline = np.array( [998.667,1241.333,1023.333,778,746.667,1411.333,655.333,668,960,497.333,641.333,616,856.667,1011.333,592.667,1211.333,1220,642] )

connect_mean_pre_72_lifeline = np.array([782.667,878.667,801.333,552,668,949.333,588.667,545.333,889.333,440,469.333,346.667,400.667,750.667,526,577.333,340,250.667])

abandon_mean_pre_72_lifeline = np.array([216,362.667,222,226.667,78.667,463.333,66.667,122.667,71.333,58,172.667,268.667,456,260.667,66.667,633.333,879.333,390.667])

wtc_mean_pre_72_lifeline = np.array([11.547,24.96,21.821,25.555,7.963,44.639,7.032,17.626,5.739,10.489,66.823,70.432,113.204,61.346,16.407,146.168,256.589,163.182])

wta_mean_pre_72_lifeline = np.array([78.243,90.123,66.236,82.766,65.357,99.597,51.025,104.289,61.895,157.069,177.557,193.055,179.03,131.282,110.171,163.504,254.992,284.539])

call_dur_mean_pre_72_lifeline = np.array([338.656,371.648,354.467,399.799,360.055,372.062,407.728,527.296,252.606,492.224,481.756,643.429,781.135,571.276,635.141,697.396,918.899,850.776])

lifeline_mean_72_array = np.vstack((enterqueue_mean_pre_72_lifeline, connect_mean_pre_72_lifeline, abandon_mean_pre_72_lifeline , wtc_mean_pre_72_lifeline, wta_mean_pre_72_lifeline, call_dur_mean_pre_72_lifeline)).T

#max arrays

enterqueue_max_72_lifeline = ([1242,1214,1056,784,700,1414,964,368,1074,570,996,978,970,1336,576,1352,1064,628])
connect_max_72_lifeline=([980,1156,780,592,620,1124,812,312,912,472,200,554,612,956,512,648,614,282])
abandon_max_72_lifeline=([262,56,276,192,80,296,152,56,162,98,758,428,358,380,64,704,448,346])
wtc_max_72_lifeline=([23.086,3.533,13.772,28.159,17.658,31.972,8.222,16.718,7.706,23.275,302.273,91.377,94.673,44.772,26.105,165.611,98.401,60.723])
wta_max_72_lifeline=([79.748,34.536,84.826,79.865,71.475,81.176,55.961,128.857,75.086,182.592,233.127,331.846,154.972,107.216,124.875,192.642,146.067,184.283])
call_dur_max_72_lifeline =([504.47,279.953,370.682,392.997,487.259,348.328,319.553,350.51,373.945,672.247,1261.622,519.766,359.925,615.146,597.604,721.795,478.369,682.725])

lifeline_max_72_array = np.vstack((enterqueue_max_72_lifeline, connect_max_72_lifeline, abandon_max_72_lifeline , wtc_max_72_lifeline, wta_max_72_lifeline, call_dur_max_72_lifeline)).T

compare_mean_max(lifeline_mean_72_array, lifeline_max_72_array)


