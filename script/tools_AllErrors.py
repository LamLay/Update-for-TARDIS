# -*- coding: utf-8 -*-
"""
Created on Thu Dec 10 10:55:11 2020

@author: Lam Lay
"""

from tkinter import Tk
from tkinter import Label
from tkinter import Button
from tkinter import Radiobutton
from tkinter import IntVar
from tkinter import StringVar
from tkinter import Entry
from tkinter import messagebox
from tkinter import filedialog
from pathlib import Path
import os
import pydicom
import math
import pickle
import pandas as pd 
import numpy as np 
import random



# GUI buttons
window = Tk()
window.title("Tool for Approximating Radiotherapy Delivery via Informed Simulation (TARDIS)")
lbl1 = Label(window, text="Input DICOM-RT plan:")
lbl1.grid(columnspan=2, row=0)
lbl18 = Label(window, text="Select Model's Folder")
lbl18.grid(columnspan=2, row=1)
lbl19 = Label(window, text="Select Scaler's Folder")
lbl19.grid(columnspan=2, row=2)
lbl2 = Label(window, text="")
lbl2.grid(columnspan=5, row=3) 
lbl3 = Label(window, text="Select machine learning prediction model:")
lbl3.grid(columnspan=5, row=4) 
lbl4 = Label(window, text="IMRT - Predicted Delivery Error")
lbl4.grid(columnspan=5, row=5) 
lbl5 = Label(window, text="IMRT - Predicted Conversion Error")
lbl5.grid(columnspan=5, row=7) 
lbl6 = Label(window, text="IMRT - Predicted Combined Error")
lbl6.grid(columnspan=5, row=9) 
lbl7 = Label(window, text="")
lbl7.grid(columnspan=5, row=11)

lbl8 = Label(window, text="VMAT - Predicted Delivery Error")
lbl8.grid(columnspan=5, row=12) 
lbl9 = Label(window, text="VMAT - Predicted Conversion Error")
lbl9.grid(columnspan=5, row=14) 
lbl10 = Label(window, text="VMAT - Predicted Combined Error")
lbl10.grid(columnspan=5, row=16) 
lbl11 = Label(window, text="")
lbl11.grid(columnspan=5, row=18) 

lbl20 = Label(window, text="Output Folder")
lbl20.grid(column=3, row=0)
lbl21 = Label(window, text="Type 'Saved_Filename.dcm'")
lbl21.grid(column=3, row=1)


# Open Dicom Files
def clicked():
    global file
    file = filedialog.askopenfilename()
    plan_name = file.split('/')
    plan_index = len(plan_name)
    plan_name = plan_name[plan_index-1]
    lbl1.configure(text=plan_name)
    
btn = Button(window, text="Open", command=clicked)
btn.grid(column=2, row=0)

# Open Models Folder
def clickedModelDir():
    global ModelsDir
    currdir = os.getcwd()
    temp_path = filedialog.askdirectory(initialdir=currdir, title='Please select a directory')
    ModelsDir = Path(temp_path)
    
    dir_name = temp_path.split('/')
    dir_index = len(dir_name)
    dir_name = dir_name[dir_index-1]
    lbl18.configure(text=dir_name)

btn = Button(window, text="Open", command=clickedModelDir)
btn.grid(column=2, row=1)

# Open Scaler Folder
def clickedScaler():
    global scalers_folder
    currdir = os.getcwd()
    temp_path2 = filedialog.askdirectory(initialdir=currdir, title='Please select a directory')
    scalers_folder = Path(temp_path2)
    
    dir_name2 = temp_path2.split('/')
    dir_index2 = len(dir_name2)
    dir_name2 = dir_name2[dir_index2-1]
    lbl19.configure(text=dir_name2)

btn = Button(window, text="Open", command=clickedScaler)
btn.grid(column=2, row=2)

# Open Destination Folder
def clickedDestination():
    global destination
    currdir = os.getcwd()
    temp_path3 = filedialog.askdirectory(initialdir=currdir, title='Please select a directory')
    destination = Path(temp_path3)
    
    dir_name3 = temp_path3.split('/')
    dir_index3 = len(dir_name3)
    dir_name3 = dir_name3[dir_index3-1]
    lbl20.configure(text=dir_name3)

btn = Button(window, text="Open", command=clickedDestination)
btn.grid(column=4, row=0)

# Input Predicted DICOM's Filename
info = StringVar() 
saved_DICOM_name = Entry(width=20, textvariable=info)
saved_DICOM_name.place(x=350,y=50) 


# Choose Machine Learning Model    
def clicked1():
    global clf
    global filename
    filename = 'IMRT_LowRes_LinearReg_Delivery.sav'
    filepath = os.path.join(ModelsDir, filename)
    clf = pickle.load(open(filepath, 'rb'))
    
def clicked2():
    global clf
    global filename
    filename = 'IMRT_LowRes_DTree_Delivery.sav'
    filepath = os.path.join(ModelsDir, filename)
    clf = pickle.load(open(filepath, 'rb'))
    
def clicked3():
    global clf
    global filename
    filename = 'IMRT_LowRes_Boosting_Delivery.sav'
    filepath = os.path.join(ModelsDir, filename)
    clf = pickle.load(open(filepath, 'rb'))
    
def clicked4():
    global clf
    global filename
    filename = 'IMRT_LowRes_Bagging_Delivery.sav'
    filepath = os.path.join(ModelsDir, filename)
    try: 
        clf = pickle.load(open(filepath, 'rb'))
    except FileNotFoundError as e:
        messagebox.showerror(message='error: "{}"'.format(e)+'\n'
                             'Please convert the bagged tree model into an .sav file before using the tool.')
        raise KeyboardInterrupt

def clicked5():
    global clf
    global filename
    filename = 'IMRT_LowRes_NeuNet_Delivery.sav'
    filepath = os.path.join(ModelsDir, filename)
    clf = pickle.load(open(filepath, 'rb'))
    
def clicked6():
    global clf
    global filename
    filename = 'IMRT_LowRes_LinearReg_Conversion.sav'
    filepath = os.path.join(ModelsDir, filename)
    clf = pickle.load(open(filepath, 'rb'))
    
def clicked7():
    global clf
    global filename
    filename = 'IMRT_LowRes_DTree_Conversion.sav'
    filepath = os.path.join(ModelsDir, filename)
    clf = pickle.load(open(filepath, 'rb'))
    
def clicked8():
    global clf
    global filename
    filename = 'IMRT_LowRes_Boosting_Conversion.sav'
    filepath = os.path.join(ModelsDir, filename)
    clf = pickle.load(open(filepath, 'rb'))
    
def clicked9():
    global clf
    global filename
    filename = 'IMRT_LowRes_Bagging_Conversion.sav'
    filepath = os.path.join(ModelsDir, filename)
    try: 
        clf = pickle.load(open(filepath, 'rb'))
    except FileNotFoundError as e:
        messagebox.showerror(message='error: "{}"'.format(e)+'\n'
                             'Please convert the bagged tree model into an .sav file before using the tool.')
        raise KeyboardInterrupt
    
def clicked10():
    global clf
    global filename
    filename = 'IMRT_LowRes_NeuNet_Conversion.sav'
    filepath = os.path.join(ModelsDir, filename)
    clf = pickle.load(open(filepath, 'rb'))
    
def clicked11():
    global clf
    global filename
    filename = 'IMRT_LowRes_LinearReg_Combined.sav'
    filepath = os.path.join(ModelsDir, filename)
    clf = pickle.load(open(filepath, 'rb'))
    
def clicked12():
    global clf
    global filename
    filename = 'IMRT_LowRes_DTree_Combined.sav'
    filepath = os.path.join(ModelsDir, filename)
    clf = pickle.load(open(filepath, 'rb'))
    
def clicked13():
    global clf
    global filename
    filename = 'IMRT_LowRes_Boosting_Combined.sav'
    filepath = os.path.join(ModelsDir, filename)
    clf = pickle.load(open(filepath, 'rb'))
    
def clicked14():
    global clf
    global filename
    filename = 'IMRT_LowRes_Bagging_Combined.sav'
    filepath = os.path.join(ModelsDir, filename)
    try: 
        clf = pickle.load(open(filepath, 'rb'))
    except FileNotFoundError as e:
        messagebox.showerror(message='error: "{}"'.format(e)+'\n'
                             'Please convert the bagged tree model into an .sav file before using the tool.')
        raise KeyboardInterrupt
    
def clicked15():
    global clf
    global filename
    filename = 'IMRT_LowRes_NeuNet_Combined.sav'
    filepath = os.path.join(ModelsDir, filename)
    clf = pickle.load(open(filepath, 'rb'))
    
def clicked16():
    global clf
    global filename
    filename = 'VMAT_LowRes_LinearReg_Delivery.sav'
    filepath = os.path.join(ModelsDir, filename)
    clf = pickle.load(open(filepath, 'rb'))
    
def clicked17():
    global clf
    global filename
    filename = 'VMAT_LowRes_DTree_Delivery.sav'
    filepath = os.path.join(ModelsDir, filename)
    clf = pickle.load(open(filepath, 'rb'))
    
def clicked18():
    global clf
    global filename
    filename = 'VMAT_LowRes_Boosting_Delivery.sav'
    filepath = os.path.join(ModelsDir, filename)
    clf = pickle.load(open(filepath, 'rb'))
    
def clicked19():
    global clf
    global filename
    filename = 'VMAT_LowRes_Bagging_Delivery.sav'
    filepath = os.path.join(ModelsDir, filename)
    try: 
        clf = pickle.load(open(filepath, 'rb'))
    except FileNotFoundError as e:
        messagebox.showerror(message='error: "{}"'.format(e)+'\n'
                             'Please convert the bagged tree model into an .sav file before using the tool.')
        raise KeyboardInterrupt
    
def clicked20():
    global clf
    global filename
    filename = 'VMAT_LowRes_NeuNet_Delivery.sav'
    filepath = os.path.join(ModelsDir, filename)
    clf = pickle.load(open(filepath, 'rb'))
    
def clicked21():
    global clf
    global filename
    filename = 'VMAT_LowRes_LinearReg_Conversion.sav'
    filepath = os.path.join(ModelsDir, filename)
    clf = pickle.load(open(filepath, 'rb'))
    
def clicked22():
    global clf
    global filename
    filename = 'VMAT_LowRes_DTree_Conversion.sav'
    filepath = os.path.join(ModelsDir, filename)
    clf = pickle.load(open(filepath, 'rb'))
    
def clicked23():
    global clf
    global filename
    filename = 'VMAT_LowRes_Boosting_Conversion.sav'
    filepath = os.path.join(ModelsDir, filename)
    clf = pickle.load(open(filepath, 'rb'))
    
def clicked24():
    global clf
    global filename
    filename = 'VMAT_LowRes_Bagging_Conversion.sav'
    filepath = os.path.join(ModelsDir, filename)
    try: 
        clf = pickle.load(open(filepath, 'rb'))
    except FileNotFoundError as e:
        messagebox.showerror(message='error: "{}"'.format(e)+'\n'
                             'Please convert the bagged tree model into an .sav file before using the tool.')
        raise KeyboardInterrupt
    
def clicked25():
    global clf
    global filename
    filename = 'VMAT_LowRes_NeuNet_Conversion.sav'
    filepath = os.path.join(ModelsDir, filename)
    clf = pickle.load(open(filepath, 'rb'))
    
def clicked26():
    global clf
    global filename
    filename = 'VMAT_LowRes_LinearReg_Combined.sav'
    filepath = os.path.join(ModelsDir, filename)
    clf = pickle.load(open(filepath, 'rb'))
    
def clicked27():
    global clf
    global filename
    filename = 'VMAT_LowRes_DTree_Combined.sav'
    filepath = os.path.join(ModelsDir, filename)
    clf = pickle.load(open(filepath, 'rb'))
    
def clicked28():
    global clf
    global filename
    filename = 'VMAT_LowRes_Boosting_Combined.sav'
    filepath = os.path.join(ModelsDir, filename)
    clf = pickle.load(open(filepath, 'rb'))
    
def clicked29():
    global clf
    global filename
    filename = 'VMAT_LowRes_Bagging_Combined.sav'
    filepath = os.path.join(ModelsDir, filename)
    try: 
        clf = pickle.load(open(filepath, 'rb'))
    except FileNotFoundError as e:
        messagebox.showerror(message='error: "{}"'.format(e)+'\n'
                             'Please convert the bagged tree model into an .sav file before using the tool.')
        raise KeyboardInterrupt
    
def clicked30():
    global clf
    global filename
    filename = 'VMAT_LowRes_NeuNet_Combined.sav'
    filepath = os.path.join(ModelsDir, filename)
    clf = pickle.load(open(filepath, 'rb'))
    
v = IntVar()
rad1 = Radiobutton(window,text='Linear', variable = v, value=1, command=clicked1)
rad1.grid(column=0, row=6)
rad2 = Radiobutton(window,text='Decision Tree', variable = v, value=2, command=clicked2)
rad2.grid(column=1, row=6)
rad3 = Radiobutton(window,text='Boosted Tree', variable = v, value=3, command=clicked3)
rad3.grid(column=2, row=6) 
rad4 = Radiobutton(window,text='Bagged Tree', variable = v, value=4, command=clicked4)
rad4.grid(column=3, row=6)
rad5 = Radiobutton(window,text='Neural Network', variable = v, value=5, command=clicked5)
rad5.grid(column=4, row=6)  
rad6 = Radiobutton(window,text='Linear', variable = v, value=6, command=clicked6)
rad6.grid(column=0, row=8)
rad7 = Radiobutton(window,text='Decision Tree', variable = v, value=7, command=clicked7)
rad7.grid(column=1, row=8)
rad8 = Radiobutton(window,text='Boosted Tree', variable = v, value=8, command=clicked8)
rad8.grid(column=2, row=8) 
rad9 = Radiobutton(window,text='Bagged Tree', variable = v, value=9, command=clicked9)
rad9.grid(column=3, row=8)
rad10 = Radiobutton(window,text='Neural Network', variable = v, value=10, command=clicked10)
rad10.grid(column=4, row=8)
rad11 = Radiobutton(window,text='Linear', variable = v, value=11, command=clicked11)
rad11.grid(column=0, row=10)
rad12 = Radiobutton(window,text='Decision Tree', variable = v, value=12, command=clicked12)
rad12.grid(column=1, row=10)
rad13 = Radiobutton(window,text='Boosted Tree', variable = v, value=13, command=clicked13)
rad13.grid(column=2, row=10) 
rad14 = Radiobutton(window,text='Bagged Tree', variable = v, value=14, command=clicked14)
rad14.grid(column=3, row=10)
rad15 = Radiobutton(window,text='Neural Network', variable = v, value=15, command=clicked15)
rad15.grid(column=4, row=10) 
rad16 = Radiobutton(window,text='Linear', variable = v, value=16, command=clicked16)
rad16.grid(column=0, row=13)
rad17 = Radiobutton(window,text='Decision Tree', variable = v, value=17, command=clicked17)
rad17.grid(column=1, row=13)
rad18 = Radiobutton(window,text='Boosted Tree', variable = v, value=18, command=clicked18)
rad18.grid(column=2, row=13) 
rad19 = Radiobutton(window,text='Bagged Tree', variable = v, value=19, command=clicked19)
rad19.grid(column=3, row=13)
rad20 = Radiobutton(window,text='Neural Network', variable = v, value=20, command=clicked20)
rad20.grid(column=4, row=13) 
rad21 = Radiobutton(window,text='Linear', variable = v, value=21, command=clicked21)
rad21.grid(column=0, row=15)
rad22 = Radiobutton(window,text='Decision Tree', variable = v, value=22, command=clicked22)
rad22.grid(column=1, row=15)
rad23 = Radiobutton(window,text='Boosted Tree', variable = v, value=23, command=clicked23)
rad23.grid(column=2, row=15) 
rad24 = Radiobutton(window,text='Bagged Tree', variable = v, value=24, command=clicked24)
rad24.grid(column=3, row=15)
rad25 = Radiobutton(window,text='Neural Network', variable = v, value=25, command=clicked25)
rad25.grid(column=4, row=15) 
rad26 = Radiobutton(window,text='Linear', variable = v, value=26, command=clicked26)
rad26.grid(column=0, row=17)
rad27 = Radiobutton(window,text='Decision Tree', variable = v, value=27, command=clicked27)
rad27.grid(column=1, row=17)
rad28 = Radiobutton(window,text='Boosted Tree', variable = v, value=28, command=clicked28)
rad28.grid(column=2, row=17) 
rad29 = Radiobutton(window,text='Bagged Tree', variable = v, value=29, command=clicked29)
rad29.grid(column=3, row=17)
rad30 = Radiobutton(window,text='Neural Network', variable = v, value=30, command=clicked30)
rad30.grid(column=4, row=17) 
  

# Run Button
def clicked31(): 
    #Extract Mechanical Parameters from DICOM    
    global li, ds, num_beam, mlc_position, df
    li=[]
    ds = pydicom.dcmread(file) 
    num_beam=ds[0x300a,0x70][0][0x300a,0x80].value    
    
    model1 = "IMRT_LowRes_LinearReg_Delivery.sav" in filename
    model2 = "IMRT_LowRes_DTree_Delivery.sav" in filename
    model3 = "IMRT_LowRes_Boosting_Delivery.sav" in filename
    model4 = "IMRT_LowRes_Bagging_Delivery.sav" in filename
    model5 = "IMRT_LowRes_NeuNet_Delivery.sav" in filename
    model6 = "IMRT_LowRes_LinearReg_Conversion.sav" in filename
    model7 = "IMRT_LowRes_DTree_Conversion.sav" in filename
    model8 = "IMRT_LowRes_Boosting_Conversion.sav" in filename
    model9 = "IMRT_LowRes_Bagging_Conversion.sav" in filename
    model10 = "IMRT_LowRes_NeuNet_Conversion.sav" in filename
    model11 = "IMRT_LowRes_LinearReg_Combined.sav" in filename
    model12 = "IMRT_LowRes_DTree_Combined.sav" in filename
    model13 = "IMRT_LowRes_Boosting_Combined.sav" in filename
    model14 = "IMRT_LowRes_Bagging_Combined.sav" in filename
    model15 = "IMRT_LowRes_NeuNet_Combined.sav" in filename
    
   
    if model1 or model2 or model3 or model4 or model5 or model6 or model7 or model8 or model9 or model10 or model11 or model12 or model13 or model14 or model15 is True: # IMRT
        for field_number in range (num_beam): 
            type = ds[0x300a,0xb0][field_number][0x300a,0xce].value
            treatment = "TREATMENT" in type
            if treatment is False:
                dataset=[]  
                df = pd.DataFrame(dataset,columns =['CP_LN','CP','LN','MU','DICOM-MLC Position','MLC_velocity','MLC_acceleration','Dose Rate',
                                                    'Cumulative % of MU','Gravity Vector-MLC','Gravity Vector-Gantry','Bank'])
                
                li.append(df)
                
            else:
                # Number of Contorl Point
                cp=ds[0x300a,0xb0][field_number][0x300a,0x110].value
                # Prescription Monitor Unit
                mu=ds[0x300a,0x70][0][0x300c,0x04][field_number][0x300a,0x86].value
                # Dose Rate Set
                dr_field=ds[0x300a,0xb0][field_number][0x300a,0x111][0][0x300a,0x115].value # Unit = MU/min
                # MU/min => MU/sec
                dr_s = dr_field/60 
                # Gantry Angle
                ga=ds[0x300a,0xb0][field_number][0x300a,0x111][0][0x300a,0x11e].value  
                gantryangle=ga/180*math.pi
                # Collimator Angle
                ca=ds[0x300a,0xb0][field_number][0x300a,0x111][0][0x300a,0x120].value 
                collimatorangle=ca/180*math.pi
                # Cumulative Meterset Weight
                meterset_weight=[]
                for i in range(cp):
                    weight=ds[0x300a,0xb0][field_number][0x300a,0x111][i][0x300a,0x134].value
                    meterset_weight.append(weight) 
            
                # Monitor Unit at CP (This is equivalent to MU recorded in TF)
                meterset_mu=[]
                meterset_cumulative_mu=[]
                planned_MU = [['MU']]
                planned_MU_mu = []
                for j in range(0,cp):   
                    if j == 0:
                        weight_cumulative_mu = 0
                    else:
                        weight_diff=meterset_weight[j]-meterset_weight[j-1]
                        weight_mu=mu*weight_diff
                        weight_cumulative_mu=mu*meterset_weight[j]
                        meterset_mu.append(weight_mu)
                    meterset_cumulative_mu.append(weight_cumulative_mu)
                    
                    for m in range(120):
                        planned_MU_mu.append(weight_cumulative_mu)
                    planned_MU.append(planned_MU_mu)
                        
                # Time Interval at CP (This is literally t_default. They are the same)
                meterset_time=[]
                for k in range(cp-1):   
                    weight_time=meterset_mu[k]/dr_s
                    meterset_time.append(weight_time) 
                    
                # MLC Position at CP (from DICOM)
                mlc=[]
                weight_mlc=ds[0x300a,0xb0][field_number][0x300a,0x111][0][0x300a,0x11a][2][0x300a,0x11c].value
                mlc.append(weight_mlc)
                for j in range(1,cp):  # Positions of all leaves at each cp
                    check = ds[0x300a,0xb0][field_number][0x300a,0x111][j][0x300a,0x11a][0][0x300a,0x11c].value
                    if len(check) == 120:
                        weight_mlc = check
                    else:
                        check = ds[0x300a,0xb0][field_number][0x300a,0x111][j][0x300a,0x11a][2][0x300a,0x11c].value
                        weight_mlc = check
                    mlc.append(weight_mlc)
                    
                mlc_position=[["DICOM-MLC Position"]]
                for i in range(cp):
                    mlc_cp=(mlc[i][:])
                    mlc_position.append(mlc_cp)  
            
                # Cumulative % of CP or MU
                control_point=[["Cumulative % of MU"]] 
                percentage = []
                for i in range(cp):
                    control_point_cp=[]
                    controlpointcp=i/cp
                    percentage.append(controlpointcp)
                    for m in range(120):
                        control_point_cp.append(controlpointcp)
                    control_point.append(control_point_cp) 
                    
                # Calculate delivered MU & t_default to get dose rate later
                t_default = [['t_default']]
                MU_delivered = [['Delivered MU']]
                for j in range(len(meterset_cumulative_mu)):
                    t_default2 = []
                    MU_delivered2 = []
                    if j == 0:
                        for m in range(120):
                            MU_delivered2.append(0)
                            t_default2.append(0)
                    else:
                        # Calculate MU delivered between two consecutive CP
                        MU_delivered1 = meterset_cumulative_mu[j] - meterset_cumulative_mu[j-1]
                       
                        # Time to deliver this MU
                        t_default1 = MU_delivered1/dr_s  # Unit = second 
                        
                        for m in range(120):
                            MU_delivered2.append(MU_delivered1)
                            t_default2.append(t_default1)
                    MU_delivered.append(MU_delivered2)          # Eventually, I used MU_delivered to get dose rate
                    t_default.append(t_default2)
                
                # Distance traveled per CP
                diff_pos = [["Distance Traveled"],[0]*120]
                for j in range(1,cp):
                    diff_pos_cp = []
                    for m in range(120):
                        diff=abs(mlc_position[j+1][m]-mlc_position[j][m])  # Unit = mm
                        diff_pos_cp.append(diff)
                    diff_pos.append(diff_pos_cp)
            
                # Calculate t_leaf
                t_leaf = [["t_leaf"]]
                for j in range(1,cp+1):
                    t_leaf_cp = []
                    for m in range(120):
                        t_leaf_val = max(diff_pos[j])/25
                        t_leaf_cp.append(t_leaf_val)
                    t_leaf.append(t_leaf_cp)          # Unit = s
                    
                # Calculate t_calc
                t_calc = [["t_calc"]]                   # Unit = s
                for j in range(1,cp+1):
                    t_calc1 = []
                    for m in range(120):
                        t_calc2 = max(t_default[j][m],t_leaf[j][m])
                        t_calc1.append(t_calc2)
                    t_calc.append(t_calc1)
                    
                # Calculate MLC velocity for IMRT (all of them should be < 2.5 cm/s or 25 mm/s)
                mlc_velocity=[["MLC_velocity"]]                 # Unit = mm/s
                for j in range(1,cp+1):
                    mlc_velocity_cp=[]
                    for m in range(120):
                        if t_calc[j][m] == 0:  
                            v = 0
                        else:
                            v = diff_pos[j][m]/t_calc[j][m]    
                        mlc_velocity_cp.append(v)
                    mlc_velocity.append(mlc_velocity_cp)
                
                # Calculate MLC acceleration for IMRT          
                mlc_acceleration=[["MLC_acceleration"]]             # Unit = mm/s^2
                for j in range(1,cp):
                    mlc_acceleration_cp=[]
                    for m in range(120):
                        diff=(mlc_velocity[j+1][m]-mlc_velocity[j][m])
                        if t_calc[j][m] == 0:
                            a = 0
                        else:
                            a=diff/t_calc[j][m]
                        mlc_acceleration_cp.append(a)
                    mlc_acceleration.append(mlc_acceleration_cp)
                mlc_acceleration.append(mlc_acceleration_cp) # Last CP => use nearest neighbor
                
                # Calculate Dose Rate at each CP
                DR_calc = [["Dose Rate"]] 
                for j in range(1,cp+1):
                    DR_calc_cp=[]
                    for m in range(120):
                        if t_calc[j][m] == 0:  
                            DR = 0
                        else:
                            DR = MU_delivered[j][m]/t_calc[j][m]*60     # Unit = MU/min   
                        DR_calc_cp.append(DR)
                    DR_calc.append(DR_calc_cp)
                    
                # Gravity Vector for MLC & Gantry
                gravity_vector_MLC=[["Gravity Vector-MLC"]] 
                gravity_vector_gantry = [["Gravity Vector-Gantry"]] 
                for i in range(cp):
                    gravityvector_MLC2 = []
                    gravityvector_gantry2 = []
                    for m in range(120):
                        gravityvector_MLC1 = math.sin(gantryangle)*math.cos(collimatorangle)
                        gravityvector_gantry1 = math.sin(gantryangle)
                        gravityvector_MLC2.append(gravityvector_MLC1)
                        gravityvector_gantry2.append(gravityvector_gantry1)
                    gravity_vector_MLC.append(gravityvector_MLC2)
                    gravity_vector_gantry.append(gravityvector_gantry2)
            
                # Index
                index=[["CP_LN"]] 
                CP_col = [['CP']]
                Leaf_Num = [['LN']]
                CP_col2 = []
                Leaf_Num2 = []
                for i in range(cp):
                    index_cp=[]
                    for m in range(120):
                        CP_col2.append(i)
                        Leaf_Num2.append(m)
                        indexcp=str(i)+"_"+str(m)
                        index_cp.append(indexcp)
                    index.append(index_cp)
                    CP_col.append(CP_col2)
                    Leaf_Num.append(Leaf_Num2)
               
                # Bank
                bank = [['Bank']]
                for i in range(cp):
                    bank2 = []
                    for m in range(120):
                        if Leaf_Num2[m] < 60:
                            bank2.append('0') # Bank A
                        else: 
                            bank2.append('1') # Bank B
                    bank.append(bank2)
    
                dataset=[]
                index_1 = [x for xs in index for x in xs]
                CP_all = [x for xs in CP_col for x in xs]
                Leaf_Num_all = [x for xs in Leaf_Num for x in xs]
                planned_MU_all = [x for xs in planned_MU for x in xs]
                mlc_position_1 = [x for xs in mlc_position for x in xs]
                mlc_velocity_1 = [x for xs in mlc_velocity for x in xs]
                mlc_acceleration_1 = [x for xs in mlc_acceleration for x in xs]
                DR_calc_all = [x for xs in DR_calc for x in xs]                
                control_point_1 = [x for xs in control_point for x in xs]
                gravity_vector_MLC_all = [x for xs in gravity_vector_MLC for x in xs]
                gravity_vector_gantry_all = [x for xs in gravity_vector_gantry for x in xs]
                Bank_all = [x for xs in bank for x in xs]
                
                dataset.append(index_1)
                dataset.append(CP_all)
                dataset.append(Leaf_Num_all)
                dataset.append(planned_MU_all)
                dataset.append(mlc_position_1)
                dataset.append(mlc_velocity_1)
                dataset.append(mlc_acceleration_1)
                dataset.append(DR_calc_all)
                dataset.append(control_point_1)
                dataset.append(gravity_vector_MLC_all)
                dataset.append(gravity_vector_gantry_all)
                dataset.append(Bank_all)
                
                matrix_t =list(map(list, zip(*dataset)))
                del matrix_t[0]
                df = pd.DataFrame(matrix_t,columns =['CP_LN','CP','LN','MU','DICOM-MLC Position','MLC_velocity','MLC_acceleration','Dose Rate',
                                                    'Cumulative % of MU','Gravity Vector-MLC','Gravity Vector-Gantry','Bank'])
                li.append(df)
                
    else:
        for field_number in range (num_beam): # VMAT
            type = ds[0x300a,0xb0][field_number][0x300a,0xce].value
            treatment = "TREATMENT" in type
            if treatment is False:
                dataset=[]  
                df = pd.DataFrame(dataset,columns =['CP_LN','CP','LN','MU','DICOM-MLC Position','MLC_velocity','MLC_acceleration',
                                                    'Dose Rate','Cumulative % of MU','Gravity Vector-MLC','Gravity Vector-Gantry',
                                                    'Gantry_velocity','Gantry_acceleration','Bank'])
                li.append(df)
            else:
                # Number of Contorl Point
                cp=ds[0x300a,0xb0][field_number][0x300a,0x110].value                
                # Prescription Monitor Unit
                mu=ds[0x300a,0x70][0][0x300c,0x04][field_number][0x300a,0x86].value
                # Dose Rate Set
                dr_field=ds[0x300a,0xb0][field_number][0x300a,0x111][0][0x300a,0x115].value # Unit = MU/min
                # MU/min => MU/sec
                dr_s=dr_field/60                 
                # Gantry Angle
                gantry_angle_actualdegree=[]
                gantry_angle_degree=[]
                gantry_angle_rad=[]
                for i in range(cp): 
                    try:
                        ga=ds[0x300a,0xb0][field_number][0x300a,0x111][i][0x300a,0x11e].value  
                        gantryangle=ga/180*math.pi
                        gantry_angle_actualdegree.append(ga)
                    except KeyError as e:
                        messagebox.showerror(message='error: "{}"'.format(e)+'\n'+
                                             'You may be trying to predict VMAT errors in a non-VMAT file.')
                        raise KeyboardInterrupt
                    if ga<180:
                        ga=180-ga
                    elif ga>180:
                        ga=540-ga        
                    gantry_angle_degree.append(ga)
                    gantry_angle_rad.append(gantryangle)
                
                # Collimator Angle
                ca=ds[0x300a,0xb0][field_number][0x300a,0x111][0][0x300a,0x120].value 
                collimatorangle=ca/180*math.pi  
                # Cumulative Meterset Weight
                meterset_weight=[]
                for i in range(cp):
                    weight=ds[0x300a,0xb0][field_number][0x300a,0x111][i][0x300a,0x134].value
                    meterset_weight.append(weight)
                # Monitor Unit at CP
                meterset_mu=[]
                meterset_cumulative_mu=[]
                planned_MU = [['MU']]
                planned_MU_mu = []
                for j in range(0,cp):   
                    if j == 0:
                        weight_cumulative_mu = 0
                    else:
                        weight_diff=meterset_weight[j]-meterset_weight[j-1]
                        weight_mu=mu*weight_diff
                        weight_cumulative_mu=mu*meterset_weight[j]
                        meterset_mu.append(weight_mu)
                    meterset_cumulative_mu.append(weight_cumulative_mu)
                    
                    for m in range(120):
                        planned_MU_mu.append(weight_cumulative_mu)
                    planned_MU.append(planned_MU_mu)
                
                # Time Interval at CP (This is max(t_default, t_gantry))
                gantry_speed=6
                meterset_time=[]
                for k in range(cp-1): 
                    max_mu_cp=abs(gantry_angle_degree[k+1]-gantry_angle_degree[k])*dr_s/gantry_speed
                    if meterset_mu[k]<max_mu_cp:
                        weight_time=abs(gantry_angle_degree[k+1]-gantry_angle_degree[k])/gantry_speed
                    elif meterset_mu[k]>max_mu_cp:
                        weight_time=meterset_mu[k]/dr_s
                    meterset_time.append(weight_time)
            
                # MLC Position at CP
                mlc=[]
                weight_mlc=ds[0x300a,0xb0][field_number][0x300a,0x111][0][0x300a,0x11a][2][0x300a,0x11c].value
                mlc.append(weight_mlc)
                for j in range(1,cp):   # Positions of all leaves at each cp
                    check = ds[0x300a,0xb0][field_number][0x300a,0x111][j][0x300a,0x11a][0][0x300a,0x11c].value
                    if len(check) == 120:
                        weight_mlc = check
                    else:
                        check = ds[0x300a,0xb0][field_number][0x300a,0x111][j][0x300a,0x11a][2][0x300a,0x11c].value
                        weight_mlc = check
                    mlc.append(weight_mlc)
                
                mlc_position=[["DICOM-MLC Position"]]
                for i in range(cp):
                    mlc_cp=(mlc[i][:])
                    mlc_position.append(mlc_cp)
                
                # Distanced Traveld per CP
                diff_pos = [["Distance Traveled"],[0]*120]
                abs_diff_pos = [["Absolute Distance Traveled"],[0]*120]
                for j in range(1,cp):
                    diff_pos_cp = []
                    abs_diff_pos_cp = []
                    for m in range(120):
                        diff=(mlc_position[j+1][m]-mlc_position[j][m])
                        abs_diff = abs(mlc_position[j+1][m]-mlc_position[j][m])   # Need this to find t_leaf
                        diff_pos_cp.append(diff)
                        abs_diff_pos_cp.append(abs_diff)
                    diff_pos.append(diff_pos_cp)
                    abs_diff_pos.append(abs_diff_pos_cp)
            
                # Cumulative % of CP or MU
                control_point=[["Cumulative % of MU"]] 
                percentage = []
                for i in range(cp):
                    control_point_cp=[]
                    controlpointcp=i/cp
                    percentage.append(controlpointcp)
                    for m in range(120):
                        control_point_cp.append(controlpointcp)
                    control_point.append(control_point_cp) 
                
                # Calculate delivered MU & t_default to get dose rate later
                t_default = [['t_default']]
                MU_delivered = [['Delivered MU']]
                for j in range(len(meterset_cumulative_mu)):
                    t_default2 = []
                    MU_delivered2 = []
                    if j == 0:
                        for m in range(120):
                            MU_delivered2.append(0)
                            t_default2.append(0)
                    else:
                        # Calculate MU delivered between two consecutive CP
                        MU_delivered1 = meterset_cumulative_mu[j] - meterset_cumulative_mu[j-1]
                        
                        # Time to deliver this MU
                        t_default1 = MU_delivered1/dr_s  # Unit = second 
                        
                        for m in range(120):
                            MU_delivered2.append(MU_delivered1)
                            t_default2.append(t_default1)
                    MU_delivered.append(MU_delivered2)              # Eventually, I used MU_delivered to get dose rate
                    t_default.append(t_default2)
            
                # Calculate t_gantry
                max_gantry_speed = 6  # 6 degree/second <= 1 RPM = 360 deg / 60 sec
                t_gantry = [["t_gantry"],[0]*120] 
                for k in range(cp-1):
                    t_gantry_cp = []
                    for m in range(120):
                        diff=abs(gantry_angle_degree[k+1]-gantry_angle_degree[k])
                        t = diff/max_gantry_speed
                        t_gantry_cp.append(t)
                    t_gantry.append(t_gantry_cp)
                
                # Calculate t_leaf
                t_leaf = [["t_leaf"]]
                for j in range(1,cp+1):
                    t_leaf_cp = []
                    for m in range(120):
                        t_leaf_val = max(abs_diff_pos[j])/25
                        t_leaf_cp.append(t_leaf_val)
                    t_leaf.append(t_leaf_cp)          # Unit = s
                    
                # Calculate t_calc
                t_calc = [["t_calc"]]                   # Unit = s
                for j in range(1,cp+1):
                    t_calc1 = []
                    for m in range(120):
                        t_calc2 = max(t_default[j][m],t_leaf[j][m],t_gantry[j][m])
                        t_calc1.append(t_calc2)
                    t_calc.append(t_calc1)
                    
                # Calculate MLC velocity for VMAT (all of them should be < 2.5 cm/s or 25 mm/s)
                mlc_velocity=[["MLC_Velocity"]]                 # Unit = mm/s
                for j in range(1,cp+1):
                    mlc_velocity_cp=[]
                    for m in range(120):
                        if t_calc[j][m] == 0:  
                            v = 0
                        else:
                            v = diff_pos[j][m]/t_calc[j][m]    
                        mlc_velocity_cp.append(v)
                    mlc_velocity.append(mlc_velocity_cp)
                    
                # Calculate new MLC acceleration            
                mlc_acceleration=[["MLC_acceleration"]]             # Unit = mm/s^2
                for j in range(1,cp):
                    mlc_acceleration_cp=[]
                    for m in range(120):
                        diff = mlc_velocity[j+1][m]-mlc_velocity[j][m]
                        if t_calc[j][m] == 0 :
                            a = 0
                        else:
                            a=diff/t_calc[j][m]
                        mlc_acceleration_cp.append(a)
                    mlc_acceleration.append(mlc_acceleration_cp)
                mlc_acceleration.append(mlc_acceleration_cp) # Last CP => use nearest neighbor
                
                # Calculate Dose Rate at each CP
                DR_calc = [["Dose Rate"]] 
                for j in range(1,cp+1):
                    DR_calc_cp=[]
                    for m in range(120):
                        if t_calc[j][m] == 0:  
                            DR = 0
                        else:
                            DR = MU_delivered[j][m]/t_calc[j][m]*60     # Unit = MU/min   
                        DR_calc_cp.append(DR)
                    DR_calc.append(DR_calc_cp)
                    
                # Gravity Vector for MLC and Gantry
                gravity_vector_MLC=[["Gravity Vector-MLC"]] 
                gravity_vector_gantry = [["Gravity Vector-Gantry"]] 
                for i in range(cp):
                    gravityvector_MLC2 = []
                    gravityvector_gantry2 = []
                    for m in range(120):
                        gravityvector_MLC1 = math.sin(gantryangle)*math.cos(collimatorangle)
                        gravityvector_gantry1 = math.sin(gantryangle)
                        gravityvector_MLC2.append(gravityvector_MLC1)
                        gravityvector_gantry2.append(gravityvector_gantry1)
                    gravity_vector_MLC.append(gravityvector_MLC2)
                    gravity_vector_gantry.append(gravityvector_gantry2) 
                    
                # Difference in gantry angle
                diff_angle = [["Diff_Gantry_Angle"],[0]*120]
                for j in range(1,cp):
                    diff_angle_cp = []
                    for m in range(120):
                        diff=(gantry_angle_degree[j]-gantry_angle_degree[j-1])
                        diff_angle_cp.append(diff)
                    diff_angle.append(diff_angle_cp)
                    
                # Gantry Velocity at CP - Only VMAT (Maximum gantry speed is 6 degree/s)
                gantry_velocity=[["Gantry_Velocity"]] 
                for j in range(1,cp+1): 
                    gantry_velocity_cp=[]
                    for m in range(120):
                        if t_calc[j][m] == 0:  
                            v = 0
                        else:
                            v = diff_angle[j][m]/t_calc[j][m]   
                        gantry_velocity_cp.append(v)
                    gantry_velocity.append(gantry_velocity_cp) 
                
                # Gantry Acceleration at CP - Only VMAT
                gantry_acceleration=[["Gantry_acceleration"]] 
                for j in range(1,cp):
                    gantry_acceleration_cp=[]
                    for m in range(120):
                        diff_v = gantry_velocity[j+1][m]-gantry_velocity[j][m]
                        if t_calc[j][m] == 0 :
                            a = 0 
                        else:
                            a = diff_v/t_calc[j][m]  
                        gantry_acceleration_cp.append(a)
                    gantry_acceleration.append(gantry_acceleration_cp)
                gantry_acceleration.append(gantry_acceleration_cp) # Last value => use nearest neighbor
            
                # Index
                index=[["CP_LN"]] 
                CP_col = [['CP']]
                Leaf_Num = [['LN']]
                CP_col2 = []
                Leaf_Num2 = []
                for i in range(cp):
                    index_cp=[]
                    for m in range(120):
                        CP_col2.append(i)
                        Leaf_Num2.append(m)
                        indexcp=str(i)+"_"+str(m)
                        index_cp.append(indexcp)
                    index.append(index_cp)
                    CP_col.append(CP_col2)
                    Leaf_Num.append(Leaf_Num2) 
                
                # Bank
                bank = [['Bank']]
                for i in range(cp):
                    bank2 = []
                    for m in range(120):
                        if Leaf_Num2[m] < 60:
                            bank2.append('0') # Bank A
                        else: 
                            bank2.append('1') # Bank B
                    bank.append(bank2)
                
                dataset=[]
                index_1 = [x for xs in index for x in xs]
                CP_all = [x for xs in CP_col for x in xs]
                Leaf_Num_all = [x for xs in Leaf_Num for x in xs]
                planned_MU_all = [x for xs in planned_MU for x in xs]
                mlc_position_1 = [x for xs in mlc_position for x in xs]
                mlc_velocity_1 = [x for xs in mlc_velocity for x in xs]
                mlc_acceleration_1 = [x for xs in mlc_acceleration for x in xs]
                DR_calc_all = [x for xs in DR_calc for x in xs]
                control_point_1 = [x for xs in control_point for x in xs]
                gravity_vector_MLC_all = [x for xs in gravity_vector_MLC for x in xs]
                gravity_vector_gantry_all = [x for xs in gravity_vector_gantry for x in xs]
                gantry_velocity_1 = [x for xs in gantry_velocity for x in xs]
                gantry_acceleration_1 = [x for xs in gantry_acceleration for x in xs]
                Bank_all = [x for xs in bank for x in xs]
                #diff_pos_all = [x for xs in diff_pos for x in xs]
                #diff_angle_all = [x for xs in diff_angle for x in xs]
                
                dataset.append(index_1)
                dataset.append(CP_all)
                dataset.append(Leaf_Num_all)
                dataset.append(planned_MU_all)
                dataset.append(mlc_position_1)
                dataset.append(mlc_velocity_1)
                dataset.append(mlc_acceleration_1)
                dataset.append(DR_calc_all)
                dataset.append(control_point_1)
                dataset.append(gravity_vector_MLC_all)
                dataset.append(gravity_vector_gantry_all)
                dataset.append(gantry_velocity_1)
                dataset.append(gantry_acceleration_1)
                dataset.append(Bank_all)
                
                matrix_t =list(map(list, zip(*dataset)))
                del matrix_t[0]
                df = pd.DataFrame(matrix_t,columns =['CP_LN','CP','LN','MU','DICOM-MLC Position','MLC_velocity','MLC_acceleration',
                                                    'Dose Rate','Cumulative % of MU','Gravity Vector-MLC','Gravity Vector-Gantry',
                                                    'Gantry_velocity','Gantry_acceleration','Bank'])
               
                li.append(df)
                
                
    # Change SOP Instance UID for reimport
    UID = ds[0x08,0x18].value
    UID_parts = UID.split('.')
    b = random.random()
    c = str(int(round(b,14)*100000000000000))
    UID_parts[-1] = c 
    d = ".".join(UID_parts)
    ds[0x08,0x18].value = d
    
    # RMS & Max Error
    rms_list=[]
    max_list=[]
    
    # Modify MLC positions   
    for field_number in range (num_beam): 
        type = ds[0x300a,0xb0][field_number][0x300a,0xce].value
        treatment = "TREATMENT" in type
        if treatment is False:
            pass
        else: 
            model1 = "IMRT_LowRes_LinearReg_Delivery.sav" in filename
            model2 = "IMRT_LowRes_DTree_Delivery.sav" in filename
            model3 = "IMRT_LowRes_Boosting_Delivery.sav" in filename
            model4 = "IMRT_LowRes_Bagging_Delivery.sav" in filename
            model5 = "IMRT_LowRes_NeuNet_Delivery.sav" in filename
            model6 = "IMRT_LowRes_LinearReg_Conversion.sav" in filename
            model7 = "IMRT_LowRes_DTree_Conversion.sav" in filename
            model8 = "IMRT_LowRes_Boosting_Conversion.sav" in filename
            model9 = "IMRT_LowRes_Bagging_Conversion.sav" in filename
            model10 = "IMRT_LowRes_NeuNet_Conversion.sav" in filename
            model11 = "IMRT_LowRes_LinearReg_Combined.sav" in filename
            model12 = "IMRT_LowRes_DTree_Combined.sav" in filename
            model13 = "IMRT_LowRes_Boosting_Combined.sav" in filename
            model14 = "IMRT_LowRes_Bagging_Combined.sav" in filename
            model15 = "IMRT_LowRes_NeuNet_Combined.sav" in filename
                    
            model16 = "VMAT_LowRes_LinearReg_Delivery.sav" in filename
            model17 = "VMAT_LowRes_DTree_Delivery.sav" in filename
            model18 = "VMAT_LowRes_Boosting_Delivery.sav" in filename
            model19 = "VMAT_LowRes_Bagging_Delivery.sav" in filename
            model20 = "VMAT_LowRes_NeuNet_Delivery.sav" in filename
            model21 = "VMAT_LowRes_LinearReg_Conversion.sav" in filename
            model22 = "VMAT_LowRes_DTree_Conversion.sav" in filename
            model23 = "VMAT_LowRes_Boosting_Conversion.sav" in filename
            model24 = "VMAT_LowRes_Bagging_Conversion.sav" in filename
            model25 = "VMAT_LowRes_NeuNet_Conversion.sav" in filename
            #model26 = "VMAT_LowRes_LinearReg_Combined.sav" in filename
            #model27 = "VMAT_LowRes_DTree_Combined.sav" in filename
            #model28 = "VMAT_LowRes_Boosting_Combined.sav" in filename
            #model29 = "VMAT_LowRes_Bagging_Combined.sav" in filename
            #model30 = "VMAT_LowRes_NeuNet_Combined.sav" in filename
            
            global y1, X
            # For IMRT Models
            if model1 or model2 or model3 or model4 or model5 or model6 or model7 or model8 or model9 or model10 or model11 or model12 or model13 or model14 or model15 is True:
                X = li[field_number][['CP','MU','MLC_velocity','MLC_acceleration','Cumulative % of MU',
                         'Gravity Vector-MLC','Gravity Vector-Gantry','Dose Rate','Bank']].values.reshape(-1,9)
                scaler_name = 'IMRT_scaler.pkl'
                scalerpath = os.path.join(scalers_folder, scaler_name)
                scaler = pickle.load(open(scalerpath, 'rb'))                
            else: # For VMAT Models
                X = li[field_number][['CP','MU','MLC_velocity','MLC_acceleration','Bank','Dose Rate','Cumulative % of MU',
                                     'Gravity Vector-MLC','Gravity Vector-Gantry','Gantry_velocity',
                                     'Gantry_acceleration']].values.reshape(-1,11)
                scaler_name = 'VMAT_scaler.pkl'
                scalerpath = os.path.join(scalers_folder, scaler_name)
                scaler = pickle.load(open(scalerpath, 'rb'))
            
            try: 
                X = scaler.transform(X)
            except ValueError:
                print('Cannot convert data to scalar')
                pass
            y1 = clf.predict(X)  # Predict MLC errors              
            
            # Save New MLC Positions to CSV
            mlc_position = pd.to_numeric((li[field_number]['DICOM-MLC Position']), errors='coerce')
            mlc_new_position = mlc_position + y1
            
            if model1 or model2 or model3 or model4 or model5 or model16 or model17 or model18 or model19 or model20 is True: 
                li[field_number]['Predicted_MLC_Delivery_Error'] = y1
            elif model6 or model7 or model8 or model9 or model10 or model21 or model22 or model23 or model24 or model25 is True:
                li[field_number]['Predicted_MLC_Conversion_Error'] = y1
            else:
                li[field_number]['Predicted_MLC_Combined_Error'] = y1
            
            li[field_number]['Predicted_MLC_position'] = mlc_new_position 
            col = li[field_number]['Predicted_MLC_position']
            
            global cp_number, li2, li2_split
            cp_number = int(len(col)/120)
            
            #Change the order of rows
            li2 = li[field_number].round({'Predicted_MLC_position':3})
            
            new_order = []
            for idx_leaf in range (120):
                row = idx_leaf
                new_order.append(row)
        
                for idx_cp in range(cp_number):
                    row = row + 120
                    if row < len(mlc_new_position):
                        new_order.append(row)
            li2 = li2.reindex(new_order)
            li2 = li2.reset_index(drop=True)
            
            
            li2_split = np.split(li2,2)
            li2_split[1] = li2_split[1].reset_index(drop=True)
            
            global leaf_gaps, new_leaf_gaps
            leaf_gaps = []
            for j in range(int(len(li2_split[1]))):
                leaf_gap = li2_split[1]['Predicted_MLC_position'][j] - li2_split[0]['Predicted_MLC_position'][j]
                leaf_gaps.append(leaf_gap)
                if leaf_gap < 0:
                    new_position = (li2_split[1]['Predicted_MLC_position'][j]+li2_split[0]['Predicted_MLC_position'][j])/2
                    new_position = round(new_position,3)
                    li2_split[0].at[j,'Predicted_MLC_position'] = new_position
                    li2_split[1].at[j,'Predicted_MLC_position'] = new_position
                    
            new_leaf_gaps = li2_split[1]['Predicted_MLC_position'] - li2_split[0]['Predicted_MLC_position']
            li3 = pd.concat([li2_split[0], li2_split[1]])
            li3 = li3.reset_index(drop=True)
            
            #Change the order of rows back to original
            new_order = []
            for idx_cp in range(cp_number):
                row = idx_cp
                new_order.append(row)
                
                for idx_leaf in range (120):
                    row = row + cp_number
                    if row < len(mlc_new_position):
                        new_order.append(row)
            li3 = li3.reindex(new_order)
            li3 = li3.reset_index(drop=True)
            
            name = saved_DICOM_name.get().split('.')
            name = '.'.join(name[:-1])
            csv_name =  name + "_RTDICOM_Field_"+str(field_number)+".csv"
            final_path = os.path.join(destination, csv_name)
            li3.to_csv(final_path)
            
            # Take predicted MLC position to DICOM
            global col_edited, actual_mlc1, actual_mlc2
            actual_mlc=[]
            col_edited = li3['Predicted_MLC_position']
            actual_mlc.append(col_edited)
            actual_mlc1=[]
            for j in range(cp_number):
                actual_mlc2=[]
                for k in range(120):  
                    a=(actual_mlc[0][120*j+k])
                    actual_mlc2.append(a)
                actual_mlc1.append(actual_mlc2) 
            
            # modify control point 0 dicom file
            print(str(field_number)+'con0',ds[0x300a,0xb0][field_number][0x300a,0x111][0][0x300a,0x11a][2][0x300a,0x11c].value)
            ds[0x300a,0xb0][field_number][0x300a,0x111][0][0x300a,0x11a][2][0x300a,0x11c].value = actual_mlc1[0]
            print(str(field_number)+'con0',ds[0x300a,0xb0][field_number][0x300a,0x111][0][0x300a,0x11a][2][0x300a,0x11c].value)
            
            
            # modify control point 1~ second last dicom file
            for m in range(1,cp_number):
                print(str(field_number)+'con',m,ds[0x300a,0xb0][field_number][0x300a,0x111][m][0x300a,0x11a][0][0x300a,0x11c].value)
                
                ds[0x300a,0xb0][field_number][0x300a,0x111][m][0x300a,0x11a][0][0x300a,0x11c].value = actual_mlc1[m]
                print(str(field_number)+'con',m,ds[0x300a,0xb0][field_number][0x300a,0x111][m][0x300a,0x11a][0][0x300a,0x11c].value)


    #  RMS & Max Error
    rms = np.sqrt(np.mean(y1**2))
    max_error = float(max(y1))
    rms_list.append(rms)
    max_list.append(max_error)            
    def square(list):
        return [i ** 2 for i in list]
    rms_all = str(round(np.sqrt(np.mean(square(rms_list))),4))
    max_all = str(round(max(max_list),4))
    
    # Show RMS and Max Error    
    lbl12.configure(text="RMS of Predicted MLC Error: "+rms_all+ " mm")
    lbl13.configure(text="Max of Predicted MLC Error: "+max_all+ " mm")
    
    # Save new revised DICOM
    print(saved_DICOM_name.get())
    final_path = os.path.join(destination, saved_DICOM_name.get())
    ds.save_as(final_path, write_like_original=False)
    print('___________________________________________________')
    print('A new DICOM has been saved in your selected folder.')
    messagebox.showinfo(message='A new DICOM has been saved in your selected folder.')


# GUI buttons
btn = Button(window, text="Run", command=clicked31)
btn.grid(columnspan=5, row=19)
lbl22 = Label(window, text="")
lbl22.grid(columnspan=5, row=20)
lbl12 = Label(window, text="RMS of Predicted MLC Error:")
lbl12.grid(column=0, columnspan=2, row=21)
lbl13 = Label(window, text="Max of Predicted MLC Error:")
lbl13.grid(column=2, columnspan=2, row=21)
lbl14 = Label(window, text="")
lbl14.grid(columnspan=5, row=22)
lbl15 = Label(window, text="For research or academic purposes. Not intended for clinical use.")
lbl15.grid(columnspan=5, row=23)
lbl16 = Label(window, text="For researchers, any publication using this tool please cite the accompanying paper")
lbl16.grid(columnspan=5, row=24)
lbl17 = Label(window, text="'Lay, Chuang, Adamson, Giles, A Tool for Approximating Radiotherapy Delivery via Informed Simulation (TARDIS), 2020'")
lbl17.grid(columnspan=5, row=25)


window.mainloop()
                
