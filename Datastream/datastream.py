class DataStream: 
    data_dict : dict[str, int] = dict()  # Created for storing data_strings and their latest timestamps
       
    def should_output_data_str(self, timestamp : int, data_string : str) -> bool :
        if data_string in self.data_dict.keys():
            if timestamp-self.data_dict[data_string] >= 5:
                self.data_dict[data_string] = timestamp
                return True
            else:
                return False
        else:
            self.data_dict[data_string] = timestamp
            return True
        
        
data_stream = DataStream()

#You will need to print each line to get the return value on the screen
data_stream.should_output_data_str(timestamp = 0, data_string = "hello")
data_stream.should_output_data_str(timestamp = 1, data_string = "world")
data_stream.should_output_data_str(timestamp = 6, data_string = "hello")
data_stream.should_output_data_str(timestamp = 7, data_string = "hello")
data_stream.should_output_data_str(timestamp = 8, data_string = "world")

