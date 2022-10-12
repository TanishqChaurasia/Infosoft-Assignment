class FuelStation:
    def __init__(self, diesel : int, petrol : int, electric : int): 
        
        self.slot_dict : dict[str, int] = dict()  #Created for tracking the max capacity of a fuel_type slot
        self.slot_dict["diesel"] = diesel
        self.slot_dict["petrol"] = petrol
        self.slot_dict["electric"] = electric
        
        self.fuel_dict : dict[str, int] = dict()  #Created for tracking the status of a fuel_type slot
        self.fuel_dict["diesel"] = diesel
        self.fuel_dict["petrol"] = petrol
        self.fuel_dict["electric"] = electric
    
    
    def fuel_vehicle(self, fuel_type : str) -> bool:
        if self.fuel_dict[fuel_type] >= 1 and fuel_type in self.fuel_dict.keys():
            self.fuel_dict[fuel_type] = self.fuel_dict[fuel_type] - 1
            return True
        else:
            return False
    
    
    def open_fuel_slot(self, fuel_type : str) -> bool:
        if fuel_type in self.fuel_dict.keys() and self.fuel_dict[fuel_type] < self.slot_dict[fuel_type]:
            self.fuel_dict[fuel_type] = self.fuel_dict[fuel_type] + 1
            return True
        else:
            return False
     
            
fuel_station = FuelStation(diesel = 2, petrol = 2, electric = 1)

#You will need to print each line to get the return value on the screen
fuel_station.fuel_vehicle("diesel")
fuel_station.fuel_vehicle("petrol")
fuel_station.fuel_vehicle("diesel")
fuel_station.fuel_vehicle("electric")
fuel_station.fuel_vehicle("diesel")
fuel_station.open_fuel_slot("diesel")
fuel_station.fuel_vehicle("diesel")
fuel_station.open_fuel_slot("electric")
fuel_station.open_fuel_slot("electric")
