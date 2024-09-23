from cmath import log
from pythonapp.helper.utils import DataTable

class IzkaziNewClass(DataTable):
    
    def __init__(self, dataframe, predopostavke, inputs, *arg, **kwargs):
        super().__init__(dataframe)
        self.predopostavke = predopostavke
        self.inputs = inputs
        self.calculated_columns = ["Izkazi_A", "Izkazi_B", "Izkazi_C", "Izkazi_D", "Izkazi_E", "strukt"]
        
    def compute_tables(self):
        self.df.loc[0, "Izkazi_A"] = None
        self.df.loc[0, "Izkazi_B"] = None
        self.df.loc[0, "Izkazi_C"] = None
        self.df.loc[0, "Izkazi_D"] = None
        self.df.loc[0, "Izkazi_E"] = None
        self.inputs['Test'] = 1000
        col = ["Izkazi_A", "Izkazi_B", "Izkazi_C", "Izkazi_D", "Izkazi_E"]
        for i in range(0, 62):
            index1 = None
            index2 = None 
            index3 = None 
            index4 = None
            count = 0
            
            for val in self.predopostavke:
                valueA = 0
                valueB = 0
                valueC = 0
                valueD = 0
                if(val['Vir'] == "Gvaop"):
                    index1 = self.getIndex('Izkazi_Gvaop', i)
                    index2 = self.getIndex('Izkazi_B', i)
                    index3 = self.getIndex('Izkazi_C', i)
                    index4 = self.getIndex('Izkazi_D', i)
                    if(index1 != None):
                        cond1 = self.df[val['Obdobja']][index1]
                        if(cond1 != "n.p." and str(cond1).lower() != 'nan'):
                            valueA = self.divide(float(cond1), 1000, isRound=True)
                    if(index2 != None):
                        cond2 = self.df[val['Obdobja']][index2]
                        if(cond2 != "n.p." and str(cond2).lower() != 'nan'):
                            valueB = self.divide(float(cond2), 1000, isRound=True)
                    if(index3 != None):
                        cond3 = self.df[val['Obdobja']][index3]
                        if(cond3 != "n.p." and str(cond3).lower() != 'nan'):
                            valueC = self.divide(float(cond3), 1000, isRound=True)
                    if(index4 != None):
                        cond4 = self.df[val['Obdobja']][index4]
                        if(cond4 != "n.p." and str(cond4).lower() != 'nan'):
                            valueD = self.divide(float(cond4), 1000, isRound=True)

                    total = valueA+valueB+valueC+valueD
                else:
                    index5 = self.getIndex('Izkazi_AOP', i)
                    index6 = self.getIndex('Izkazi_F', i)
                    index7 = self.getIndex('Izkazi_G', i)
                    index8 = self.getIndex('Izkazi_H', i)
                    if(index5 != None):
                        cond1 = self.df[val['Obdobja']][index5]
                        if(cond1 != "n.p." and str(cond1).lower() != 'nan'):
                            valueA = self.divide(float(cond1), 1000, isRound=True)
                    if(index6 != None):
                        cond2 = self.df[val['Obdobja']][index6]
                        if(cond2 != "n.p." and str(cond2).lower() != 'nan'):
                            valueB = self.divide(float(cond2), 1000, isRound=True)
                    if(index7 != None):
                        cond3 = self.df[val['Obdobja']][index7]
                        if(cond3 != "n.p." and str(cond3).lower() != 'nan'):
                            valueC = self.divide(float(cond3), 1000, isRound=True)
                    if(index8 != None):
                        cond4 = self.df[val['Obdobja']][index8]
                        if(cond4 != "n.p." and str(cond4).lower() != 'nan'):
                            valueD = self.divide(float(cond4), 1000, isRound=True)

                    total = valueA+valueB+valueC+valueD
                if(count == 0):
                    self.df.loc[i, "Izkazi_A"] = total
                elif(count == 1):
                    self.df.loc[i, "Izkazi_B"] = total
                elif(count == 2):
                    self.df.loc[i, "Izkazi_C"] = total
                elif(count == 3):
                    self.df.loc[i, "Izkazi_D"] = total
                elif(count == 4):
                    self.df.loc[i, "Izkazi_E"] = total
                count = count+1

        
        if (self.df.loc[61, "Izkazi_A"] > 0):
            self.df.loc[62, "Izkazi_A"] = round(self.df.loc[38, "Izkazi_A"]/self.df.loc[61, "Izkazi_A"] * 100) 
        else:
            self.df.loc[62, "Izkazi_A"] = 0
        if(self.df.loc[61, "Izkazi_B"] > 0):    
            self.df.loc[62, "Izkazi_B"] = round(self.df.loc[38, "Izkazi_B"]/self.df.loc[61, "Izkazi_B"] * 100) 
        else:
            self.df.loc[62, "Izkazi_B"] = 0
        if(self.df.loc[61, "Izkazi_C"] > 0):    
            self.df.loc[62, "Izkazi_C"] = round(self.df.loc[38, "Izkazi_C"]/self.df.loc[61, "Izkazi_C"] * 100)
        else:
            self.df.loc[62, "Izkazi_C"] = 0
        if(self.df.loc[61, "Izkazi_D"] > 0):    
            self.df.loc[62, "Izkazi_D"] = round(self.df.loc[38, "Izkazi_D"]/self.df.loc[61, "Izkazi_D"] * 100)
        else:
            self.df.loc[62, "Izkazi_D"] = 0
        if(self.df.loc[61, "Izkazi_E"] > 0):    
            self.df.loc[62, "Izkazi_E"] = round(self.df.loc[38, "Izkazi_E"]/self.df.loc[61, "Izkazi_E"] * 100)
        else:
            self.df.loc[62, "Izkazi_E"] = 0
            
        self.df.loc[63, "Izkazi_A"] = self.df.loc[20, "Izkazi_A"] + self.df.loc[26, "Izkazi_A"] + self.df.loc[29, "Izkazi_A"] - self.df.loc[58, "Izkazi_A"] - self.df.loc[60, "Izkazi_A"] 
        self.df.loc[63, "Izkazi_B"] = self.df.loc[20, "Izkazi_B"] + self.df.loc[26, "Izkazi_B"] + self.df.loc[29, "Izkazi_B"] - self.df.loc[58, "Izkazi_B"] - self.df.loc[60, "Izkazi_B"] 
        self.df.loc[63, "Izkazi_C"] = self.df.loc[20, "Izkazi_C"] + self.df.loc[26, "Izkazi_C"] + self.df.loc[29, "Izkazi_C"] - self.df.loc[58, "Izkazi_C"] - self.df.loc[60, "Izkazi_C"] 
        self.df.loc[63, "Izkazi_D"] = self.df.loc[20, "Izkazi_D"] + self.df.loc[26, "Izkazi_D"] + self.df.loc[29, "Izkazi_D"] - self.df.loc[58, "Izkazi_D"] - self.df.loc[60, "Izkazi_D"] 
        self.df.loc[63, "Izkazi_E"] = self.df.loc[20, "Izkazi_E"] + self.df.loc[26, "Izkazi_E"] + self.df.loc[29, "Izkazi_E"] - self.df.loc[58, "Izkazi_E"] - self.df.loc[60, "Izkazi_E"]
            
        self.df.loc[64, "Izkazi_A"] = self.df.loc[9, "Izkazi_A"] + self.df.loc[22, "Izkazi_A"] + self.df.loc[27, "Izkazi_A"] - self.df.loc[45, "Izkazi_A"] - self.df.loc[55, "Izkazi_A"] 
        self.df.loc[64, "Izkazi_B"] = self.df.loc[9, "Izkazi_B"] + self.df.loc[22, "Izkazi_B"] + self.df.loc[27, "Izkazi_B"] - self.df.loc[45, "Izkazi_B"] - self.df.loc[55, "Izkazi_B"] 
        self.df.loc[64, "Izkazi_C"] = self.df.loc[9, "Izkazi_C"] + self.df.loc[22, "Izkazi_C"] + self.df.loc[27, "Izkazi_C"] - self.df.loc[45, "Izkazi_C"] - self.df.loc[55, "Izkazi_C"] 
        self.df.loc[64, "Izkazi_D"] = self.df.loc[9, "Izkazi_D"] + self.df.loc[22, "Izkazi_D"] + self.df.loc[27, "Izkazi_D"] - self.df.loc[45, "Izkazi_D"] - self.df.loc[55, "Izkazi_D"] 
        self.df.loc[64, "Izkazi_E"] = self.df.loc[9, "Izkazi_E"] + self.df.loc[22, "Izkazi_E"] + self.df.loc[27, "Izkazi_E"] - self.df.loc[45, "Izkazi_E"] - self.df.loc[55, "Izkazi_E"]

        self.df.loc[65, "Izkazi_A"] = self.roundToOne((self.df.loc[28, "Izkazi_A"] + self.df.loc[29, "Izkazi_A"]) / (self.df.loc[59, "Izkazi_A"] + self.df.loc[60, "Izkazi_A"]))
        self.df.loc[65, "Izkazi_B"] = self.roundToOne((self.df.loc[28, "Izkazi_B"] + self.df.loc[29, "Izkazi_B"]) / (self.df.loc[59, "Izkazi_B"] + self.df.loc[60, "Izkazi_B"]))
        self.df.loc[65, "Izkazi_C"] = self.roundToOne((self.df.loc[28, "Izkazi_C"] + self.df.loc[29, "Izkazi_C"]) / (self.df.loc[59, "Izkazi_C"] + self.df.loc[60, "Izkazi_C"]))
        self.df.loc[65, "Izkazi_D"] = self.roundToOne((self.df.loc[28, "Izkazi_D"] + self.df.loc[29, "Izkazi_D"]) / (self.df.loc[59, "Izkazi_D"] + self.df.loc[60, "Izkazi_D"]))
        self.df.loc[65, "Izkazi_E"] = self.roundToOne((self.df.loc[28, "Izkazi_E"] + self.df.loc[29, "Izkazi_E"]) / (self.df.loc[59, "Izkazi_E"] + self.df.loc[60, "Izkazi_E"]))

        self.df.loc[66, "Izkazi_A"] = self.roundToOne((self.df.loc[13, "Izkazi_A"]) / (self.df.loc[41, "Izkazi_A"] + self.df.loc[50, "Izkazi_A"]))
        self.df.loc[66, "Izkazi_B"] = self.roundToOne((self.df.loc[13, "Izkazi_B"]) / (self.df.loc[41, "Izkazi_B"] + self.df.loc[50, "Izkazi_B"]))
        self.df.loc[66, "Izkazi_C"] = self.roundToOne((self.df.loc[13, "Izkazi_C"]) / (self.df.loc[41, "Izkazi_C"] + self.df.loc[50, "Izkazi_C"]))
        self.df.loc[66, "Izkazi_D"] = self.roundToOne((self.df.loc[13, "Izkazi_D"]) / (self.df.loc[41, "Izkazi_D"] + self.df.loc[50, "Izkazi_D"]))
        self.df.loc[66, "Izkazi_E"] = self.roundToOne((self.df.loc[13, "Izkazi_E"]) / (self.df.loc[41, "Izkazi_E"] + self.df.loc[50, "Izkazi_E"]))

        for i in range(0, 62):
            if(self.inputs['isAOP'] == "Da"):
                self.df.loc[i, "strukt"] = round(self.df.loc[i, col[len(self.predopostavke)-1]]/self.df.loc[30, col[len(self.predopostavke)-1]], 2) * 100
            else:
                self.df.loc[i, "strukt"] = round(self.df.loc[i, col[len(self.predopostavke)-2]]/self.df.loc[30, col[len(self.predopostavke)-2]], 2) * 100
            
    def getIndex(self, case, i):
        if(case == 'Izkazi_Gvaop'):
            for j in range(0, len(self.df.Gvaop)):
                if(self.df.Izkazi_Const_Gvaop[i] == self.df.Gvaop[j]):
                    return j
        elif(case == 'Izkazi_B'):
            for j in range(0, len(self.df.Gvaop)):
                if(self.df.Izkazi_Const_B[i] == self.df.Gvaop[j]):
                    return j
        elif(case == 'Izkazi_C'):
            for j in range(0, len(self.df.Gvaop)):
                if(self.df.Izkazi_Const_C[i] == self.df.Gvaop[j]):
                    return j
        elif(case == 'Izkazi_D'):
            for j in range(0, len(self.df.Gvaop)):
                if(self.df.Izkazi_Const_D[i] == self.df.Gvaop[j]):
                    return j
        elif(case == 'Izkazi_AOP'):
            for j in range(0, len(self.df.AOP)):
                if(self.df.Izkazi_Const_AOP[i] == self.df.AOP[j]):
                    return j
        elif(case == 'Izkazi_F'):
            for j in range(0, len(self.df.AOP)):
                if(self.df.Izkazi_Const_F[i] == self.df.AOP[j]):
                    return j
        elif(case == 'Izkazi_G'):
            for j in range(0, len(self.df.AOP)):
                if(self.df.Izkazi_Const_G[i] == self.df.AOP[j]):
                    return j
        elif(case == 'Izkazi_H'):
            for j in range(0, len(self.df.AOP)):
                if(self.df.Izkazi_Const_H[i] == self.df.AOP[j]):
                    return j
    
    def roundToOne(self, val):
        if(val):
            return round(val, 1)

    def divide(self, num1, num2, isRound = False, roundTo = None):
        result = 0
        if(num2 != 0):
            result = num1/num2
            if(str(result).lower() != 'nan'):
                if(isRound):
                    return round(result, roundTo)
        return result

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
