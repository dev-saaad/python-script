from pythonapp import calculate
import time
import logging

start = time.time()
LOG = logging.getLogger(f"default")

def main():
    inputFiles = {
        # "gvin" :{
        #     "file_path": "./docs/gvin_input_data.xlsx",
        #     "input_sheets": ["BS_Gvin", "IPI_Gvin"],
        #     "start_row": 8 #The actual starting row where are the header; donot subtract with -1
        # },
        # "ajpes": {
        #     "file_path": "./docs/ajpes_input_data.xlsx",
        #     "input_sheets": ["BS_Ajpes", "IPI_Ajpes"],
        #     "start_row": 15 #The actual starting row where are the header; donot subtract with -1
        # },
        "input_path": "./docs/input.xlsx",
        # "input_sheets": ["BS_Gvin", "IPI_Gvin", "BS_Ajpes", "IPI_Ajpes", "Izkazi_Const"],
        "input_sheets": ["Izkazi_Const", "Ajpes"],
        # "headers": [8, 8, 15, 15, 1],
        "headers": [1, 2],
        "output_path": "./docs/Output Report.xlsx",
        "api_data_xml": "./docs/api_xml.xml",
        "Predpostavke_vir": "Gvaop", #Two possible values : Gvaop, AOP
    }
    calculate(inputFiles)
    
    end = time.time()
    time_total = end-start
    print(f"Completed in {time_total}")
main()