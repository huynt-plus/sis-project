import json
import os
from section_identify import extract_section
import numpy as np
import sys


#Load values of "use of proceeds" checkboxes
def load_all_use_of_proceeds():
	x_data = []
	y_data = []
	
	arr = os.listdir("data/raw_data/FORMS/")
	for file in arr:		
		with open('data/raw_data/FORMS/'+ file) as data_file:
			try:
				data = json.load(data_file)	
			except:
				print("Json load error",sys.exc_info(), data_file)
				continue
		try:
			#edit here to get the expected field
			if (data["form_data"]["sections"]["Review Overview"]["Scope of Review"]["use of proceeds"]) == True:
				y = 1
			else:
				y = 0
		except: 
			print ("Field load error in ",file)
			continue
		
		report_file = file.replace("_erf.json",".json")
		report_file = report_file.replace(".json","_report.txt")
		if not os.path.exists('data/raw_data/REPORT_TXT/'+ report_file):
			print ("File doesnt exist:", 'data/raw_data/REPORT_TXT/'+ report_file)
			continue
			
		sections = extract_section('data/raw_data/REPORT_TXT/'+ report_file)
		x_data_sample = ' '.join(sections)
		x_data.append(x_data_sample)
		y_data.append(y)

	print ("len(x), len(y)", len(x_data), len(y_data))
	return np.array(x_data), np.array(y_data)



	
#Load values of "linkage to individual bond(s)" checkboxes	
def load_all_use_of_proceeds_Detailed_Review_Reporting_Use_of_Proceeds_Reporting_linkage_to_individual_bond():
	x_data = []
	y_data = []
	
	arr = os.listdir("data/form/")
	for file in arr:		
		with open('data/form/'+ file) as data_file:
			try:
				data = json.load(data_file)	
			except:
				print("Json load error",sys.exc_info(), data_file)
				continue
		try:
			if (data["form_data"]["sections"]["Detailed Review"]["Reporting"]["Use of Proceeds Reporting"]["linkage to individual bond(s)"]) == True:
				y = 1
			else:
				y = 0
		except: 
			print ("Field load error in ",file)
			continue
		
		report_file = file.replace("_erf.json",".json")
		report_file = report_file.replace(".json","_report.txt")
		if not os.path.exists('data/report/'+ report_file):
			print ("File doesnt exist:", 'data/report/'+ report_file)
			continue
			
		sections = extract_section('data/report/'+ report_file)		
		x_data_sample = ' '.join(sections)
		x_data.append(x_data_sample)
		y_data.append(y)

	print ("len(x), len(y)", len(x_data), len(y_data))
	return np.array(x_data), np.array(y_data)

	
# chu chay thu 2 ham phia duoi de view bug	
load_all_use_of_proceeds()

#load_all_use_of_proceeds_Detailed_Review_Reporting_Use_of_Proceeds_Reporting_linkage_to_individual_bond
