# This python script take an input file and:
# turn it into nested dictionaries with key:value pairs
# use tuples or lists when you have multiple objects in one tag
# use Numpy arrays when you have more than one float/int.

import numpy as np


data_scale=["Title","Keywords","Number of Beta Electrons","Full Virial Ratio, -(V - W)/T"]
data_scale_string=["Title","Keywords"]
data_scale_int=["Number of Beta Electrons"]
data_scale_float=["Full Virial Ratio, -(V - W)/T"]


data_list=["Nuclear Names","Primitive Centers","Nuclear Charges"]
data_list_string=["Nuclear Names"]
data_list_int=["Primitive Centers"]
data_list_float=["Nuclear Charges"]

data_matrix=["Nuclear Cartesian Energy Gradients"]
data_dictionary=["Molecular Orbital Primitive Coefficients"]

class Data(object):
	def __init__(self,file_handle):
		self.dic = dict()
		self.f = file_handle
	def read_to_scale(self,lable,data_type):
        	if data_type == 'string':
                	self.dic[lable]=self.f.readline().strip('\ \n')
        	if data_type == 'int':
                	self.dic[lable]=int(self.f.readline().strip('\ \n'))
        	if data_type == 'float':
                	self.dic[lable]=float(self.f.readline().strip('\ \n'))
	def read_to_list(self,lable,data_type):
        	if data_type == 'string':
                	self.dic[lable]=[]
                	while(1):
                        	tmp=self.f.readline().strip('\/\ \<\n\>')
                        	if tmp != lable:
                                	tmp=tmp.split()
                                        self.dic[lable]=self.dic[lable]+tmp
                        	else:
                                	break
        	if data_type == 'int':
                	self.dic[lable]=[]
                	while(1):
                        	tmp=self.f.readline().strip('\/\ \<\n\>')
                        	if tmp != lable:
                                	tmp=tmp.split()
					tmp=map(int,tmp)
                                        self.dic[lable]=self.dic[lable]+tmp
                        	else:
                                	break
        	if data_type == 'float':
                	self.dic[lable]=[]
                	while(1):
                        	tmp=self.f.readline().strip('\/\ \<\n\>')
                        	if tmp != lable:
                                	tmp=tmp.split()
					tmp=map(float,tmp)
                                        self.dic[lable]=self.dic[lable]+tmp
                        	else:
                                	break


	def read_to_matrix(self,label,data_type):
        	if data_type == 'float':
	                matrix=[]
        	        while(1):
                	        tmp=self.f.readline().strip('\/\ \<\n\>')
                       		if tmp != label:
                                	tmp=tmp.split()[1:]
                                	tmp=map(float,tmp)
                                	matrix.append(tmp)
                        	else:
                                	break
                	self.dic[label]=np.array(matrix)

	def read_to_dictionary(self,label,data_type):
        	if data_type == 'float':
			sub_dic={}
                	matrix=[]
                	sub_label=self.f.readline().strip('\/\ \<\n\>')
                	sub_dic[sub_label]=self.f.readline().strip('\/\ \<\n\>')
                	self.f.readline()
                	while(1):
                        	tmp=self.f.readline().strip('\/\ \<\n\>')
                        	if tmp != label:
                                	tmp=tmp.split()
                                	tmp=map(float,tmp)
                                	matrix.append(tmp)
                        	else:
                                	break
                	sub_dic["Coeffs"]=np.array(matrix)
                	self.dic[label]=sub_dic




def read_data(input_file):
	with open(input_file,'r') as f:
		data=Data(f)
       		for line in iter(f.readline,''):
                	tmp=line.strip('\<\n\>')
			if tmp in data_scale:
				if tmp in data_scale_string:
					data.read_to_scale(tmp,'string')
				elif tmp in data_scale_int:
					data.read_to_scale(tmp,'int')
				elif tmp in data_scale_float:
					data.read_to_scale(tmp,'float')
			elif tmp in data_list:
				if tmp in data_list_string:
					data.read_to_list(tmp,'string')
				elif tmp in data_list_int:
					data.read_to_list(tmp,'int')
				elif tmp in data_list_float:
					data.read_to_list(tmp,'float')
			elif tmp in data_matrix:
				data.read_to_matrix(tmp,'float')
			elif tmp in data_dictionary:
				data.read_to_dictionary(tmp,'float')
	return data.dic



print read_data('input_file')
