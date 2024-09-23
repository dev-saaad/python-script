import pandas as pd

def readExcelData(file,sheets,header):
    print(f"Reading File from ==> {file}")
    bs_data = pd.read_excel(file, sheet_name=sheets[0], header=header)
    ipi_data = pd.read_excel(file, sheet_name=sheets[1], header=header)
    return bs_data, ipi_data

def readAllSheetInSingleDf(input):
    file = input["input_path"]
    sheets = input["input_sheets"]
    headers = input["headers"]

    print(f"Reading File from ==> {file}")
    print(f"Sheets ==> {sheets}")
    df = pd.DataFrame(index=range(346))
    for i in range(len(sheets)):
        sheetDf = pd.read_excel(file, sheet_name=sheets[i], header=headers[i]-1)
        if(sheets[i] == 'Izkazi_Const'):
            sheetDf.rename(columns=lambda x: str(sheets[i])+"_"+str(x), inplace=True)
        df = pd.concat([df, sheetDf], axis=1)
    
    return df

def readAllSheetSeparately(input):
    print(f"Reading File from ==> {file}")
    file = input["input_path"]
    sheets = input["input_sheets"]
    headers = input["headers"]

    bs_gavin_data = pd.read_excel(file, sheet_name=sheets[0], header=headers[0])
    ipi_gavin_data = pd.read_excel(file, sheet_name=sheets[1], header=headers[1])
    bs_ajpes_data = pd.read_excel(file, sheet_name=sheets[2], header=headers[2])
    ipi_ajpes_data = pd.read_excel(file, sheet_name=sheets[3], header=headers[3])
    iskazi_const_data = pd.read_excel(file, sheet_name=sheets[4], header=headers[4])
    info_data = pd.read_excel(file, sheet_name=sheets[5], header=headers[0])

    return bs_gavin_data, ipi_gavin_data, bs_ajpes_data, ipi_ajpes_data, iskazi_const_data, info_data


def readXMLDataPodjetjeFinancni(file):
    return pd.read_xml(file,xpath="//PodjetjeFinancni/Item")

def readXMLDataPodjetjeOsnovno(file):
    return pd.read_xml(file,xpath="//PodjetjeOsnovno/Item")

def readXMLDataPodjetjeBlokadeTRR(file):
    return pd.read_xml(file,xpath="//PodjetjeBlokadeTRR/Item")

def readXMLDataPodjetjeNaroki(file):
    return pd.read_xml(file,xpath="//PodjetjeNaroki/Item")