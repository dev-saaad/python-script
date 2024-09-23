from pythonapp.helper.utils import DataTable
import pandas as pd

class ReportClass(DataTable):
    
    def __init__(self, dataframe, info, *arg, **kwargs):
        super().__init__(dataframe)
        self.calculated_columns = ["Report_A", "Report_B", "Report_C", "Report_D", "Report_E", "Report_F", "Report_G", "Report_H", "Report_I", "Report_J", "Report_K", "Report_L", "Report_M", "Report_N", "Report_O", "Report_P", "Report_Q", "Report_R"]
        self.output_cols = []
        self.info = info
        
    def compute_tables(self):
        self.df.loc[0, "Report_A"] = None
        self.df.loc[0, "Report_B"] = None
        self.df.loc[0, "Report_C"] = None
        self.df.loc[0, "Report_D"] = None
        self.df.loc[0, "Report_E"] = None
        self.df.loc[0, "Report_F"] = None
        self.df.loc[0, "Report_G"] = None
        self.df.loc[0, "Report_H"] = None
        self.df.loc[0, "Report_I"] = None
        self.df.loc[0, "Report_J"] = None
        self.df.loc[0, "Report_K"] = None
        self.df.loc[0, "Report_L"] = None
        self.df.loc[0, "Report_M"] = None
        self.df.loc[0, "Report_N"] = None
        self.df.loc[0, "Report_O"] = None
        self.df.loc[0, "Report_P"] = None
        self.df.loc[0, "Report_Q"] = None
        self.df.loc[0, "Report_R"] = None

        if(self.info.Imamo_podatke_za == "Da"):
            data8 = ((self.df.loc[3, "Izkazi2_E"]/self.df.loc[0, "St_Mesecev"]*12)/self.df.loc[3, "Izkazi2_D"])-1
        else:
            data8 = (self.df.loc[3, "Izkazi2_D"]/self.df.loc[3, "Izkazi2_C"])-1


        for i in range(1, 346):
            
            if(i == 3):
                self.df.loc[i, "Report_A"] = self.info.Dolznik
            if(i == 5):
                self.df.loc[i, "Report_A"] = self.info.Naslov
            if(i == 6):
                self.df.loc[i, "Report_B"] = self.info.Maticna_stevilka
            if(i == 7):
                self.df.loc[i, "Report_B"] = self.info.Davcna_stevilka

            if(i == 13):
                self.df.loc[i, "Report_J"] = self.info.Priporocen_limit_W18
                self.df.loc[i, "Report_K"] = self.info.Priporocen_limit_W19

            if(i == 16):
                self.df.loc[i, "Report_K"] = self.info.Povprecni_dnevi_zamud
                self.df.loc[i, "Report_O"] = self.info.Max_dnevi_zamud
            
            if(i == 17):
                self.df.loc[i, "Report_F"] = self.info.Cesija_K1

            

            if(i == 19):
                if(self.info.Imamo_podatke_za == "Da"):
                    if(data8 < 0-self.info.Pogoj):
                        self.df.loc[i, "Report_H"] = round(self.df.loc[4, "Kazalniki_114"]*1000)
                    else:
                        self.df.loc[i, "Report_H"] = round(((self.df.loc[4, "Kazalniki_114"] + self.df.loc[3, "Kazalniki_114"])/2)*1000)
                    
                    self.df.loc[i, "Report_K"] = round((self.df.loc[3, "Kazalniki_20"] + self.df.loc[4, "Kazalniki_20"])/2, 2)
                else:
                    if(data8 < 0-self.info.Pogoj):
                        self.df.loc[i, "Report_H"] = round(self.df.loc[3, "Kazalniki_114"]*1000)
                    else:
                        self.df.loc[i, "Report_H"] = round(((self.df.loc[3, "Kazalniki_114"] + self.df.loc[2, "Kazalniki_114"])/2)*1000)

                    self.df.loc[i, "Report_K"] = round((self.df.loc[2, "Kazalniki_20"] + self.df.loc[3, "Kazalniki_20"])/2, 2)

                self.df.loc[i, "Report_O"] = round(self.info.Pogoj/100)
            
            if(i == 20):
                self.df.loc[i, "Report_H"] = min(self.df.loc[i-1, "Report_H"] , self.info.Max_limit_E13)


            if(i == 22):
                self.df.loc[i, "Report_K"] = self.info.Stevilo_blokiranih_TRR
                self.df.loc[i, "Report_O"] = self.info.Stevilo_rezervacij
            
            if(i == 25):
                self.df.loc[i, "Report_K"] = self.info.Lastniki
                self.df.loc[i, "Report_O"] = self.info.Zastopniki

            if(i == 27):
                self.df.loc[i, "Report_B"] = self.df.loc[0, "St_Mesecev"]
            if(i == 29):
                self.df.loc[i, "Report_B"] = self.df.loc[4, "Obdobja_BS"]
                self.df.loc[i, "Report_C"] = self.df.loc[3, "Obdobja_BS"]
                self.df.loc[i, "Report_D"] = self.df.loc[2, "Obdobja_BS"]
                self.df.loc[i, "Report_E"] = self.df.loc[1, "Obdobja_BS"]
                self.df.loc[i, "Report_F"] = self.df.loc[0, "Obdobja_BS"]
            
            if(i == 30):
                self.reportForIskazi(i, 30)
            
            if(i == 31):
                self.reportForIskazi(i, 38, -1)

            if(i == 32):
                self.df.loc[i, "Report_B"] = -self.df.loc[45, "Izkazi_A"] - self.df.loc[55, "Izkazi_A"]
                self.df.loc[i, "Report_C"] = -self.df.loc[45, "Izkazi_B"] - self.df.loc[55, "Izkazi_B"]
                self.df.loc[i, "Report_D"] = -self.df.loc[45, "Izkazi_C"] - self.df.loc[55, "Izkazi_C"]
                self.df.loc[i, "Report_E"] = -self.df.loc[45, "Izkazi_D"] - self.df.loc[55, "Izkazi_D"]
                self.df.loc[i, "Report_F"] = -self.df.loc[45, "Izkazi_E"] - self.df.loc[55, "Izkazi_E"]
            
            if(i == 33):
                self.df.loc[i, "Report_B"] = (-self.df.loc[30, "Izkazi_A"] + self.df.loc[38, "Izkazi_A"]) - self.df.loc[32, "Report_B"]
                self.df.loc[i, "Report_C"] = (-self.df.loc[30, "Izkazi_B"] + self.df.loc[38, "Izkazi_B"]) - self.df.loc[32, "Report_C"]
                self.df.loc[i, "Report_D"] = (-self.df.loc[30, "Izkazi_C"] + self.df.loc[38, "Izkazi_C"]) - self.df.loc[32, "Report_D"]
                self.df.loc[i, "Report_E"] = (-self.df.loc[30, "Izkazi_D"] + self.df.loc[38, "Izkazi_D"]) - self.df.loc[32, "Report_E"]
                self.df.loc[i, "Report_F"] = (-self.df.loc[30, "Izkazi_E"] + self.df.loc[38, "Izkazi_E"]) - self.df.loc[32, "Report_F"]
########################################################
            if(i == 34):
                self.df.loc[i, "Report_B"] = self.df.loc[4, "Obdobja_IPI"]
                self.df.loc[i, "Report_C"] = self.df.loc[3, "Obdobja_IPI"]
                self.df.loc[i, "Report_D"] = self.df.loc[2, "Obdobja_IPI"]
                self.df.loc[i, "Report_E"] = self.df.loc[1, "Obdobja_IPI"]
                self.df.loc[i, "Report_F"] = self.df.loc[0, "Obdobja_IPI"]
            
            if(i == 35):
                self.df.loc[i, "Report_B"] = self.df.loc[3, "Izkazi2_A"] + self.df.loc[4, "Izkazi2_A"] + self.df.loc[8, "Izkazi2_A"] + self.df.loc[19, "Izkazi2_A"] + self.df.loc[24, "Izkazi2_A"]
                self.df.loc[i, "Report_C"] = self.df.loc[3, "Izkazi2_B"] + self.df.loc[4, "Izkazi2_B"] + self.df.loc[8, "Izkazi2_B"] + self.df.loc[19, "Izkazi2_B"] + self.df.loc[24, "Izkazi2_B"]
                self.df.loc[i, "Report_D"] = self.df.loc[3, "Izkazi2_C"] + self.df.loc[4, "Izkazi2_C"] + self.df.loc[8, "Izkazi2_C"] + self.df.loc[19, "Izkazi2_C"] + self.df.loc[24, "Izkazi2_C"]
                self.df.loc[i, "Report_E"] = self.df.loc[3, "Izkazi2_D"] + self.df.loc[4, "Izkazi2_D"] + self.df.loc[8, "Izkazi2_D"] + self.df.loc[19, "Izkazi2_D"] + self.df.loc[24, "Izkazi2_D"]
                self.df.loc[i, "Report_F"] = self.df.loc[3, "Izkazi2_E"] + self.df.loc[4, "Izkazi2_E"] + self.df.loc[8, "Izkazi2_E"] + self.df.loc[19, "Izkazi2_E"] + self.df.loc[24, "Izkazi2_E"]

            if(i == 36):
                self.df.loc[i, "Report_B"] = self.df.loc[5, "Izkazi2_A"] + self.df.loc[10, "Izkazi2_A"] + self.df.loc[11, "Izkazi2_A"] + self.df.loc[12, "Izkazi2_A"] + self.df.loc[17, "Izkazi2_A"] + self.df.loc[23, "Izkazi2_A"] + self.df.loc[25, "Izkazi2_A"]
                self.df.loc[i, "Report_C"] = self.df.loc[5, "Izkazi2_B"] + self.df.loc[10, "Izkazi2_B"] + self.df.loc[11, "Izkazi2_B"] + self.df.loc[12, "Izkazi2_B"] + self.df.loc[17, "Izkazi2_B"] + self.df.loc[23, "Izkazi2_B"] + self.df.loc[25, "Izkazi2_B"]
                self.df.loc[i, "Report_D"] = self.df.loc[5, "Izkazi2_C"] + self.df.loc[10, "Izkazi2_C"] + self.df.loc[11, "Izkazi2_C"] + self.df.loc[12, "Izkazi2_C"] + self.df.loc[17, "Izkazi2_C"] + self.df.loc[23, "Izkazi2_C"] + self.df.loc[25, "Izkazi2_C"]
                self.df.loc[i, "Report_E"] = self.df.loc[5, "Izkazi2_D"] + self.df.loc[10, "Izkazi2_D"] + self.df.loc[11, "Izkazi2_D"] + self.df.loc[12, "Izkazi2_D"] + self.df.loc[17, "Izkazi2_D"] + self.df.loc[23, "Izkazi2_D"] + self.df.loc[25, "Izkazi2_D"]
                self.df.loc[i, "Report_F"] = self.df.loc[5, "Izkazi2_E"] + self.df.loc[10, "Izkazi2_E"] + self.df.loc[11, "Izkazi2_E"] + self.df.loc[12, "Izkazi2_E"] + self.df.loc[17, "Izkazi2_E"] + self.df.loc[23, "Izkazi2_E"] + self.df.loc[25, "Izkazi2_E"]
            
            if(i == 37):
                val133B = self.df.loc[3, "Izkazi2_A"] + self.df.loc[4, "Izkazi2_A"] + self.df.loc[8, "Izkazi2_A"] + self.df.loc[19, "Izkazi2_A"] + self.df.loc[24, "Izkazi2_A"]
                val133C = self.df.loc[3, "Izkazi2_B"] + self.df.loc[4, "Izkazi2_B"] + self.df.loc[8, "Izkazi2_B"] + self.df.loc[19, "Izkazi2_B"] + self.df.loc[24, "Izkazi2_B"]
                val133D = self.df.loc[3, "Izkazi2_C"] + self.df.loc[4, "Izkazi2_C"] + self.df.loc[8, "Izkazi2_C"] + self.df.loc[19, "Izkazi2_C"] + self.df.loc[24, "Izkazi2_C"]
                val133E = self.df.loc[3, "Izkazi2_D"] + self.df.loc[4, "Izkazi2_D"] + self.df.loc[8, "Izkazi2_D"] + self.df.loc[19, "Izkazi2_D"] + self.df.loc[24, "Izkazi2_D"]
                val133F = self.df.loc[3, "Izkazi2_E"] + self.df.loc[4, "Izkazi2_E"] + self.df.loc[8, "Izkazi2_E"] + self.df.loc[19, "Izkazi2_E"] + self.df.loc[24, "Izkazi2_E"]
                
                self.df.loc[i, "Report_B"] = round((val133B + self.df.loc[i-1, "Report_B"]) / val133B * 100)
                self.df.loc[i, "Report_C"] = round((val133C + self.df.loc[i-1, "Report_C"]) / val133C  * 100)
                self.df.loc[i, "Report_D"] = round((val133D + self.df.loc[i-1, "Report_D"]) / val133D * 100)
                self.df.loc[i, "Report_E"] = round((val133E + self.df.loc[i-1, "Report_E"]) / val133E * 100)
                self.df.loc[i, "Report_F"] = round((val133F + self.df.loc[i-1, "Report_F"]) / val133F * 100)

            if(i == 39 or i == 49 or i == 59):
                if(self.info.Imamo_podatke_za == "Da"):
                    self.df.loc[i, "Report_D"] = self.df.loc[2, "Obdobja_IPI"]
                    self.df.loc[i, "Report_F"] = self.df.loc[1, "Obdobja_IPI"]
                    self.df.loc[i, "Report_H"] = self.df.loc[0, "Obdobja_IPI"]
                else:
                    self.df.loc[i, "Report_D"] = self.df.loc[3, "Obdobja_IPI"]
                    self.df.loc[i, "Report_F"] = self.df.loc[2, "Obdobja_IPI"]
                    self.df.loc[i, "Report_H"] = self.df.loc[1, "Obdobja_IPI"]

            if( i == 40):
                self.reportForIskazi2NxtCol(i, 7)
            if( i == 41):
                self.reportForIskazi2NxtCol(i, 13)
            if( i == 42):
                self.reportForIskazi2NxtCol(i, 29)
            if( i == 43):
                self.reportForIskazi2NxtCol(i, 30)

            if(i >= 40 and i <= 43):
                self.calMethod1(i)

            if(i == 44):
                self.df.loc[i, "Report_D"] = round(self.df.loc[i-1, "Report_D"] / self.df.loc[i-2, "Report_D"], 1)
                self.df.loc[i, "Report_F"] = round(self.df.loc[i-1, "Report_F"] / self.df.loc[i-2, "Report_F"], 1)
                self.df.loc[i, "Report_H"] = round(self.df.loc[i-1, "Report_H"] / self.df.loc[i-2, "Report_H"], 1)
            
            if(i >= 45 and i <= 46):
                self.calMethod1(i)

            if(i >= 50 and i <= 54):
                self.calMethod1(i)

            if(i == 55):
                self.df.loc[i, "Report_D"] = self.rangeSum(i-5, i-1, "Report_D")
                self.df.loc[i, "Report_F"] = self.rangeSum(i-5, i-1, "Report_F")
                self.df.loc[i, "Report_H"] = self.rangeSum(i-5, i-1, "Report_H")
            
            if(i == 56):
                self.df.loc[i, "Report_D"] = round(self.df.loc[i-1, "Report_D"] / self.df.loc[i-14, "Report_D"], 1)
                self.df.loc[i, "Report_F"] = round(self.df.loc[i-1, "Report_F"] / self.df.loc[i-14, "Report_F"], 1)
                self.df.loc[i, "Report_H"] = round(self.df.loc[i-1, "Report_H"] / self.df.loc[i-14, "Report_H"], 1)
            
            if(i >= 60 and i <= 64):
                self.calMethod1(i)
    
            if(i == 65):
                self.df.loc[i, "Report_D"] = self.rangeSum(i-5, i-1, "Report_D")
                self.df.loc[i, "Report_F"] = self.rangeSum(i-5, i-1, "Report_F")
                self.df.loc[i, "Report_H"] = self.rangeSum(i-5, i-1, "Report_H")

            if(i == 66):
                if(self.df.loc[i-1, "Report_D"] > 0):
                    self.df.loc[i, "Report_D"] = 0
                else:
                    self.df.loc[i, "Report_D"] = round(-self.df.loc[i-1, "Report_D"] / self.df.loc[i-23, "Report_D"], 1)
                if(self.df.loc[i-1, "Report_F"] > 0):
                    self.df.loc[i, "Report_F"] = 0
                else:
                    self.df.loc[i, "Report_F"] = round(-self.df.loc[i-1, "Report_F"] / self.df.loc[i-23, "Report_F"], 1)
                if(self.df.loc[i-1, "Report_H"] > 0):
                    self.df.loc[i, "Report_H"] = 0
                else:
                    self.df.loc[i, "Report_H"] = round(-self.df.loc[i-1, "Report_H"] / (self.df.loc[i-23, "Report_H"]/self.df.loc[0, "St_Mesecev"]*12), 1)

            if(i == 67):
                if(self.df.loc[i-3, "Report_D"] == 0):
                    self.df.loc[i, "Report_D"] = "n/a"
                else:
                    self.df.loc[i, "Report_D"] = round(self.df.loc[i-24, "Report_D"] / (-self.df.loc[i-3, "Report_D"]), 1)
                if(self.df.loc[i-3, "Report_F"] == 0):
                    self.df.loc[i, "Report_F"] = "n/a"
                else:
                    self.df.loc[i, "Report_F"] = round(self.df.loc[i-24, "Report_F"] / (-self.df.loc[i-3, "Report_F"]), 1)
                if(self.df.loc[i-3, "Report_H"] == 0):
                    self.df.loc[i, "Report_H"] = "n/a"
                else:
                    self.df.loc[i, "Report_H"] = round((self.df.loc[i-24, "Report_H"]/self.df.loc[0, "St_Mesecev"]*12) / (-self.df.loc[i-3, "Report_H"]), 1)

            if(i == 68):
                if(self.info.Imamo_podatke_za == "Da"):
                    self.df.loc[i, "Report_D"] = self.df.loc[33, "Izkazi2_C"]
                    self.df.loc[i, "Report_F"] = self.df.loc[33, "Izkazi2_D"]
                    self.df.loc[i, "Report_H"] = self.df.loc[33, "Izkazi2_E"]
                else:
                    self.df.loc[i, "Report_D"] = self.df.loc[33, "Izkazi2_B"]
                    self.df.loc[i, "Report_F"] = self.df.loc[33, "Izkazi2_C"]
                    self.df.loc[i, "Report_H"] = self.df.loc[33, "Izkazi2_D"]

            if(i == 69):
                self.df.loc[i, "Report_D"] = round((-self.df.loc[i-6, "Report_D"]-self.df.loc[i-5, "Report_D"])/self.df.loc[i-29, "Report_D"] *100, 1)
                self.df.loc[i, "Report_F"] = round((-self.df.loc[i-6, "Report_F"]-self.df.loc[i-5, "Report_F"])/self.df.loc[i-29, "Report_F"] *100, 1)
                self.df.loc[i, "Report_H"] = round((-self.df.loc[i-6, "Report_H"]-self.df.loc[i-5, "Report_H"])/self.df.loc[i-29, "Report_H"] *100, 1)

            if(i == 50):
                self.calMethodKazalkiniNxtCol(i, "Kazalniki_21", -1)
            if(i == 51):
                self.calMethodKazalkiniNxtCol(i, "Kazalniki_20")
            if(i == 52):
                self.calMethodKazalkiniNxtCol(i, "Kazalniki_19")
            # Table 2
            # tbl2Indexs = [3, 4, 5, "6", 7, 8, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 23, 24, 25, 26, 27, 28]
            if(i == 76):
                self.df.loc[i, "Report_F"] = self.df.loc[4, "Obdobja_IPI"]
                self.df.loc[i, "Report_H"] = self.df.loc[3, "Obdobja_IPI"]
                self.df.loc[i, "Report_J"] = self.df.loc[2, "Obdobja_IPI"]
                self.df.loc[i, "Report_N"] = self.df.loc[1, "Obdobja_IPI"]
                self.df.loc[i, "Report_R"] = self.df.loc[0, "Obdobja_IPI"]

            if(i >= 78 and i <= 83 ):
                self.calMethodForIsKazi2(i, i-75) # [3, 4, 5, 6, 7, 8]

            if(i >= 84 and i <= 93):
                self.calMethodForIsKazi2(i, i-74) # [10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
            
            if(i >= 94 and i <= 99):
                self.calMethodForIsKazi2(i, i-71) # [23, 24, 25, 26, 27, 28]

            
            if(i >= 102 and i <= 106):
                self.calMethodForIsKazi2(i, i-73) # 

            if(i == 110):
                self.reportForIskazi2(i, 3)
            if(i == 111):
                self.reportForIskazi2(i, 13)
            if(i == 112):
                self.reportForIskazi2(i, 28)
            if(i == 113):
                self.reportForIskazi2(i, 30, 100)
            if(i == 123):
                self.reportForIskazi2(i, 10, -1)
            if(i == 124):
                self.reportForIskazi2(i, 11, -1)
            if(i == 125):
                m = -1
                self.df.loc[i, "Report_B"] = m*round(self.divide(self.df.loc[10, "Izkazi2_A"], self.df.loc[3, "Izkazi2_A"])*100, 2)
                self.df.loc[i, "Report_C"] = m*round(self.divide(self.df.loc[10, "Izkazi2_B"], self.df.loc[3, "Izkazi2_B"])*100, 2)
                self.df.loc[i, "Report_D"] = m*round(self.divide(self.df.loc[10, "Izkazi2_C"], self.df.loc[3, "Izkazi2_C"])*100, 2)
                self.df.loc[i, "Report_E"] = m*round(self.divide(self.df.loc[10, "Izkazi2_D"], self.df.loc[3, "Izkazi2_D"])*100, 2)
                self.df.loc[i, "Report_F"] = m*round(self.divide(self.df.loc[10, "Izkazi2_E"], self.df.loc[3, "Izkazi2_E"])*100, 2)
            if(i == 126):
                m = -1
                self.df.loc[i, "Report_B"] = m*round(self.divide(self.df.loc[11, "Izkazi2_A"], self.df.loc[3, "Izkazi2_A"])*100, 2)
                self.df.loc[i, "Report_C"] = m*round(self.divide(self.df.loc[11, "Izkazi2_B"], self.df.loc[3, "Izkazi2_B"])*100, 2)
                self.df.loc[i, "Report_D"] = m*round(self.divide(self.df.loc[11, "Izkazi2_C"], self.df.loc[3, "Izkazi2_C"])*100, 2)
                self.df.loc[i, "Report_E"] = m*round(self.divide(self.df.loc[11, "Izkazi2_D"], self.df.loc[3, "Izkazi2_D"])*100, 2)
                self.df.loc[i, "Report_F"] = m*round(self.divide(self.df.loc[11, "Izkazi2_E"], self.df.loc[3, "Izkazi2_E"])*100, 2)

            # Table 3
            if(i == 146):
                self.df.loc[i, "Report_F"] = self.df.loc[4, "Obdobja_BS"]
                self.df.loc[i, "Report_H"] = self.df.loc[3, "Obdobja_BS"]
                self.df.loc[i, "Report_J"] = self.df.loc[2, "Obdobja_BS"]
                self.df.loc[i, "Report_N"] = self.df.loc[1, "Obdobja_BS"]
                self.df.loc[i, "Report_R"] = self.df.loc[0, "Obdobja_BS"]

            if(i == 148):
                self.calMethodForIsKazi(i, i-146) # 
            
            if(i >= 149 and i <= 150):
                self.calMethodForIsKazi(i, i-143) #

            if(i >= 151 and i <= 155):
                self.calMethodForIsKazi(i, i-141) #

            if(i == 156):
                self.calMethodForIsKazi(i, i-136) # 
            
            if(i == 157):
                self.calMethodForIsKazi(i, i-134) # 
            
            if(i >= 158 and i <= 162):
                self.calMethodForIsKazi(i, i-132) #

            if(i == 164):
                self.calMethodForIsKazi(i, i-126) #
            
            if(i == 165):
                self.calMethodForIsKazi(i, i-125) #
            
            if(i == 166):
                self.calMethodForIsKazi(i, i-121) #

            if(i >= 167 and i <= 170):
                self.calMethodForIsKazi(i, i-119) #

            if(i == 171):
                self.calMethodForIsKazi(i, i-116) #

            if(i >= 172 and i <= 175):
                self.calMethodForIsKazi(i, i-114) #

            if(i >= 178 and i <= 180):
                self.calMethodForIsKazi(i, i-116) # 
            
            if(i >= 182 and i <= 183):
                self.calMethodForIsKazi(i, i-117) # 

            if(i == 185):
                self.calMethodKazalkini(i, "Kazalniki_20")
            if(i == 186):
                self.calMethodKazalkini(i, "Kazalniki_19")
            if(i == 187):
                self.calMethodKazalkini(i, "Kazalniki_21")
            if(i == 188):
                self.calMethodKazalkini(i, "Kazalniki_22")
            if(i == 197):
                self.calMethodKazalkini(i, "Kazalniki_25")
            if(i == 198):
                self.calMethodKazalkini(i, "Kazalniki_28")
            if(i == 199):
                self.calMethodKazalkini(i, "Kazalniki_26")

            # After Tables
            if(i == 215):
                if(self.info.Imamo_podatke_za == "Da"):
                    self.df.loc[i, "Report_D"] = self.df.loc[2, "Obdobja"] 
                    self.df.loc[i, "Report_F"] = self.df.loc[3, "Obdobja"] 
                    self.df.loc[i, "Report_H"] = self.df.loc[4, "Obdobja"] 
                else:
                    self.df.loc[i, "Report_D"] = self.df.loc[1, "Obdobja"] 
                    self.df.loc[i, "Report_F"] = self.df.loc[2, "Obdobja"] 
                    self.df.loc[i, "Report_H"] = self.df.loc[3, "Obdobja"]

            if(i == 216):
                if(self.info.Imamo_podatke_za == "Da"):
                    self.df.loc[i, "Report_D"] = self.df.loc[2, "Kazalniki_36"] 
                    self.df.loc[i, "Report_F"] = self.df.loc[3, "Kazalniki_36"] 
                    self.df.loc[i, "Report_H"] = self.df.loc[4, "Kazalniki_36"] 
                else:
                    self.df.loc[i, "Report_D"] = self.df.loc[1, "Kazalniki_36"] 
                    self.df.loc[i, "Report_F"] = self.df.loc[2, "Kazalniki_36"] 
                    self.df.loc[i, "Report_H"] = self.df.loc[3, "Kazalniki_36"] 
            
            if(i == 226):
                if(self.info.Imamo_podatke_za == "Da"):
                    self.df.loc[i, "Report_D"] = self.df.loc[2, "Kazalniki_53"] 
                    self.df.loc[i, "Report_F"] = self.df.loc[3, "Kazalniki_53"] 
                    self.df.loc[i, "Report_H"] = self.df.loc[4, "Kazalniki_53"] 
                else:
                    self.df.loc[i, "Report_D"] = self.df.loc[1, "Kazalniki_53"] 
                    self.df.loc[i, "Report_F"] = self.df.loc[2, "Kazalniki_53"] 
                    self.df.loc[i, "Report_H"] = self.df.loc[3, "Kazalniki_53"] 
            
            if(i == 236):
                if(self.info.Imamo_podatke_za == "Da"):
                    self.df.loc[i, "Report_D"] = self.df.loc[2, "Kazalniki_77"] 
                    self.df.loc[i, "Report_F"] = self.df.loc[3, "Kazalniki_77"] 
                    self.df.loc[i, "Report_H"] = self.df.loc[4, "Kazalniki_77"] 
                else:
                    self.df.loc[i, "Report_D"] = self.df.loc[1, "Kazalniki_77"] 
                    self.df.loc[i, "Report_F"] = self.df.loc[2, "Kazalniki_77"] 
                    self.df.loc[i, "Report_H"] = self.df.loc[3, "Kazalniki_77"] 
            
            if(i == 246):
                if(self.info.Imamo_podatke_za == "Da"):
                    self.df.loc[i, "Report_D"] = self.df.loc[2, "Kazalniki_91"] 
                    self.df.loc[i, "Report_F"] = self.df.loc[3, "Kazalniki_91"] 
                    self.df.loc[i, "Report_H"] = self.df.loc[4, "Kazalniki_91"] 
                else:
                    self.df.loc[i, "Report_D"] = self.df.loc[1, "Kazalniki_91"] 
                    self.df.loc[i, "Report_F"] = self.df.loc[2, "Kazalniki_91"] 
                    self.df.loc[i, "Report_H"] = self.df.loc[3, "Kazalniki_91"] 

            if(i == 256):
                if(self.info.Imamo_podatke_za == "Da"):
                    self.df.loc[i, "Report_D"] = self.df.loc[2, "Kazalniki_97"] 
                    self.df.loc[i, "Report_F"] = self.df.loc[3, "Kazalniki_97"] 
                    self.df.loc[i, "Report_H"] = self.df.loc[4, "Kazalniki_97"] 
                else:
                    self.df.loc[i, "Report_D"] = self.df.loc[1, "Kazalniki_97"] 
                    self.df.loc[i, "Report_F"] = self.df.loc[2, "Kazalniki_97"] 
                    self.df.loc[i, "Report_H"] = self.df.loc[3, "Kazalniki_97"] 


            
            if(i == 218):
                self.calMethodKazalkini(i, "Kazalniki_43")
            elif(i == 219):
                self.calMethodKazalkini(i, "Kazalniki_44")
            elif(i == 220):
                self.calMethodKazalkini(i, "Kazalniki_45")
            elif(i == 221):
                self.df.loc[i, "Report_B"] = self.df.loc[4, "Obdobja_IPI"]
                self.df.loc[i, "Report_C"] = self.df.loc[3, "Obdobja_IPI"]
                self.df.loc[i, "Report_D"] = self.df.loc[2, "Obdobja_IPI"]
                self.df.loc[i, "Report_E"] = self.df.loc[1, "Obdobja_IPI"]
                self.df.loc[i, "Report_F"] = self.df.loc[0, "Obdobja_IPI"]
            elif(i == 222):
                self.calMethodKazalkini(i, "Kazalniki_36")
            elif(i == 228):
                self.calMethodKazalkini(i, "Kazalniki_66")
            elif(i == 229):
                self.calMethodKazalkini(i, "Kazalniki_65")
            elif(i == 230):
                self.calMethodKazalkini(i, "Kazalniki_64")
            elif(i == 231):
                self.calMethodKazalkini(i, "Kazalniki_63")
            elif(i == 232):
                self.calMethodKazalkini(i, "Kazalniki_62")
            elif(i == 233):
                self.calMethodKazalkini(i, "Kazalniki_53")
            elif(i == 238):
                self.calMethodKazalkini(i, "Kazalniki_83")
            elif(i == 239):
                self.calMethodKazalkini(i, "Kazalniki_82")
            elif(i == 240):
                self.calMethodKazalkini(i, "Kazalniki_77")
            elif(i == 248):
                self.calMethodKazalkini(i, "Kazalniki_91")
            elif(i == 258):
                self.calMethodKazalkini(i, "Kazalniki_106")
            elif(i == 259):
                self.calMethodKazalkini(i, "Kazalniki_105")
            elif(i == 260):
                self.calMethodKazalkini(i, "Kazalniki_104")
            elif(i == 261):
                self.calMethodKazalkini(i, "Kazalniki_97")
            
            elif(i == 286):
                self.setArray(i, [1.89, 1.85, 2.02, 1.96])
            elif(i == 287):
                m = 1
                self.df.loc[i, "Report_B"] = m*round(self.divide(self.df.loc[28, "Izkazi_A"], self.df.loc[59, "Izkazi_A"]), 2)
                self.df.loc[i, "Report_C"] = m*round(self.divide(self.df.loc[28, "Izkazi_B"], self.df.loc[59, "Izkazi_B"]), 2)
                self.df.loc[i, "Report_D"] = m*round(self.divide(self.df.loc[28, "Izkazi_C"], self.df.loc[59, "Izkazi_C"]), 2)
                self.df.loc[i, "Report_E"] = m*round(self.divide(self.df.loc[28, "Izkazi_D"], self.df.loc[59, "Izkazi_D"]), 2)
                self.df.loc[i, "Report_F"] = m*round(self.divide(self.df.loc[28, "Izkazi_E"], self.df.loc[59, "Izkazi_E"]), 2)
            elif(i == 289):
                self.setArray(i, [1.31, 1.25, 1.37, 1.35])
            elif(i == 290):
                m = 1
                self.df.loc[i, "Report_B"] = m*round(self.divide(self.df.loc[28, "Izkazi_A"] - self.df.loc[20, "Izkazi_A"], self.df.loc[59, "Izkazi_A"]), 2)
                self.df.loc[i, "Report_C"] = m*round(self.divide(self.df.loc[28, "Izkazi_B"] - self.df.loc[20, "Izkazi_B"], self.df.loc[59, "Izkazi_B"]), 2)
                self.df.loc[i, "Report_D"] = m*round(self.divide(self.df.loc[28, "Izkazi_C"] - self.df.loc[20, "Izkazi_C"], self.df.loc[59, "Izkazi_C"]), 2)
                self.df.loc[i, "Report_E"] = m*round(self.divide(self.df.loc[28, "Izkazi_D"] - self.df.loc[20, "Izkazi_D"], self.df.loc[59, "Izkazi_D"]), 2)
                self.df.loc[i, "Report_F"] = m*round(self.divide(self.df.loc[28, "Izkazi_E"] - self.df.loc[20, "Izkazi_E"], self.df.loc[59, "Izkazi_E"]), 2)

            elif(i == 297):
                self.calMethodKazalkini(i, "Kazalniki_20")
            elif(i == 298):
                self.setArray(i, [71.39, 68.84, 66.47, 61.82])
            elif(i == 300):
                self.setArray(i, [1.20, 1.14, 1.20, 1.21])
            elif(i == 301):
                self.df.loc[i, "Report_B"] = m*round(self.divide(self.df.loc[38, "Izkazi_A"] + self.df.loc[50, "Izkazi_A"], self.df.loc[20, "Izkazi_A"] + self.df.loc[13, "Izkazi_A"]), 2)
                self.df.loc[i, "Report_C"] = m*round(self.divide(self.df.loc[38, "Izkazi_B"] + self.df.loc[50, "Izkazi_B"], self.df.loc[20, "Izkazi_B"] + self.df.loc[13, "Izkazi_B"]), 2)
                self.df.loc[i, "Report_D"] = m*round(self.divide(self.df.loc[38, "Izkazi_C"] + self.df.loc[50, "Izkazi_C"], self.df.loc[20, "Izkazi_C"] + self.df.loc[13, "Izkazi_C"]), 2)
                self.df.loc[i, "Report_E"] = m*round(self.divide(self.df.loc[38, "Izkazi_D"] + self.df.loc[50, "Izkazi_D"], self.df.loc[20, "Izkazi_D"] + self.df.loc[13, "Izkazi_D"]), 2)
                self.df.loc[i, "Report_F"] = m*round(self.divide(self.df.loc[38, "Izkazi_E"] + self.df.loc[50, "Izkazi_E"], self.df.loc[20, "Izkazi_E"] + self.df.loc[13, "Izkazi_E"]), 2)
                
            elif(i == 310):
                self.df.loc[i, "Report_B"] = m*round(self.divide(self.df.loc[50, "Izkazi_A"] + self.df.loc[59, "Izkazi_A"], self.df.loc[61, "Izkazi_A"])*100, 2)
                self.df.loc[i, "Report_C"] = m*round(self.divide(self.df.loc[50, "Izkazi_B"] + self.df.loc[59, "Izkazi_B"], self.df.loc[61, "Izkazi_B"])*100, 2)
                self.df.loc[i, "Report_D"] = m*round(self.divide(self.df.loc[50, "Izkazi_C"] + self.df.loc[59, "Izkazi_C"], self.df.loc[61, "Izkazi_C"])*100, 2)
                self.df.loc[i, "Report_E"] = m*round(self.divide(self.df.loc[50, "Izkazi_D"] + self.df.loc[59, "Izkazi_D"], self.df.loc[61, "Izkazi_D"])*100, 2)
                self.df.loc[i, "Report_F"] = m*round(self.divide(self.df.loc[50, "Izkazi_E"] + self.df.loc[59, "Izkazi_E"], self.df.loc[61, "Izkazi_E"])*100, 2)
            elif(i == 311):
                self.setArray(i, [48.1, 50.1, 47.7, 49.0])
            elif(i == 313):
                self.setArray(i, [13.5, 11.3, 10.1, 11.0])
            elif(i == 314):
                self.reportForIskazi2(i, 33)
            
            elif(i == 323):
                self.calMethodKazalkini(i, "Kazalniki_31", 100)
            elif(i == 324):
                self.setArray(i, [13.7, 12.6, 12.1, 14.9])
            elif(i == 326):
                self.calMethodKazalkini(i, "Kazalniki_32", 100)
            elif(i == 327):
                self.setArray(i, [6.7, 6.1, 5.9, 7.3])

            elif(i == 334):
                m = 1
                self.df.loc[i, "Report_B"] = m*round(self.divide(self.df.loc[28, "Izkazi2_A"], self.df.loc[3, "Izkazi2_A"])*100, 2)
                self.df.loc[i, "Report_C"] = m*round(self.divide(self.df.loc[28, "Izkazi2_B"], self.df.loc[3, "Izkazi2_B"])*100, 2)
                self.df.loc[i, "Report_D"] = m*round(self.divide(self.df.loc[28, "Izkazi2_C"], self.df.loc[3, "Izkazi2_C"])*100, 2)
                self.df.loc[i, "Report_E"] = m*round(self.divide(self.df.loc[28, "Izkazi2_D"], self.df.loc[3, "Izkazi2_D"])*100, 2)
                self.df.loc[i, "Report_F"] = m*round(self.divide(self.df.loc[28, "Izkazi2_E"], self.df.loc[3, "Izkazi2_E"])*100, 2)                
            elif(i == 335):
                self.setArray(i, [4.0, 3.6, 3.6, 4.2])
            elif(i == 337):
                self.setArray(i, [4.7, 4.5, 4.6, 5.1])
            elif(i == 338):
                m = 1
                self.df.loc[i, "Report_B"] = m*round(self.divide(self.df.loc[18, "Izkazi2_A"], self.df.loc[3, "Izkazi2_A"])*100, 2)
                self.df.loc[i, "Report_C"] = m*round(self.divide(self.df.loc[18, "Izkazi2_B"], self.df.loc[3, "Izkazi2_B"])*100, 2)
                self.df.loc[i, "Report_D"] = m*round(self.divide(self.df.loc[18, "Izkazi2_C"], self.df.loc[3, "Izkazi2_C"])*100, 2)
                self.df.loc[i, "Report_E"] = m*round(self.divide(self.df.loc[18, "Izkazi2_D"], self.df.loc[3, "Izkazi2_D"])*100, 2)
                self.df.loc[i, "Report_F"] = m*round(self.divide(self.df.loc[18, "Izkazi2_E"], self.df.loc[3, "Izkazi2_E"])*100, 2)     
                




    def calMethod1(self, i):
        j = 0
        m = 1
        IZ2 = False

        if(i == 40): j = 30
        elif(i == 41): j = 38
        elif(i == 42): 
            j = 3
            IZ2 = True
        elif(i == 43): 
            j = 13
            IZ2 = True
        elif(i == 45): 
            j = 18
            IZ2 = True
        elif(i == 46): 
            j = 28
            IZ2 = True
        elif(i == 50): j = 20
        elif(i == 51): j = 26
        elif(i == 52): j = 29
        elif(i == 53): 
            j = 58 
            m = -1
        elif(i == 54): j = 60
        elif(i == 60): j = 27
        elif(i == 61): j = 9
        elif(i == 62): j = 22
        elif(i == 63): 
            j = 45
            m = -1
        elif(i == 64): 
            j = 55
            m = -1

        if(self.info.Imamo_podatke_za == "Da"):
            if(IZ2):
                self.df.loc[i, "Report_D"] = m * self.df.loc[j, "Izkazi2_C"] * 1000
                self.df.loc[i, "Report_F"] = m * self.df.loc[j, "Izkazi2_D"] * 1000
                self.df.loc[i, "Report_H"] = m * self.df.loc[j, "Izkazi2_E"] * 1000
            else:
                self.df.loc[i, "Report_D"] = m * self.df.loc[j, "Izkazi_C"] * 1000
                self.df.loc[i, "Report_F"] = m * self.df.loc[j, "Izkazi_D"] * 1000
                self.df.loc[i, "Report_H"] = m * self.df.loc[j, "Izkazi_E"] * 1000
        else:
            if(IZ2):
                self.df.loc[i, "Report_D"] = m * self.df.loc[j, "Izkazi_B"] * 1000
                self.df.loc[i, "Report_F"] = m * self.df.loc[j, "Izkazi_C"] * 1000
                self.df.loc[i, "Report_H"] = m * self.df.loc[j, "Izkazi_D"] * 1000
            else:
                self.df.loc[i, "Report_D"] = m * self.df.loc[j, "Izkazi_B"] * 1000
                self.df.loc[i, "Report_F"] = m * self.df.loc[j, "Izkazi_C"] * 1000
                self.df.loc[i, "Report_H"] = m * self.df.loc[j, "Izkazi_D"] * 1000

    def calMethodForIsKazi2(self, i, j):
        if(pd.notnull(self.df.loc[j, "Izkazi2_A"])):
            self.df.loc[i, "Report_F"] = self.df.loc[j, "Izkazi2_A"]
        else:
            self.df.loc[i, "Report_F"] = ""
        if (pd.notnull(self.df.loc[j, "Izkazi2_B"])):
            self.df.loc[i, "Report_H"] = self.df.loc[j, "Izkazi2_B"]
        else:
            self.df.loc[i, "Report_H"] = ""
        if(pd.notnull(self.df.loc[j, "Izkazi2_C"])):
            self.df.loc[i, "Report_J"] = self.df.loc[j, "Izkazi2_C"]
        else:
            self.df.loc[i, "Report_J"] = ""
        if(pd.notnull(self.df.loc[j, "Izkazi2_D"])):
            self.df.loc[i, "Report_N"] = self.df.loc[j, "Izkazi2_D"]
        else:
            self.df.loc[i, "Report_N"] = ""
        if(pd.notnull(self.df.loc[j, "Izkazi2_E"])):
            self.df.loc[i, "Report_R"] = self.df.loc[j, "Izkazi2_E"]
        else:
            self.df.loc[i, "Report_R"] = ""
    
    def calMethodKazalkini(self, i, kCol, m = 1):
        self.df.loc[i, "Report_B"] = self.df.loc[0, kCol] * m 
        self.df.loc[i, "Report_C"] = self.df.loc[1, kCol] * m 
        self.df.loc[i, "Report_D"] = self.df.loc[2, kCol] * m 
        self.df.loc[i, "Report_E"] = self.df.loc[3, kCol] * m 
        self.df.loc[i, "Report_F"] = self.df.loc[4, kCol] * m
    
    def calMethodKazalkiniNxtCol(self, i, kCol, m = 1):
        self.df.loc[i, "Report_N"] = m * self.df.loc[0, kCol] 
        self.df.loc[i, "Report_O"] = m * self.df.loc[1, kCol] 
        self.df.loc[i, "Report_P"] = m * self.df.loc[2, kCol] 
        self.df.loc[i, "Report_Q"] = m * self.df.loc[3, kCol] 
        self.df.loc[i, "Report_R"] = m * self.df.loc[4, kCol]

    def calMethodForIsKazi(self, i, j):
        if(pd.notnull(self.df.loc[j, "Izkazi_A"])):
            self.df.loc[i, "Report_F"] = self.df.loc[j, "Izkazi_A"]
        else:
            self.df.loc[i, "Report_F"] = ""
        if (pd.notnull(self.df.loc[j, "Izkazi_B"])):
            self.df.loc[i, "Report_H"] = self.df.loc[j, "Izkazi_B"]
        else:
            self.df.loc[i, "Report_H"] = ""
        if(pd.notnull(self.df.loc[j, "Izkazi_C"])):
            self.df.loc[i, "Report_J"] = self.df.loc[j, "Izkazi_C"]
        else:
            self.df.loc[i, "Report_J"] = ""
        if(pd.notnull(self.df.loc[j, "Izkazi_D"])):
            self.df.loc[i, "Report_N"] = self.df.loc[j, "Izkazi_D"]
        else:
            self.df.loc[i, "Report_N"] = ""
        if(pd.notnull(self.df.loc[j, "Izkazi_E"])):
            self.df.loc[i, "Report_R"] = self.df.loc[j, "Izkazi_E"]
        else:
            self.df.loc[i, "Report_R"] = ""

    def rangeSum(self, s, e, col):
        sum = 0
        for i in range(s, e+1):
            sum = sum + self.df.loc[i, col]
        return sum
    
    def reportForIskazi(self, i, j, m = 1):
        self.df.loc[i, "Report_B"] = m*self.df.loc[j, "Izkazi_A"]
        self.df.loc[i, "Report_C"] = m*self.df.loc[j, "Izkazi_B"]
        self.df.loc[i, "Report_D"] = m*self.df.loc[j, "Izkazi_C"]
        self.df.loc[i, "Report_E"] = m*self.df.loc[j, "Izkazi_D"]
        self.df.loc[i, "Report_F"] = m*self.df.loc[j, "Izkazi_E"]
    
    def reportForIskazi2(self, i, j, m = 1):
        self.df.loc[i, "Report_B"] = m*self.df.loc[j, "Izkazi2_A"]
        self.df.loc[i, "Report_C"] = m*self.df.loc[j, "Izkazi2_B"]
        self.df.loc[i, "Report_D"] = m*self.df.loc[j, "Izkazi2_C"]
        self.df.loc[i, "Report_E"] = m*self.df.loc[j, "Izkazi2_D"]
        self.df.loc[i, "Report_F"] = m*self.df.loc[j, "Izkazi2_E"]
    
    def reportForIskaziNxtCol(self, i, j, m = 1):
        self.df.loc[i, "Report_N"] = m*self.df.loc[j, "Izkazi_A"]
        self.df.loc[i, "Report_O"] = m*self.df.loc[j, "Izkazi_B"]
        self.df.loc[i, "Report_P"] = m*self.df.loc[j, "Izkazi_C"]
        self.df.loc[i, "Report_Q"] = m*self.df.loc[j, "Izkazi_D"]
        self.df.loc[i, "Report_R"] = m*self.df.loc[j, "Izkazi_E"]

    def reportForIskazi2NxtCol(self, i, j, m = 1):
        self.df.loc[i, "Report_N"] = m*self.df.loc[j, "Izkazi2_A"]
        self.df.loc[i, "Report_O"] = m*self.df.loc[j, "Izkazi2_B"]
        self.df.loc[i, "Report_P"] = m*self.df.loc[j, "Izkazi2_C"]
        self.df.loc[i, "Report_Q"] = m*self.df.loc[j, "Izkazi2_D"]
        self.df.loc[i, "Report_R"] = m*self.df.loc[j, "Izkazi2_E"]

    def setArray(self, i, arr):
        self.df.loc[i, "Report_B"] = arr[0]
        self.df.loc[i, "Report_C"] = arr[1]
        self.df.loc[i, "Report_D"] = arr[2]
        self.df.loc[i, "Report_E"] = arr[3]
        if(len(arr) > 4):
            self.df.loc[i, "Report_F"] = arr[4]

    def divide(self, num1, num2):
        try:
            return num1/num2
        except:
            return ""

    @property
    def Report_A(self):
        return self.df.Report_A
    @property
    def Report_B(self):
        return self.df.Report_B
    @property
    def Report_C(self):
        return self.df.Report_C
    @property
    def Report_D(self):
        return self.df.Report_D
    @property
    def Report_E(self):
        return self.df.Report_E
    @property
    def Report_F(self):
        return self.df.Report_F
    @property
    def Report_G(self):
        return self.df.Report_G
    @property
    def Report_H(self):
        return self.df.Report_H
    @property
    def Report_I(self):
        return self.df.Report_I
    @property
    def Report_J(self):
        return self.df.Report_J
    @property
    def Report_K(self):
        return self.df.Report_K
    @property
    def Report_L(self):
        return self.df.Report_L
    @property
    def Report_M(self):
        return self.df.Report_M
    @property
    def Report_N(self):
        return self.df.Report_N
    @property
    def Report_O(self):
        return self.df.Report_O
    @property
    def Report_P(self):
        return self.df.Report_P
    @property
    def Report_Q(self):
        return self.df.Report_Q
    @property
    def Report_R(self):
        return self.df.Report_R
    