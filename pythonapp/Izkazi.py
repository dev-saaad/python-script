from cmath import log
from pythonapp.helper.utils import DataTable

class IzkaziClass(DataTable):
    
    def __init__(self, dataframe, info, *arg, **kwargs):
        super().__init__(dataframe)
        self.info = info
        self.calculated_columns = ["Izkazi_A", "Izkazi_B", "Izkazi_C", "Izkazi_D", "Izkazi_E", "strukt"]
        print("Dataframe\n", dataframe.head(10))
        
    def compute_tables(self):
        predpostafkeVir = 'Gvaop'


        for i in range(0, 67):
            index = None
            valueA = 0
            valueB = 0
            valueC = 0
            valueD = 0
            valueE = 0
            if(i >= 0 and i <= 61):
                for j in range(0,4):
                    index = None
                    if(j == 0):
                        index = self.getIndex('Izkazi_Gvaop', i)
                    elif(j == 1):
                        index = self.getIndex('Izkazi_B', i)
                    elif(j == 2):
                        index = self.getIndex('Izkazi_C', i)
                    elif(j == 3):
                        index = self.getIndex('Izkazi_D', i)

                    if(index != None):
                        cond1 = self.df['BS_Gvin_'+str(int(self.df.Obdobja[4]))][index]
                        cond2 = self.df['BS_Gvin_'+str(int(self.df.Obdobja[3]))][index]
                        cond3 = self.df['BS_Gvin_'+str(int(self.df.Obdobja[2]))][index]
                        if(cond1 != "n.p." and str(cond1).lower() != 'nan'):
                            valueA = round( valueA + float(cond1)/1000)
                        if(cond2 != "n.p." and str(cond2).lower() != 'nan'):
                            valueB = round(valueB + float(cond2)/1000)
                        if(cond3 != "n.p." and str(cond3).lower() != 'nan'):
                            valueC = round(valueC + float(cond3)/1000)

                for j in range(0,4):
                    index = None
                    if(j == 0):
                        index = self.getIndex('Izkazi_AOP', i)
                    elif(j == 1):
                        index = self.getIndex('Izkazi_F', i)
                    elif(j == 2):
                        index = self.getIndex('Izkazi_G', i)
                    elif(j == 3):
                        index = self.getIndex('Izkazi_H', i)

                    if(index != None):
                        cond4 = self.df['BS_Ajpes_'+str(int(self.df.Obdobja[1]))][index]
                        cond5 = self.df['BS_Ajpes_'+str(int(self.df.Obdobja[0]))][index]
                        if(cond4 != "n.p." and str(cond4).lower() != 'nan'):
                            valueD = round(valueD + float(cond4)/1000)
                        if(cond5 != "n.p." and str(cond5).lower() != 'nan'):
                            valueE = round(valueE + float(cond5)/1000)


                self.df.loc[i, "Izkazi_A"] = valueA
                self.df.loc[i, "Izkazi_B"] = valueB
                self.df.loc[i, "Izkazi_C"] = valueC
                self.df.loc[i, "Izkazi_D"] = valueD
                self.df.loc[i, "Izkazi_E"] = valueE

            if(i == 62):
                if (self.df.loc[61, "Izkazi_A"] > 0):
                    self.df.loc[i, "Izkazi_A"] = round(self.df.loc[38, "Izkazi_A"]/self.df.loc[61, "Izkazi_A"] * 100) 
                else:
                    self.df.loc[i, "Izkazi_A"] = 0
                if(self.df.loc[61, "Izkazi_B"] > 0):    
                    self.df.loc[i, "Izkazi_B"] = round(self.df.loc[38, "Izkazi_B"]/self.df.loc[61, "Izkazi_B"] * 100) 
                else:
                    self.df.loc[i, "Izkazi_B"] = 0
                if(self.df.loc[61, "Izkazi_C"] > 0):    
                    self.df.loc[i, "Izkazi_C"] = round(self.df.loc[38, "Izkazi_C"]/self.df.loc[61, "Izkazi_C"] * 100)
                else:
                    self.df.loc[i, "Izkazi_C"] = 0
                if(self.df.loc[61, "Izkazi_D"] > 0):    
                    self.df.loc[i, "Izkazi_D"] = round(self.df.loc[38, "Izkazi_D"]/self.df.loc[61, "Izkazi_D"] * 100)
                else:
                    self.df.loc[i, "Izkazi_D"] = 0
                if(self.df.loc[61, "Izkazi_E"] > 0):    
                    self.df.loc[i, "Izkazi_E"] = round(self.df.loc[38, "Izkazi_E"]/self.df.loc[61, "Izkazi_E"] * 100)
                else:
                    self.df.loc[i, "Izkazi_E"] = 0
            
            if(i == 63):
                self.df.loc[i, "Izkazi_A"] = self.df.loc[20, "Izkazi_A"] + self.df.loc[26, "Izkazi_A"] + self.df.loc[29, "Izkazi_A"] - self.df.loc[58, "Izkazi_A"] - self.df.loc[60, "Izkazi_A"] 
                self.df.loc[i, "Izkazi_B"] = self.df.loc[20, "Izkazi_B"] + self.df.loc[26, "Izkazi_B"] + self.df.loc[29, "Izkazi_B"] - self.df.loc[58, "Izkazi_B"] - self.df.loc[60, "Izkazi_B"] 
                self.df.loc[i, "Izkazi_C"] = self.df.loc[20, "Izkazi_C"] + self.df.loc[26, "Izkazi_C"] + self.df.loc[29, "Izkazi_C"] - self.df.loc[58, "Izkazi_C"] - self.df.loc[60, "Izkazi_C"] 
                self.df.loc[i, "Izkazi_D"] = self.df.loc[20, "Izkazi_D"] + self.df.loc[26, "Izkazi_D"] + self.df.loc[29, "Izkazi_D"] - self.df.loc[58, "Izkazi_D"] - self.df.loc[60, "Izkazi_D"] 
                self.df.loc[i, "Izkazi_E"] = self.df.loc[20, "Izkazi_E"] + self.df.loc[26, "Izkazi_E"] + self.df.loc[29, "Izkazi_E"] - self.df.loc[58, "Izkazi_E"] - self.df.loc[60, "Izkazi_E"] 
            if(i == 64):
                self.df.loc[i, "Izkazi_A"] = self.df.loc[9, "Izkazi_A"] + self.df.loc[22, "Izkazi_A"] + self.df.loc[27, "Izkazi_A"] - self.df.loc[45, "Izkazi_A"] - self.df.loc[55, "Izkazi_A"] 
                self.df.loc[i, "Izkazi_B"] = self.df.loc[9, "Izkazi_B"] + self.df.loc[22, "Izkazi_B"] + self.df.loc[27, "Izkazi_B"] - self.df.loc[45, "Izkazi_B"] - self.df.loc[55, "Izkazi_B"] 
                self.df.loc[i, "Izkazi_C"] = self.df.loc[9, "Izkazi_C"] + self.df.loc[22, "Izkazi_C"] + self.df.loc[27, "Izkazi_C"] - self.df.loc[45, "Izkazi_C"] - self.df.loc[55, "Izkazi_C"] 
                self.df.loc[i, "Izkazi_D"] = self.df.loc[9, "Izkazi_D"] + self.df.loc[22, "Izkazi_D"] + self.df.loc[27, "Izkazi_D"] - self.df.loc[45, "Izkazi_D"] - self.df.loc[55, "Izkazi_D"] 
                self.df.loc[i, "Izkazi_E"] = self.df.loc[9, "Izkazi_E"] + self.df.loc[22, "Izkazi_E"] + self.df.loc[27, "Izkazi_E"] - self.df.loc[45, "Izkazi_E"] - self.df.loc[55, "Izkazi_E"]

            if(i == 65):
                self.df.loc[i, "Izkazi_A"] = self.roundToOne((self.df.loc[28, "Izkazi_A"] + self.df.loc[29, "Izkazi_A"]) / (self.df.loc[59, "Izkazi_A"] + self.df.loc[60, "Izkazi_A"]))
                self.df.loc[i, "Izkazi_B"] = self.roundToOne((self.df.loc[28, "Izkazi_B"] + self.df.loc[29, "Izkazi_B"]) / (self.df.loc[59, "Izkazi_B"] + self.df.loc[60, "Izkazi_B"]))
                self.df.loc[i, "Izkazi_C"] = self.roundToOne((self.df.loc[28, "Izkazi_C"] + self.df.loc[29, "Izkazi_C"]) / (self.df.loc[59, "Izkazi_C"] + self.df.loc[60, "Izkazi_C"]))
                self.df.loc[i, "Izkazi_D"] = self.roundToOne((self.df.loc[28, "Izkazi_D"] + self.df.loc[29, "Izkazi_D"]) / (self.df.loc[59, "Izkazi_D"] + self.df.loc[60, "Izkazi_D"]))
                self.df.loc[i, "Izkazi_E"] = self.roundToOne((self.df.loc[28, "Izkazi_E"] + self.df.loc[29, "Izkazi_E"]) / (self.df.loc[59, "Izkazi_E"] + self.df.loc[60, "Izkazi_E"]))

            if(i == 66):
                self.df.loc[i, "Izkazi_A"] = self.roundToOne((self.df.loc[13, "Izkazi_A"]) / (self.df.loc[41, "Izkazi_A"] + self.df.loc[50, "Izkazi_A"]))
                self.df.loc[i, "Izkazi_B"] = self.roundToOne((self.df.loc[13, "Izkazi_B"]) / (self.df.loc[41, "Izkazi_B"] + self.df.loc[50, "Izkazi_B"]))
                self.df.loc[i, "Izkazi_C"] = self.roundToOne((self.df.loc[13, "Izkazi_C"]) / (self.df.loc[41, "Izkazi_C"] + self.df.loc[50, "Izkazi_C"]))
                self.df.loc[i, "Izkazi_D"] = self.roundToOne((self.df.loc[13, "Izkazi_D"]) / (self.df.loc[41, "Izkazi_D"] + self.df.loc[50, "Izkazi_D"]))
                self.df.loc[i, "Izkazi_E"] = self.roundToOne((self.df.loc[13, "Izkazi_E"]) / (self.df.loc[41, "Izkazi_E"] + self.df.loc[50, "Izkazi_E"]))

        for i in range(0, 62):
            if(self.info.Imamo_podatke_za == "Da"):
                self.df.loc[i, "strukt"] = int((self.df.loc[i, "Izkazi_E"]/self.df.loc[30, "Izkazi_E"]))
            else:
                self.df.loc[i, "strukt"] = int((self.df.loc[i, "Izkazi_D"]/self.df.loc[30, "Izkazi_D"]))


    def getIndex(self, case, i):
        if(case == 'Izkazi_Gvaop'):
            for j in range(0, len(self.df.BS_Gvin_Gvaop)):
                if(self.df.Izkazi_Const_Gvaop[i] == self.df.BS_Gvin_Gvaop[j]):
                    return j
        elif(case == 'Izkazi_B'):
            for j in range(0, len(self.df.BS_Gvin_Gvaop)):
                if(self.df.Izkazi_Const_B[i] == self.df.BS_Gvin_Gvaop[j]):
                    return j
        elif(case == 'Izkazi_C'):
            for j in range(0, len(self.df.BS_Gvin_Gvaop)):
                if(self.df.Izkazi_Const_C[i] == self.df.BS_Gvin_Gvaop[j]):
                    return j
        elif(case == 'Izkazi_D'):
            for j in range(0, len(self.df.BS_Gvin_Gvaop)):
                if(self.df.Izkazi_Const_D[i] == self.df.BS_Gvin_Gvaop[j]):
                    return j
        elif(case == 'Izkazi_AOP'):
            for j in range(0, len(self.df['BS_Ajpes_Oznaka \nza AOP'])):
                if(self.df.Izkazi_Const_AOP[i] == self.df['BS_Ajpes_Oznaka \nza AOP'][j]):
                    return j
        elif(case == 'Izkazi_F'):
            for j in range(0, len(self.df['BS_Ajpes_Oznaka \nza AOP'])):
                if(self.df.Izkazi_Const_F[i] == self.df['BS_Ajpes_Oznaka \nza AOP'][j]):
                    return j
        elif(case == 'Izkazi_G'):
            for j in range(0, len(self.df['BS_Ajpes_Oznaka \nza AOP'])):
                if(self.df.Izkazi_Const_G[i] == self.df['BS_Ajpes_Oznaka \nza AOP'][j]):
                    return j
        elif(case == 'Izkazi_H'):
            for j in range(0, len(self.df['BS_Ajpes_Oznaka \nza AOP'])):
                if(self.df.Izkazi_Const_H[i] == self.df['BS_Ajpes_Oznaka \nza AOP'][j]):
                    return j
    
    def roundToOne(self, val):
        if(val):
            return round(val, 1)

    @property
    def Izkazi_A(self):
        return self.df.Izkazi_A
    
    @property
    def Izkazi_B(self):
        return self.df.Izkazi_B
    
    @property
    def Izkazi_C(self):
        return self.df.Izkazi_C

    @property
    def Izkazi_D(self):
        return self.df.Izkazi_D
    
    @property
    def Izkazi_E(self):
        return self.df.Izkazi_E
    
    @property
    def strukt(self):
        return self.df.strukt