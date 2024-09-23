from pythonapp.helper.utils import DataTable

class PredopostavkeClass(DataTable):
    
    def __init__(self, dataframe, info, *arg, **kwargs):
        super().__init__(dataframe)
        self.calculated_columns = ["Obdobja", "Obdobja_IPI", "Obdobja_BS", "St_Mesecev"]
        self.output_cols = ["Obdobja", "Obdobja_IPI", "Obdobja_BS", "St_Mesecev"]
        self.info = info
        # print("Dataframe\n", dataframe.head(10))
        
    def compute_tables(self):

        self.df.loc[0, "Obdobja"] = self.info.Zadnje_gvin_bilance + 1 
        
        var = str(int(self.Obdobja[0]))[-2:]

        if(self.info.Zadnje_obdobje_v_key == "December"):
            self.df.loc[0, "Obdobja_IPI"] = "PL" + var
        else:
            self.df.loc[0, "Obdobja_IPI"] = "1- " + var

        self.df.loc[0, "Obdobja_BS"] = str(self.info.Zadnje_obdobje_v_key)[0:3] + var  
        
        self.df.loc[0, "St_Mesecev"] = self.info.Zadnje_obdobje_v_value  

        for i in range(1, 5):
            if(i==1):
                self.df.loc[1, "Obdobja"] = self.info.Zadnje_gvin_bilance
            else:
                self.df.loc[i, "Obdobja"] = self.Obdobja[i-1]-1
    
            self.df.loc[i, "Obdobja_IPI"] = "PL" + str(int(self.Obdobja[i]))[-2:]
            
            self.df.loc[i, "Obdobja_BS"] = "Dec" + str(int(self.Obdobja[i]))[-2:]  

            self.df.loc[i, "St_Mesecev"] = 12  

    @property
    def Obdobja(self):
        return self.df.Obdobja
    
    @property
    def Obdobja_IPI(self):
        return self.df.Obdobja_IPI
    
    @property
    def Obdobja_BS(self):
        return self.df.Obdobja_BS
    
    @property
    def St_Mesecev(self):
        return self.df.St_Mesecev