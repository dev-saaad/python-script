from cmath import log
from pythonapp.helper.utils import DataTable

class WeinrichClass(DataTable):
    
    def __init__(self, dataframe, predopostavke, *arg, **kwargs):
        super().__init__(dataframe)
        self.predopostavke = predopostavke
        self.calculated_columns = ["Weinrich_A", "Weinrich_B", "Weinrich_C", "Weinrich_D", "Weinrich_E"]
        
    def compute_tables(self):

        for i in range(0, 41):
            count = 0
            for val in self.predopostavke:
                if(i == 0):
                    self.df.loc[i, "Weinrich_"+chr(count+65)] = self.getValueByGvaopIndex('[00301]', val['Obdobja']) / 1000
                elif(i == 1):
                    self.df.loc[i, "Weinrich_"+chr(count+65)] = self.getValueByGvaopIndex('[003]', val['Obdobja']) / 1000 - self.df.loc[i-1, "Weinrich_"+chr(count+65)]
                elif(i == 2):
                    self.df.loc[i, "Weinrich_"+chr(count+65)] = self.getValueByGvaopIndex('[00102]', val['Obdobja']) / 1000
                elif(i == 3):
                    self.df.loc[i, "Weinrich_"+chr(count+65)] = self.getValueByGvaopIndex('[0010201]', val['Obdobja']) / 1000
                elif(i == 4):
                    self.df.loc[i, "Weinrich_"+chr(count+65)] = self.df.loc[i-2, "Weinrich_"+chr(count+65)] - self.df.loc[i-1, "Weinrich_"+chr(count+65)]
                elif(i == 5):
                    self.df.loc[i, "Weinrich_"+chr(count+65)] = self.getValueByGvaopIndex('[0010204]', val['Obdobja']) / 1000
                elif(i == 6):
                    self.df.loc[i, "Weinrich_"+chr(count+65)] = self.getValueByGvaopIndex('[0030305]', val['Obdobja']) / 1000
                elif(i == 7):
                    self.df.loc[i, "Weinrich_"+chr(count+65)] = self.getValueByGvaopIndex('[060]', val['Obdobja']) / 1000
                elif(i == 8):
                    self.df.loc[i, "Weinrich_"+chr(count+65)] = self.getValueByGvaopIndex('[071]', val['Obdobja']) / 1000
                elif(i == 9):
                    self.df.loc[i, "Weinrich_"+chr(count+65)] = self.getValueByGvaopIndex('[06404]', val['Obdobja']) / 1000
                elif(i == 10):
                    self.df.loc[i, "Weinrich_"+chr(count+65)] = self.getValueByGvaopIndex('[050]', val['Obdobja']) / 1000
                elif(i == 11):
                    self.df.loc[i, "Weinrich_"+chr(count+65)] = self.getValueByGvaopIndex('[075]', val['Obdobja']) / 1000
                elif(i == 12):
                    self.df.loc[i, "Weinrich_"+chr(count+65)] = self.getValueByGvaopIndex('[0570101]', val['Obdobja']) / 1000
                elif(i == 13):
                    self.df.loc[i, "Weinrich_"+chr(count+65)] = self.getValueByGvaopIndex('[0030204]', val['Obdobja']) / 1000
                elif(i == 14):
                    self.df.loc[i, "Weinrich_"+chr(count+65)] = self.getValueByGvaopIndex('[00304]', val['Obdobja']) / 1000
                elif(i == 15):
                    self.df.loc[i, "Weinrich_"+chr(count+65)] = self.getValueByGvaopIndex('[00103]', val['Obdobja']) / 1000
                elif(i == 16):
                    self.df.loc[i, "Weinrich_"+chr(count+65)] = self.getValueByGvaopIndex('[0030104]', val['Obdobja']) / 1000
                elif(i == 17):
                    self.df.loc[i, "Weinrich_"+chr(count+65)] = self.df.loc[11, "Weinrich_"+chr(count+65)] + self.df.loc[12, "Weinrich_"+chr(count+65)] + self.df.loc[13, "Weinrich_"+chr(count+65)] + self.df.loc[14, "Weinrich_"+chr(count+65)] + self.df.loc[15, "Weinrich_"+chr(count+65)] + self.df.loc[16, "Weinrich_"+chr(count+65)]
                elif(i == 18):
                    self.df.loc[i, "Weinrich_"+chr(count+65)] = self.getValueByGvaopIndex('[05501]', val['Obdobja']) / 1000
                elif(i == 19):
                    self.df.loc[i, "Weinrich_"+chr(count+65)] = self.getValueByGvaopIndex('[003030502]', val['Obdobja']) / 1000

                elif(i == 22):
                    self.df.loc[i, "Weinrich_"+chr(count+65)] = self.df.loc[0, "Weinrich_"+chr(count+65)] / self.df.loc[1, "Weinrich_"+chr(count+65)]
                elif(i == 23):
                    self.df.loc[i, "Weinrich_"+chr(count+65)] = self.df.loc[4, "Weinrich_"+chr(count+65)] / self.df.loc[0, "Weinrich_"+chr(count+65)]
                elif(i == 24):
                    self.df.loc[i, "Weinrich_"+chr(count+65)] = (self.df.loc[5, "Weinrich_"+chr(count+65)] - self.df.loc[6, "Weinrich_"+chr(count+65)]) / self.df.loc[7, "Weinrich_"+chr(count+65)]
                elif(i == 25):
                    self.df.loc[i, "Weinrich_"+chr(count+65)] = (self.df.loc[8, "Weinrich_"+chr(count+65)] + self.df.loc[9, "Weinrich_"+chr(count+65)]) / self.df.loc[0, "Weinrich_"+chr(count+65)]
                elif(i == 26):
                    self.df.loc[i, "Weinrich_"+chr(count+65)] =  self.df.loc[10, "Weinrich_"+chr(count+65)] / self.df.loc[0, "Weinrich_"+chr(count+65)]
                elif(i == 27):
                    self.df.loc[i, "Weinrich_"+chr(count+65)] = self.df.loc[1, "Weinrich_"+chr(count+65)] / self.df.loc[17, "Weinrich_"+chr(count+65)]
                elif(i == 28):
                    self.df.loc[i, "Weinrich_"+chr(count+65)] = (self.df.loc[1, "Weinrich_"+chr(count+65)] - self.df.loc[5, "Weinrich_"+chr(count+65)]) / (self.df.loc[17, "Weinrich_"+chr(count+65)] - self.df.loc[3, "Weinrich_"+chr(count+65)])
                elif(i == 29):
                    self.df.loc[i, "Weinrich_"+chr(count+65)] = self.df.loc[19, "Weinrich_"+chr(count+65)] / self.df.loc[18, "Weinrich_"+chr(count+65)]

                elif(i == 32):
                    if self.df.loc[22, "Weinrich_"+chr(count+65)] > 0.433:
                        self.df.loc[i, "Weinrich_"+chr(count+65)] =  1
                    elif self.df.loc[22, "Weinrich_"+chr(count+65)] > 0.121:
                        self.df.loc[i, "Weinrich_"+chr(count+65)] =  2
                    elif self.df.loc[22, "Weinrich_"+chr(count+65)] > 0.085:
                        self.df.loc[i, "Weinrich_"+chr(count+65)] =  3
                    elif self.df.loc[22, "Weinrich_"+chr(count+65)] > -0.047:
                        self.df.loc[i, "Weinrich_"+chr(count+65)] =  4
                    elif self.df.loc[22, "Weinrich_"+chr(count+65)] < 0.047:
                        self.df.loc[i, "Weinrich_"+chr(count+65)] =  5
                    else:
                        self.df.loc[i, "Weinrich_"+chr(count+65)] =  0
                elif(i == 33):
                    if self.df.loc[23, "Weinrich_"+chr(count+65)] > 0.075:
                        self.df.loc[i, "Weinrich_"+chr(count+65)] =  1
                    elif self.df.loc[23, "Weinrich_"+chr(count+65)] > 0.02:
                        self.df.loc[i, "Weinrich_"+chr(count+65)] =  2
                    elif self.df.loc[23, "Weinrich_"+chr(count+65)] > 0.009:
                        self.df.loc[i, "Weinrich_"+chr(count+65)] =  3
                    elif self.df.loc[23, "Weinrich_"+chr(count+65)] > 0.002:
                        self.df.loc[i, "Weinrich_"+chr(count+65)] =  4
                    elif self.df.loc[23, "Weinrich_"+chr(count+65)] < 0.002:
                        self.df.loc[i, "Weinrich_"+chr(count+65)] =  5
                    else:
                        self.df.loc[i, "Weinrich_"+chr(count+65)] =  0
                elif(i == 34):
                    if self.df.loc[24, "Weinrich_"+chr(count+65)] > -0.088:
                        self.df.loc[i, "Weinrich_"+chr(count+65)] =  1
                    elif self.df.loc[24, "Weinrich_"+chr(count+65)] > -0.293:
                        self.df.loc[i, "Weinrich_"+chr(count+65)] =  2
                    elif self.df.loc[24, "Weinrich_"+chr(count+65)] > -0.462:
                        self.df.loc[i, "Weinrich_"+chr(count+65)] =  3
                    elif self.df.loc[24, "Weinrich_"+chr(count+65)] > -0.899:
                        self.df.loc[i, "Weinrich_"+chr(count+65)] =  4
                    elif self.df.loc[24, "Weinrich_"+chr(count+65)] < -0.899:
                        self.df.loc[i, "Weinrich_"+chr(count+65)] =  5
                    else:
                        self.df.loc[i, "Weinrich_"+chr(count+65)] =  0
                elif(i == 35):
                    if self.df.loc[25, "Weinrich_"+chr(count+65)] > 0.213:
                        self.df.loc[i, "Weinrich_"+chr(count+65)] =  1
                    elif self.df.loc[25, "Weinrich_"+chr(count+65)] > 0.072:
                        self.df.loc[i, "Weinrich_"+chr(count+65)] =  2
                    elif self.df.loc[25, "Weinrich_"+chr(count+65)] > 0.043:
                        self.df.loc[i, "Weinrich_"+chr(count+65)] =  3
                    elif self.df.loc[25, "Weinrich_"+chr(count+65)] > 0.009:
                        self.df.loc[i, "Weinrich_"+chr(count+65)] =  4
                    elif self.df.loc[25, "Weinrich_"+chr(count+65)] < 0.009:
                        self.df.loc[i, "Weinrich_"+chr(count+65)] =  5
                    else:
                        self.df.loc[i, "Weinrich_"+chr(count+65)] =  0
                elif(i == 36):
                    if self.df.loc[26, "Weinrich_"+chr(count+65)] > 2.574:
                        self.df.loc[i, "Weinrich_"+chr(count+65)] =  1
                    elif self.df.loc[26, "Weinrich_"+chr(count+65)] > 2.007:
                        self.df.loc[i, "Weinrich_"+chr(count+65)] =  2
                    elif self.df.loc[26, "Weinrich_"+chr(count+65)] > 0.907:
                        self.df.loc[i, "Weinrich_"+chr(count+65)] =  3
                    elif self.df.loc[26, "Weinrich_"+chr(count+65)] > 0.621:
                        self.df.loc[i, "Weinrich_"+chr(count+65)] =  4
                    elif self.df.loc[26, "Weinrich_"+chr(count+65)] < 0.621:
                        self.df.loc[i, "Weinrich_"+chr(count+65)] =  5
                    else:
                        self.df.loc[i, "Weinrich_"+chr(count+65)] =  0
                elif(i == 37):
                    if self.df.loc[27, "Weinrich_"+chr(count+65)] < 2.849:
                        self.df.loc[i, "Weinrich_"+chr(count+65)] =  1
                    elif self.df.loc[27, "Weinrich_"+chr(count+65)] < 12.103:
                        self.df.loc[i, "Weinrich_"+chr(count+65)] =  2
                    elif self.df.loc[27, "Weinrich_"+chr(count+65)] < 14.517:
                        self.df.loc[i, "Weinrich_"+chr(count+65)] =  3
                    elif self.df.loc[27, "Weinrich_"+chr(count+65)] < 99.899:
                        self.df.loc[i, "Weinrich_"+chr(count+65)] =  4
                    elif self.df.loc[27, "Weinrich_"+chr(count+65)] > 99.9:
                        self.df.loc[i, "Weinrich_"+chr(count+65)] =  5
                    else:
                        self.df.loc[i, "Weinrich_"+chr(count+65)] =  0
                elif(i == 38):
                    if self.df.loc[28, "Weinrich_"+chr(count+65)] < 1.653:
                        self.df.loc[i, "Weinrich_"+chr(count+65)] =  1
                    elif self.df.loc[28, "Weinrich_"+chr(count+65)] < 11.683:
                        self.df.loc[i, "Weinrich_"+chr(count+65)] =  2
                    elif self.df.loc[28, "Weinrich_"+chr(count+65)] < 12.312:
                        self.df.loc[i, "Weinrich_"+chr(count+65)] =  3
                    elif self.df.loc[28, "Weinrich_"+chr(count+65)] < 99.899:
                        self.df.loc[i, "Weinrich_"+chr(count+65)] =  4
                    elif self.df.loc[28, "Weinrich_"+chr(count+65)] > 99.9:
                        self.df.loc[i, "Weinrich_"+chr(count+65)] =  5
                    else:
                        self.df.loc[i, "Weinrich_"+chr(count+65)] =  0
                elif(i == 39):
                    if self.df.loc[29, "Weinrich_"+chr(count+65)] < 0.097:
                        self.df.loc[i, "Weinrich_"+chr(count+65)] =  1
                    elif self.df.loc[29, "Weinrich_"+chr(count+65)] < 0.278:
                        self.df.loc[i, "Weinrich_"+chr(count+65)] =  2
                    elif self.df.loc[29, "Weinrich_"+chr(count+65)] < 0.479:
                        self.df.loc[i, "Weinrich_"+chr(count+65)] =  3
                    elif self.df.loc[29, "Weinrich_"+chr(count+65)] < 0.799:
                        self.df.loc[i, "Weinrich_"+chr(count+65)] =  4
                    elif self.df.loc[29, "Weinrich_"+chr(count+65)] > 0.799:
                        self.df.loc[i, "Weinrich_"+chr(count+65)] =  5
                    else:
                        self.df.loc[i, "Weinrich_"+chr(count+65)] =  0
                elif(i == 40):
                    self.df.loc[i, "Weinrich_"+chr(count+65)] =  self.df.loc[32, "Weinrich_"+chr(count+65)] + self.df.loc[33, "Weinrich_"+chr(count+65)] + self.df.loc[34, "Weinrich_"+chr(count+65)] + self.df.loc[35, "Weinrich_"+chr(count+65)] + self.df.loc[36, "Weinrich_"+chr(count+65)] + self.df.loc[37, "Weinrich_"+chr(count+65)] + self.df.loc[38, "Weinrich_"+chr(count+65)] + self.df.loc[39, "Weinrich_"+chr(count+65)]

                count = count + 1

    def getValueByGvaopIndex(self, gvaop, year) -> float:
        try:
            return self.df.loc[self.df['Gvaop'] == gvaop, year].values[0]
        except:
            return 0
        
    def divide(self, num1, num2, isRound = False, roundTo = None):
        result = 0
        if(num2 != 0):
            result = num1/num2
            if(str(result).lower() != 'nan'):
                if(isRound):
                    return round(result, roundTo)
        return result

    @property
    def Weinrich_A(self):
        return self.df.Weinrich_A
    
    @property
    def Weinrich_B(self):
        return self.df.Weinrich_B
    
    @property
    def Weinrich_C(self):
        return self.df.Weinrich_C

    @property
    def Weinrich_D(self):
        return self.df.Weinrich_D
    
    @property
    def Weinrich_E(self):
        return self.df.Weinrich_E
