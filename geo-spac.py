
#GUI Version
# import rasterio
# from rasterio.plot import show
# import matplotlib.pyplot as plt
# from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
# import tkinter as tk

# with rasterio.open('2025-02-28-00_00_2025-02-28-23_59_Sentinel-1_IW_VV+VH_VH_-_decibel_gamma0(2).tiff') as src:
#     sar_image = src.read(1)
#     transform = src.transform

#     # Logic to convert pixel to geographical coordinates using affine transformation
#     def pixel_to_geo(x, y, transform):
#         col, row = x, y
#         lon, lat = transform * (col, row)
#         return lon, lat

#     # This handles the mouse clicks(bascially pin pointing the location)
#     def onclick(event):
#         if event.xdata is not None and event.ydata is not None:
#             x, y = int(event.xdata), int(event.ydata)
#             lon, lat = pixel_to_geo(x, y, transform)
#             print(f'Pixel Coordinates: ({x}, {y})')
#             print(f'Geographical Coordinates: ({lat},{lon})')
#             pixel_label.config(text=f'Pixel Coordinates: ({x}, {y})')
#             coord_label.config(text=f'Lat: {lat:.6f}, Lon: {lon:.6f}')

#     root = tk.Tk()
#     root.title("Geospatial Coordinates")
#     fig, ax = plt.subplots()
#     ax.imshow(sar_image, cmap='gray')
#     fig.colorbar(ax.imshow(sar_image, cmap='gray'))

#     # canvas for the image
#     canvas = FigureCanvasTkAgg(fig, master=root)
#     canvas.draw()
#     canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
#     toolbar = NavigationToolbar2Tk(canvas, root)
#     toolbar.update()
#     canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
#     pixel_label = tk.Label(root, text="Pixel Coordinates: ", font=("Helvetica", 12))
#     pixel_label.pack(side=tk.BOTTOM, fill=tk.X)
#     coord_label = tk.Label(root, text="Lat: , Lon: ", font=("Helvetica", 12))
#     coord_label.pack(side=tk.BOTTOM, fill=tk.X)
#     cid = fig.canvas.mpl_connect('button_press_event', onclick)
#     root.mainloop()



import rasterio

# Open the SAR image
with rasterio.open('2025-02-28-00_00_2025-02-28-23_59_Sentinel-1_IW_VV+VH_VH_-_decibel_gamma0(2).tiff') as src:
    sar_image = src.read(1)  # Read the first band
    transform = src.transform  # Get the affine transformation

    # Function to convert pixel coordinates to geographical coordinates
    def pixel_to_geo(x, y, transform):
        col, row = x, y
        lon, lat = transform * (col, row)
        return lon, lat

    # Helper function to convert multiple pixel coordinates
    def convert_pixel_coords(pixel_coords, transform):
        geo_coords = []
        for x, y in pixel_coords:
            lon, lat = pixel_to_geo(x, y, transform)
            geo_coords.append((lat, lon))
        return geo_coords

    # Test use
    pixel_coords = [(924, 595), (1442, 609), (1428, 636), (1451, 632)]
    geo_coords = convert_pixel_coords(pixel_coords, transform)

    for (x, y), (lat, lon) in zip(pixel_coords, geo_coords):
        print(f'Pixel Coordinates: ({x}, {y}) -> Geographical Coordinates: ({lat:.6f}, {lon:.6f})')