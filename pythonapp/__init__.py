import pandas as pd
from pythonapp.Data import DataClass
from pythonapp.Izkazi2 import Izkazi2Class
from pythonapp.Izkazi2new import Izkazi2NewClass
from pythonapp.Izkazinew import IzkaziNewClass
from pythonapp.Predopostavke import PredopostavkeClass
from pythonapp.Izkazi import IzkaziClass
from pythonapp.helper.utils import ProductDescriptionsMacroFile
from pythonapp.kazalniki import KazalnikiClass
from pythonapp.kazalnikiNew import KazalnikiNewClass
from pythonapp.report import ReportClass
from pythonapp.reportNew import ReportNewClass
from pythonapp.weinrich import WeinrichClass
from pythonapp.weinrichNew import WeinrichNewClass
from pythonapp.helper.getData import readAllSheetInSingleDf, readExcelData, readXMLDataPodjetjeBlokadeTRR, readXMLDataPodjetjeFinancni, readXMLDataPodjetjeNaroki, readXMLDataPodjetjeOsnovno
import openpyxl
import os
import win32com.client
from pywintypes import com_error

def getInputDataFromExcel(input):
    #Reading gvin input sheets
    gvin_file_path = input["gvin"]["file_path"]
    gvin_input_sheets = input["gvin"]["input_sheets"]
    gvin_start_row = input["gvin"]["start_row"] - 1
    bs_gvin_data, ipi_gvin_data = readExcelData(gvin_file_path, gvin_input_sheets, gvin_start_row)
    # print(f"BS_Gvin file data \n {bs_gvin_data}")
    
    #Reading ajpes input sheets
    ajpes_file_path = input["ajpes"]["file_path"]
    ajpes_input_sheets = input["ajpes"]["input_sheets"]
    ajpes_start_row = input["ajpes"]["start_row"] - 1
    bs_ajpes_data, ipi_ajpes_data = readExcelData(ajpes_file_path, ajpes_input_sheets, ajpes_start_row)
    # print(f"BS_ajpes file data \n {bs_ajpes_data}")
    
    # print("Reading xml file")
    # xml_file = input['api_data_xml']
    # api_data = readXMLData(xml_file)
    # return bs_gvin_data, ipi_gvin_data, bs_ajpes_data, ipi_ajpes_data, api_data

def calculate(input):
    #    bs_gvin_data, ipi_gvin_data, bs_ajpes_data, ipi_ajpes_data, api_data = getInputDataFromExcel(input)
        df = readAllSheetInSingleDf(input)
        infoDf = ProductDescriptionsMacroFile(pd.read_excel(input['input_path'], sheet_name='Info', header=0)) 

        print("Reading xml file")
        xml_file = input['api_data_xml']
        api_data = readXMLDataPodjetjeFinancni(xml_file)
        apiPodjetjeOsnovno = readXMLDataPodjetjeOsnovno(xml_file)
        apiPodjetjeBlokadeTRR = readXMLDataPodjetjeBlokadeTRR(xml_file)
        apiPodjetjeNaroki = readXMLDataPodjetjeNaroki(xml_file)

        writer = pd.ExcelWriter(input['output_path'], engine='xlsxwriter')

        api_data = api_data.set_index('Leto').T.reset_index()
        api_data = api_data.drop(columns=[2017], axis=1)
        apiDataCol = api_data.columns.delete(0).tolist()

        apiDataCol.reverse()
        predopostavkeList = {
            "PL": [],
            "St_Mesecev": []
        }

        predopostavke = []
        for val in apiDataCol:
            predopostavke.append({
                "Obdobja": val,
                "Vir": "Gvaop",
                "St_Mesecev": 12
            })
            predopostavkeList['PL'].append("PL"+str(int(val))[-2:])
            predopostavkeList['St_Mesecev'].append(12)
        
        if(infoDf.info['Obdobja-1']):
            predopostavke.append({
                "Obdobja": infoDf.info['Obdobja-1'],
                "Vir": "AOP",
                "St_Mesecev": infoDf.info['St-Mesecev-1']
            })
            predopostavkeList['PL'].append("PL"+str(int(infoDf.info['Obdobja-1']))[-2:])
            predopostavkeList['St_Mesecev'].append(infoDf.info['St-Mesecev-1'])

        if(infoDf.info['Obdobja-2']):
            predopostavke.append({
                "Obdobja": infoDf.info['Obdobja-2'],
                "Vir": "AOP",
                "St_Mesecev": infoDf.info['St-Mesecev-2']
            })
            predopostavkeList['PL'].append("PL"+str(int(infoDf.info['Obdobja-2']))[-2:])
            predopostavkeList['St_Mesecev'].append(infoDf.info['St-Mesecev-2'])

            
        api_data['Gvaop'] = api_data['index'].str.replace('gvaop', "[") + "]"
        api_data = api_data[["index", "Gvaop"]+apiDataCol]
        df = df.rename(columns={'Unnamed: 2': 'AOP'})
        df = df.drop(columns=['Unnamed: 0', 'Unnamed: 1'], axis=1)
        df = pd.concat([df, api_data], axis=1)
        api_data.to_excel(writer, sheet_name="API Data", index=False, header=True, startrow=0, startcol=0)
        df.to_excel(writer, sheet_name="Input Dataframe", index=False, header=True, startrow=0, startcol=0)

        inputs = {
            "isAOP": infoDf.info['Imamo_podatke_za'] if(infoDf.info['Imamo_podatke_za']) else "Da",
            "St_Mesecev": 12,
            "Pogoj": 20,
            "Kazalniki_B39": 2.99,
            "Kazalniki_B40": 1.81,
            "Kazalniki_B45": 1.81,
            "Kazalniki_B56": 0,
            "Kazalniki_B57": 1,
            "Kazalniki_B58": 2,
            "Kazalniki_B59": 3,
            "Kazalniki_B79": 0.5,
            "Kazalniki_B99": 14,
            "Kazalniki_B100": 24,
            "Kazalniki_B101": 32,
            "Dolznik": apiPodjetjeOsnovno.at[0, 'Naziv'],
            "Naslov": apiPodjetjeOsnovno.at[0, 'Ulica'] + ", " + str(apiPodjetjeOsnovno.at[0, 'PostnaSt']) + " " + apiPodjetjeOsnovno.at[0, 'PostaNaziv'],
            "Maticna_stevilka": apiPodjetjeOsnovno.at[0, 'Maticna'],
            "Davcna_stevilka": apiPodjetjeOsnovno.at[0, 'Davcna'],
            "Stevilo_blokiranih_TRR": apiPodjetjeBlokadeTRR[apiPodjetjeBlokadeTRR.RezBlo == 'B'].count()['RezBlo'],
            "Stevilo_rezervacij": apiPodjetjeBlokadeTRR[apiPodjetjeBlokadeTRR.RezBlo == 'R'].count()['RezBlo'],
            "Lastniki_Tozeni": apiPodjetjeNaroki[apiPodjetjeNaroki.Status == 'tozeni'].sum()['Znesek'],
            "Zastopniki_Tozeci": apiPodjetjeNaroki[apiPodjetjeNaroki.Status == 'tozeci'].sum()['Znesek'],
            "Povprecni_dnevi_zamud": 0,
            "Max_dnevi_zamud": 0,
            "Povprecni_prihodki": 0,
            "Maksimalen_limit": 0,
            "Priporocen_limit": 0,
            "Priporocen_limit_Trend": 0,
            "Priporocen_limit_W18": 0,
            "Priporocen_limit_W19": 0,
            'Cesija_K1': ""
            # "Prihodki_od_prodaje": df.loc[df['Gvaop'] == '[050]', predopostavke[-1]['Obdobja']].values[0] if((df.loc[df['Gvaop'] == '[050]', predopostavke[-1]['Obdobja']].values[0] / df.loc[df['Gvaop'] == '[050]', predopostavke[-2]['Obdobja']].values[0])-1 < -20/100) else (df.loc[df['Gvaop'] == '[050]', predopostavke[-1]['Obdobja']].values[0] + df.loc[df['Gvaop'] == '[050]', predopostavke[-2]['Obdobja']].values[0])/2 
        }
        # print(df.columns)
        # for p in predopostavke:
        #     print(p)
        # print(predopostavkeList )
        # for pl in predopostavkeList:
        #     print("pl",pl)
        # for i in inputs:
        #     print(i)
        # # print(inputs)

        iskaziNewDf = IzkaziNewClass(df, predopostavke, inputs)
        iskaziNewDf.compute_tables()
        pd.DataFrame([iskaziNewDf.Izkazi_A, iskaziNewDf.Izkazi_B, iskaziNewDf.Izkazi_C, iskaziNewDf.Izkazi_D, iskaziNewDf.Izkazi_E, iskaziNewDf.strukt]).transpose().to_excel(writer,sheet_name="IskaziNew", index=False)

        iskazi2NewDf = Izkazi2NewClass(df, predopostavke)
        iskazi2NewDf.compute_tables()
        pd.DataFrame([iskazi2NewDf.Izkazi2_A, iskazi2NewDf.Izkazi2_B, iskazi2NewDf.Izkazi2_C, iskazi2NewDf.Izkazi2_D, iskazi2NewDf.Izkazi2_E, iskazi2NewDf.Izkazi2_strukt]).transpose().to_excel(writer,sheet_name="Iskazi2New", index=False)
        
        weinrichDf = WeinrichNewClass(df, predopostavke, inputs, predopostavkeList)
        weinrichDf.compute_tables()
        pd.DataFrame([weinrichDf.Weinrich_A, weinrichDf.Weinrich_B, weinrichDf.Weinrich_C, weinrichDf.Weinrich_D, weinrichDf.Weinrich_E]).transpose().to_excel(writer,sheet_name="Weinrich", index=False)

        kazalnikiNew = KazalnikiNewClass(df, predopostavke, inputs, predopostavkeList)
        kazalnikiNew.compute_tables()
        pd.DataFrame([kazalnikiNew.Kazalniki_4, kazalnikiNew.Kazalniki_5, kazalnikiNew.Kazalniki_8, kazalnikiNew.Kazalniki_9, kazalnikiNew.Kazalniki_10, kazalnikiNew.Kazalniki_11, kazalnikiNew.Kazalniki_14, kazalnikiNew.Kazalniki_15, kazalnikiNew.Kazalniki_16, kazalnikiNew.Kazalniki_19, kazalnikiNew.Kazalniki_20, kazalnikiNew.Kazalniki_21, kazalnikiNew.Kazalniki_22, kazalnikiNew.Kazalniki_25, kazalnikiNew.Kazalniki_26, kazalnikiNew.Kazalniki_27, kazalnikiNew.Kazalniki_28, kazalnikiNew.Kazalniki_31, kazalnikiNew.Kazalniki_32, kazalnikiNew.Kazalniki_34, kazalnikiNew.Kazalniki_36, kazalnikiNew.Kazalniki_38, kazalnikiNew.Kazalniki_39, kazalnikiNew.Kazalniki_40, kazalnikiNew.Kazalniki_43, kazalnikiNew.Kazalniki_44, kazalnikiNew.Kazalniki_45, kazalnikiNew.Kazalniki_53, kazalnikiNew.Kazalniki_62, kazalnikiNew.Kazalniki_63, kazalnikiNew.Kazalniki_64, kazalnikiNew.Kazalniki_65, kazalnikiNew.Kazalniki_66, kazalnikiNew.Kazalniki_77, kazalnikiNew.Kazalniki_79, kazalnikiNew.Kazalniki_82, kazalnikiNew.Kazalniki_83, kazalnikiNew.Kazalniki_91, kazalnikiNew.Kazalniki_97, kazalnikiNew.Kazalniki_104, kazalnikiNew.Kazalniki_105, kazalnikiNew.Kazalniki_106, kazalnikiNew.Kazalniki_114 ]).transpose().to_excel(writer,sheet_name="KazalnikiNew", index=False)

        data = DataClass(df, predopostavke, inputs, predopostavkeList)
        data.compute_tables()

        print(inputs)

        reportNew = ReportNewClass(df, predopostavke, inputs, predopostavkeList)
        reportNew.compute_tables()
        pd.DataFrame([reportNew.Report_A, reportNew.Report_B, reportNew.Report_C, reportNew.Report_D, reportNew.Report_E, reportNew.Report_F, reportNew.Report_G, reportNew.Report_H, reportNew.Report_I, reportNew.Report_J, reportNew.Report_K, reportNew.Report_L, reportNew.Report_M, reportNew.Report_N, reportNew.Report_O, reportNew.Report_P, reportNew.Report_Q, reportNew.Report_R]).transpose().to_excel(writer,sheet_name="Report", index=False, header=False)

        writer.save()

        wb = openpyxl.load_workbook('./docs/Report.xlsx')

        writer = pd.ExcelWriter('./docs/Report.xlsx', engine='openpyxl')
        writer.book = wb
        writer.sheets = dict((ws.title, ws) for ws in wb.worksheets)

        print("Writing Output...")
        report = ReportNewClass(df, predopostavke, inputs, predopostavkeList)
        report.compute_tables()
        pd.DataFrame([report.Report_A, report.Report_B, report.Report_C, report.Report_D, report.Report_E, report.Report_F, report.Report_G, report.Report_H, report.Report_I, report.Report_J, report.Report_K, report.Report_L, report.Report_M, report.Report_N, report.Report_O, report.Report_P, report.Report_Q, report.Report_R]).transpose().to_excel(writer, sheet_name="Data", index=False, header=False, startrow=0, startcol=0)

        writer.save()

        wb_path = os.getcwd()+'\docs\Report.xlsx'
        PDF_path = os.getcwd()+'\docs\Report.pdf'
        excel = win32com.client.Dispatch("Excel.Application")
        excel.Visible = False
        try:
            print('Start conversion to PDF')
            # Open
            wb = excel.Workbooks.Open(wb_path)
            # Specify the sheet you want to save by index. 1 is the first (leftmost) sheet.
            ws_index_list = [2]
            wb.WorkSheets(ws_index_list).Select()
            # Save
            wb.ActiveSheet.ExportAsFixedFormat(0, PDF_path)
        except com_error as e:
            print('failed.', e)
        else:
            print('Succeeded.')

        finally:
            excel.Quit()

        #    print("\n\n izkazi output \n\n\n")
        #    print("izkazi.outputColumns \n ",izkazi.output_cols)
        #    izkazi_ouput = pd.DataFrame([izkazi.test, izkazi.Gvaop]).transpose() 
        #    print(izkazi_ouput)
        #    print(api_data)
        