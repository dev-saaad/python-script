from pythonapp.helper.utils import DataTable

class Izkazi2NewClass(DataTable):
    
    def __init__(self, dataframe, predopostavke, *arg, **kwargs):
        super().__init__(dataframe)
        self.predopostavke = predopostavke
        self.calculated_columns = ["Izkazi2_A", "Izkazi2_B", "Izkazi2_C", "Izkazi2_D", "Izkazi2_E", "Izkazi2_strukt"]
        
    def compute_tables(self):
        self.df.loc[0, "Izkazi2_A"] = None
        self.df.loc[0, "Izkazi2_B"] = None
        self.df.loc[0, "Izkazi2_C"] = None
        self.df.loc[0, "Izkazi2_D"] = None
        self.df.loc[0, "Izkazi2_E"] = None
        col = ["Izkazi_A", "Izkazi_B", "Izkazi_C", "Izkazi_D", "Izkazi_E"]
        col2 = ["Izkazi2_A", "Izkazi2_B", "Izkazi2_C", "Izkazi2_D", "Izkazi2_E"]
        for i in range(0, 34):
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
                    index1 = self.getIndex('Izkazi2_Gvaop', i)
                    index2 = self.getIndex('Izkazi2_B', i)
                    index3 = self.getIndex('Izkazi2_C', i)
                    index4 = self.getIndex('Izkazi2_D', i)
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
                    index5 = self.getIndex('Izkazi2_AOP', i)
                    index6 = self.getIndex('Izkazi2_F', i)
                    index7 = self.getIndex('Izkazi2_G', i)
                    index8 = self.getIndex('Izkazi2_H', i)
                    if(index5 != None):
                        cond5 = self.df[val['Obdobja']][index5]
                        if(cond5 != "n.p." and str(cond5).lower() != 'nan'):
                            valueA = self.divide(float(cond5), 1000, isRound=True)
                    if(index6 != None):
                        cond6 = self.df[val['Obdobja']][index6]
                        if(cond6 != "n.p." and str(cond6).lower() != 'nan'):
                            valueB = self.divide(float(cond6), 1000, isRound=True)
                    if(index7 != None):
                        cond7 = self.df[val['Obdobja']][index7]
                        if(cond7 != "n.p." and str(cond7).lower() != 'nan'):
                            valueC = self.divide(float(cond7), 1000, isRound=True)
                    if(index8 != None):
                        cond8 = self.df[val['Obdobja']][index8]
                        if(cond8 != "n.p." and str(cond8).lower() != 'nan'):
                            valueD = self.divide(float(cond8), 1000, isRound=True)

                    total = valueA+valueB+valueC+valueD
                
                if(count == 0):
                    self.df.loc[i, "Izkazi2_A"] = total
                elif(count == 1):
                    self.df.loc[i, "Izkazi2_B"] = total
                elif(count == 2):
                    self.df.loc[i, "Izkazi2_C"] = total
                elif(count == 3):
                    self.df.loc[i, "Izkazi2_D"] = total
                elif(count == 4):
                    self.df.loc[i, "Izkazi2_E"] = total
                count = count+1

            if(i == 5 or ( i >= 10 and i <= 17) or ( i >= 20 and i <= 23) or ( i >= 25 and i <= 128)):
                self.df.loc[i, "Izkazi2_A"] = -self.df.loc[i, "Izkazi2_A"]
                self.df.loc[i, "Izkazi2_B"] = -self.df.loc[i, "Izkazi2_B"]
                self.df.loc[i, "Izkazi2_C"] = -self.df.loc[i, "Izkazi2_C"]
                self.df.loc[i, "Izkazi2_D"] = -self.df.loc[i, "Izkazi2_D"]
                self.df.loc[i, "Izkazi2_E"] = -self.df.loc[i, "Izkazi2_E"]
            else:
                self.df.loc[i, "Izkazi2_A"] = self.df.loc[i, "Izkazi2_A"]
                self.df.loc[i, "Izkazi2_B"] = self.df.loc[i, "Izkazi2_B"]
                self.df.loc[i, "Izkazi2_C"] = self.df.loc[i, "Izkazi2_C"]
                self.df.loc[i, "Izkazi2_D"] = self.df.loc[i, "Izkazi2_D"]
                self.df.loc[i, "Izkazi2_E"] = self.df.loc[i, "Izkazi2_E"]
            
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
                
                if(self.df.loc[64, col[len(self.predopostavke)-1]] > 0):
                    self.df.loc[i, col2[len(self.predopostavke)-1]] = 0
                else:
                    self.df.loc[i, col2[len(self.predopostavke)-1]] = round(-self.df.loc[64, col[len(self.predopostavke)-1]] / (self.df.loc[13, col2[len(self.predopostavke)-1]]/self.predopostavke[-1]['St_Mesecev']*12), 1)


            if(i == 32):
                self.df.loc[i, "Izkazi2_A"] = round(self.df.loc[13, "Izkazi2_A"] / self.df.loc[55, "Izkazi_A"], 1)
                self.df.loc[i, "Izkazi2_B"] = round(self.df.loc[13, "Izkazi2_B"] / self.df.loc[55, "Izkazi_B"], 1)
                self.df.loc[i, "Izkazi2_C"] = round(self.df.loc[13, "Izkazi2_C"] / self.df.loc[55, "Izkazi_C"], 1)
                self.df.loc[i, "Izkazi2_D"] = round(self.df.loc[13, "Izkazi2_D"] / self.df.loc[55, "Izkazi_D"], 1)
                self.df.loc[i, col2[len(self.predopostavke)-1]] = round( (self.df.loc[13, col2[len(self.predopostavke)-1]] / self.predopostavke[-1]['St_Mesecev']*12) / self.df.loc[55, col[len(self.predopostavke)-1]], 1)

            if(i == 33):
                self.df.loc[i, "Izkazi2_A"] = -round(self.df.loc[18, "Izkazi2_A"] / self.df.loc[23, "Izkazi2_A"], 1)
                self.df.loc[i, "Izkazi2_B"] = -round(self.df.loc[18, "Izkazi2_B"] / self.df.loc[23, "Izkazi2_B"], 1)
                self.df.loc[i, "Izkazi2_C"] = -round(self.df.loc[18, "Izkazi2_C"] / self.df.loc[23, "Izkazi2_C"], 1)
                self.df.loc[i, "Izkazi2_D"] = -round(self.df.loc[18, "Izkazi2_D"] / self.df.loc[23, "Izkazi2_D"], 1)
                self.df.loc[i, "Izkazi2_E"] = -round(self.df.loc[18, "Izkazi2_E"] / self.df.loc[23, "Izkazi2_E"], 1)
            
            if i < 29:
                if self.df.loc[i, "Izkazi2_D"] > 0 :
                    self.df.loc[i, "Izkazi2_strukt"] = round(((self.df.loc[i, "Izkazi2_E"]/self.df.loc[i, "Izkazi2_D"])-1), 2)   *100
                else:
                    self.df.loc[i, "Izkazi2_strukt"] = 0

    def divide(self, num1, num2, isRound = False, roundTo = None):
        result = 0
        if(num2 != 0):
            result = num1/num2
            if(str(result).lower() != 'nan'):
                if(isRound):
                    return round(result, roundTo)
        return result

    def getIndex(self, case, i):
        i = i + 75
        if(case == 'Izkazi2_Gvaop'):
            for j in range(0, len(self.df.Gvaop)):
                if(self.df.Izkazi_Const_Gvaop[i] == self.df.Gvaop[j]):
                    return j
        elif(case == 'Izkazi2_B'):
            for j in range(0, len(self.df.Gvaop)):
                if(self.df.Izkazi_Const_B[i] == self.df.Gvaop[j]):
                    return j
        elif(case == 'Izkazi2_C'):
            for j in range(0, len(self.df.Gvaop)):
                if(self.df.Izkazi_Const_C[i] == self.df.Gvaop[j]):
                    return j
        elif(case == 'Izkazi2_D'):
            for j in range(0, len(self.df.Gvaop)):
                if(self.df.Izkazi_Const_D[i] == self.df.Gvaop[j]):
                    return j
        elif(case == 'Izkazi2_AOP'):
            for j in range(0, len(self.df.AOP)):
                if(self.df.Izkazi_Const_AOP[i] == self.df.AOP[j]):
                    return j
        elif(case == 'Izkazi2_F'):
            for j in range(0, len(self.df.AOP)):
                if(self.df.Izkazi_Const_F[i] == self.df.AOP[j]):
                    return j
        elif(case == 'Izkazi2_G'):
            for j in range(0, len(self.df.AOP)):
                if(self.df.Izkazi_Const_G[i] == self.df.AOP[j]):
                    return j
        elif(case == 'Izkazi2_H'):
            for j in range(0, len(self.df.AOP)):
                if(self.df.Izkazi_Const_H[i] == self.df.AOP[j]):
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