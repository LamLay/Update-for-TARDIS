# Update-for-TARDIS
## Artificial Intelligence Powered Prediction for Online Adaptive Patient Specific QA ## 

### A Tool for Approximating Radiotherapy Delivery via Informed Simulation (TARDIS) ###
This is the update of Chuang's project: https://github.com/k1a2i3oscar/TARDIS#a-tool-for-approximating-radiotherapy-delivery-via-informed-simulation-tardis

Note: Currently the machine learning models that use Bootstrap Aggregation (Bagging) are too big to be uploaded on GitHub. I will upload them later.

Tutorial:

* Download tool.py and the models. Make sure that the models and the tool.py are in the same folder. 
* Open the tool.py with Python platform and run the script. 
* At GUI, open desired DICOM-RT plan by clicking "Open" button.uplo 
* Decide what type of MLC errors you want to predict. The tool can predict 3 types of MLC errors:
  * Delivery error at the machine
  * Conversion error from DICOM-RT to deliverable trajectory
  * Combined error - sum of delivery error and conversion error 
* Choose one machine learning model based on treatment technique. Random error check box and percent of confidence interval provide an option to add a random component into the prediction. 
* Random error components account for the unpredictable components in the machine learning model. 
* A new DICOM-RT with predicted MLC positions, and command separate values (CSV) files including mechanical parameters and predicted MLC errors and positions for individual field (arc) are then generated by clicking the “Run” button. 
* Re-import the new DICOM-RT into treatment planning system to evaluate the change in dose. 

For research or academic purposes. Not intended for clinical use. 
For researchers, any publication using this tool please cite the accompanying paper 
“Lay, Chuang, Adamson, Giles, A Tool for Patient Specific Prediction of Delivery Discrepancies in Machine Parameters Using Trajectory Log Files, 2020"
