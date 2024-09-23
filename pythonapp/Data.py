from cmath import log
from pythonapp.helper.utils import DataTable

class DataClass(DataTable):
    
    def __init__(self, dataframe, predopostavke, inputs, predopostavkeList, *arg, **kwargs):
        super().__init__(dataframe)
        self.predopostavke = predopostavke
        self.inputs = inputs
        self.predopostavkeList = predopostavkeList
        
    def compute_tables(self):
        izkaziCol = ["Izkazi_A", "Izkazi_B", "Izkazi_C", "Izkazi_D", "Izkazi_E"]
        izkazi2Col = ["Izkazi2_A", "Izkazi2_B", "Izkazi2_C", "Izkazi2_D", "Izkazi2_E"]
        lastIndex = len(self.predopostavke)-1
        if(self.inputs["isAOP"] == "Da"):
            rast_prihodkov = (self.df.loc[3, izkazi2Col[lastIndex]] / self.predopostavkeList['St_Mesecev'][lastIndex]*12) / self.df.loc[3, izkazi2Col[lastIndex-1]] - 1
        else:
            rast_prihodkov = self.df.loc[3, izkazi2Col[lastIndex]]  / self.df.loc[3, izkazi2Col[lastIndex-1]] - 1
        rast_prihodkov = round(rast_prihodkov * 100, 1)
        if(rast_prihodkov < 0 - self.inputs["Pogoj"]):
            if(self.inputs["isAOP"] == "Da"):
                self.inputs['Povprecni_prihodki'] = (self.df.loc[3, izkazi2Col[lastIndex]] / self.predopostavkeList['St_Mesecev'][lastIndex]*12) * 1000
            else:
                self.inputs['Povprecni_prihodki'] = (self.df.loc[3, izkazi2Col[lastIndex]]) * 1000
        else:
            if(self.inputs["isAOP"] == "Da"):
                self.inputs['Povprecni_prihodki'] = ((self.df.loc[3, izkazi2Col[lastIndex-1]] + (self.df.loc[3, izkazi2Col[lastIndex]] / self.predopostavkeList['St_Mesecev'][lastIndex]*12) ) / 2 ) * 1000
            else:
                sum = 0
                for i in range(0, lastIndex+1):
                    sum = sum + self.df.loc[3, izkazi2Col[i]]
                self.inputs['Povprecni_prihodki'] = (sum/(lastIndex+1)) * 1000
        
        if(self.inputs['Povprecni_prihodki'] <= 1000000):
            self.inputs['Maksimalen_limit'] = 0.1*(self.inputs['Povprecni_prihodki'])
        elif(self.inputs['Povprecni_prihodki'] <= 2500000):
            self.inputs['Maksimalen_limit'] = 100000+0.08*(self.inputs['Povprecni_prihodki'] - 1000000)
        elif(self.inputs['Povprecni_prihodki'] <= 5000000):
            self.inputs['Maksimalen_limit'] = 220000+0.06*(self.inputs['Povprecni_prihodki'] - 2500000)
        elif(self.inputs['Povprecni_prihodki'] <= 7500000):
            self.inputs['Maksimalen_limit'] = 370000+0.04*(self.inputs['Povprecni_prihodki'] - 5000000)
        elif(self.inputs['Povprecni_prihodki'] <= 10000000):
            self.inputs['Maksimalen_limit'] = 470000+0.02*(self.inputs['Povprecni_prihodki'] - 7500000)
        else:
            self.inputs['Maksimalen_limit'] = 520000+0.01*(self.inputs['Povprecni_prihodki'] - 10000000)
        self.inputs['Maksimalen_limit'] = round(self.inputs['Maksimalen_limit'])


        Priporocen_limit_v19 = (self.getOCol(self.df.loc[31, izkazi2Col[lastIndex]] , [1,0.9,0.75,0.5,0.2], [3,4,6,8]) * 0.2 * 0.5) + (self.getOCol(self.df.loc[32, izkazi2Col[lastIndex]] , [1,0.9,0.75,0.5], [1.1,1,0.7], checkZero = True) * 0.2 * 0.5) + ((1 if self.df.loc[33, izkazi2Col[lastIndex]] > 1 else 0.5) * 0.2 * 0.5) + (self.getOCol(self.df.loc[65, izkaziCol[lastIndex]] , [0.5,0.9,1,0.95,0.85], [0.8,1,1.5,2]) *0.2 * 0.5) + (self.getOCol(self.df.loc[26, izkaziCol[lastIndex]] / (self.df.loc[3, izkazi2Col[lastIndex]] / self.predopostavkeList['St_Mesecev'][lastIndex]*12), [1,0.9,0.75,0.4,0.2], [0.2,0.4,0.6,0.8]) * 0.1 *0.5) + (self.getOCol(self.df.loc[38, izkaziCol[lastIndex]] / self.df.loc[30, izkaziCol[lastIndex]] , [0.2,0.4,0.65,0.8,0.9,1], [0.2,0.25,0.3,0.35,0.45]) * 0.1 *0.5) 

        Priporocen_limit_v58 = (self.getOCol(self.df.loc[lastIndex, "Kazalniki_36"], [1,0.7,0.5], [3.0,1.8], checkZero=True)*0.3*0.5)+(self.getOCol(self.df.loc[lastIndex, "Kazalniki_53"], [0,0.1,0.4,0.6,0.85,0.9,0.95,1], [-1,0,0.3,1,1.5,2.2,3])*0.3*0.5)+(self.getOCol(self.df.loc[lastIndex, "Kazalniki_77"], [1,0.5], [0.5])*0.15*0.5)+(self.getOCol(self.df.loc[lastIndex, "Kazalniki_91"], [1,0.5], [0.5])*0.1*0.5)+(self.getOCol(self.df.loc[lastIndex, "Kazalniki_97"], [1,0.8,0.55,0.2], [14,24,32])*0.15*0.5)

        Priporocen_limit_v18 = Priporocen_limit_v19 + Priporocen_limit_v58
        
        Priporocen_limit_u19 = (self.getOCol(self.df.loc[31, izkazi2Col[lastIndex-1]] , [1,0.9,0.75,0.5,0.2], [3,4,6,8]) * 0.2 * 0.5) + (self.getOCol(self.df.loc[32, izkazi2Col[lastIndex-1]] , [1,0.9,0.75,0.5], [1.1,1,0.7], checkZero = True) * 0.2 * 0.5) + ((1 if self.df.loc[33, izkazi2Col[lastIndex-1]] > 1 else 0.5) * 0.2 * 0.5) + (self.getOCol(self.df.loc[65, izkaziCol[lastIndex-1]] , [0.5,0.9,1,0.95,0.85], [0.8,1,1.5,2]) *0.2 * 0.5) + (self.getOCol(self.df.loc[26, izkaziCol[lastIndex-1]] / (self.df.loc[3, izkazi2Col[lastIndex-1]] / self.predopostavkeList['St_Mesecev'][lastIndex-1]*12), [1,0.9,0.75,0.4,0.2], [0.2,0.4,0.6,0.8]) * 0.1 *0.5) + (self.getOCol(self.df.loc[38, izkaziCol[lastIndex-1]] / self.df.loc[30, izkaziCol[lastIndex-1]] , [0.2,0.4,0.65,0.8,0.9,1], [0.2,0.25,0.3,0.35,0.45]) * 0.1 *0.5) 

        Priporocen_limit_u58 = (self.getOCol(self.df.loc[lastIndex-1, "Kazalniki_36"], [1,0.7,0.5], [3.0,1.8], checkZero=True)*0.3*0.5)+(self.getOCol(self.df.loc[lastIndex-1, "Kazalniki_53"], [0,0.1,0.4,0.6,0.85,0.9,0.95,1], [-1,0,0.3,1,1.5,2.2,3])*0.3*0.5)+(self.getOCol(self.df.loc[lastIndex-1, "Kazalniki_77"], [1,0.5], [0.5])*0.15*0.5)+(self.getOCol(self.df.loc[lastIndex-1, "Kazalniki_91"], [1,0.5], [0.5])*0.1*0.5)+(self.getOCol(self.df.loc[lastIndex-1, "Kazalniki_97"], [1,0.8,0.55,0.2], [14,24,32])*0.15*0.5)

        Priporocen_limit_u18 = Priporocen_limit_u19 + Priporocen_limit_u58

        Priporocen_limit_t19 = (self.getOCol(self.df.loc[31, izkazi2Col[lastIndex-2]] , [1,0.9,0.75,0.5,0.2], [3,4,6,8]) * 0.2 * 0.5) + (self.getOCol(self.df.loc[32, izkazi2Col[lastIndex-2]] , [1,0.9,0.75,0.5], [1.1,1,0.7], checkZero = True) * 0.2 * 0.5) + ((1 if self.df.loc[33, izkazi2Col[lastIndex-2]] > 1 else 0.5) * 0.2 * 0.5) + (self.getOCol(self.df.loc[65, izkaziCol[lastIndex-2]] , [0.5,0.9,1,0.95,0.85], [0.8,1,1.5,2]) *0.2 * 0.5) + (self.getOCol(self.df.loc[26, izkaziCol[lastIndex-2]] / (self.df.loc[3, izkazi2Col[lastIndex-2]] / self.predopostavkeList['St_Mesecev'][lastIndex-2]*12), [1,0.9,0.75,0.4,0.2], [0.2,0.4,0.6,0.8]) * 0.1 *0.5) + (self.getOCol(self.df.loc[38, izkaziCol[lastIndex-2]] / self.df.loc[30, izkaziCol[lastIndex-2]] , [0.2,0.4,0.65,0.8,0.9,1], [0.2,0.25,0.3,0.35,0.45]) * 0.1 *0.5) 

        Priporocen_limit_t58 = (self.getOCol(self.df.loc[lastIndex-2, "Kazalniki_36"], [1,0.7,0.5], [3.0,1.8], checkZero=True)*0.3*0.5)+(self.getOCol(self.df.loc[lastIndex-2, "Kazalniki_53"], [0,0.1,0.4,0.6,0.85,0.9,0.95,1], [-1,0,0.3,1,1.5,2.2,3])*0.3*0.5)+(self.getOCol(self.df.loc[lastIndex-2, "Kazalniki_77"], [1,0.5], [0.5])*0.15*0.5)+(self.getOCol(self.df.loc[lastIndex-2, "Kazalniki_91"], [1,0.5], [0.5])*0.1*0.5)+(self.getOCol(self.df.loc[lastIndex-2, "Kazalniki_97"], [1,0.8,0.55,0.2], [14,24,32])*0.15*0.5)

        Priporocen_limit_t18 = Priporocen_limit_t19 + Priporocen_limit_t58

        self.inputs['Priporocen_limit_W18'] = round((Priporocen_limit_t18 + Priporocen_limit_u18 + Priporocen_limit_v18)/3 * 100)
        self.inputs['Priporocen_limit_W19'] = 100 - self.inputs['Priporocen_limit_W18']


        if((self.df.loc[3, izkazi2Col[lastIndex]] * self.df.loc[3, izkazi2Col[lastIndex-2]]) <= 0):
            trend_m4 = "n/a"
        elif(self.df.loc[3, izkazi2Col[lastIndex-2]] > self.df.loc[3, izkazi2Col[lastIndex]]):
            trend_m4 = -abs(pow(self.df.loc[3, izkazi2Col[lastIndex]] / self.df.loc[3, izkazi2Col[lastIndex-2]], 0.5))-1
        else:
            trend_m4 = abs(pow(self.df.loc[3, izkazi2Col[lastIndex]] / self.df.loc[3, izkazi2Col[lastIndex-2]], 0.5))-1
        
        if(self.inputs["isAOP"] == "Da"):
            trend_n4 = (((self.df.loc[3, izkazi2Col[1]]/self.df.loc[3, izkazi2Col[0]])-1) + ((self.df.loc[3, izkazi2Col[2]]/self.df.loc[3, izkazi2Col[1]])-1) + ((self.df.loc[3, izkazi2Col[3]]/self.df.loc[3, izkazi2Col[2]])-1) + ((self.df.loc[3, izkazi2Col[4]]/self.df.loc[3, izkazi2Col[3]])-1) + trend_m4) / 5
        else:
            trend_n4 = (0 + ((self.df.loc[3, izkazi2Col[1]]/self.df.loc[3, izkazi2Col[0]])-1) + ((self.df.loc[3, izkazi2Col[2]]/self.df.loc[3, izkazi2Col[1]])-1) + ((self.df.loc[3, izkazi2Col[3]]/self.df.loc[3, izkazi2Col[2]])-1) + trend_m4) / 5



        if((self.df.loc[13, izkazi2Col[lastIndex]] * self.df.loc[13, izkazi2Col[lastIndex-2]]) <= 0):
            trend_m9 = "n/a"
        elif(self.df.loc[13, izkazi2Col[lastIndex-2]]*1000 > self.df.loc[13, izkazi2Col[lastIndex]]*1000):
            trend_m9 = -abs(pow(self.df.loc[13, izkazi2Col[lastIndex]] / self.df.loc[13, izkazi2Col[lastIndex-2]], 0.5))-1
        else:
            trend_m9 = abs(pow(self.df.loc[13, izkazi2Col[lastIndex]] / self.df.loc[13, izkazi2Col[lastIndex-2]], 0.5))-1
        
        if(self.inputs["isAOP"] == "Da"):
            trend_n9 = (((self.df.loc[13, izkazi2Col[1]]/self.df.loc[13, izkazi2Col[0]])-1) + ((self.df.loc[13, izkazi2Col[2]]/self.df.loc[13, izkazi2Col[1]])-1) + ((self.df.loc[13, izkazi2Col[3]]/self.df.loc[13, izkazi2Col[2]])-1) + ((self.df.loc[13, izkazi2Col[4]]/self.df.loc[13, izkazi2Col[3]])-1) + trend_m9) / 5
        else:
            trend_n9 = (0 + ((self.df.loc[13, izkazi2Col[1]]/self.df.loc[13, izkazi2Col[0]])-1) + ((self.df.loc[13, izkazi2Col[2]]/self.df.loc[13, izkazi2Col[1]])-1) + ((self.df.loc[13, izkazi2Col[3]]/self.df.loc[13, izkazi2Col[2]])-1) + trend_m9) / 5



        if((self.df.loc[18, izkazi2Col[lastIndex]] * self.df.loc[18, izkazi2Col[lastIndex-2]]) <= 0):
            trend_m14 = "n/a"
        elif(self.df.loc[18, izkazi2Col[lastIndex-2]]*1000 > self.df.loc[18, izkazi2Col[lastIndex]]*1000):
            trend_m14 = -abs(pow(self.df.loc[18, izkazi2Col[lastIndex]] / self.df.loc[18, izkazi2Col[lastIndex-2]], 0.5))-1
        else:
            trend_m14 = abs(pow(self.df.loc[18, izkazi2Col[lastIndex]] / self.df.loc[18, izkazi2Col[lastIndex-2]], 0.5))-1
        
        if(self.inputs["isAOP"] == "Da"):
            trend_n14 = (((self.df.loc[18, izkazi2Col[1]]/self.df.loc[18, izkazi2Col[0]])-1) + ((self.df.loc[18, izkazi2Col[2]]/self.df.loc[18, izkazi2Col[1]])-1) + ((self.df.loc[18, izkazi2Col[3]]/self.df.loc[18, izkazi2Col[2]])-1) + ((self.df.loc[18, izkazi2Col[4]]/self.df.loc[18, izkazi2Col[3]])-1) + trend_m14) / 5
        else:
            trend_n14 = (0 + ((self.df.loc[18, izkazi2Col[1]]/self.df.loc[18, izkazi2Col[0]])-1) + ((self.df.loc[18, izkazi2Col[2]]/self.df.loc[18, izkazi2Col[1]])-1) + ((self.df.loc[18, izkazi2Col[3]]/self.df.loc[18, izkazi2Col[2]])-1) + trend_m14) / 5

        trend = (self.getRCol(trend_n4, [0,-0.1,-0.2], [1,0.9,0.75,0.4])*0.4)+(self.getRCol(trend_n9, [0,-0.1,-0.2], [1,0.9,0.75,0.4])*0.3)+(self.getRCol(trend_n14, [0,-0.1,-0.2], [1,0.9,0.75,0.4])*0.3)


        self.inputs['Priporocen_limit'] = round( (self.inputs['Maksimalen_limit'] * 1 if self.df.loc[38, izkaziCol[lastIndex]] > 0 else 0 * 1 if (self.df.loc[28, izkazi2Col[lastIndex]]-self.df.loc[15, izkazi2Col[lastIndex]]-self.df.loc[16, izkazi2Col[lastIndex]]) > 0 else 0 * 1 if self.df.loc[13, izkazi2Col[lastIndex]] > 0 else 0 * 1 if (self.df.loc[lastIndex, "Kazalniki_25"] / (-self.df.loc[14, izkaziCol[lastIndex]])) > -3 else 0 ) * ((Priporocen_limit_v18) * self.inputs['Priporocen_limit_W18'] / 100) * trend, -3)

        cesija_k1_sum = (1 if(self.df.loc[38, izkaziCol[lastIndex]]/self.df.loc[30, izkaziCol[lastIndex]] <= 0.2) else 0) + (1 if(self.df.loc[31, izkazi2Col[lastIndex]] >= 8.0) else 0) + (1 if(self.df.loc[33, izkazi2Col[lastIndex]] <= 0.5) else 0) + (1 if(self.df.loc[lastIndex, "Kazalniki_36"] <= 1.81) else 0) + (1 if(self.df.loc[lastIndex, "Kazalniki_53"] <= -1.0) else 0)
        
        self.inputs["Cesija_K1"] = "Da" if(cesija_k1_sum > 0) else "Ne"

    def getOCol(self, N, C, F, checkZero = False):
        if(checkZero):
            if(N == 0):
                return 1
            else:
                for i in range(0, len(F)):
                    if(N > F[i]):
                        return C[i]
        else:        
            for i in range(0, len(F)):
                if(N < F[i]):
                    return C[i]
        return C[-1]

    def getRCol(self, N, P, Q):        
        for i in range(0, len(P)):
            if(N > P[i]):
                return Q[i]

        return Q[-1]