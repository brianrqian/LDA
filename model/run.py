#!/usr/bin/env python
# coding: utf-8

# In[3]:


import sys
import os
import json
import pandas as pd

sys.path.insert(0, 'test')
sys.path.insert(0, 'model')
import LDA

# import env_setup
# from etl import get_data
# from features import apply_features

def main(targets):
    '''
    Runs the main project pipeline logic, given the targets.
    targets must contain: 'data', 'analysis', 'model'. 
    
    `main` runs the targets in order of data=>analysis=>model.
    '''

    # env_setup.make_datadir()
    # env_setup.auth()

    #if 'test' in targets:
    #with open('test-params.json') as fh:
    #    data_cfg = json.load(fh)
    #with open('hdsi-params.json') as fh:
    #    hdsi_cfg = json.load(fh)
    #LDA.LDA_model(**data_cfg, **hdsi_cfg)
    data = 'final_hdsi_faculty_updated.csv'
    hdsi = 'HDSI.csv'
    LDA.LDA_model(data, hdsi)

        # make the data target
    #    df_test = pd.DataFrame.from_dict(data_cfg, orient="index").transpose()

    #    print(df_test)

    # if 'features' in targets:
    #     with open('config/features-params.json') as fh:
    #         feats_cfg = json.load(fh)

    #     feats, labels = apply_features(data, **feats_cfg)

    # if 'model' in targets:
    #     with open('config/model-params.json') as fh:
    #         model_cfg = json.load(fh)

    #     # make the data target
    #     model_build(feats, labels, **model_cfg)

    #return df_test

if __name__ == '__main__':
    # run via:
    # python main.py data features model
    targets = sys.argv[1:]
    main(targets)


# In[ ]:




