
# http://fcc-physics-events.web.cern.ch/fcc-physics-events/FCCee/winter2023/Delphesevents_IDEA.php

def get_datasets(baseDir = ""):

    datasets = []
    subDir = "/winter2023/IDEA/"
    baseDir = f"{baseDir}/{subDir}"

    ## muon signal samples
    datasets.append({"name": "wzp6_ee_mumuH_ecm240",                    "datadir": f"{baseDir}/wzp6_ee_mumuH_ecm240",                           "xsec": 0.0067643})
    datasets.append({"name": "wzp6_ee_mumuH_mH-lower-50MeV_ecm240",     "datadir": f"{baseDir}/wzp6_ee_mumuH_mH-lower-50MeV_ecm240",            "xsec": 0.0067738})
    datasets.append({"name": "wzp6_ee_mumuH_mH-lower-100MeV_ecm240",    "datadir": f"{baseDir}/wzp6_ee_mumuH_mH-lower-100MeV_ecm240",           "xsec": 0.0067849})
    datasets.append({"name": "wzp6_ee_mumuH_mH-higher-100MeV_ecm240",   "datadir": f"{baseDir}/wzp6_ee_mumuH_mH-higher-100MeV_ecm240",          "xsec": 0.0067393})
    datasets.append({"name": "wzp6_ee_mumuH_mH-higher-50MeV_ecm240",    "datadir": f"{baseDir}/wzp6_ee_mumuH_mH-higher-50MeV_ecm240",           "xsec": 0.0067488})
    datasets.append({"name": "wzp6_ee_mumuH_BES-higher-1pc_ecm240",     "datadir": f"{baseDir}/wzp6_ee_mumuH_BES-higher-1pc_ecm240",            "xsec": 0.0067614})
    datasets.append({"name": "wzp6_ee_mumuH_BES-lower-1pc_ecm240",      "datadir": f"{baseDir}/wzp6_ee_mumuH_BES-lower-1pc_ecm240",             "xsec": 0.00676093})
    
    # electron signal samples
    datasets.append({"name": "wzp6_ee_eeH_ecm240",                      "datadir": f"{baseDir}/wzp6_ee_eeH_ecm240",                             "xsec": 0.0071611})
    datasets.append({"name": "wzp6_ee_eeH_mH-higher-100MeV_ecm240",     "datadir": f"{baseDir}/wzp6_ee_eeH_mH-higher-100MeV_ecm240",            "xsec": 0.007137})
    datasets.append({"name": "wzp6_ee_eeH_mH-higher-50MeV_ecm240",      "datadir": f"{baseDir}/wzp6_ee_eeH_mH-higher-50MeV_ecm240",             "xsec": 0.007152})
    datasets.append({"name": "wzp6_ee_eeH_mH-lower-100MeV_ecm240",      "datadir": f"{baseDir}/wzp6_ee_eeH_mH-lower-100MeV_ecm240",             "xsec": 0.007188})
    datasets.append({"name": "wzp6_ee_eeH_mH-lower-50MeV_ecm240",       "datadir": f"{baseDir}/wzp6_ee_eeH_mH-lower-50MeV_ecm240",              "xsec": 0.007169})
    datasets.append({"name": "wzp6_ee_eeH_BES-higher-1pc_ecm240",       "datadir": f"{baseDir}/wzp6_ee_eeH_BES-higher-1pc_ecm240",              "xsec": 0.007159})
    datasets.append({"name": "wzp6_ee_eeH_BES-lower-1pc_ecm240",        "datadir": f"{baseDir}/wzp6_ee_eeH_BES-lower-1pc_ecm240",               "xsec": 0.007169})
    
    
    # other ZH production mode samples
    datasets.append({"name": "wzp6_ee_tautauH_ecm240",                  "datadir": f"{baseDir}/wzp6_ee_tautauH_ecm240",                         "xsec": 0.0067518})
    datasets.append({"name": "wzp6_ee_nunuH_ecm240",                    "datadir": f"{baseDir}/wzp6_ee_nunuH_ecm240",                           "xsec": 0.046191})
    datasets.append({"name": "wzp6_ee_qqH_ecm240",                      "datadir": f"{baseDir}/wzp6_ee_qqH_ecm240",                             "xsec": 0.13635 })
    
    
    # Hmumu samples
    datasets.append({"name": "wzp6_ee_nunuH_Hmumu_ecm240",              "datadir": f"{baseDir}/wzp6_ee_nunuH_Hmumu_ecm240",                     "xsec": 1.005e-05})
    datasets.append({"name": "wzp6_ee_eeH_Hmumu_ecm240",                "datadir": f"{baseDir}/wzp6_ee_eeH_Hmumu_ecm240",                       "xsec": 1.558e-06})
    datasets.append({"name": "wzp6_ee_tautauH_Hmumu_ecm240",            "datadir": f"{baseDir}/wzp6_ee_tautauH_Hmumu_ecm240",                   "xsec": 1.469e-06})
    datasets.append({"name": "wzp6_ee_ccH_Hmumu_ecm240",                "datadir": f"{baseDir}/wzp6_ee_ccH_Hmumu_ecm240",                       "xsec": 5.079e-06})
    datasets.append({"name": "wzp6_ee_bbH_Hmumu_ecm240",                "datadir": f"{baseDir}/wzp6_ee_bbH_Hmumu_ecm240",                       "xsec": 6.521e-06})
    datasets.append({"name": "wzp6_ee_qqH_Hmumu_ecm240",                "datadir": f"{baseDir}/wzp6_ee_qqH_Hmumu_ecm240",                       "xsec": 1.161e-05})
    datasets.append({"name": "wzp6_ee_ssH_Hmumu_ecm240",                "datadir": f"{baseDir}/wzp6_ee_ssH_Hmumu_ecm240",                       "xsec": 6.519e-06})
    datasets.append({"name": "wzp6_ee_mumuH_Hmumu_ecm240",              "datadir": f"{baseDir}/wzp6_ee_mumuH_Hmumu_ecm240",                     "xsec": 1.472e-06})
    

    ## diboson backgrounds
    datasets.append({"name": "p8_ee_WW_ecm240",                         "datadir": f"{baseDir}/p8_ee_WW_ecm240",                                "xsec": 16.4385})
    datasets.append({"name": "p8_ee_ZZ_ecm240",                         "datadir": f"{baseDir}/p8_ee_ZZ_ecm240",                                "xsec": 1.35899})
    datasets.append({"name": "p8_ee_Zqq_ecm240",                        "datadir": f"{baseDir}/p8_ee_Zqq_ecm240",                               "xsec": 52.6539})
    
    
    # dilepton backgrounds
    datasets.append({"name": "wzp6_ee_mumu_ecm240",                     "datadir": f"{baseDir}/wzp6_ee_mumu_ecm240",                            "xsec": 5.288})
    datasets.append({"name": "wzp6_ee_tautau_ecm240",                   "datadir": f"{baseDir}/wzp6_ee_tautau_ecm240",                          "xsec": 4.668})
    datasets.append({"name": "wzp6_ee_ee_Mee_30_150_ecm240",            "datadir": f"{baseDir}/wzp6_ee_ee_Mee_30_150_ecm240",                   "xsec": 8.305})
    datasets.append({"name": "wzp6_ee_nuenueZ_ecm240",                  "datadir": f"{baseDir}/wzp6_ee_nuenueZ_ecm240",                         "xsec": 0.033274})
      
     
    ## e-gamma backgrounds
    datasets.append({"name": "wzp6_egamma_eZ_Zmumu_ecm240",             "datadir": f"{baseDir}/wzp6_egamma_eZ_Zmumu_ecm240",                    "xsec": 0.10368})
    datasets.append({"name": "wzp6_gammae_eZ_Zmumu_ecm240",             "datadir": f"{baseDir}/wzp6_gammae_eZ_Zmumu_ecm240",                    "xsec": 0.10368})
    datasets.append({"name": "wzp6_egamma_eZ_Zee_ecm240",               "datadir": f"{baseDir}/wzp6_egamma_eZ_Zee_ecm240",                      "xsec": 0.05198})
    datasets.append({"name": "wzp6_gammae_eZ_Zee_ecm240",               "datadir": f"{baseDir}/wzp6_gammae_eZ_Zee_ecm240",                      "xsec": 0.05198})
  
    
    # gamma-gamma backgrounds
    datasets.append({"name": "wzp6_gaga_mumu_60_ecm240",                "datadir": f"{baseDir}/wzp6_gaga_mumu_60_ecm240",                       "xsec": 1.5523})
    datasets.append({"name": "wzp6_gaga_tautau_60_ecm240",              "datadir": f"{baseDir}/wzp6_gaga_tautau_60_ecm240",                     "xsec": 0.836})
    datasets.append({"name": "wzp6_gaga_ee_60_ecm240",                  "datadir": f"{baseDir}/wzp6_gaga_ee_60_ecm240",                         "xsec": 0.873 })

    return datasets
    