import cdstoolbox as ct
import numpy as np
import xarray as xr


@ct.application(title='Retrieve Data')

### Log

# Launched for all months at 16:38 on 10/8/2021

@ct.output.download()
@ct.output.download()
@ct.output.download()

def retrieve_sample_data():
    
    cubes = []
    cubes_t = []
    cubes_bin = []
    
    years  = np.arange(1979,2022,6)
    
    for i in range(len(years)-1):
        
        y0 = years[i]
        y1 = years[i+1]
        print(y0,y1)

        (ptype, tp) = ct.catalogue.retrieve(
            'reanalysis-era5-single-levels',
            {
                'product_type': 'reanalysis',
                'variable': [
                    'precipitation_type', 'total_precipitation',
                ],
                'year': [str(x) for x in np.arange(y0,y1)],

                'month': [
                 #   '01', '02', '03', '04',
                    '10', '11', '12',
                ],

                'day': [
                    '01', '02', '03',
                    '04', '05', '06',
                    '07', '08', '09',
                    '10', '11', '12',
                    '13', '14', '15',
                    '16', '17', '18',
                    '19', '20', '21',
                    '22', '23', '24',
                    '25', '26', '27',
                    '28', '29', '30',
                    '31',            ],

                'time': [
                    '00:00', '01:00', '02:00',
                    '03:00', '04:00', '05:00',
                    '06:00', '07:00', '08:00',
                    '09:00', '10:00', '11:00',
                    '12:00', '13:00', '14:00',
                    '15:00', '16:00', '17:00',
                    '18:00', '19:00', '20:00',
                    '21:00', '22:00', '23:00',
                ],

                "area":[90,-180,75,180],
            }
        )

        # cube.where works like this:
        # Where True, yield x, otherwise yield y.

        # 5 is snow
        # 8 is ice pellets
        # Yield array elements where ptype is not frozen (where it is wet), else yield zero

        x = ct.cube.where(ptype != 5, tp, 0) #must be != 
        x = ct.cube.where(ptype != 8, x, 0)

        # multiply from metres per sec to milimetres per hr

        x = ct.operator.mul(x, 1000*3600)

        x_thresh = ct.cube.where(x > 0.1/24, x, 0)
        
        # Look at changing duration/time
        
        x_bin_thresh = ct.cube.where(x_thresh == 0, x_thresh, 1)
        x_bin_thresh = ct.cube.where(x_bin_thresh != 1, x_bin_thresh, 0)
        
        x_hrs_raining = ct.cube.resample(x_bin_thresh, how='sum', freq = 'month')

        # sum up all non-zero for the year

        ann_sum = ct.cube.resample(x, how='sum',freq='month')

        ann_sum_thresh = ct.cube.resample(x_thresh, how='sum',freq='month')
        
        cubes.append(ann_sum)
        cubes_t.append(ann_sum_thresh)
        cubes_bin.append(x_hrs_raining)
        
    all_data = ct.cube.concat(cubes, dim='time')
    all_data_t = ct.cube.concat(cubes_t, dim='time')
    all_data_bin = ct.cube.concat(cubes_bin, dim='time')
        
    
    return (all_data, all_data_t, all_data_bin)