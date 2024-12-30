# auxiliar functions for the app
# path: ./app/utils.py

# libraries
import pandas as pd

#- func 1 -#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#
"""Returns the option lists for the selectboxes."""
def get_options():

    options_dict = {#listas
        'marital_opt'      : ['married_civ_spouse', 'never_married',
                              'divorced', 'widowed','separated',
                              'married_spouse_absent','married_AF_spouse'],

        'relationship_opt' : ['husband', 'not_in_family', 'own_child','unmarried'
                              'wife', 'other_relative'],

        'education_opt'    : ['hs_grad', 'some_college', 'bachelors', 'masters',
                              'assoc_voc', 'assoc_acdm', 'prof_school', '11th',
                              'doctorate', '10th', '7th-8th', '9th', '12th',
                              '5th-6th', '1st-4th', 'preschool'],        

        'occupation_opt'   : ['exec_managerial', 'prof_specialty', 'craft_repair',
                              'sales', 'adm_clerical', 'other_service', 'machine_op_inspct',
                              'transport_moving', 'handlers_cleaners', 'tech_support',
                              'farming_fishing', 'protective_serv', 'priv_house_serv',
                              'armed_forces']
                    }
    
    return options_dict

#- func 2 -#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#
"""makes the prediction and returns the prediction and the probabilities"""
def translate_pred(pipeline, new_data, return_prob= False)-> str|tuple:
    pred = pipeline.predict(new_data)
    prob = pipeline.predict_proba(new_data)
    
    pred_class = 'yes' if int(pred[0]) == 1 else 'no'
    prob_no    = prob[0][0]
    prob_yes   = prob[0][1]
    
    return (pred_class, prob_no, prob_yes) if return_prob else pred_class
    












