from perscription_drugs import *

trial_patients = ["Denise", "Eddie", "Frank", "Georgia", "Kenny"]

#Remove Warfarin and add Edoxaban
for patient in trial_patients:
    prescription = patients[patient]

    prescription.remove(warfarin)
    prescription.add(edoxaban)
    print(patient, prescription)