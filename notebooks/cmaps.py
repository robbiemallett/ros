from matplotlib.colors import LinearSegmentedColormap

def grain_type_colormap():

    """Returns a matplotlib colormap suitable for grain-type classification plots"""

    colors = [('white'),  # 1, precipitation particles
              ('green'),  # 2, Decomposing fragmented PP
              ('yellow'),  # 3 Rounded Grains (RG)
              ('orange'),  # 4 Faceted Crystals
              ('blue'),  # 5 Depth Hoar
              ('gray'),  # 6 Surface Hoar
              ('red'),  # 7 Melt FOrms
              ('cyan'),  # 8 Ice formations
              ('black'),  # 9 Rounded faceted particles
              ]


    cmap_name = 'grain_type_map'

    my_cmap = LinearSegmentedColormap.from_list(cmap_name, colors, N=9)

    return(my_cmap)

def get_grain_tick_labels():

    """Returns a list of labels for a grain-type classification plot"""

    grain_tick_labels = ['No Precipitation',
                         'Rain',
                         'NA',
                         'Freezing rain',
                         'NA',
                         'Snow',
                         'Wet snow',
                         'Rain/Snow Mix',
                         'Ice pellets']

    return(grain_tick_labels)

def get_grain_tick_labels2():

    """Returns a list of labels for a grain-type classification plot"""

    grain_tick_labels = ['',
                         'Rain',
                         'Ice pellets',
                         'Freezing rain',
                         'Rain/Snow Mix',
                         'Snow',
                         'Wet snow']

    return(grain_tick_labels)