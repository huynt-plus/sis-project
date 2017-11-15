import json
import os
from section_identify import extract_section
import numpy as np
import sys


#Load values of "use of proceeds" checkboxes
def load_all_use_of_proceeds():
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
			#edit here to get the expected field
			if (data["form_data"]["sections"]["Review Overview"]["Scope of Review"]["Use of proceeds"]) == True:
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
			if (data["form_data"]["sections"]["Detailed Review"]["Reporting"]["Use of Proceeds Reporting"]["Linkage to individual bond(s)"]) == True:
				y = 1
			else:
				y = 0
		except: 
			print ("Field load error in ",file,sys.exc_info())
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

def load_Review_Overview__Roles_of_Review_Provider_certification():
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
			if (data["form_data"]["sections"]["Review Overview"]["Role(s) of Review Provider"]["Certification"]) == True:
				y = 1
			else:
				y = 0
		except: 
			print ("Field load error in ",file,sys.exc_info())
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

def load_Review_Overview__Roles_of_Review_Provider_consultancy():
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
			if (data["form_data"]["sections"]["Review Overview"]["Role(s) of Review Provider"]["Consultancy (incl. 2 nd opinion)"]) == True:
				y = 1
			else:
				y = 0
		except: 
			print ("Field load error in ",file,sys.exc_info())
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
	
def load_Review_Overview__Roles_of_Review_Provider_other():
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
			if (data["form_data"]["sections"]["Review Overview"]["Role(s) of Review Provider"]["Other (please specify)"]) == True:
				y = 1
			else:
				y = 0
		except: 
			print ("Field load error in ",file,sys.exc_info())
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

def load_Review_Overview__Roles_of_Review_Provider_rating():
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
			if (data["form_data"]["sections"]["Review Overview"]["Role(s) of Review Provider"]["Rating"]) == True:
				y = 1
			else:
				y = 0
		except: 
			print ("Field load error in ",file,sys.exc_info())
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

def load_Review_Overview__Roles_of_Review_Provider_verification():
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
			if (data["form_data"]["sections"]["Review Overview"]["Role(s) of Review Provider"]["Verification"]) == True:
				y = 1
			else:
				y = 0
		except: 
			print ("Field load error in ",file,sys.exc_info())
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


def load_Detailed_Review__Use_of_Proceeds_clean_transportation():
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
			if (data["form_data"]["sections"]["Detailed Review"]["Use of Proceeds"]["Use of Proceeds Categories as per GBP"]["Clean transportation"]) == True:
				y = 1
			else:
				y = 0
		except: 
			print ("Field load error in ",file,sys.exc_info())
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

def load_Detailed_Review__Use_of_Proceeds_climate_change_adaptation():
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
			if (data["form_data"]["sections"]["Detailed Review"]["Use of Proceeds"]["Use of Proceeds Categories as per GBP"]["Climate change adaptation"]) == True:
				y = 1
			else:
				y = 0
		except: 
			print ("Field load error in ",file,sys.exc_info())
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

def load_Detailed_Review__Use_of_Proceeds_eco_efficient():
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
			if (data["form_data"]["sections"]["Detailed Review"]["Use of Proceeds"]["Use of Proceeds Categories as per GBP"]["Eco-efficient products, production technologies and processes"]) == True:
				y = 1
			else:
				y = 0
		except: 
			print ("Field load error in ",file,sys.exc_info())
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

def load_Detailed_Review__Use_of_Proceeds_energy_efficiency():
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
			if (data["form_data"]["sections"]["Detailed Review"]["Use of Proceeds"]["Use of Proceeds Categories as per GBP"]["Energy efficiency"]) == True:
				y = 1
			else:
				y = 0
		except: 
			print ("Field load error in ",file,sys.exc_info())
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
	

def load_Detailed_Review__Use_of_Proceeds_other():
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
			if (data["form_data"]["sections"]["Detailed Review"]["Use of Proceeds"]["Use of Proceeds Categories as per GBP"]["Other (please specify)"]) == True:
				y = 1
			else:
				y = 0
		except: 
			print ("Field load error in ",file,sys.exc_info())
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

def load_Detailed_Review__Use_of_Proceeds_pollution_prevention():
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
			if (data["form_data"]["sections"]["Detailed Review"]["Use of Proceeds"]["Use of Proceeds Categories as per GBP"]["Pollution prevention and control"]) == True:
				y = 1
			else:
				y = 0
		except: 
			print ("Field load error in ",file,sys.exc_info())
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

def load_Detailed_Review__Use_of_Proceeds_renewable_energy():
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
			if (data["form_data"]["sections"]["Detailed Review"]["Use of Proceeds"]["Use of Proceeds Categories as per GBP"]["Renewable energy"]) == True:
				y = 1
			else:
				y = 0
		except: 
			print ("Field load error in ",file,sys.exc_info())
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

def load_Detailed_Review__Use_of_Proceeds_sustainable_management():
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
			if (data["form_data"]["sections"]["Detailed Review"]["Use of Proceeds"]["Use of Proceeds Categories as per GBP"]["Sustainable management of living natural resources"]) == True:
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

def load_Detailed_Review__Use_of_Proceeds_sustainable_water_management():
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
			if (data["form_data"]["sections"]["Detailed Review"]["Use of Proceeds"]["Use of Proceeds Categories as per GBP"]["Sustainable water management"]) == True:
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
	
def load_Detailed_Review__Use_of_Proceeds_terrestrial():
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
			if (data["form_data"]["sections"]["Detailed Review"]["Use of Proceeds"]["Use of Proceeds Categories as per GBP"]["Terrestrial and aquatic biodiversity conservation"]) == True:
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

def load_Detailed_Review__Use_of_Proceeds_unknown():
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
			if (data["form_data"]["sections"]["Detailed Review"]["Use of Proceeds"]["Use of Proceeds Categories as per GBP"]["Unknown at issuance but currently expected to conform with GBP categories, or other eligible areas not yet stated in GBPs"]) == True:
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
	
def load_Detailed_Review__Process_for_Project_Evaluation_and_Selection_defined():
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
			if (data["form_data"]["sections"]["Detailed Review"]["Process for Project Evaluation and Selection"]["Evaluation and Selection"]["Defined and transparent criteria for projects eligible for Green Bond proceeds"]) == True:
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

def load_Detailed_Review__Process_for_Project_Evaluation_and_Selection_documented():
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
			if (data["form_data"]["sections"]["Detailed Review"]["Process for Project Evaluation and Selection"]["Evaluation and Selection"]["Documented process to determine that projects fit within defined categories"]) == True:
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
	

#load_all_use_of_proceeds()

# chu uncomment cac ham phia duoi de test nha
load_all_use_of_proceeds_Detailed_Review_Reporting_Use_of_Proceeds_Reporting_linkage_to_individual_bond()
load_Review_Overview__Roles_of_Review_Provider_certification()
load_Review_Overview__Roles_of_Review_Provider_consultancy()
load_Review_Overview__Roles_of_Review_Provider_other()
load_Review_Overview__Roles_of_Review_Provider_rating()
load_Review_Overview__Roles_of_Review_Provider_verification()
load_Detailed_Review__Use_of_Proceeds_clean_transportation()
load_Detailed_Review__Use_of_Proceeds_climate_change_adaptation()
load_Detailed_Review__Use_of_Proceeds_eco_efficient()
load_Detailed_Review__Use_of_Proceeds_energy_efficiency()
load_Detailed_Review__Use_of_Proceeds_other()
load_Detailed_Review__Use_of_Proceeds_pollution_prevention()
load_Detailed_Review__Use_of_Proceeds_renewable_energy()
load_Detailed_Review__Use_of_Proceeds_sustainable_management()
load_Detailed_Review__Use_of_Proceeds_sustainable_water_management()
load_Detailed_Review__Use_of_Proceeds_terrestrial()
load_Detailed_Review__Use_of_Proceeds_unknown()
load_Detailed_Review__Process_for_Project_Evaluation_and_Selection_defined()
load_Detailed_Review__Process_for_Project_Evaluation_and_Selection_documented()





