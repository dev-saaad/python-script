from audioop import findmax
import math
from pythonapp.helper.utils import DataTable

class KazalnikiClass(DataTable):
    
    def __init__(self, dataframe, info, *arg, **kwargs):
        super().__init__(dataframe)
        self.info = info
        self.calculated_columns = ["Kazalniki_4", "Kazalniki_5", "Kazalniki_8", "Kazalniki_9", "Kazalniki_10", "Kazalniki_11", "Kazalniki_14", "Kazalniki_15", "Kazalniki_16", "Kazalniki_19", "Kazalniki_20", "Kazalniki_21", "Kazalniki_22", "Kazalniki_25", "Kazalniki_26", "Kazalniki_27", "Kazalniki_28", "Kazalniki_31", "Kazalniki_32", "Kazalniki_34", "Kazalniki_36", "Kazalniki_38", "Kazalniki_39", "Kazalniki_40", "Kazalniki_43", "Kazalniki_44", "Kazalniki_45", "Kazalniki_53", "Kazalniki_62", "Kazalniki_63", "Kazalniki_64", "Kazalniki_65", "Kazalniki_66", "Kazalniki_77", "Kazalniki_79", "Kazalniki_82", "Kazalniki_83", "Kazalniki_91", "Kazalniki_97", "Kazalniki_104", "Kazalniki_105", "Kazalniki_106", "Kazalniki_114"]
        print("Dataframe\n", dataframe.head(10))
        
    def compute_tables(self):

        val12 = 6
        val19 = 13
        val26 = 20
        val32 = 26
        val33 = 27
        val34 = 28
        val35 = 29
        val36 = 30
        val43 = 36
        val45 = 38
        val48 = 41
        val52 = 45
        val57 = 50
        val62 = 55
        val65 = 58
        val66 = 59
        val67 = 60
        val68 = 61
        v2al85 = 3
        v2al87 = 5
        v2al90 = 8
        v2al91 = 9
        v2al92 = 10
        v2al93 = 11
        v2al94 = 12
        v2al95 = 13
        v2al96 = 14
        v2al100 = 18    
        v2al108 = 26
        v2al110 = 28
        v2al114 = 31

        izkaziCol = ["Izkazi_A", "Izkazi_B", "Izkazi_C", "Izkazi_D", "Izkazi_E"]
        izkazi2Col = ["Izkazi2_A", "Izkazi2_B", "Izkazi2_C", "Izkazi2_D", "Izkazi2_E"]

        for i in range(len(izkaziCol)):
            self.df.loc[i, "Kazalniki_4"] = self.divide(self.df.loc[val45, izkaziCol[i]], self.df.loc[val68, izkaziCol[i]], True)
            
            self.df.loc[i, "Kazalniki_5"] = self.divide( self.df.loc[val52, izkaziCol[i]] + self.df.loc[val62, izkaziCol[i]], self.df.loc[val68, izkaziCol[i]], True )
            
            self.df.loc[i, "Kazalniki_8"] = self.divide(self.df.loc[val45, izkaziCol[i]] + self.df.loc[val48, izkaziCol[i]] + self.df.loc[val57, izkaziCol[i]], self.df.loc[val19, izkaziCol[i]] + self.df.loc[val26, izkaziCol[i]])
            
            self.df.loc[i, "Kazalniki_9"] = self.divide(self.df.loc[val34, izkaziCol[i]], self.df.loc[val66, izkaziCol[i]])
            
            self.df.loc[i, "Kazalniki_10"] = self.divide(self.df.loc[val34, izkaziCol[i]] - self.df.loc[val26, izkaziCol[i]], self.df.loc[val66, izkaziCol[i]])
            
            self.df.loc[i, "Kazalniki_11"] = self.divide(self.df.loc[val32, izkaziCol[i]], self.df.loc[v2al85, izkazi2Col[i]] + self.df.loc[v2al90, izkazi2Col[i]])           
            
            if( i == 0 ):
                self.df.loc[i, "Kazalniki_14"] = self.divide(-self.df.loc[v2al87, izkazi2Col[i]]/self.df.loc[4, "St_Mesecev"]*12, self.df.loc[val26, izkaziCol[i]]/2)

                self.df.loc[i, "Kazalniki_15"] = self.divide( (self.df.loc[v2al85, izkazi2Col[i]] + self.df.loc[v2al91, izkazi2Col[i]])/self.df.loc[4, "St_Mesecev"]*12 , self.df.loc[val32, izkaziCol[i]]/2)           

                self.df.loc[i, "Kazalniki_16"] = self.divide((-self.df.loc[v2al87, izkazi2Col[i]] - self.df.loc[v2al92, izkazi2Col[i]] - self.df.loc[v2al93, izkazi2Col[i]] - self.df.loc[v2al94, izkazi2Col[i]])/self.df.loc[4, "St_Mesecev"]*12, self.df.loc[val65, izkaziCol[i]]/2)

                self.df.loc[i, "Kazalniki_19"] = round( (self.df.loc[val26, izkaziCol[i]]/2) / ( (-self.df.loc[v2al87, izkazi2Col[i]])/self.df.loc[4, "St_Mesecev"]*12) * 365)

                self.df.loc[i, "Kazalniki_20"] = round( (self.df.loc[val32, izkaziCol[i]]/2) / (( self.df.loc[v2al85, izkazi2Col[i]] + self.df.loc[v2al91, izkazi2Col[i]])/self.df.loc[4, "St_Mesecev"]*12) * 365)

                self.df.loc[i, "Kazalniki_21"] = -round( (self.df.loc[val65, izkaziCol[i]]/2) / (( - self.df.loc[v2al87, izkazi2Col[i]] - self.df.loc[v2al92, izkazi2Col[i]] - self.df.loc[v2al93, izkazi2Col[i]] - self.df.loc[v2al94, izkazi2Col[i]]) / self.df.loc[4, "St_Mesecev"]*12) * 365)
            else:
                self.df.loc[i, "Kazalniki_14"] = self.divide(-self.df.loc[v2al87, izkazi2Col[i]]/self.df.loc[4-i, "St_Mesecev"]*12, (self.df.loc[val26, izkaziCol[i]] + self.df.loc[val26, izkaziCol[i-1]])/2)

                self.df.loc[i, "Kazalniki_15"] = self.divide( (self.df.loc[v2al85, izkazi2Col[i]] + self.df.loc[v2al91, izkazi2Col[i]])/self.df.loc[4-i, "St_Mesecev"]*12 , (self.df.loc[val32, izkaziCol[i]] + self.df.loc[val32, izkaziCol[i-1]])/2)

                self.df.loc[i, "Kazalniki_16"] = self.divide((-self.df.loc[v2al87, izkazi2Col[i]] - self.df.loc[v2al92, izkazi2Col[i]] - self.df.loc[v2al93, izkazi2Col[i]] - self.df.loc[v2al94, izkazi2Col[i]])/self.df.loc[4-i, "St_Mesecev"]*12, (self.df.loc[val65, izkaziCol[i]] + self.df.loc[val65, izkaziCol[i-1]])/2)

                self.df.loc[i, "Kazalniki_19"] = round( ((self.df.loc[val26, izkaziCol[i]]+self.df.loc[val26, izkaziCol[i-1]])/2) / (( -self.df.loc[v2al87, izkazi2Col[i]])/self.df.loc[4-i, "St_Mesecev"]*12) * 365)

                self.df.loc[i, "Kazalniki_20"] = round( ((self.df.loc[val32, izkaziCol[i]] + self.df.loc[val32, izkaziCol[i-1]])/2) / (( self.df.loc[v2al85, izkazi2Col[i]] + self.df.loc[v2al91, izkazi2Col[i]])/self.df.loc[4-i, "St_Mesecev"]*12)  * 365)

                self.df.loc[i, "Kazalniki_21"] = -round( ((self.df.loc[val65, izkaziCol[i]] + self.df.loc[val65, izkaziCol[i-1]])/2) / (( -self.df.loc[v2al87, izkazi2Col[i]] - self.df.loc[v2al92, izkazi2Col[i]] - self.df.loc[v2al93, izkazi2Col[i]] - self.df.loc[v2al94, izkazi2Col[i]])/self.df.loc[4-i, "St_Mesecev"]*12) * 365)

            self.df.loc[i, "Kazalniki_22"] = round( self.df.loc[i, "Kazalniki_19"] + self.df.loc[i, "Kazalniki_20"] + self.df.loc[i, "Kazalniki_21"] )

            if(i > 0 and i <= 3):
                self.df.loc[i, "Kazalniki_25"] = round( self.df.loc[val12, izkaziCol[i]] - self.df.loc[val12, izkaziCol[i-1]] - self.df.loc[v2al96, izkazi2Col[i]] )
            if(i == 4):
                if(self.info.Imamo_podatke_za == "Da"):
                    self.df.loc[i, "Kazalniki_25"] = round( self.df.loc[val12, izkaziCol[i]] - self.df.loc[val12, izkaziCol[i-1]] - self.df.loc[v2al96, izkazi2Col[i]] )
                else:
                    self.df.loc[i, "Kazalniki_25"] = 0
            
            if(i > 0 and self.df.loc[v2al85, izkazi2Col[i]] > 0):
                self.df.loc[i, "Kazalniki_26"] = self.divide( self.df.loc[i, "Kazalniki_25"], self.df.loc[v2al85, izkazi2Col[i]], True )

                self.df.loc[i, "Kazalniki_27"] = self.divide( self.df.loc[i, "Kazalniki_25"], self.df.loc[v2al95, izkazi2Col[i]], True )
                
                self.df.loc[i, "Kazalniki_28"] = -self.df.loc[v2al96, izkazi2Col[i]]

            if i == 0  :
                self.df.loc[i, "Kazalniki_31"] = round(self.divideOnly( self.df.loc[v2al110, izkazi2Col[i]], self.df.loc[val45, izkaziCol[i]]), 3)
                
                self.df.loc[i, "Kazalniki_32"] = round(self.divideOnly( self.df.loc[v2al110, izkazi2Col[i]] , self.df.loc[val36, izkaziCol[i]]), 3)

            elif i > 0 and i <= 3:
                self.df.loc[i, "Kazalniki_31"] = round(self.divideOnly( self.df.loc[v2al110, izkazi2Col[i]], (self.df.loc[val45, izkaziCol[i-1]] + self.df.loc[val45, izkaziCol[i]])/2), 3)

                self.df.loc[i, "Kazalniki_32"] = round(self.divideOnly( self.df.loc[v2al110, izkazi2Col[i]], (self.df.loc[val36, izkaziCol[i-1]] + self.df.loc[val36, izkaziCol[i]])/2), 3)
            elif i == 4:
                if(self.info.Imamo_podatke_za == "Da"):
                    self.df.loc[i, "Kazalniki_31"] = round(self.divideOnly( self.df.loc[v2al110, izkazi2Col[i]], (self.df.loc[val45, izkaziCol[i-1]] + self.df.loc[val45, izkaziCol[i]])/2), 3)

                    self.df.loc[i, "Kazalniki_32"] = round(self.divideOnly( self.df.loc[v2al110, izkazi2Col[i]], (self.df.loc[val36, izkaziCol[i-1]]  + self.df.loc[val36, izkaziCol[i]])/2), 3)
                else:
                    self.df.loc[i, "Kazalniki_31"] = 0
                    self.df.loc[i, "Kazalniki_32"] = 0
            
            self.df.loc[i, "Kazalniki_34"] = self.df.loc[v2al114, izkazi2Col[i]]

            if( i >= 0 and i <= 3 and self.df.loc[val36, izkaziCol[i]] ):
                self.df.loc[i, "Kazalniki_36"] = round(
                    1.2*((self.df.loc[val34, izkaziCol[i]] + self.df.loc[val35, izkaziCol[i]])/self.df.loc[val36, izkaziCol[i]]) + 1.4*((self.df.loc[val43, izkaziCol[i]])/self.df.loc[val36, izkaziCol[i]]) + 3.3*((self.df.loc[v2al100, izkazi2Col[i]])/self.df.loc[val36, izkaziCol[i]]) + 0.6*((self.df.loc[val45, izkaziCol[i]])/(self.df.loc[val48, izkaziCol[i]] + self.df.loc[val57, izkaziCol[i]] + self.df.loc[val66, izkaziCol[i]] + self.df.loc[val67, izkaziCol[i]])) + 0.999* (self.df.loc[v2al85, izkazi2Col[i]]/self.df.loc[val36, izkaziCol[i]])  
                , 2)
            elif( i == 4 and self.df.loc[val36, izkaziCol[i]] ):
                self.df.loc[i, "Kazalniki_36"] = round(
                    1.2*((self.df.loc[val34, izkaziCol[i]] + self.df.loc[val35, izkaziCol[i]])/self.df.loc[val36, izkaziCol[i]]) + 1.4*((self.df.loc[val43, izkaziCol[i]])/self.df.loc[val36, izkaziCol[i]]) + 3.3*((self.df.loc[v2al100, izkazi2Col[i]]/self.df.loc[0, "St_Mesecev"]*12)/self.df.loc[val36, izkaziCol[i]]) + 0.6*((self.df.loc[val45, izkaziCol[i]])/(self.df.loc[val48, izkaziCol[i]] + self.df.loc[val57, izkaziCol[i]] + self.df.loc[val66, izkaziCol[i]] + self.df.loc[val67, izkaziCol[i]])) + 0.999* ((self.df.loc[v2al85, izkazi2Col[i]]/self.df.loc[4-i, "St_Mesecev"]*12)/self.df.loc[val36, izkaziCol[i]])  
                , 2)
            else:
                self.df.loc[i, "Kazalniki_36"] = 0

            if( i >= 0 and i <= 3 ):
                self.df.loc[i, "Kazalniki_53"] = round(
                    (1.5*(self.df.loc[v2al95, izkazi2Col[i]] / (self.df.loc[val57, izkaziCol[i]]+self.df.loc[val66, izkaziCol[i]]))) + (0.08*(self.df.loc[val36, izkaziCol[i]] / (self.df.loc[val57, izkaziCol[i]] + self.df.loc[val66, izkaziCol[i]] ))) + (10*(self.df.loc[v2al110, izkazi2Col[i]] / self.df.loc[val36, izkaziCol[i]])) + (5*(self.df.loc[v2al110, izkazi2Col[i]]/self.df.loc[v2al85, izkazi2Col[i]])) + (0.3*(self.df.loc[val26, izkaziCol[i]]/self.df.loc[v2al85, izkazi2Col[i]])) + (0.1 *(self.df.loc[v2al85, izkazi2Col[i]] / self.df.loc[val36, izkaziCol[i]])), 2)
            elif( i == 4 and self.df.loc[val36, izkaziCol[i]] ):
                self.df.loc[i, "Kazalniki_53"] = round(
                    (1.5*((self.df.loc[v2al95, izkazi2Col[i]] / self.df.loc[4-i, "St_Mesecev"]*12) / (self.df.loc[val57, izkaziCol[i]]+self.df.loc[val66, izkaziCol[i]]))) + (0.08*(self.df.loc[val36, izkaziCol[i]] / (self.df.loc[val57, izkaziCol[i]] + self.df.loc[val66, izkaziCol[i]] ))) + (10*((self.df.loc[v2al110, izkazi2Col[i]]/self.df.loc[4-i, "St_Mesecev"]*12) / self.df.loc[val36, izkaziCol[i]])) + (5*(self.df.loc[v2al110, izkazi2Col[i]]/self.df.loc[v2al85, izkazi2Col[i]])) + (0.3*(self.df.loc[val26, izkaziCol[i]]/(self.df.loc[v2al85, izkazi2Col[i]]/self.df.loc[4-i, "St_Mesecev"]*12))) + (0.1 *((self.df.loc[v2al85, izkazi2Col[i]] /self.df.loc[4-i, "St_Mesecev"]*12) / self.df.loc[val36, izkaziCol[i]])), 2)
            else:
                self.df.loc[i, "Kazalniki_53"] = 0

            if( i >= 0 and i <= 4 and self.df.loc[val36, izkaziCol[i]] and self.df.loc[val33, izkaziCol[i]] ):
                self.df.loc[i, "Kazalniki_76"] = round(
                    ((self.df.loc[val33, izkaziCol[i]]*5.24) / self.df.loc[val36, izkaziCol[i]]) + 1111111 if(self.df.loc[val33, izkaziCol[i]] < 1) else ((self.df.loc[v2al85, izkazi2Col[i]] * 0.0053)/ self.df.loc[val33, izkaziCol[i]]) +  ((self.df.loc[v2al108, izkazi2Col[i]] * 6.6507)/self.df.loc[val36, izkaziCol[i]]) + (((self.df.loc[val52, izkaziCol[i]] + self.df.loc[val62, izkaziCol[i]])*4.409)/self.df.loc[val36, izkaziCol[i]]) + ((self.df.loc[val19, izkaziCol[i]] * 0.0791)/self.df.loc[val36, izkaziCol[i]]) + ((self.df.loc[val34, izkaziCol[i]] * 0.102)/self.df.loc[v2al85, izkazi2Col[i]]), 2)
            else:
                self.df.loc[i, "Kazalniki_76"] = 0

            self.df.loc[i, "Kazalniki_77"] = round(1/(1 + pow(math.exp(1), -(-2.043 + self.df.loc[i, "Kazalniki_76"]))), 2)

            if( i >= 0 and i <= 4 and self.df.loc[val36, izkaziCol[i]] and self.df.loc[val66, izkaziCol[i]] ):
                self.df.loc[i, "Kazalniki_90"] = round(
                    ((-4.5*(self.df.loc[v2al110, izkazi2Col[i]]/self.df.loc[val36, izkaziCol[i]])) + (5.7 * (( self.df.loc[val57, izkaziCol[i]] + self.df.loc[val66, izkaziCol[i]] + self.df.loc[val67, izkaziCol[i]])/self.df.loc[val36, izkaziCol[i]])) - (0.004*(self.df.loc[val34, izkaziCol[i]]/ self.df.loc[val66, izkaziCol[i]]))), 2)
            else:
                self.df.loc[i, "Kazalniki_90"] = 0

            self.df.loc[i, "Kazalniki_91"] = round(1/(1 + pow(math.exp(1), -(-4.3 + self.df.loc[i, "Kazalniki_90"]))), 2)


            self.df.loc[i, "Kazalniki_114"] = round((self.df.loc[v2al85, izkazi2Col[i]] + self.df.loc[v2al93, izkazi2Col[i]]) / self.df.loc[4-i, "St_Mesecev"])

        for i in range(len(izkaziCol)):
            try:
                self.df.loc[i, "Kazalniki_38"] = round(self.findMax("Kazalniki_36", 5)) + 0.61
            except:
                self.df.loc[i, "Kazalniki_38"] = round(self.findMax("Kazalniki_36", 4)) + 0.61

            self.df.loc[i, "Kazalniki_38"] = max(4, self.df.loc[i, "Kazalniki_38"])
            self.df.loc[i, "Kazalniki_39"] = self.info.Kazalniki_B39
            self.df.loc[i, "Kazalniki_40"] = self.info.Kazalniki_B40

            self.df.loc[i, "Kazalniki_43"] = self.df.loc[i, "Kazalniki_38"] - self.df.loc[i, "Kazalniki_39"]
            self.df.loc[i, "Kazalniki_44"] = self.df.loc[i, "Kazalniki_39"] - self.df.loc[i, "Kazalniki_40"]
            self.df.loc[i, "Kazalniki_45"] = self.info.Kazalniki_B45
            self.df.loc[i, "Kazalniki_62"] = -0.5-self.info.Kazalniki_B56
            self.df.loc[i, "Kazalniki_63"] = self.info.Kazalniki_B57
            self.df.loc[i, "Kazalniki_64"] = self.info.Kazalniki_B58 - self.info.Kazalniki_B57
            self.df.loc[i, "Kazalniki_65"] = self.info.Kazalniki_B59 - self.info.Kazalniki_B58
            self.df.loc[i, "Kazalniki_66"] = 5 - self.info.Kazalniki_B59
            self.df.loc[i, "Kazalniki_79"] = self.info.Kazalniki_B79
            self.df.loc[i, "Kazalniki_82"] = self.df.loc[i, "Kazalniki_79"]
            self.df.loc[i, "Kazalniki_83"] = 1 - self.df.loc[i, "Kazalniki_79"]
            self.df.loc[i, "Kazalniki_104"] = self.info.Kazalniki_B99
            self.df.loc[i, "Kazalniki_105"] = self.info.Kazalniki_B100 - self.info.Kazalniki_B99
            self.df.loc[i, "Kazalniki_106"] = self.info.Kazalniki_B101 - self.info.Kazalniki_B100
        
        self.df.loc[0, "Kazalniki_97"] = self.info.Weinrich_B42
        self.df.loc[1, "Kazalniki_97"] = self.info.Weinrich_C42
        self.df.loc[2, "Kazalniki_97"] = self.info.Weinrich_D42
        self.df.loc[3, "Kazalniki_97"] = self.info.Weinrich_E42
        self.df.loc[4, "Kazalniki_97"] = self.info.Weinrich_F42


    def findMax(self, col, nDigit):
        if(nDigit == 5):
            return max([self.df.loc[0, col], self.df.loc[1, col], self.df.loc[2, col], self.df.loc[3, col], self.df.loc[4, col]])
        else:
            return max([self.df.loc[0, col], self.df.loc[1, col], self.df.loc[2, col], self.df.loc[3, col]])


    def divide(self, num1, num2, isPercentage = False , isRoundToOne = False):
        result = 0
        if(num2 != 0):
            result = num1/num2
            if(str(result).lower() != 'nan'):
                if(isPercentage and isRoundToOne):
                    return round(result, 1)
                if(not isPercentage):
                    return round(result, 1)
                else:
                    return round(result*100)
        return result
    
    def divideOnly(self, num1, num2):
        result = 0
        if(num2 != 0):
            return num1/num2
        return result

    def add(num1, num2):
        return num1 + num2

    @property
    def Kazalniki_4(self):
        return self.df.Kazalniki_4
    
    @property
    def Kazalniki_5(self):
        return self.df.Kazalniki_5
    
    @property
    def Kazalniki_8(self):
        return self.df.Kazalniki_8

    @property
    def Kazalniki_9(self):
        return self.df.Kazalniki_9

    @property
    def Kazalniki_10(self):
        return self.df.Kazalniki_10

    @property
    def Kazalniki_11(self):
        return self.df.Kazalniki_11
    
    @property
    def Kazalniki_14(self):
        return self.df.Kazalniki_14

    @property
    def Kazalniki_15(self):
        return self.df.Kazalniki_15

    @property
    def Kazalniki_16(self):
        return self.df.Kazalniki_16

    @property
    def Kazalniki_19(self):
        return self.df.Kazalniki_19

    @property
    def Kazalniki_20(self):
        return self.df.Kazalniki_20

    @property
    def Kazalniki_21(self):
        return self.df.Kazalniki_21
    
    @property
    def Kazalniki_22(self):
        return self.df.Kazalniki_22
 
    @property
    def Kazalniki_25(self):
        return self.df.Kazalniki_25
    
    @property
    def Kazalniki_26(self):
        return self.df.Kazalniki_26
    
    @property
    def Kazalniki_27(self):
        return self.df.Kazalniki_27

    @property
    def Kazalniki_28(self):
        return self.df.Kazalniki_28
   
    @property
    def Kazalniki_31(self):
        return self.df.Kazalniki_31
   
    @property
    def Kazalniki_32(self):
        return self.df.Kazalniki_32
   
    @property
    def Kazalniki_34(self):
        return self.df.Kazalniki_34

    @property
    def Kazalniki_36(self):
        return self.df.Kazalniki_36
    
    @property
    def Kazalniki_38(self):
        return self.df.Kazalniki_38

    @property
    def Kazalniki_39(self):
        return self.df.Kazalniki_39
    
    @property
    def Kazalniki_40(self):
        return self.df.Kazalniki_40

    @property
    def Kazalniki_43(self):
        return self.df.Kazalniki_43

    @property
    def Kazalniki_44(self):
        return self.df.Kazalniki_44

    @property
    def Kazalniki_45(self):
        return self.df.Kazalniki_45
    
    @property
    def Kazalniki_53(self):
        return self.df.Kazalniki_53

    @property
    def Kazalniki_62(self):
        return self.df.Kazalniki_62
    
    @property
    def Kazalniki_63(self):
        return self.df.Kazalniki_63
    
    @property
    def Kazalniki_64(self):
        return self.df.Kazalniki_64
    
    @property
    def Kazalniki_65(self):
        return self.df.Kazalniki_65
    
    @property
    def Kazalniki_66(self):
        return self.df.Kazalniki_66
    
    @property
    def Kazalniki_77(self):
        return self.df.Kazalniki_77
    
    @property
    def Kazalniki_79(self):
        return self.df.Kazalniki_79
    
    @property
    def Kazalniki_82(self):
        return self.df.Kazalniki_82

    @property
    def Kazalniki_83(self):
        return self.df.Kazalniki_83

    @property
    def Kazalniki_91(self):
        return self.df.Kazalniki_91

    @property
    def Kazalniki_97(self):
        return self.df.Kazalniki_97

    @property
    def Kazalniki_104(self):
        return self.df.Kazalniki_104

    @property
    def Kazalniki_105(self):
        return self.df.Kazalniki_105

    @property
    def Kazalniki_106(self):
        return self.df.Kazalniki_106
    
    @property
    def Kazalniki_114(self):
        return self.df.Kazalniki_114