from pythonapp.helper.utils import DataTable

class Izkazi2Class(DataTable):
    
    def __init__(self, dataframe, info, *arg, **kwargs):
        super().__init__(dataframe)
        self.info = info
        self.calculated_columns = ["Izkazi2_A", "Izkazi2_B", "Izkazi2_C", "Izkazi2_D", "Izkazi2_E", "Izkazi2_strukt"]
        print("Dataframe\n", dataframe.head(10))
        
    def compute_tables(self):
        predpostafkeVir = 'Gvaop'


        for i in range(0, 34):
            index = None
            valueA = 0
            valueB = 0
            valueC = 0
            valueD = 0
            valueE = 0
            if(i >= 0 and i <= 28):
                for j in range(0,4):
                    index = None
                    if(j == 0):
                        index = self.getIndex('Izkazi2_Gvaop', i)
                    elif(j == 1):
                        index = self.getIndex('Izkazi2_B', i)
                    elif(j == 2):
                        index = self.getIndex('Izkazi2_C', i)
                    elif(j == 3):
                        index = self.getIndex('Izkazi2_D', i)

                    if(index != None):
                        cond1 = self.df['IPI_Gvin_'+str(int(self.df.Obdobja[4]))][index]
                        cond2 = self.df['IPI_Gvin_'+str(int(self.df.Obdobja[3]))][index]
                        cond3 = self.df['IPI_Gvin_'+str(int(self.df.Obdobja[2]))][index]
                        if(cond1 != "n.p." and str(cond1).lower() != 'nan'):
                            valueA = round(valueA + float(cond1)/1000)
                        if(cond2 != "n.p." and str(cond2).lower() != 'nan'):
                            valueB = round(valueB + float(cond2)/1000)
                        if(cond3 != "n.p." and str(cond3).lower() != 'nan'):
                            valueC = round(valueC + float(cond3)/1000)

                for j in range(0,4):
                    index = None
                    if(j == 0):
                        index = self.getIndex('Izkazi2_AOP', i)
                    elif(j == 1):
                        index = self.getIndex('Izkazi2_F', i)
                    elif(j == 2):
                        index = self.getIndex('Izkazi2_G', i)
                    elif(j == 3):
                        index = self.getIndex('Izkazi2_H', i)

                    if(index != None):
                        cond4 = self.df['IPI_Ajpes_'+str(int(self.df.Obdobja[1]))][index]
                        cond5 = self.df['IPI_Ajpes_'+str(int(self.df.Obdobja[0]))][index]
                        if(cond4 != "n.p." and str(cond4).lower() != 'nan'):
                            valueD = round(valueD + float(cond4)/1000)
                        if(cond5 != "n.p." and str(cond5).lower() != 'nan'):
                            valueE = round(valueE + float(cond5)/1000)

                if(i == 5 or ( i >= 10 and i <= 17) or ( i >= 20 and i <= 23) or ( i >= 25 and i <= 128)):
                    self.df.loc[i, "Izkazi2_A"] = -valueA
                    self.df.loc[i, "Izkazi2_B"] = -valueB
                    self.df.loc[i, "Izkazi2_C"] = -valueC
                    self.df.loc[i, "Izkazi2_D"] = -valueD
                    self.df.loc[i, "Izkazi2_E"] = -valueE
                else:
                    self.df.loc[i, "Izkazi2_A"] = valueA
                    self.df.loc[i, "Izkazi2_B"] = valueB
                    self.df.loc[i, "Izkazi2_C"] = valueC
                    self.df.loc[i, "Izkazi2_D"] = valueD
                    self.df.loc[i, "Izkazi2_E"] = valueE
                
                if(i == 6):
                    self.df.loc[i, "Izkazi2_A"] = self.df.loc[i-1, "Izkazi2_A"] + self.df.loc[i-2, "Izkazi2_A"]
                    self.df.loc[i, "Izkazi2_B"] = self.df.loc[i-1, "Izkazi2_B"] + self.df.loc[i-2, "Izkazi2_B"]
                    self.df.loc[i, "Izkazi2_C"] = self.df.loc[i-1, "Izkazi2_C"] + self.df.loc[i-2, "Izkazi2_C"]
                    self.df.loc[i, "Izkazi2_D"] = self.df.loc[i-1, "Izkazi2_D"] + self.df.loc[i-2, "Izkazi2_D"]
                    self.df.loc[i, "Izkazi2_E"] = self.df.loc[i-1, "Izkazi2_E"] + self.df.loc[i-2, "Izkazi2_E"]

                if(i == 7):
                    self.df.loc[i, "Izkazi2_A"] = self.df.loc[i-1, "Izkazi2_A"] + self.df.loc[i-4, "Izkazi2_A"]
                    self.df.loc[i, "Izkazi2_B"] = self.df.loc[i-1, "Izkazi2_B"] + self.df.loc[i-4, "Izkazi2_B"]
                    self.df.loc[i, "Izkazi2_C"] = self.df.loc[i-1, "Izkazi2_C"] + self.df.loc[i-4, "Izkazi2_C"]
                    self.df.loc[i, "Izkazi2_D"] = self.df.loc[i-1, "Izkazi2_D"] + self.df.loc[i-4, "Izkazi2_D"]
                    self.df.loc[i, "Izkazi2_E"] = self.df.loc[i-1, "Izkazi2_E"] + self.df.loc[i-4, "Izkazi2_E"]
                
                if(i == 13):
                    self.df.loc[i, "Izkazi2_A"] = self.df.loc[i-1, "Izkazi2_A"] + self.df.loc[i-2, "Izkazi2_A"] + self.df.loc[i-3, "Izkazi2_A"] + self.df.loc[i-4, "Izkazi2_A"] + self.df.loc[i-5, "Izkazi2_A"] + self.df.loc[i-6, "Izkazi2_A"]
                    self.df.loc[i, "Izkazi2_B"] = self.df.loc[i-1, "Izkazi2_B"] + self.df.loc[i-2, "Izkazi2_B"] + self.df.loc[i-3, "Izkazi2_B"] + self.df.loc[i-4, "Izkazi2_B"] + self.df.loc[i-5, "Izkazi2_B"] + self.df.loc[i-6, "Izkazi2_B"]
                    self.df.loc[i, "Izkazi2_C"] = self.df.loc[i-1, "Izkazi2_C"] + self.df.loc[i-2, "Izkazi2_C"] + self.df.loc[i-3, "Izkazi2_C"] + self.df.loc[i-4, "Izkazi2_C"] + self.df.loc[i-5, "Izkazi2_C"] + self.df.loc[i-6, "Izkazi2_C"]
                    self.df.loc[i, "Izkazi2_D"] = self.df.loc[i-1, "Izkazi2_D"] + self.df.loc[i-2, "Izkazi2_D"] + self.df.loc[i-3, "Izkazi2_D"] + self.df.loc[i-4, "Izkazi2_D"] + self.df.loc[i-5, "Izkazi2_D"] + self.df.loc[i-6, "Izkazi2_D"]
                    self.df.loc[i, "Izkazi2_E"] = self.df.loc[i-1, "Izkazi2_E"] + self.df.loc[i-2, "Izkazi2_E"] + self.df.loc[i-3, "Izkazi2_E"] + self.df.loc[i-4, "Izkazi2_E"] + self.df.loc[i-5, "Izkazi2_E"] + self.df.loc[i-6, "Izkazi2_E"]

                if(i == 18):
                    self.df.loc[i, "Izkazi2_A"] = self.df.loc[i-1, "Izkazi2_A"] + self.df.loc[i-5, "Izkazi2_A"]
                    self.df.loc[i, "Izkazi2_B"] = self.df.loc[i-1, "Izkazi2_B"] + self.df.loc[i-5, "Izkazi2_B"]
                    self.df.loc[i, "Izkazi2_C"] = self.df.loc[i-1, "Izkazi2_C"] + self.df.loc[i-5, "Izkazi2_C"]
                    self.df.loc[i, "Izkazi2_D"] = self.df.loc[i-1, "Izkazi2_D"] + self.df.loc[i-5, "Izkazi2_D"]
                    self.df.loc[i, "Izkazi2_E"] = self.df.loc[i-1, "Izkazi2_E"] + self.df.loc[i-5, "Izkazi2_E"]

                if(i == 26):
                    self.df.loc[i, "Izkazi2_A"] = self.df.loc[18, "Izkazi2_A"] + self.df.loc[19, "Izkazi2_A"] + self.df.loc[23, "Izkazi2_A"] + self.df.loc[24, "Izkazi2_A"] + self.df.loc[25, "Izkazi2_A"]
                    self.df.loc[i, "Izkazi2_B"] = self.df.loc[18, "Izkazi2_B"] + self.df.loc[19, "Izkazi2_B"] + self.df.loc[23, "Izkazi2_B"] + self.df.loc[24, "Izkazi2_B"] + self.df.loc[25, "Izkazi2_B"]
                    self.df.loc[i, "Izkazi2_C"] = self.df.loc[18, "Izkazi2_C"] + self.df.loc[19, "Izkazi2_C"] + self.df.loc[23, "Izkazi2_C"] + self.df.loc[24, "Izkazi2_C"] + self.df.loc[25, "Izkazi2_C"]
                    self.df.loc[i, "Izkazi2_D"] = self.df.loc[18, "Izkazi2_D"] + self.df.loc[19, "Izkazi2_D"] + self.df.loc[23, "Izkazi2_D"] + self.df.loc[24, "Izkazi2_D"] + self.df.loc[25, "Izkazi2_D"]
                    self.df.loc[i, "Izkazi2_E"] = self.df.loc[18, "Izkazi2_E"] + self.df.loc[19, "Izkazi2_E"] + self.df.loc[23, "Izkazi2_E"] + self.df.loc[24, "Izkazi2_E"] + self.df.loc[25, "Izkazi2_E"]

                if(i == 28):
                    self.df.loc[i, "Izkazi2_A"] = self.df.loc[i-1, "Izkazi2_A"] + self.df.loc[i-2, "Izkazi2_A"]
                    self.df.loc[i, "Izkazi2_B"] = self.df.loc[i-1, "Izkazi2_B"] + self.df.loc[i-2, "Izkazi2_B"]
                    self.df.loc[i, "Izkazi2_C"] = self.df.loc[i-1, "Izkazi2_C"] + self.df.loc[i-2, "Izkazi2_C"]
                    self.df.loc[i, "Izkazi2_D"] = self.df.loc[i-1, "Izkazi2_D"] + self.df.loc[i-2, "Izkazi2_D"]
                    self.df.loc[i, "Izkazi2_E"] = self.df.loc[i-1, "Izkazi2_E"] + self.df.loc[i-2, "Izkazi2_E"]

                if valueD > 0 :
                    self.df.loc[i, "Izkazi2_strukt"] = int(((valueE/valueD)-1)*100)
                else:
                    self.df.loc[i, "Izkazi2_strukt"] = 0

            if(i == 29):
                self.df.loc[i, "Izkazi2_A"] = round(self.df.loc[7, "Izkazi2_A"] / self.df.loc[3, "Izkazi2_A"], 2)
                self.df.loc[i, "Izkazi2_B"] = round(self.df.loc[7, "Izkazi2_B"] / self.df.loc[3, "Izkazi2_B"], 2)
                self.df.loc[i, "Izkazi2_C"] = round(self.df.loc[7, "Izkazi2_C"] / self.df.loc[3, "Izkazi2_C"], 2)
                self.df.loc[i, "Izkazi2_D"] = round(self.df.loc[7, "Izkazi2_D"] / self.df.loc[3, "Izkazi2_D"], 2)
                self.df.loc[i, "Izkazi2_E"] = round(self.df.loc[7, "Izkazi2_E"] / self.df.loc[3, "Izkazi2_E"], 2)
            if(i == 30):
                self.df.loc[i, "Izkazi2_A"] = round(self.df.loc[13, "Izkazi2_A"] / self.df.loc[3, "Izkazi2_A"], 2)
                self.df.loc[i, "Izkazi2_B"] = round(self.df.loc[13, "Izkazi2_B"] / self.df.loc[3, "Izkazi2_B"], 2)
                self.df.loc[i, "Izkazi2_C"] = round(self.df.loc[13, "Izkazi2_C"] / self.df.loc[3, "Izkazi2_C"], 2)
                self.df.loc[i, "Izkazi2_D"] = round(self.df.loc[13, "Izkazi2_D"] / self.df.loc[3, "Izkazi2_D"], 2)
                self.df.loc[i, "Izkazi2_E"] = round(self.df.loc[13, "Izkazi2_E"] / self.df.loc[3, "Izkazi2_E"], 2)
            if(i == 31):
                if(self.df.loc[64, "Izkazi_A"] > 0):
                    self.df.loc[i, "Izkazi2_A"] = 0
                else:
                    self.df.loc[i, "Izkazi2_A"] = round(-self.df.loc[64, "Izkazi_A"] / self.df.loc[13, "Izkazi2_A"], 1)
                
                if(self.df.loc[64, "Izkazi_B"] > 0):
                    self.df.loc[i, "Izkazi2_B"] = 0
                else:
                    self.df.loc[i, "Izkazi2_B"] = round(-self.df.loc[64, "Izkazi_B"] / self.df.loc[13, "Izkazi2_B"], 1)
                
                if(self.df.loc[64, "Izkazi_C"] > 0):
                    self.df.loc[i, "Izkazi2_C"] = 0
                else:
                    self.df.loc[i, "Izkazi2_C"] = round(-self.df.loc[64, "Izkazi_C"] / self.df.loc[13, "Izkazi2_C"], 1)
                
                if(self.df.loc[64, "Izkazi_D"] > 0):
                    self.df.loc[i, "Izkazi2_D"] = 0
                else:
                    self.df.loc[i, "Izkazi2_D"] = round(-self.df.loc[64, "Izkazi_D"] / self.df.loc[13, "Izkazi2_D"], 1)
                
                if(self.df.loc[64, "Izkazi_E"] > 0):
                    self.df.loc[i, "Izkazi2_E"] = 0
                else:
                    self.df.loc[i, "Izkazi2_E"] = round(-self.df.loc[64, "Izkazi_E"] / (self.df.loc[13, "Izkazi2_E"]/self.df.loc[0, "St_Mesecev"]*12), 1)


            if(i == 32):
                self.df.loc[i, "Izkazi2_A"] = round(self.df.loc[13, "Izkazi2_A"] / self.df.loc[55, "Izkazi_A"], 1)
                self.df.loc[i, "Izkazi2_B"] = round(self.df.loc[13, "Izkazi2_B"] / self.df.loc[55, "Izkazi_B"], 1)
                self.df.loc[i, "Izkazi2_C"] = round(self.df.loc[13, "Izkazi2_C"] / self.df.loc[55, "Izkazi_C"], 1)
                self.df.loc[i, "Izkazi2_D"] = round(self.df.loc[13, "Izkazi2_D"] / self.df.loc[55, "Izkazi_D"], 1)
                self.df.loc[i, "Izkazi2_E"] = round( (self.df.loc[13, "Izkazi2_E"] / self.df.loc[4, "St_Mesecev"]*12) / self.df.loc[55, "Izkazi_E"], 1)

            if(i == 33):
                self.df.loc[i, "Izkazi2_A"] = -round(self.df.loc[18, "Izkazi2_A"] / self.df.loc[23, "Izkazi2_A"], 1)
                self.df.loc[i, "Izkazi2_B"] = -round(self.df.loc[18, "Izkazi2_B"] / self.df.loc[23, "Izkazi2_B"], 1)
                self.df.loc[i, "Izkazi2_C"] = -round(self.df.loc[18, "Izkazi2_C"] / self.df.loc[23, "Izkazi2_C"], 1)
                self.df.loc[i, "Izkazi2_D"] = -round(self.df.loc[18, "Izkazi2_D"] / self.df.loc[23, "Izkazi2_D"], 1)
                self.df.loc[i, "Izkazi2_E"] = -round(self.df.loc[18, "Izkazi2_E"] / self.df.loc[23, "Izkazi2_E"], 1)


    def getIndex(self, case, i):
        i = i + 75
        if(case == 'Izkazi2_Gvaop'):
            for j in range(0, len(self.df.IPI_Gvin_Gvaop)):
                if(self.df.Izkazi_Const_Gvaop[i] == self.df.IPI_Gvin_Gvaop[j]):
                    return j
        elif(case == 'Izkazi2_B'):
            for j in range(0, len(self.df.IPI_Gvin_Gvaop)):
                if(self.df.Izkazi_Const_B[i] == self.df.IPI_Gvin_Gvaop[j]):
                    return j
        elif(case == 'Izkazi2_C'):
            for j in range(0, len(self.df.IPI_Gvin_Gvaop)):
                if(self.df.Izkazi_Const_C[i] == self.df.IPI_Gvin_Gvaop[j]):
                    return j
        elif(case == 'Izkazi2_D'):
            for j in range(0, len(self.df.IPI_Gvin_Gvaop)):
                if(self.df.Izkazi_Const_D[i] == self.df.IPI_Gvin_Gvaop[j]):
                    return j
        elif(case == 'Izkazi2_AOP'):
            for j in range(0, len(self.df['IPI_Ajpes_Unnamed: 2'])):
                if(self.df.Izkazi_Const_AOP[i] == self.df['IPI_Ajpes_Unnamed: 2'][j]):
                    return j
        elif(case == 'Izkazi2_F'):
            for j in range(0, len(self.df['IPI_Ajpes_Unnamed: 2'])):
                if(self.df.Izkazi_Const_F[i] == self.df['IPI_Ajpes_Unnamed: 2'][j]):
                    return j
        elif(case == 'Izkazi2_G'):
            for j in range(0, len(self.df['IPI_Ajpes_Unnamed: 2'])):
                if(self.df.Izkazi_Const_G[i] == self.df['IPI_Ajpes_Unnamed: 2'][j]):
                    return j
        elif(case == 'Izkazi2_H'):
            for j in range(0, len(self.df['IPI_Ajpes_Unnamed: 2'])):
                if(self.df.Izkazi_Const_H[i] == self.df['IPI_Ajpes_Unnamed: 2'][j]):
                    return j
    
            
    @property
    def Izkazi2_A(self):
        return self.df.Izkazi2_A
    
    @property
    def Izkazi2_B(self):
        return self.df.Izkazi2_B
    
    @property
    def Izkazi2_C(self):
        return self.df.Izkazi2_C

    @property
    def Izkazi2_D(self):
        return self.df.Izkazi2_D
    
    @property
    def Izkazi2_E(self):
        return self.df.Izkazi2_E
    
    @property
    def Izkazi2_strukt(self):
        return self.df.Izkazi2_strukt