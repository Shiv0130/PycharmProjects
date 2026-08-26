# Attempt
# sideTile=int(input("Enter length of tiles in cm^2:"))
# # area of tile is side**2(same as calc area of a square)
# size_of_floor_tile=sideTile**2
# # length of room
# lenRoom=float(input("Enter length of room:"))
# # breadth of room
# bRoom=float(input("Enter breadth of room:"))
# # The floor area is in square feet already
# Floor_area_of_room=lenRoom*bRoom
# # Converting the size of floor tile to square feet 1cm**2 =0.001sq.feet
# sq_size_of_floor_tile=size_of_floor_tile*0.001
# # Getting the number of tiles required
# num_of_tiles_reqd=Floor_area_of_room/sq_size_of_floor_tile
#
# print(f"Number of tiles required for a room is:{num_of_tiles_reqd}")

#  Correction
# import math
#
# # sideTile = int(input("Enter length of tiles in cm^2:"))
# #
# # # area of tile is side**2 (same as calc area of a square)
# # size_of_floor_tile = sideTile ** 2
# #
# # # length of room
# # lenRoom = float(input("Enter length of room(ft):"))
# #
# # # breadth of room
# # bRoom = float(input("Enter breadth of room(ft):"))
# #
# # # The floor area is in square feet already
# # Floor_area_of_room = lenRoom * bRoom
# #
# # # Converting the size of floor tile to square feet 1cm**2 = 0.001sq.feet
# # sq_size_of_floor_tile = size_of_floor_tile * 0.001
# #
# # # Getting the number of tiles required
# # num_of_tiles_reqd = math.ceil(Floor_area_of_room / sq_size_of_floor_tile)
# #
# # print(f"Number of tiles required for a room is: {num_of_tiles_reqd}")

# Update this simple program by using classes

# Attempt
# class House:
#     def __init__(self,size):
#         self.size=size
#
#
#     def area_of_tile(self):
#         areaTile=self.size**2
#         return areaTile
#
#     def area_of_rooom(self,length,breadth):
#         self.length=length
#         self.breadth=breadth
#         areaRoom=self.length*self.breadth
#         return areaRoom
#
#     def num_of_tiles_required(self):
#         number_of_tiles_required=math.ceil(self.area_of_rooom(self.length,self.breadth)/self.area_of_tile())
#         return number_of_tiles_required
#
# sideTile=int(input("Enter the length of tiles in cm^2:"))
# lenRoom=int(input("Enter the length of room(ft):"))
# bRoom=int(input("Enter the breadth of room(ft):"))
#
# Home=House(sideTile)
#
# area_of_tile=Home.area_of_tile()
# area_of_rm=Home.area_of_rooom(lenRoom,bRoom)
#
# num_of_tiles_reqd=Home.num_of_tiles_required()
#
# print(num_of_tiles_reqd)

# # Correction
# import math
#
# class TileCalculator:
#     def __init__(self, side_length_cm):
#         self.side_length_cm = side_length_cm
#
#     def calculate_tile_area(self):
#         # Calculate the area of a single tile (assumes the tile is square)
#         return self.side_length_cm ** 2
#
#     def calculate_floor_area(self, length_ft, breadth_ft):
#         # Calculate the floor area of the room in square feet
#         return length_ft * breadth_ft
#
#     def calculate_num_of_tiles_required(self, length_ft, breadth_ft):
#         # Calculate the number of tiles required for the given room
#         tile_area_cm2 = self.calculate_tile_area()
#         floor_area_ft2 = self.calculate_floor_area(length_ft, breadth_ft)
#         sq_size_of_floor_tile = tile_area_cm2 * 0.001
#         num_of_tiles_reqd = math.ceil(floor_area_ft2 / sq_size_of_floor_tile)
#         return num_of_tiles_reqd
#
# # Taking input from the user
# side_tile_cm = int(input("Enter the length of tiles side in cm^2:"))
# len_room_ft = float(input("Enter the length of room (ft):"))
# b_room_ft = float(input("Enter the breadth of room (ft):"))
#
# # Creating an instance of the TileCalculator class
# tile_calculator = TileCalculator(side_tile_cm)
#
# # Calculating the number of tiles required and printing the result
# num_of_tiles_reqd = tile_calculator.calculate_num_of_tiles_required(len_room_ft, b_room_ft)
# print(f"Number of tiles required for the room is: {num_of_tiles_reqd}")


# Take the above code and implement it into a tkinter program:
import tkinter as tk
from tkinter import ttk
import math

class TileCalculator:
    def __init__(self, side_length_cm):
        # Constructor to initialize the TileCalculator object with the length of one side of the tile
        self.side_length_cm = side_length_cm

    def calculate_tile_area(self):
        # Method to calculate the area of a single tile (assumes the tile is square)
        return self.side_length_cm ** 2

    def calculate_floor_area(self, length_ft, breadth_ft):
        # Method to calculate the floor area of the room in square feet
        return length_ft * breadth_ft

    def calculate_num_of_tiles_required(self, length_ft, breadth_ft):
        # Method to calculate the number of tiles required for the given room
        tile_area_cm2 = self.calculate_tile_area()
        floor_area_ft2 = self.calculate_floor_area(length_ft, breadth_ft)
        sq_size_of_floor_tile = tile_area_cm2 * 0.001
        num_of_tiles_reqd = math.ceil(floor_area_ft2 / sq_size_of_floor_tile)
        return num_of_tiles_reqd

def calculate_tiles():
    # Callback function for the Calculate button
    # Takes input values from the entry widgets, performs calculations, and updates the result label
    side_tile_cm = int(tile_length_entry.get())
    len_room_ft = float(length_entry.get())
    b_room_ft = float(breadth_entry.get())

    tile_calculator = TileCalculator(side_tile_cm)
    num_of_tiles_reqd = tile_calculator.calculate_num_of_tiles_required(len_room_ft, b_room_ft)

    # Updating the result label to display the calculated number of tiles required
    result_label.config(text=f"Number of tiles required: {num_of_tiles_reqd}")

# Creating the main Tkinter window
root = tk.Tk()
root.title("Tile Calculator For Room")
root.geometry("300x200")

# Creating input widgets and labels
tile_length_label = ttk.Label(root, text="Enter the length of tiles side in cm^2:")
tile_length_entry = ttk.Entry(root)

length_label = ttk.Label(root, text="Enter the length of room (ft):")
length_entry = ttk.Entry(root)

breadth_label = ttk.Label(root, text="Enter the breadth of room (ft):")
breadth_entry = ttk.Entry(root)

calculate_button = ttk.Button(root, text="Calculate", command=calculate_tiles)

result_label = ttk.Label(root, text="")

# Placing widgets on the grid
tile_length_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")
tile_length_entry.grid(row=0, column=1, padx=10, pady=10)

length_label.grid(row=1, column=0, padx=10, pady=10, sticky="w")
length_entry.grid(row=1, column=1, padx=10, pady=10)

breadth_label.grid(row=2, column=0, padx=10, pady=10, sticky="w")
breadth_entry.grid(row=2, column=1, padx=10, pady=10)

calculate_button.grid(row=3, column=0, columnspan=2, pady=10)

result_label.grid(row=4, column=0, columnspan=2, pady=10)

# Running the Tkinter main loop
root.mainloop()




