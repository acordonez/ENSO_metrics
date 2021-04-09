# -*- coding:UTF-8 -*-
#
# Define ENSO metrics plots
#
from copy import deepcopy
from numpy import arange as NUMPYarange
# ENSO_metrics functions
from .EnsoCollectionsLib import defCollection
from .KeyArgLib import default_arg_values


dict_colorbar = {
    "amplitude": "amp",
    "anomalies": "balance",
    "PR": "rain",
    "SST": "thermal",
}

dict_label = {
    "amplitude": [round(ii, 1) for ii in NUMPYarange(0, 2.1, 0.5)],
    "amplitude5": list(range(0, 6, 1)),
    "amplitude10": [round(ii, 1) for ii in NUMPYarange(0, 10.1, 2.5)],
    "amplitude15": list(range(0, 16, 5)),
    "amplitude60": list(range(0, 61, 20)),
    "PR": list(range(0, 13, 4)),
    "PRA": [round(ii, 1) for ii in NUMPYarange(-1, 1.1, 0.5)],
    "REG03": [round(ii, 1) for ii in NUMPYarange(-0.3, 0.35, 0.1)],
    "REG05": [round(ii, 2) for ii in NUMPYarange(-0.5, 0.55, 0.25)],
    "REG12": [round(ii, 1) for ii in NUMPYarange(-1.2, 1.4, 0.6)],
    "REG2": list(range(-2, 3, 1)),
    "REG25": [round(ii, 1) for ii in NUMPYarange(-2.5, 2.6, 1.0)],
    "REG3": list(range(-3, 4, 1)),
    "REG4": list(range(-4, 5, 1)),
    "REG5": [round(ii, 1) for ii in NUMPYarange(-5, 6, 2.5)],
    "REG20": list(range(-20, 25, 10)),
    "REG30": list(range(-30, 35, 15)),
    "REG50": list(range(-50, 55, 25)),
    "REG60": list(range(-60, 65, 30)),
    "REG80": list(range(-80, 85, 40)),
    "SKEW": [round(ii, 1) for ii in NUMPYarange(-1.5, 1.6, 0.5)],
    "dSST": list(range(-2, 3, 1)),
    "SST": list(range(21, 31, 3)),
    "SSTA": [round(ii, 1) for ii in NUMPYarange(-1, 1.1, 0.5)],
    "TAUX": list(range(-100, 110, 50)),
    "TAUY": list(range(-40, 41, 20)),
}

output_variables = {
    "BiasPrLatRmse": ["pr_lat__", "pr_map__"],
    "BiasPrLonRmse": ["pr_lon__", "pr_map__"],
    "BiasPrMapRmse": ["pr_map__"],
    "BiasSshLatRmse": ["ssh_lat__", "ssh_map__"],
    "BiasSshLonRmse": ["ssh_lon__", "ssh_map__"],
    "BiasSshMapRmse": ["ssh_map__"],
    "BiasSstLatRmse": ["sst_lat__", "sst_map__"],
    "BiasSstLonRmse": ["sst_lon__", "sst_map__"],
    "BiasSstMapRmse": ["sst_map__"],
    "BiasTauxLatRmse": ["taux_lat__", "taux_map__"],
    "BiasTauxLonRmse": ["taux_lon__", "taux_map__"],
    "BiasTauxMapRmse": ["taux_map__"],
    "BiasTauyLatRmse": ["tauy_lat__", "tauy_map__"],
    "BiasTauyLonRmse": ["tauy_lon__", "tauy_map__"],
    "BiasTauyMapRmse": ["tauy_map__"],
    "EnsoAmpl": ["sstStd_lon__", "sstStd_map__"],
    "EnsoSstSkew": ["sstSke_lon__", "sstSke_map__"],
    "EnsoSeasonality": [
        "sstStd_ts__", "sstStd_hov__", "sstStd_NDJ_lon__", "sstStd_MAM_lon__", "sstStd_NDJ_map__",
        "sstStd_MAM_map__"],
    "EnsoSstDiversity": ["enso_lon_pos_maxSSTA__", "nina_lon_pos_minSSTA__", "nino_lon_pos_maxSSTA__",
                         "enso_lon_SSTA__", "nina_lon_SSTA__", "nino_lon_SSTA__"],
    "EnsoDuration": ["reg_sst_ts_onto_sst_onto__", "nina_duration__", "nino_duration__"],
    "EnsodSstOce": [
        "dSST_ts__", "dSSTthf_ts__", "dSSToce_ts__", "dSSTthf_lon__", "dSSToce_lon__", "dSST_hov__", "dSSTthf_hov__",
        "dSSToce_hov__"],
    "EnsoPrLonRmse": [
        "reg_pr_lon_onto_sst__", "reg_pr_map_onto_sst__", "nina_pr_lon__", "nino_pr_lon__", "nina_pr_map__",
        "nino_pr_map__"],
    "EnsoSshLonRmse": [
        "reg_ssh_lon_onto_sst__", "nina_ssh_lon__", "nino_ssh_lon__", "reg_ssh_map_onto_sst__", "nina_ssh_map__",
        "nino_ssh_map__"],
    "EnsoSstLonRmse": [
        "reg_sst_lon_onto_sst__", "nina_sst_lon__", "nino_sst_lon__", "reg_sst_map_onto_sst__", "nina_sst_map__",
        "nino_sst_map__"],
    "EnsoTauxLonRmse": [
        "reg_taux_lon_onto_sst__", "nina_taux_lon__", "nino_taux_lon__", "reg_taux_map_onto_sst__", "nina_taux_map__",
        "nino_taux_map__"],
    "EnsoTauyLonRmse": [
        "reg_tauy_lon_onto_sst__", "nina_tauy_lon__", "nino_tauy_lon__", "reg_tauy_map_onto_sst__", "nina_tauy_map__",
        "nino_tauy_map__"],
    "EnsoPrTsRmse": [
        "reg_pr_ts_onto_sst__", "nina_pr_ts__", "nino_pr_ts__", "reg_pr_hov_onto_sst__", "nina_pr_hov__",
        "nino_pr_hov__"],
    "EnsoSshTsRmse": [
        "reg_ssh_ts_onto_sst__", "nina_ssh_ts__", "nino_ssh_ts__", "reg_ssh_hov_onto_sst__", "nina_ssh_hov__",
        "nino_ssh_hov__"],
    "EnsoSstTsRmse": [
        "reg_sst_ts_onto_sst__", "nina_sst_ts__", "nino_sst_ts__", "reg_sst_hov_onto_sst__", "nina_sst_hov__",
        "nino_sst_hov__"],
    "EnsoTauxTsRmse": [
        "reg_taux_ts_onto_sst__", "nina_taux_ts__", "nino_taux_ts__", "reg_taux_hov_onto_sst__", "nina_taux_hov__",
        "nino_taux_hov__"],
    "EnsoTauyTsRmse": [
        "reg_tauy_ts_onto_sst__", "nina_tauy_ts__", "nino_tauy_ts__", "reg_tauy_hov_onto_sst__", "nina_tauy_hov__",
        "nino_tauy_hov__"],
    "EnsoFbSshSst": [
        "ssh__", "sst__", "reg_sst_lon_onto_ssh__", "reg_sst_lon_onto_sshPOS__", "reg_sst_lon_onto_sshNEG__",
        "reg_sst_hov_onto_ssh__", "reg_sst_hov_onto_sshPOS__", "reg_sst_hov_onto_sshNEG__"],
    "EnsoFbSstLhf": [
        "sst__", "lhf__", "reg_lhf_lon_onto_sst__", "reg_lhf_lon_onto_sstPOS__", "reg_lhf_lon_onto_sstNEG__",
        "reg_lhf_hov_onto_sst__", "reg_lhf_hov_onto_sstPOS__", "reg_lhf_hov_onto_sstNEG__"],
    "EnsoFbSstLwr": [
        "sst__", "lwr__", "reg_lwr_lon_onto_sst__", "reg_lwr_lon_onto_sstPOS__", "reg_lwr_lon_onto_sstNEG__",
        "reg_lwr_hov_onto_sst__", "reg_lwr_hov_onto_sstPOS__", "reg_lwr_hov_onto_sstNEG__"],
    "EnsoFbSstShf": [
        "sst__", "shf__", "reg_shf_lon_onto_sst__", "reg_shf_lon_onto_sstPOS__", "reg_shf_lon_onto_sstNEG__",
        "reg_shf_hov_onto_sst__", "reg_shf_hov_onto_sstPOS__", "reg_shf_hov_onto_sstNEG__"],
    "EnsoFbSstSwr": [
        "sst__", "swr__", "reg_swr_lon_onto_sst__", "reg_swr_lon_onto_sstPOS__", "reg_swr_lon_onto_sstNEG__",
        "reg_swr_hov_onto_sst__", "reg_swr_hov_onto_sstPOS__", "reg_swr_hov_onto_sstNEG__"],
    "EnsoFbSstTaux": [
        "sst__", "taux__", "reg_taux_lon_onto_sst__", "reg_taux_lon_onto_sstPOS__", "reg_taux_lon_onto_sstNEG__",
        "reg_taux_hov_onto_sst__", "reg_taux_hov_onto_sstPOS__", "reg_taux_hov_onto_sstNEG__"],
    "EnsoFbSstThf": [
        "sst__", "thf__", "reg_thf_lon_onto_sst__", "reg_thf_lon_onto_sstPOS__", "reg_thf_lon_onto_sstNEG__",
        "reg_thf_hov_onto_sst__", "reg_thf_hov_onto_sstPOS__", "reg_thf_hov_onto_sstNEG__"],
    "EnsoFbTauxSsh": [
        "taux__", "ssh__", "reg_ssh_lon_onto_taux__", "reg_ssh_lon_onto_tauxPOS__", "reg_ssh_lon_onto_tauxNEG__",
        "reg_ssh_hov_onto_taux__", "reg_ssh_hov_onto_tauxPOS__", "reg_ssh_hov_onto_tauxNEG__"],
    "EnsoPrMap": [
        "reg_pr_map_onto_sst__", "nina_pr_map__", "nino_pr_map__", "reg_pr_map_onto_sst_africaSE__",
        "nina_pr_map_africaSE__", "nino_pr_map_africaSE__", "reg_pr_map_onto_sst_americaN__", "nina_pr_map_americaN__",
        "nino_pr_map_americaN__", "reg_pr_map_onto_sst_americaS__", "nina_pr_map_americaS__", "nino_pr_map_americaS__",
        "reg_pr_map_onto_sst_asiaS__", "nina_pr_map_asiaS__", "nino_pr_map_asiaS__", "reg_pr_map_onto_sst_oceania__",
        "nina_pr_map_oceania__", "nino_pr_map_oceania__"],
    "EnsoPrMapDjf": [
        "reg_pr_map_onto_sst_djf__", "nina_pr_map_djf__", "nino_pr_map_djf__", "reg_pr_map_onto_sst_djf_africaSE__",
        "nina_pr_map_djf_africaSE__", "nino_pr_map_djf_africaSE__", "reg_pr_map_onto_sst_djf_americaN__",
        "nina_pr_map_djf_americaN__", "nino_pr_map_djf_americaN__", "reg_pr_map_onto_sst_djf_americaS__",
        "nina_pr_map_djf_americaS__", "nino_pr_map_djf_americaS__", "reg_pr_map_onto_sst_djf_asiaS__",
        "nina_pr_map_djf_asiaS__", "nino_pr_map_djf_asiaS__", "reg_pr_map_onto_sst_djf_oceania__",
        "nina_pr_map_djf_oceania__", "nino_pr_map_djf_oceania__"],
    "EnsoPrMapJja": [
        "reg_pr_map_onto_sst_jja__", "nina_pr_map_jja__", "nino_pr_map_jja__", "reg_pr_map_onto_sst_jja_africaSE__",
        "reg_pr_map_onto_sst_jja_americaN__", "reg_pr_map_onto_sst_jja_americaS__", "reg_pr_map_onto_sst_jja_asiaS__",
        "reg_pr_map_onto_sst_jja_oceania__", "nina_pr_map_jja_africaSE__", "nino_pr_map_jja_africaSE__",
        "nina_pr_map_jja_americaN__", "nino_pr_map_jja_americaN__", "nina_pr_map_jja_americaS__",
        "nino_pr_map_jja_americaS__", "nina_pr_map_jja_asiaS__", "nino_pr_map_jja_asiaS__", "nina_pr_map_jja_oceania__",
        "nino_pr_map_jja_oceania__"],
    "EnsoSlpMap": [
        "reg_slp_map_onto_sst__", "reg_slp_map_onto_sst_africaSE__", "reg_slp_map_onto_sst_americaN__",
        "reg_slp_map_onto_sst_americaS__", "reg_slp_map_onto_sst_asiaS__", "reg_slp_map_onto_sst_oceania__"],
    "EnsoSlpMapDjf": [
        "reg_slp_map_onto_sst_djf__", "nina_slp_map_djf__", "nino_slp_map_djf__", "reg_slp_map_onto_sst_djf_africaSE__",
        "reg_slp_map_onto_sst_djf_americaN__", "reg_slp_map_onto_sst_djf_americaS__",
        "reg_slp_map_onto_sst_djf_asiaS__", "reg_slp_map_onto_sst_djf_oceania__", "nina_slp_map_djf_africaSE__",
        "nino_slp_map_djf_africaSE__", "nina_slp_map_djf_americaN__", "nino_slp_map_djf_americaN__",
        "nina_slp_map_djf_americaS__", "nino_slp_map_djf_americaS__", "nina_slp_map_djf_asiaS__",
        "nino_slp_map_djf_asiaS__", "nina_slp_map_djf_oceania__", "nino_slp_map_djf_oceania__"],
    "EnsoSlpMapJja": [
        "reg_slp_map_onto_sst_jja__", "nina_slp_map_jja__", "nino_slp_map_jja__", "reg_slp_map_onto_sst_jja_africaSE__",
        "reg_slp_map_onto_sst_jja_americaN__", "reg_slp_map_onto_sst_jja_americaS__",
        "reg_slp_map_onto_sst_jja_asiaS__", "reg_slp_map_onto_sst_jja_oceania__", "nina_slp_map_jja_africaSE__",
        "nino_slp_map_jja_africaSE__", "nina_slp_map_jja_americaN__", "nino_slp_map_jja_americaN__",
        "nina_slp_map_jja_americaS__", "nino_slp_map_jja_americaS__", "nina_slp_map_jja_asiaS__",
        "nino_slp_map_jja_asiaS__", "nina_slp_map_jja_oceania__", "nino_slp_map_jja_oceania__"],
    "EnsoSstMap": [
        "reg_tas_map_onto_sst__", "reg_tas_map_onto_sst_africaSE__", "reg_tas_map_onto_sst_americaN__",
        "reg_tas_map_onto_sst_americaS__", "reg_tas_map_onto_sst_asiaS__", "reg_tas_map_onto_sst_oceania__"],
    "EnsoSstMapDjf": [
        "reg_tas_map_onto_sst_djf__", "nina_tas_map_djf__", "nino_tas_map_djf__", "reg_tas_map_onto_sst_djf_africaSE__",
        "reg_tas_map_onto_sst_djf_americaN__", "reg_tas_map_onto_sst_djf_americaS__",
        "reg_tas_map_onto_sst_djf_asiaS__", "reg_tas_map_onto_sst_djf_oceania__", "nina_tas_map_djf_africaSE__",
        "nino_tas_map_djf_africaSE__", "nina_tas_map_djf_americaN__", "nino_tas_map_djf_americaN__",
        "nina_tas_map_djf_americaS__", "nino_tas_map_djf_americaS__", "nina_tas_map_djf_asiaS__",
        "nino_tas_map_djf_asiaS__", "nina_tas_map_djf_oceania__", "nino_tas_map_djf_oceania__"],
    "EnsoSstMapJja": [
        "reg_tas_map_onto_sst_jja__", "nina_tas_map_jja__", "nino_tas_map_jja__", "reg_tas_map_onto_sst_jja_africaSE__",
        "reg_tas_map_onto_sst_jja_americaN__", "reg_tas_map_onto_sst_jja_americaS__",
        "reg_tas_map_onto_sst_jja_asiaS__", "reg_tas_map_onto_sst_jja_oceania__", "nina_tas_map_jja_africaSE__",
        "nino_tas_map_jja_africaSE__", "nina_tas_map_jja_americaN__", "nino_tas_map_jja_americaN__",
        "nina_tas_map_jja_americaS__", "nino_tas_map_jja_americaS__", "nina_tas_map_jja_asiaS__",
        "nino_tas_map_jja_asiaS__", "nina_tas_map_jja_oceania__", "nino_tas_map_jja_oceania__"],
    "grad_lat_pr": ["pr_lat__", "pr_map__"],
    "grad_lat_sst": ["sst_lat__", "sst_map__"],
    "grad_lon_pr": ["pr_lon__", "pr_map__"],
    "grad_lon_sst": ["sst_lon__", "sst_map__"],
    "SeasonalPrLatRmse": ["prMacStd_lat__", "prMacStd_map__", "prMac_hov__"],
    "SeasonalPrLonRmse": ["prMacStd_lon__", "prMacStd_map__", "prMac_hov__"],
    "SeasonalSshLatRmse": ["sshMacStd_lat__", "sshMacStd_map__", "sshMac_hov__"],
    "SeasonalSshLonRmse": ["sshMacStd_lon__", "sshMacStd_map__", "sshMac_hov__"],
    "SeasonalSstLatRmse": ["sstMacStd_lat__", "sstMacStd_map__", "sstMac_hov__"],
    "SeasonalSstLonRmse": ["sstMacStd_lon__", "sstMacStd_map__", "sstMac_hov__"],
    "SeasonalTauxLatRmse": ["tauxMacStd_lat__", "tauxMacStd_map__", "tauxMac_hov__"],
    "SeasonalTauxLonRmse": ["tauxMacStd_lon__", "tauxMacStd_map__", "tauxMac_hov__"],
    "SeasonalTauyLatRmse": ["tauyMacStd_lat__", "tauyMacStd_map__", "tauyMac_hov__"],
    "SeasonalTauyLonRmse": ["tauyMacStd_lon__", "tauyMacStd_map__", "tauyMac_hov__"],
}

plot_parameters = {
    "BiasPrLatRmse": {
        "diagnostic": {
            "plot_type": "curve",
            "nbr_panel": 1,
            "title": "Mean PR",  # "a) Mean meridional PR",  #
            "varpattern": output_variables["BiasPrLatRmse"][0],
            "xname": "latitude",
            "yname": "PR",
            "method": "1) Linearly detrended\n2) Temporal averaged\n3) Regridded to 1°x1°\n" +
                      "4) Zonal averaged (see box)\n\nMetric: RMSE$_y$",
        },
        "dive_down01": {
            "plot_type": "map",
            "nbr_panel": 2,
            "colorbar": dict_colorbar["PR"],
            "label": dict_label["PR"],
            "maskland": True,
            "title": ["Mean PR", "Mean PR"],
            "varpattern": output_variables["BiasPrLatRmse"][1],
            "xname": "longitude",
            "yname": "latitude",
            "zname": "PR",
            "method": "1) Linearly detrended\n2) Temporal averaged\n3) Regridded to 1°x1°",
        },
    },
    "BiasPrLonRmse": {
        "diagnostic": {
            "plot_type": "curve",
            "nbr_panel": 1,
            "title": "Mean PR",
            "varpattern": output_variables["BiasPrLonRmse"][0],
            "xname": "longitude",
            "yname": "PR",
            "method": "1) Linearly detrended\n2) Temporal averaged\n3) Regridded to 1°x1°\n" +
                      "4) Meridional averaged (see box)\n\nMetric: RMSE$_x$",
        },
        "dive_down01": {
            "plot_type": "map",
            "nbr_panel": 2,
            "colorbar": dict_colorbar["PR"],
            "label": dict_label["PR"],
            "maskland": True,
            "title": ["Mean PR", "Mean PR"],
            "varpattern": output_variables["BiasPrLonRmse"][1],
            "xname": "longitude",
            "yname": "latitude",
            "zname": "PR",
            "method": "1) Linearly detrended\n2) Temporal averaged\n3) Regridded to 1°x1°",
        },
    },
    "BiasPrMapRmse": {
        "diagnostic": {
            "plot_type": "map",
            "nbr_panel": 2,
            "colorbar": dict_colorbar["PR"],
            "label": dict_label["PR"],
            "maskland": True,
            "title": ["Mean PR", "Mean PR"],
            "varpattern": output_variables["BiasPrMapRmse"][0],
            "xname": "longitude",
            "yname": "latitude",
            "zname": "PR",
            "method": "1) Linearly detrended\n2) Temporal averaged\n3) Regridded to 1°x1°\n\nMetric: RMSE$_{xy}$",
        },
    },
    "BiasSshLatRmse": {
        "diagnostic": {
            "plot_type": "curve",
            "nbr_panel": 1,
            "title": "Mean SSH",
            "varpattern": output_variables["BiasSshLatRmse"][0],
            "xname": "latitude",
            "yname": "SSH",
            "method": "1) Linearly detrended\n2) Temporal averaged\n3) Regridded to 1°x1°\n" +
                      "4) Zonal averaged (see box)\n\nMetric: RMSE$_y$",
        },
        "dive_down01": {
            "plot_type": "map",
            "nbr_panel": 2,
            "colorbar": dict_colorbar["SST"],  # YYP: I do not know yet the colobar / label needed
            "label": dict_label["SST"],
            "maskland": True,
            "title": ["Mean SSH", "Mean SSH"],
            "varpattern": output_variables["BiasSshLatRmse"][1],
            "xname": "longitude",
            "yname": "latitude",
            "zname": "SSH",
            "method": "1) Linearly detrended\n2) Temporal averaged\n3) Regridded to 1°x1°",
        },
    },
    "BiasSshLonRmse": {
        "diagnostic": {
            "plot_type": "curve",
            "nbr_panel": 1,
            "title": "Mean SSH",
            "varpattern": output_variables["BiasSshLonRmse"][0],
            "xname": "longitude",
            "yname": "SSH",
            "method": "1) Linearly detrended\n2) Temporal averaged\n3) Regridded to 1°x1°\n" +
                      "4) Meridional averaged (see box)\n\nMetric: RMSE$_x$",
        },
        "dive_down01": {
            "plot_type": "map",
            "nbr_panel": 2,
            "colorbar": dict_colorbar["SST"],  # YYP: I do not know yet the colobar / label needed
            "label": dict_label["SST"],
            "maskland": True,
            "title": ["Mean SSH", "Mean SSH"],
            "varpattern": output_variables["BiasSshLonRmse"][1],
            "xname": "longitude",
            "yname": "latitude",
            "zname": "SSH",
            "method": "1) Linearly detrended\n2) Temporal averaged\n3) Regridded to 1°x1°",
        },
    },
    "BiasSshMapRmse": {
        "diagnostic": {
            "plot_type": "map",
            "nbr_panel": 2,
            "colorbar": dict_colorbar["SST"],  # YYP: I do not know yet the colobar / label needed
            "label": dict_label["SST"],
            "maskland": True,
            "title": ["Mean SSH", "Mean SSH"],
            "varpattern": output_variables["BiasSshMapRmse"][0],
            "xname": "longitude",
            "yname": "latitude",
            "zname": "SSH",
            "method": "1) Linearly detrended\n2) Temporal averaged\n3) Regridded to 1°x1°\n\nMetric: RMSE$_{xy}$",
        },
    },
    "BiasSstLatRmse": {
        "diagnostic": {
            "plot_type": "curve",
            "nbr_panel": 1,
            "title": "Mean SST",
            "varpattern": output_variables["BiasSstLatRmse"][0],
            "xname": "latitude",
            "yname": "SST",
            "method": "1) Linearly detrended\n2) Temporal averaged\n3) Regridded to 1°x1°\n" +
                      "4) Zonal averaged (see box)\n\nMetric: RMSE$_y$",
        },
        "dive_down01": {
            "plot_type": "map",
            "nbr_panel": 2,
            "colorbar": dict_colorbar["SST"],
            "label": dict_label["SST"],
            "maskland": True,
            "title": ["Mean SST", "Mean SST"],
            "varpattern": output_variables["BiasSstLatRmse"][1],
            "xname": "longitude",
            "yname": "latitude",
            "zname": "SST",
            "method": "1) Linearly detrended\n2) Temporal averaged\n3) Regridded to 1°x1°",
        },
    },
    "BiasSstLonRmse": {
        "diagnostic": {
            "plot_type": "curve",
            "nbr_panel": 1,
            "title": "Mean SST",
            "varpattern": output_variables["BiasSstLonRmse"][0],
            "xname": "longitude",
            "yname": "SST",
            "method": "1) Linearly detrended\n2) Temporal averaged\n3) Regridded to 1°x1°\n" +
                      "4) Meridional averaged (see box)\n\nMetric: RMSE$_x$",
        },
        "dive_down01": {
            "plot_type": "map",
            "nbr_panel": 2,
            "colorbar": dict_colorbar["SST"],
            "label": dict_label["SST"],
            "maskland": True,
            "title": ["Mean SST", "Mean SST"],
            "varpattern": output_variables["BiasSstLonRmse"][1],
            "xname": "longitude",
            "yname": "latitude",
            "zname": "SST",
            "method": "1) Linearly detrended\n2) Temporal averaged\n3) Regridded to 1°x1°",
        },
    },
    "BiasSstMapRmse": {
        "diagnostic": {
            "plot_type": "map",
            "nbr_panel": 2,
            "colorbar": dict_colorbar["SST"],
            "label": dict_label["SST"],
            "maskland": True,
            "title": ["Mean SST", "Mean SST"],
            "varpattern": output_variables["BiasSstMapRmse"][0],
            "xname": "longitude",
            "yname": "latitude",
            "zname": "SST",
            "method": "1) Linearly detrended\n2) Temporal averaged\n3) Regridded to 1°x1°\n\nMetric: RMSE$_{xy}$",
        },
    },
    "BiasTauxLatRmse": {
        "diagnostic": {
            "plot_type": "curve",
            "nbr_panel": 1,
            "title": "Mean TAUX",
            "varpattern": output_variables["BiasTauxLatRmse"][0],
            "xname": "latitude",
            "yname": "TAUX",
            "method": "1) Linearly detrended\n2) Temporal averaged\n3) Regridded to 1°x1°\n" +
                      "4) Zonal averaged (see box)\n\nMetric: RMSE$_y$",
        },
        "dive_down01": {
            "plot_type": "map",
            "nbr_panel": 2,
            "colorbar": dict_colorbar["anomalies"],
            "label": dict_label["TAUX"],
            "maskland": True,
            "title": ["Mean TAUX", "Mean TAUX"],
            "varpattern": output_variables["BiasTauxLatRmse"][1],
            "xname": "longitude",
            "yname": "latitude",
            "zname": "TAUX",
            "method": "1) Linearly detrended\n2) Temporal averaged\n3) Regridded to 1°x1°",
        },
    },
    "BiasTauxLonRmse": {
        "diagnostic": {
            "plot_type": "curve",
            "nbr_panel": 1,
            "title": "Mean TAUX",
            "varpattern": output_variables["BiasTauxLonRmse"][0],
            "xname": "longitude",
            "yname": "TAUX",
            "method": "1) Linearly detrended\n2) Temporal averaged\n3) Regridded to 1°x1°\n" +
                      "4) Meridional averaged (see box)\n\nMetric: RMSE$_x$",
        },
        "dive_down01": {
            "plot_type": "map",
            "nbr_panel": 2,
            "colorbar": dict_colorbar["anomalies"],
            "label": dict_label["TAUX"],
            "maskland": True,
            "title": ["Mean TAUX", "Mean TAUX"],
            "varpattern": output_variables["BiasTauxLonRmse"][1],
            "xname": "longitude",
            "yname": "latitude",
            "zname": "TAUX",
            "method": "1) Linearly detrended\n2) Temporal averaged\n3) Regridded to 1°x1°",
        },
    },
    "BiasTauxMapRmse": {
        "diagnostic": {
            "plot_type": "map",
            "nbr_panel": 2,
            "colorbar": dict_colorbar["anomalies"],
            "label": dict_label["TAUX"],
            "maskland": True,
            "title": ["Mean TAUX", "Mean TAUX"],
            "varpattern": output_variables["BiasTauxMapRmse"][0],
            "xname": "longitude",
            "yname": "latitude",
            "zname": "TAUX",
            "method": "1) Linearly detrended\n2) Temporal averaged\n3) Regridded to 1°x1°\n\nMetric: RMSE$_{xy}$",
        },
    },
    "BiasTauyLatRmse": {
        "diagnostic": {
            "plot_type": "curve",
            "nbr_panel": 1,
            "title": "Mean TAUY",
            "varpattern": output_variables["BiasTauyLatRmse"][0],
            "xname": "latitude",
            "yname": "TAUY",
            "method": "1) Linearly detrended\n2) Temporal averaged\n3) Regridded to 1°x1°\n" +
                      "4) Zonal averaged (see box)\n\nMetric: RMSE$_y$",
        },
        "dive_down01": {
            "plot_type": "map",
            "nbr_panel": 2,
            "colorbar": dict_colorbar["anomalies"],
            "label": dict_label["TAUY"],
            "maskland": True,
            "title": ["Mean TAUY", "Mean TAUY"],
            "varpattern": output_variables["BiasTauyLatRmse"][1],
            "xname": "longitude",
            "yname": "latitude",
            "zname": "TAUY",
            "method": "1) Linearly detrended\n2) Temporal averaged\n3) Regridded to 1°x1°",
        },
    },
    "BiasTauyLonRmse": {
        "diagnostic": {
            "plot_type": "curve",
            "nbr_panel": 1,
            "title": "Mean TAUY",
            "varpattern": output_variables["BiasTauyLonRmse"][0],
            "xname": "longitude",
            "yname": "TAUY",
            "method": "1) Linearly detrended\n2) Temporal averaged\n3) Regridded to 1°x1°\n" +
                      "4) Meridional averaged (see box)\n\nMetric: RMSE$_x$",
        },
        "dive_down01": {
            "plot_type": "map",
            "nbr_panel": 2,
            "colorbar": dict_colorbar["anomalies"],
            "label": dict_label["TAUY"],
            "maskland": True,
            "title": ["Mean TAUY", "Mean TAUY"],
            "varpattern": output_variables["BiasTauyLonRmse"][1],
            "xname": "longitude",
            "yname": "latitude",
            "zname": "TAUY",
            "method": "1) Linearly detrended\n2) Temporal averaged\n3) Regridded to 1°x1°",
        },
    },
    "BiasTauyMapRmse": {
        "diagnostic": {
            "plot_type": "map",
            "nbr_panel": 2,
            "colorbar": dict_colorbar["anomalies"],
            "label": dict_label["TAUY"],
            "maskland": True,
            "title": ["Mean TAUY", "Mean TAUY"],
            "varpattern": output_variables["BiasTauyMapRmse"][0],
            "xname": "longitude",
            "yname": "latitude",
            "zname": "TAUY",
            "method": "1) Linearly detrended\n2) Temporal averaged\n3) Regridded to 1°x1°\n\nMetric: RMSE$_{xy}$",
        },
    },
    "EnsoAmpl": {
        "diagnostic": {
            "plot_type": "dot",
            "nbr_panel": 1,
            "title": "ENSO's SSTA amplitude",
            "varpattern": "diagnostic",
            "yname": "SSTA std",
            "method": "1) REGION1 averaged\n2) Linearly detrended\n3) Seasonal cycle removed\n" +
                      "4) Standard deviation\n\nMetric: abs((STD$_{mod}$-STD$_{ref}$)/STD$_{ref}$)*100",

        },
        "dive_down01": {
            "plot_type": "curve",
            "nbr_panel": 1,
            "title": "SSTA standard deviation",
            "varpattern": output_variables["EnsoAmpl"][0],
            "xname": "longitude",
            "yname": "SSTA std",
            "method": "1) Linearly detrended\n2) Seasonal cycle removed\n3) Standard deviation\n" +
                      "4) Regridded to 1°x1°\n5) 5S-5N meridional averaged",
        },
        "dive_down02": {
            "plot_type": "map",
            "nbr_panel": 2,
            "colorbar": dict_colorbar["amplitude"],
            "label": dict_label["amplitude"],
            "maskland": True,
            "title": ["SSTA standard deviation", "SSTA standard deviation"],
            "varpattern": output_variables["EnsoAmpl"][1],
            "xname": "longitude",
            "yname": "latitude",
            "zname": "SSTA std",
            "method": "1) Linearly detrended\n2) Seasonal cycle removed\n3) Standard deviation\n" +
                      "4) Regridded to 1°x1°",
        },
    },
    "EnsodSstOce": {
        "diagnostic": {
            "plot_type": "dot",
            "nbr_panel": 1,
            "title": "ENSO ocean-driven SST change",
            "varpattern": "diagnostic",
            "yname": "normalized dSSToce",
            "method": "1) Horizontal averaged\n2) Linearly detrended\n3) Seasonal cycle removed\n" +
                      "4) Detect El Nino and La Nina\n    (NDJ N3.4 SSTA > 0.5 STD 5 cons. seasons)\n" +
                      "5) dSST = REGION1 SSTA Dec. - Jul.\n6) REGION1 NHFA summed from Jul. to Dec.\n" +
                      "7) dSST = dSST/dSST and dSSTnhf = dSSTnhf/dSST\n" +
                      "8) dSSToce = dSST - dSSTnhf\n9) Mean dSSToce both El Nino and La Nina\n\n" +
                      "Metric: abs((dSSToce$_{mod}$-dSSToce$_{ref}$)/dSSToce$_{ref}$)*100",
        },
        "dive_down01": {
            "plot_type": "curve",
            "nbr_panel": 1,
            "title": "ENSO SST change",
            "varpattern": output_variables["EnsodSstOce"][:3],
            "colors": {"model": ["black", "red", "blue"], "reference": ["black", "red", "blue"]},
            "linestyles": {"model": ["-", "-", "-"], "reference": ["-.", "-.", "-."]},
            "legend": ["dSST", "dSSTnhf", "dSSToce"],
            "xname": "months",
            "yname": "normalized dSST",
            "method": "1) Horizontal averaged\n2) Linearly detrended\n3) Seasonal cycle removed\n" +
                      "4) Detect El Nino and La Nina\n    (NDJ N3.4 SSTA > 0.5 STD 5 cons. seasons)\n" +
                      "5) dSST$_i$ = REGION1 SSTA M$_i$ - M$_{i-1}$\n" +
                      "6) dSSTnhf$_i$ = REGION1 NHFA summed from M$_0$ to M$_i$\n" +
                      "7) dt = dSST$_{dec}$-dSST$_{jul}$,\n    dSST$_i$ = dSST$_i$/dt,\n    " +
                      "dSSTnhf$_i$ = dSSTnhf$_i$/dt\n" +
                      "8) dSSToce$_i$ = dSST$_i$ - dSSTnhf$_i$\n9) Mean dSSToce both El Nino and La Nina",
        },
        "dive_down02": {
            "plot_type": "curve",
            "nbr_panel": 1,
            "title": "ENSO SST change",
            "varpattern": output_variables["EnsodSstOce"][3:5],
            "colors": {"model": ["red", "blue"], "reference": ["red", "blue"]},
            "linestyles": {"model": ["-", "-"], "reference": ["-.", "-."]},
            "legend": ["dSSTnhf", "dSSToce"],
            "xname": "longitude",
            "yname": "normalized dSST",
            "method": "1) N3.4 SST averaged\n2) Linearly detrended\n3) Seasonal cycle removed\n" +
                      "4) Detect El Nino and La Nina\n    (NDJ N3.4 SSTA > 0.5 STD 5 cons. seasons)\n" +
                      "5) Regridded to 1°x1°\n6) 5S-5N meridional averaged\n" +
                      "7) dSST = SSTA Dec. - Jul.\n8) NHFA summed from Jul. to Dec.\n" +
                      "9) dSST = dSST/dSST and dSSTnhf = dSSTnhf/dSST\n" +
                      "10) dSSToce = dSST - dSSTnhf\n11) Mean dSSToce both El Nino and La Nina",
        },
        "dive_down03": {
            "plot_type": "hovmoeller",
            "nbr_panel": 6,
            "colorbar": dict_colorbar["anomalies"],
            "label": dict_label["dSST"],
            "title": ["ENSO dSST", "ENSO heat flux dSST", "ENSO ocean dSST"],
            "varpattern": output_variables["EnsodSstOce"][5:],
            "xname": "longitude",
            "yname": "months",
            "zname": "normalized dSST",
            "method": "1) N3.4 SST averaged\n2) Linearly detrended\n3) Seasonal cycle removed\n" +
                      "4) Detect El Nino and La Nina\n    (NDJ N3.4 SSTA > 0.5 STD 5 cons. seasons)\n" +
                      "5) Regridded to 1°x1°\n6) 5S-5N meridional averaged\n" +
                      "7) dSST$_i$ = SSTA M$_i$ - M$_{i-1}$\n8) dSSTnhf$_i$ = NHFA summed from M$_0$ to M$_i$\n" +
                      "9) dt = dSST$_{dec}$-dSST$_{jul}$,\n    dSST$_i$ = dSST$_i$/dt,\n    " +
                      "dSSTnhf$_i$ = dSSTnhf$_i$/dt\n" +
                      "10) dSSToce$_i$ = dSST$_i$ - dSSTnhf$_i$\n11) Mean dSSToce both El Nino and La Nina",
        },

    },
    "EnsoDuration": {
        "diagnostic": {
            "plot_type": "dot",
            "nbr_panel": 1,
            "title": "ENSO duration",
            "varpattern": "diagnostic",
            "yname": "duration (reg>0.25)",
            "method": "1) REGION1 averaged\n2) Linearly detrended\n3) Seasonal cycle removed\n" +
                      "4) 5-month triangular running ave.\n5) REGION1 SSTA regressed onto NDJ REGION1 SSTA\n" +
                      "6) Duration = nbr months > 0.25\n\nMetric: abs((DUR$_{mod}$-DUR$_{ref}$)/DUR$_{ref}$)*100",
        },
        "dive_down01": {
            "plot_type": "curve",
            "nbr_panel": 1,
            "title": "ENSO life-cycle",
            "varpattern": output_variables["EnsoDuration"][0],
            "xname": "months",
            "yname": "reg(SSTA, SSTA)",
            "method": "1) REGION1 averaged\n2) Linearly detrended\n3) Seasonal cycle removed\n" +
                      "4) 5-month triangular running ave.\n5) REGION1 SSTA regressed onto NDJ REGION1 SSTA",
        },
        "dive_down02": {
            "plot_type": "boxplot",
            "nbr_panel": 2,
            "title": ["La Nina duration", "El Nino duration"],
            "varpattern": output_variables["EnsoDuration"][1:],
            "yname": ["duration (SSTA<-0.5)", "duration (SSTA>0.5)"],
            "method": "1) REGION1 SST averaged\n2) Linearly detrended\n3) Seasonal cycle removed\n" +
                      "4) 5-month triangular running ave.\n" +
                      "5) Detect El Nino and La Nina\n    (NDJ REGION1 SSTA > 0.5 STD 5 cons. seasons)\n" +
                      "6) Duration = nbr months > 0.5 ENSO STD",
        },
    },
    "EnsoFbSshSst": {
        "diagnostic": {
            "plot_type": "scatterplot",
            "nbr_panel": 1,
            "title": "SSH-SST feedback",
            "varpattern": output_variables["EnsoFbSshSst"][:2],
            "xname": "SSHA",
            "yname": "SSTA",
            "method": "1) Horizontal averaged\n2) Linearly detrended\n3) Seasonal cycle removed\n" +
                      "4) REGION1 SSTA regressed onto REGION1 SSHA\n\n" +
                      "Metric: abs((Slope$_{mod}$-Slope$_{ref}$)/Slope$_{ref}$)*100",
        },
        "dive_down01": {
            "plot_type": "scatterplot",
            "nbr_panel": 2,
            "title": "nonlinarity",
            "varpattern": output_variables["EnsoFbSshSst"][:2],
            "xname": "SSHA",
            "yname": "SSTA",
            "method": "1) Horizontal averaged\n2) Linearly detrended\n3) Seasonal cycle removed\n" +
                      "4) REGION1 SSTA regressed onto REGION1 SSHA>0 (SSHA<0)",
        },
        "dive_down02": {
            "plot_type": "curve",
            "nbr_panel": 1,
            "title": "SSH-SST feedback",
            "varpattern": output_variables["EnsoFbSshSst"][2:5],
            "colors": {"model": ["black", "red", "blue"], "reference": ["black", "red", "blue"]},
            "linestyles": {"model": ["-", "-", "-"], "reference": ["-.", "-.", "-."]},
            "legend": ["All", "SSHA>0", "SSHA<0"],
            "xname": "longitude",
            "yname": "reg(SSHA, SSTA)",
            "method": "1) Linearly detrended\n2) Seasonal cycle removed\n" +
                      "3) Regridded to 1°x1°\n4) 5S-5N meridional averaged\n5) 30° zonal running ave.\n" +
                      "6) SSTA regressed onto SSHA or SSHA>0 or SSHA<0",
        },
        "dive_down03": {
            "plot_type": "hovmoeller",
            "nbr_panel": 6,
            "colorbar": dict_colorbar["anomalies"],
            "label": dict_label["REG03"],
            "title": ["reg(SSHA, SSTA)", "reg(SSHA>0, SSTA)", "reg(SSHA<0, SSTA)"],
            "varpattern": output_variables["EnsoFbSshSst"][5:],
            "xname": "longitude",
            "yname": "months",
            "zname": "regression",
            "method": "1) Linearly detrended\n2) Seasonal cycle removed\n" +
                      "3) Regridded to 1°x1°\n4) 5S-5N meridional averaged\n5) 30° zonal running ave.\n" +
                      "6) For each calendar month:\n    SSTA regressed onto SSHA or SSHA>0 or SSHA<0",
        },
    },
    "EnsoFbSstLhf": {
        "diagnostic": {
            "plot_type": "scatterplot",
            "nbr_panel": 1,
            "title": "SST-LHF feedback",
            "varpattern": output_variables["EnsoFbSstLhf"][:2],
            "xname": "SSTA",
            "yname": "LHFA",
            "method": "1) Horizontal averaged\n2) Linearly detrended\n3) Seasonal cycle removed\n" +
                      "4) REGION1 LHFA regressed onto REGION1 SSTA\n\n" +
                      "Metric: abs((Slope$_{mod}$-Slope$_{ref}$)/Slope$_{ref}$)*100",
        },
        "dive_down01": {
            "plot_type": "scatterplot",
            "nbr_panel": 2,
            "title": "nonlinarity",
            "varpattern": output_variables["EnsoFbSstLhf"][:2],
            "xname": "SSTA",
            "yname": "LHFA",
            "method": "1) Horizontal averaged\n2) Linearly detrended\n3) Seasonal cycle removed\n" +
                      "4) REGION1 LHFA regressed onto REGION1 SSTA>0 (SSTA<0)",
        },
        "dive_down02": {
            "plot_type": "curve",
            "nbr_panel": 1,
            "title": "SST-LHF feedback",
            "varpattern": output_variables["EnsoFbSstLhf"][2:5],
            "colors": {"model": ["black", "red", "blue"], "reference": ["black", "red", "blue"]},
            "linestyles": {"model": ["-", "-", "-"], "reference": ["-.", "-.", "-."]},
            "legend": ["All", "SSTA>0", "SSTA<0"],
            "xname": "longitude",
            "yname": "reg(SSTA, LHFA)",
            "method": "1) Linearly detrended\n2) Seasonal cycle removed\n" +
                      "3) Regridded to 1°x1°\n4) 5S-5N meridional averaged\n5) 30° zonal running ave.\n" +
                      "6) LHFA regressed onto SSTA or SSTA>0 or SSTA<0",
        },
        "dive_down03": {
            "plot_type": "hovmoeller",
            "nbr_panel": 6,
            "colorbar": dict_colorbar["anomalies"],
            "label": dict_label["REG20"],
            "title": ["reg(SSTA, LHFA)", "reg(SSTA>0, LHFA)", "reg(SSTA<0, LHFA)"],
            "varpattern": output_variables["EnsoFbSstLhf"][5:],
            "xname": "longitude",
            "yname": "months",
            "zname": "regression",
            "method": "1) Linearly detrended\n2) Seasonal cycle removed\n" +
                      "3) Regridded to 1°x1°\n4) 5S-5N meridional averaged\n5) 30° zonal running ave.\n" +
                      "6) For each calendar month:\n    LHFA regressed onto SSTA or SSTA>0 or SSTA<0",
        },
    },
    "EnsoFbSstLwr": {
        "diagnostic": {
            "plot_type": "scatterplot",
            "nbr_panel": 1,
            "title": "SST-LWR feedback",
            "varpattern": output_variables["EnsoFbSstLwr"][:2],
            "xname": "SSTA",
            "yname": "LWRA",
            "method": "1) Horizontal averaged\n2) Linearly detrended\n3) Seasonal cycle removed\n" +
                      "4) REGION1 LWRA regressed onto REGION1 SSTA\n\n" +
                      "Metric: abs((Slope$_{mod}$-Slope$_{ref}$)/Slope$_{ref}$)*100",
        },
        "dive_down01": {
            "plot_type": "scatterplot",
            "nbr_panel": 2,
            "title": "nonlinarity",
            "varpattern": output_variables["EnsoFbSstLwr"][:2],
            "xname": "SSTA",
            "yname": "LWRA",
            "method": "1) Horizontal averaged\n2) Linearly detrended\n3) Seasonal cycle removed\n" +
                      "4) REGION1 LWRA regressed onto REGION1 SSTA>0 (SSTA<0)",
        },
        "dive_down02": {
            "plot_type": "curve",
            "nbr_panel": 1,
            "title": "SST-LWR feedback",
            "varpattern": output_variables["EnsoFbSstLwr"][2:5],
            "colors": {"model": ["black", "red", "blue"], "reference": ["black", "red", "blue"]},
            "linestyles": {"model": ["-", "-", "-"], "reference": ["-.", "-.", "-."]},
            "legend": ["All", "SSTA>0", "SSTA<0"],
            "xname": "longitude",
            "yname": "reg(SSTA, LWRA)",
            "method": "1) Linearly detrended\n2) Seasonal cycle removed\n" +
                      "3) Regridded to 1°x1°\n4) 5S-5N meridional averaged\n5) 30° zonal running ave.\n" +
                      "6) LWRA regressed onto SSTA or SSTA>0 or SSTA<0",
        },
        "dive_down03": {
            "plot_type": "hovmoeller",
            "nbr_panel": 6,
            "colorbar": dict_colorbar["anomalies"],
            "label": dict_label["REG20"],
            "title": ["reg(SSTA, LWRA)", "reg(SSTA>0, LWRA)", "reg(SSTA<0, LWRA)"],
            "varpattern": output_variables["EnsoFbSstLwr"][5:],
            "xname": "longitude",
            "yname": "months",
            "zname": "regression",
            "method": "1) Linearly detrended\n2) Seasonal cycle removed\n" +
                      "3) Regridded to 1°x1°\n4) 5S-5N meridional averaged\n5) 30° zonal running ave.\n" +
                      "6) For each calendar month:\n    LWRA regressed onto SSTA or SSTA>0 or SSTA<0",
        },
    },
    "EnsoFbSstShf": {
        "diagnostic": {
            "plot_type": "scatterplot",
            "nbr_panel": 1,
            "title": "SST-SHF feedback",
            "varpattern": output_variables["EnsoFbSstShf"][:2],
            "xname": "SSTA",
            "yname": "SHFA",
            "method": "1) Horizontal averaged\n2) Linearly detrended\n3) Seasonal cycle removed\n" +
                      "4) REGION1 SHFA regressed onto REGION1 SSTA\n\n" +
                      "Metric: abs((Slope$_{mod}$-Slope$_{ref}$)/Slope$_{ref}$)*100",
        },
        "dive_down01": {
            "plot_type": "scatterplot",
            "nbr_panel": 2,
            "title": "nonlinarity",
            "varpattern": output_variables["EnsoFbSstShf"][:2],
            "xname": "SSTA",
            "yname": "SHFA",
            "method": "1) Horizontal averaged\n2) Linearly detrended\n3) Seasonal cycle removed\n" +
                      "4) REGION1 SHFA regressed onto REGION1 SSTA>0 (SSTA<0)",
        },
        "dive_down02": {
            "plot_type": "curve",
            "nbr_panel": 1,
            "title": "SST-SHF feedback",
            "varpattern": output_variables["EnsoFbSstShf"][2:5],
            "colors": {"model": ["black", "red", "blue"], "reference": ["black", "red", "blue"]},
            "linestyles": {"model": ["-", "-", "-"], "reference": ["-.", "-.", "-."]},
            "legend": ["All", "SSTA>0", "SSTA<0"],
            "xname": "longitude",
            "yname": "reg(SSTA, SHFA)",
            "method": "1) Linearly detrended\n2) Seasonal cycle removed\n" +
                      "3) Regridded to 1°x1°\n4) 5S-5N meridional averaged\n5) 30° zonal running ave.\n" +
                      "6) SHFA regressed onto SSTA or SSTA>0 or SSTA<0",
        },
        "dive_down03": {
            "plot_type": "hovmoeller",
            "nbr_panel": 6,
            "colorbar": dict_colorbar["anomalies"],
            "label": dict_label["REG5"],
            "title": ["reg(SSTA, SHFA)", "reg(SSTA>0, SHFA)", "reg(SSTA<0, SHFA)"],
            "varpattern": output_variables["EnsoFbSstShf"][5:],
            "xname": "longitude",
            "yname": "months",
            "zname": "regression",
            "method": "1) Linearly detrended\n2) Seasonal cycle removed\n" +
                      "3) Regridded to 1°x1°\n4) 5S-5N meridional averaged\n5) 30° zonal running ave.\n" +
                      "6) For each calendar month:\n    SHFA regressed onto SSTA or SSTA>0 or SSTA<0",
        },
    },
    "EnsoFbSstSwr": {
        "diagnostic": {
            "plot_type": "scatterplot",
            "nbr_panel": 1,
            "title": "SST-SWR feedback",
            "varpattern": output_variables["EnsoFbSstSwr"][:2],
            "xname": "SSTA",
            "yname": "SWRA",
            "method": "1) Horizontal averaged\n2) Linearly detrended\n3) Seasonal cycle removed\n" +
                      "4) REGION1 SWRA regressed onto REGION1 SSTA\n\n" +
                      "Metric: abs((Slope$_{mod}$-Slope$_{ref}$)/Slope$_{ref}$)*100",
        },
        "dive_down01": {
            "plot_type": "scatterplot",
            "nbr_panel": 2,
            "title": "nonlinarity",
            "varpattern": output_variables["EnsoFbSstSwr"][:2],
            "xname": "SSTA",
            "yname": "SWRA",
            "method": "1) Horizontal averaged\n2) Linearly detrended\n3) Seasonal cycle removed\n" +
                      "4) REGION1 SWRA regressed onto REGION1 SSTA>0 (SSTA<0)",
        },
        "dive_down02": {
            "plot_type": "curve",
            "nbr_panel": 1,
            "title": "SST-SWR feedback",
            "varpattern": output_variables["EnsoFbSstSwr"][2:5],
            "colors": {"model": ["black", "red", "blue"], "reference": ["black", "red", "blue"]},
            "linestyles": {"model": ["-", "-", "-"], "reference": ["-.", "-.", "-."]},
            "legend": ["All", "SSTA>0", "SSTA<0"],
            "xname": "longitude",
            "yname": "reg(SSTA, SWRA)",
            "method":  "1) Linearly detrended\n2) Seasonal cycle removed\n" +
                      "3) Regridded to 1°x1°\n4) 5S-5N meridional averaged\n5) 30° zonal running ave.\n" +
                      "6) SWRA regressed onto SSTA or SSTA>0 or SSTA<0",
        },
        "dive_down03": {
            "plot_type": "hovmoeller",
            "nbr_panel": 6,
            "colorbar": dict_colorbar["anomalies"],
            "label": dict_label["REG50"],
            "title": ["reg(SSTA, SWRA)", "reg(SSTA>0, SWRA)", "reg(SSTA<0, SWRA)"],
            "varpattern": output_variables["EnsoFbSstSwr"][5:],
            "xname": "longitude",
            "yname": "months",
            "zname": "regression",
            "method": "1) Linearly detrended\n2) Seasonal cycle removed\n" +
                      "3) Regridded to 1°x1°\n4) 5S-5N meridional averaged\n5) 30° zonal running ave.\n" +
                      "6) For each calendar month:\n    SWRA regressed onto SSTA or SSTA>0 or SSTA<0",
        },
    },
    "EnsoFbSstTaux": {
        "diagnostic": {
            "plot_type": "scatterplot",
            "nbr_panel": 1,
            "title": "SST-Taux feedback",
            "varpattern": output_variables["EnsoFbSstTaux"][:2],
            "xname": "SSTA",
            "yname": "TAUXA",
            "method": "1) Horizontal averaged\n2) Linearly detrended\n3) Seasonal cycle removed\n" +
                      "4) REGION2 TAUXA regressed onto REGION1 SSTA\n\n" +
                      "Metric: abs((Slope$_{mod}$-Slope$_{ref}$)/Slope$_{ref}$)*100",
        },
        "dive_down01": {
            "plot_type": "scatterplot",
            "nbr_panel": 2,
            "title": "nonlinarity",
            "varpattern": output_variables["EnsoFbSstTaux"][:2],
            "xname": "SSTA",
            "yname": "TAUXA",
            "method": "1) Horizontal averaged\n2) Linearly detrended\n3) Seasonal cycle removed\n" +
                      "4) REGION2 TAUXA regressed onto REGION1 SSTA>0 (SSTA<0)",
        },
        "dive_down02": {
            "plot_type": "curve",
            "nbr_panel": 1,
            "title": "SST-Taux feedback",
            "varpattern": output_variables["EnsoFbSstTaux"][2:5],
            "colors": {"model": ["black", "red", "blue"], "reference": ["black", "red", "blue"]},
            "linestyles": {"model": ["-", "-", "-"], "reference": ["-.", "-.", "-."]},
            "legend": ["All", "SSTA>0", "SSTA<0"],
            "xname": "longitude",
            "yname": "reg(SSTA, TAUXA)",
            "method": "1) REGION1 SST averaged\n2) Linearly detrended\n3) Seasonal cycle removed\n" +
                      "4) TAUXA regridded to 1°x1°\n5) TAUXA 5S-5N meridional averaged\n" +
                      "6) TAUXA 30° zonal running ave.\n7) TAUXA regressed onto REGION1 SSTA or SSTA>0 or SSTA<0",
        },
        "dive_down03": {
            "plot_type": "hovmoeller",
            "nbr_panel": 6,
            "colorbar": dict_colorbar["anomalies"],
            "label": dict_label["REG20"],
            "title": ["reg(SSTA, TAUXA)", "reg(SSTA>0, TAUXA)", "reg(SSTA<0, TAUXA)"],
            "varpattern": output_variables["EnsoFbSstTaux"][5:],
            "xname": "longitude",
            "yname": "months",
            "zname": "regression",
            "method": "1) REGION1 SST averaged\n2) Linearly detrended\n3) Seasonal cycle removed\n" +
                      "4) TAUXA regridded to 1°x1°\n5) TAUXA 5S-5N meridional averaged\n" +
                      "6) TAUXA 30° zonal running ave.\n" +
                      "7) For each calendar month:\n    TAUXA regressed onto REGION1 SSTA or SSTA>0 or SSTA<0",
        },
    },
    "EnsoFbSstThf": {
        "diagnostic": {
            "plot_type": "scatterplot",
            "nbr_panel": 1,
            "title": "SST-NHF feedback",
            "varpattern": output_variables["EnsoFbSstThf"][:2],
            "xname": "SSTA",
            "yname": "NHFA",
            "method": "1) Horizontal averaged\n2) Linearly detrended\n3) Seasonal cycle removed\n" +
                      "4) REGION1 NHFA regressed onto REGION1 SSTA\n\n" +
                      "Metric: abs((Slope$_{mod}$-Slope$_{ref}$)/Slope$_{ref}$)*100",
        },
        "dive_down01": {
            "plot_type": "scatterplot",
            "nbr_panel": 2,
            "title": "nonlinarity",
            "varpattern": output_variables["EnsoFbSstThf"][:2],
            "xname": "SSTA",
            "yname": "NHFA",
            "method": "1) Horizontal averaged\n2) Linearly detrended\n3) Seasonal cycle removed\n" +
                      "4) REGION1 NHFA regressed onto REGION1 SSTA>0 (SSTA<0)",
        },
        "dive_down02": {
            "plot_type": "curve",
            "nbr_panel": 1,
            "title": "SST-NHF feedback",
            "varpattern": output_variables["EnsoFbSstThf"][2:5],
            "colors": {"model": ["black", "red", "blue"], "reference": ["black", "red", "blue"]},
            "linestyles": {"model": ["-", "-", "-"], "reference": ["-.", "-.", "-."]},
            "legend": ["All", "SSTA>0", "SSTA<0"],
            "xname": "longitude",
            "yname": "reg(SSTA, NHFA)",
            "method": "1) Linearly detrended\n2) Seasonal cycle removed\n" +
                      "3) Regridded to 1°x1°\n4) 5S-5N meridional averaged\n5) 30° zonal running ave.\n" +
                      "6) NHFA regressed onto SSTA or SSTA>0 or SSTA<0",
        },
        "dive_down03": {
            "plot_type": "hovmoeller",
            "nbr_panel": 6,
            "colorbar": dict_colorbar["anomalies"],
            "label": dict_label["REG50"],
            "title": ["reg(SSTA, NHFA)", "reg(SSTA>0, NHFA)", "reg(SSTA<0, NHFA)"],
            "varpattern": output_variables["EnsoFbSstThf"][5:],
            "xname": "longitude",
            "yname": "months",
            "zname": "regression",
            "method": "1) Linearly detrended\n2) Seasonal cycle removed\n" +
                      "3) Regridded to 1°x1°\n4) 5S-5N meridional averaged\n5) 30° zonal running ave.\n" +
                      "6) For each calendar month:\n    NHFA regressed onto SSTA or SSTA>0 or SSTA<0",
        },
    },
    "EnsoFbTauxSsh": {
        "diagnostic": {
            "plot_type": "scatterplot",
            "nbr_panel": 1,
            "title": "Taux-SSH feedback",
            "varpattern": output_variables["EnsoFbTauxSsh"][:2],
            "xname": "TAUXA",
            "yname": "SSHA",
            "method": "1) Horizontal averaged\n2) Linearly detrended\n3) Seasonal cycle removed\n" +
                      "4) REGION2 SSHA regressed onto REGION1 TAUXA\n\n" +
                      "Metric: abs((Slope$_{mod}$-Slope$_{ref}$)/Slope$_{ref}$)*100",
        },
        "dive_down01": {
            "plot_type": "scatterplot",
            "nbr_panel": 2,
            "title": "nonlinarity",
            "varpattern": output_variables["EnsoFbTauxSsh"][:2],
            "xname": "TAUXA",
            "yname": "SSHA",
            "method": "1) Horizontal averaged\n2) Linearly detrended\n3) Seasonal cycle removed\n" +
                      "4) REGION2 SSHA regressed onto REGION1 TAUXA>0 (TAUXA<0)",
        },
        "dive_down02": {
            "plot_type": "curve",
            "nbr_panel": 1,
            "title": "Taux-SSH feedback",
            "varpattern": output_variables["EnsoFbTauxSsh"][2:5],
            "colors": {"model": ["black", "red", "blue"], "reference": ["black", "red", "blue"]},
            "linestyles": {"model": ["-", "-", "-"], "reference": ["-.", "-.", "-."]},
            "legend": ["All", "TAUXA>0", "TAUXA<0"],
            "xname": "longitude",
            "yname": "reg(TAUXA, SSHA)",
            "method": "1) REGION1 TAUX averaged\n2) Linearly detrended\n3) Seasonal cycle removed\n" +
                      "4) SSHA regridded to 1°x1°\n5) SSHA 5S-5N meridional averaged\n6) SSHA 30° zonal running ave.\n"
                      + "7) SSHA regressed onto REGION1 TAUXA or TAUXA>0 or TAUXA<0",
        },
        "dive_down03": {
            "plot_type": "hovmoeller",
            "nbr_panel": 6,
            "colorbar": dict_colorbar["anomalies"],
            "label": dict_label["REG05"],
            "title": ["reg(TAUXA, SSHA)", "reg(TAUXA>0, SSHA)", "reg(TAUXA<0, SSHA)"],
            "varpattern": output_variables["EnsoFbTauxSsh"][5:],
            "xname": "longitude",
            "yname": "months",
            "zname": "regression",
            "method": "1) REGION1 TAUX averaged\n2) Linearly detrended\n3) Seasonal cycle removed\n" +
                      "4) SSHA regridded to 1°x1°\n5) SSHA 5S-5N meridional averaged\n6) SSHA 30° zonal running ave.\n"
                      + "7) For each calendar month:\n    SSHA regressed onto REGION1 TAUXA or TAUXA>0 or TAUXA<0",
        },
    },
    "EnsoPrMap": {
        "diagnostic": {
            "plot_type": "map",
            "nbr_panel": 2,
            "colorbar": dict_colorbar["anomalies"],
            "label": dict_label["PRA"],
            "maskland": False,
            "title": ["reg(ENSO SSTA, PRA)", "reg(ENSO SSTA, PRA)"],
            "varpattern": output_variables["EnsoPrMap"][0],
            "xname": "longitude",
            "yname": "latitude",
            "zname": "regression",
            "method": "1) N3.4 SST averaged\n2) Linearly detrended\n3) Seasonal cycle removed\n" +
                      "4) 5-month triangular running ave.\n5) PRA regridded to 1°x1°\n" +
                      "6) Dec. PRA regressed onto Dec. N3.4 SSTA\n7) Equatorial Pacific masked\n\nMetric: RMSE$_{xy}$",
        },
        # ["africaSE", "americaN", "americaS", "asiaS", "oceania"]
        "dive_down01": {
            "plot_type": "map",
            "nbr_panel": 2,
            "colorbar": dict_colorbar["anomalies"],
            "label": dict_label["PRA"],
            "maskland": False,
            "maskocean": True,
            "title": ["reg(ENSO SSTA, PRA)", "reg(ENSO SSTA, PRA)"],
            "varpattern": output_variables["EnsoPrMap"][1],
            "xname": "longitude",
            "yname": "latitude",
            "zname": "regression",
            "method": "1) N3.4 SST averaged\n2) Linearly detrended\n3) Seasonal cycle removed\n" +
                      "4) 5-month triangular running ave.\n5) PRA regridded to 1°x1°\n" +
                      "6) Dec. PRA regressed onto Dec. N3.4 SSTA\n7) Mask ocean",
        },
        "dive_down02": {
            "plot_type": "map",
            "nbr_panel": 2,
            "colorbar": dict_colorbar["anomalies"],
            "label": dict_label["PRA"],
            "maskland": False,
            "maskocean": True,
            "title": ["reg(ENSO SSTA, PRA)", "reg(ENSO SSTA, PRA)"],
            "varpattern": output_variables["EnsoPrMap"][2],
            "xname": "longitude",
            "yname": "latitude",
            "zname": "regression",
            "method": "1) N3.4 SST averaged\n2) Linearly detrended\n3) Seasonal cycle removed\n" +
                      "4) 5-month triangular running ave.\n5) PRA regridded to 1°x1°\n" +
                      "6) Dec. PRA regressed onto Dec. N3.4 SSTA\n7) Mask ocean",
        },
        "dive_down03": {
            "plot_type": "map",
            "nbr_panel": 2,
            "colorbar": dict_colorbar["anomalies"],
            "label": dict_label["PRA"],
            "maskland": False,
            "maskocean": True,
            "title": ["reg(ENSO SSTA, PRA)", "reg(ENSO SSTA, PRA)"],
            "varpattern": output_variables["EnsoPrMap"][3],
            "xname": "longitude",
            "yname": "latitude",
            "zname": "regression",
            "method": "1) N3.4 SST averaged\n2) Linearly detrended\n3) Seasonal cycle removed\n" +
                      "4) 5-month triangular running ave.\n5) PRA regridded to 1°x1°\n" +
                      "6) Dec. PRA regressed onto Dec. N3.4 SSTA\n7) Mask ocean",
        },
        "dive_down04": {
            "plot_type": "map",
            "nbr_panel": 2,
            "colorbar": dict_colorbar["anomalies"],
            "label": dict_label["PRA"],
            "maskland": False,
            "maskocean": True,
            "title": ["reg(ENSO SSTA, PRA)", "reg(ENSO SSTA, PRA)"],
            "varpattern": output_variables["EnsoPrMap"][4],
            "xname": "longitude",
            "yname": "latitude",
            "zname": "regression",
            "method": "1) N3.4 SST averaged\n2) Linearly detrended\n3) Seasonal cycle removed\n" +
                      "4) 5-month triangular running ave.\n5) PRA regridded to 1°x1°\n" +
                      "6) Dec. PRA regressed onto Dec. N3.4 SSTA\n7) Mask ocean",
        },
        "dive_down05": {
            "plot_type": "map",
            "nbr_panel": 2,
            "colorbar": dict_colorbar["anomalies"],
            "label": dict_label["PRA"],
            "maskland": False,
            "maskocean": True,
            "title": ["reg(ENSO SSTA, PRA)", "reg(ENSO SSTA, PRA)"],
            "varpattern": output_variables["EnsoPrMap"][5],
            "xname": "longitude",
            "yname": "latitude",
            "zname": "regression",
            "method": "1) N3.4 SST averaged\n2) Linearly detrended\n3) Seasonal cycle removed\n" +
                      "4) 5-month triangular running ave.\n5) PRA regridded to 1°x1°\n" +
                      "6) Dec. PRA regressed onto Dec. N3.4 SSTA\n7) Mask ocean",
        },
    },
    "EnsoPrMapDjf": {
        "diagnostic": {
            "plot_type": "map",
            "nbr_panel": 2,
            "colorbar": dict_colorbar["anomalies"],
            "label": dict_label["PRA"],
            "maskland": False,
            "title": ["reg(ENSO SSTA, PRA) DJF", "reg(ENSO SSTA, PRA) DJF"],
            "varpattern": output_variables["EnsoPrMapDjf"][0],
            "xname": "longitude",
            "yname": "latitude",
            "zname": "regression",
            "method": "1) N3.4 SST averaged\n2) Linearly detrended\n3) Seasonal cycle removed\n" +
                      "4) PRA regridded to 1°x1°\n5) DJF PRA regressed onto DJF N3.4 SSTA\n" +
                      "6) Equatorial Pacific masked\n\nMetric: RMSE$_{xy}$",
        },
        "dive_down01": {
            "plot_type": "map",
            "nbr_panel": 4,
            "colorbar": dict_colorbar["anomalies"],
            "label": dict_label["REG2"],
            "maskland": False,
            "title": ["La Nina PRA DJF", "El Nino PRA DJF"],
            "varpattern": output_variables["EnsoPrMapDjf"][1:3],
            "xname": "longitude",
            "yname": "latitude",
            "zname": "PRA",
            "method": "1) N3.4 SST averaged\n2) Linearly detrended\n3) Seasonal cycle removed\n" +
                      "4) Detect El Nino and La Nina\n    (NDJ N3.4 SSTA > 0.5 STD 5 cons. seasons)\n" +
                      "5) PRA regridded to 1°x1°\n6) El Nino and La Nina DJF PRA composited\n" +
                      "6) Equatorial Pacific masked",
        },
        # ["africaSE", "americaN", "americaS", "asiaS", "oceania"]
        "dive_down02": {
            "plot_type": "map",
            "nbr_panel": 2,
            "colorbar": dict_colorbar["anomalies"],
            "label": dict_label["PRA"],
            "maskland": False,
            "maskocean": True,
            "title": ["reg(ENSO SSTA, PRA) DJF", "reg(ENSO SSTA, PRA) DJF"],
            "varpattern": output_variables["EnsoPrMapDjf"][3],
            "xname": "longitude",
            "yname": "latitude",
            "zname": "regression",
            "method": "1) N3.4 SST averaged\n2) Linearly detrended\n3) Seasonal cycle removed\n" +
                      "4) PRA regridded to 1°x1°\n5) DJF PRA regressed onto DJF N3.4 SSTA\n6) Mask ocean",
        },
        "dive_down03": {
            "plot_type": "map",
            "nbr_panel": 4,
            "colorbar": dict_colorbar["anomalies"],
            "label": dict_label["REG2"],
            "maskland": False,
            "maskocean": True,
            "title": ["La Nina PRA DJF", "El Nino PRA DJF"],
            "varpattern": output_variables["EnsoPrMapDjf"][4:6],
            "xname": "longitude",
            "yname": "latitude",
            "zname": "PRA",
            "method": "1) N3.4 SST averaged\n2) Linearly detrended\n3) Seasonal cycle removed\n" +
                      "4) Detect El Nino and La Nina\n    (NDJ N3.4 SSTA > 0.5 STD 5 cons. seasons)\n" +
                      "5) PRA regridded to 1°x1°\n6) El Nino and La Nina DJF PRA composited\n7) Mask ocean",
        },
        "dive_down04": {
            "plot_type": "map",
            "nbr_panel": 2,
            "colorbar": dict_colorbar["anomalies"],
            "label": dict_label["PRA"],
            "maskland": False,
            "maskocean": True,
            "title": ["reg(ENSO SSTA, PRA) DJF", "reg(ENSO SSTA, PRA) DJF"],
            "varpattern": output_variables["EnsoPrMapDjf"][6],
            "xname": "longitude",
            "yname": "latitude",
            "zname": "regression",
            "method": "1) N3.4 SST averaged\n2) Linearly detrended\n3) Seasonal cycle removed\n" +
                      "4) PRA regridded to 1°x1°\n5) DJF PRA regressed onto DJF N3.4 SSTA\n6) Mask ocean",
        },
        "dive_down05": {
            "plot_type": "map",
            "nbr_panel": 4,
            "colorbar": dict_colorbar["anomalies"],
            "label": dict_label["REG2"],
            "maskland": False,
            "maskocean": True,
            "title": ["La Nina PRA DJF", "El Nino PRA DJF"],
            "varpattern": output_variables["EnsoPrMapDjf"][7:9],
            "xname": "longitude",
            "yname": "latitude",
            "zname": "PRA",
            "method": "1) N3.4 SST averaged\n2) Linearly detrended\n3) Seasonal cycle removed\n" +
                      "4) Detect El Nino and La Nina\n    (NDJ N3.4 SSTA > 0.5 STD 5 cons. seasons)\n" +
                      "5) PRA regridded to 1°x1°\n6) El Nino and La Nina DJF PRA composited\n7) Mask ocean",
        },
        "dive_down06": {
            "plot_type": "map",
            "nbr_panel": 2,
            "colorbar": dict_colorbar["anomalies"],
            "label": dict_label["PRA"],
            "maskland": False,
            "maskocean": True,
            "title": ["reg(ENSO SSTA, PRA) DJF", "reg(ENSO SSTA, PRA) DJF"],
            "varpattern": output_variables["EnsoPrMapDjf"][9],
            "xname": "longitude",
            "yname": "latitude",
            "zname": "regression",
            "method": "1) N3.4 SST averaged\n2) Linearly detrended\n3) Seasonal cycle removed\n" +
                      "4) PRA regridded to 1°x1°\n5) DJF PRA regressed onto DJF N3.4 SSTA\n6) Mask ocean",
        },
        "dive_down07": {
            "plot_type": "map",
            "nbr_panel": 4,
            "colorbar": dict_colorbar["anomalies"],
            "label": dict_label["REG2"],
            "maskland": False,
            "maskocean": True,
            "title": ["La Nina PRA DJF", "El Nino PRA DJF"],
            "varpattern": output_variables["EnsoPrMapDjf"][10:12],
            "xname": "longitude",
            "yname": "latitude",
            "zname": "PRA",
            "method": "1) N3.4 SST averaged\n2) Linearly detrended\n3) Seasonal cycle removed\n" +
                      "4) Detect El Nino and La Nina\n    (NDJ N3.4 SSTA > 0.5 STD 5 cons. seasons)\n" +
                      "5) PRA regridded to 1°x1°\n6) El Nino and La Nina DJF PRA composited\n7) Mask ocean",
        },
        "dive_down08": {
            "plot_type": "map",
            "nbr_panel": 2,
            "colorbar": dict_colorbar["anomalies"],
            "label": dict_label["PRA"],
            "maskland": False,
            "maskocean": True,
            "title": ["reg(ENSO SSTA, PRA) DJF", "reg(ENSO SSTA, PRA) DJF"],
            "varpattern": output_variables["EnsoPrMapDjf"][12],
            "xname": "longitude",
            "yname": "latitude",
            "zname": "regression",
            "method": "1) N3.4 SST averaged\n2) Linearly detrended\n3) Seasonal cycle removed\n" +
                      "4) PRA regridded to 1°x1°\n5) DJF PRA regressed onto DJF N3.4 SSTA\n6) Mask ocean",
        },
        "dive_down09": {
            "plot_type": "map",
            "nbr_panel": 4,
            "colorbar": dict_colorbar["anomalies"],
            "label": dict_label["REG2"],
            "maskland": False,
            "maskocean": True,
            "title": ["La Nina PRA DJF", "El Nino PRA DJF"],
            "varpattern": output_variables["EnsoPrMapDjf"][13:15],
            "xname": "longitude",
            "yname": "latitude",
            "zname": "PRA",
            "method": "1) N3.4 SST averaged\n2) Linearly detrended\n3) Seasonal cycle removed\n" +
                      "4) Detect El Nino and La Nina\n    (NDJ N3.4 SSTA > 0.5 STD 5 cons. seasons)\n" +
                      "5) PRA regridded to 1°x1°\n6) El Nino and La Nina DJF PRA composited\n7) Mask ocean",
        },
        "dive_down10": {
            "plot_type": "map",
            "nbr_panel": 2,
            "colorbar": dict_colorbar["anomalies"],
            "label": dict_label["PRA"],
            "maskland": False,
            "maskocean": True,
            "title": ["reg(ENSO SSTA, PRA) DJF", "reg(ENSO SSTA, PRA) DJF"],
            "varpattern": output_variables["EnsoPrMapDjf"][15],
            "xname": "longitude",
            "yname": "latitude",
            "zname": "regression",
            "method": "1) N3.4 SST averaged\n2) Linearly detrended\n3) Seasonal cycle removed\n" +
                      "4) PRA regridded to 1°x1°\n5) DJF PRA regressed onto DJF N3.4 SSTA\n6) Mask ocean",
        },
        "dive_down11": {
            "plot_type": "map",
            "nbr_panel": 4,
            "colorbar": dict_colorbar["anomalies"],
            "label": dict_label["REG2"],
            "maskland": False,
            "maskocean": True,
            "title": ["La Nina PRA DJF", "El Nino PRA DJF"],
            "varpattern": output_variables["EnsoPrMapDjf"][16:],
            "xname": "longitude",
            "yname": "latitude",
            "zname": "PRA",
            "method": "1) N3.4 SST averaged\n2) Linearly detrended\n3) Seasonal cycle removed\n" +
                      "4) Detect El Nino and La Nina\n    (NDJ N3.4 SSTA > 0.5 STD 5 cons. seasons)\n" +
                      "5) PRA regridded to 1°x1°\n6) El Nino and La Nina DJF PRA composited\n7) Mask ocean",
        },
    },
    "EnsoPrMapJja": {
        "diagnostic": {
            "plot_type": "map",
            "nbr_panel": 2,
            "colorbar": dict_colorbar["anomalies"],
            "label": dict_label["PRA"],
            "maskland": False,
            "title": ["reg(ENSO SSTA, PRA) JJA", "reg(ENSO SSTA, PRA) JJA"],
            "varpattern": output_variables["EnsoPrMapJja"][0],
            "xname": "longitude",
            "yname": "latitude",
            "zname": "regression",
            "method": "1) N3.4 SST averaged\n2) Linearly detrended\n3) Seasonal cycle removed\n" +
                      "4) PRA regridded to 1°x1°\n5) JJA PRA regressed onto JJA N3.4 SSTA\n" +
                      "6) Equatorial Pacific masked\n\nMetric: RMSE$_{xy}$",
        },
        "dive_down01": {
            "plot_type": "map",
            "nbr_panel": 4,
            "colorbar": dict_colorbar["anomalies"],
            "label": dict_label["SKEW"],
            "maskland": False,
            "title": ["La Nina PRA JJA", "El Nino PRA JJA"],
            "varpattern": output_variables["EnsoPrMapJja"][1:3],
            "xname": "longitude",
            "yname": "latitude",
            "zname": "PRA",
            "method": "1) N3.4 SST averaged\n2) Linearly detrended\n3) Seasonal cycle removed\n" +
                      "4) Detect El Nino and La Nina\n    (NDJ N3.4 SSTA > 0.5 STD 5 cons. seasons)\n" +
                      "5) PRA regridded to 1°x1°\n6) El Nino and La Nina JJA PRA composited\n" +
                      "6) Equatorial Pacific masked",
        },
        # ["africaSE", "americaN", "americaS", "asiaS", "oceania"]
        "dive_down02": {
            "plot_type": "map",
            "nbr_panel": 2,
            "colorbar": dict_colorbar["anomalies"],
            "label": dict_label["PRA"],
            "maskland": False,
            "maskocean": True,
            "title": ["reg(ENSO SSTA, PRA) JJA", "reg(ENSO SSTA, PRA) JJA"],
            "varpattern": output_variables["EnsoPrMapJja"][3],
            "xname": "longitude",
            "yname": "latitude",
            "zname": "regression",
            "method": "1) N3.4 SST averaged\n2) Linearly detrended\n3) Seasonal cycle removed\n" +
                      "4) PRA regridded to 1°x1°\n5) JJA PRA regressed onto JJA N3.4 SSTA\n6) Mask ocean",
        },
        "dive_down03": {
            "plot_type": "map",
            "nbr_panel": 4,
            "colorbar": dict_colorbar["anomalies"],
            "label": dict_label["SKEW"],
            "maskland": False,
            "maskocean": True,
            "title": ["La Nina PRA JJA", "El Nino PRA JJA"],
            "varpattern": output_variables["EnsoPrMapJja"][4:6],
            "xname": "longitude",
            "yname": "latitude",
            "zname": "PRA",
            "method": "1) N3.4 SST averaged\n2) Linearly detrended\n3) Seasonal cycle removed\n" +
                      "4) Detect El Nino and La Nina\n    (NDJ N3.4 SSTA > 0.5 STD 5 cons. seasons)\n" +
                      "5) PRA regridded to 1°x1°\n6) El Nino and La Nina JJA PRA composited\n7) Mask ocean",
        },
        "dive_down04": {
            "plot_type": "map",
            "nbr_panel": 2,
            "colorbar": dict_colorbar["anomalies"],
            "label": dict_label["PRA"],
            "maskland": False,
            "maskocean": True,
            "title": ["reg(ENSO SSTA, PRA) JJA", "reg(ENSO SSTA, PRA) JJA"],
            "varpattern": output_variables["EnsoPrMapJja"][6],
            "xname": "longitude",
            "yname": "latitude",
            "zname": "regression",
            "method": "1) N3.4 SST averaged\n2) Linearly detrended\n3) Seasonal cycle removed\n" +
                      "4) PRA regridded to 1°x1°\n5) JJA PRA regressed onto JJA N3.4 SSTA\n6) Mask ocean",
        },
        "dive_down05": {
            "plot_type": "map",
            "nbr_panel": 4,
            "colorbar": dict_colorbar["anomalies"],
            "label": dict_label["SKEW"],
            "maskland": False,
            "maskocean": True,
            "title": ["La Nina PRA JJA", "El Nino PRA JJA"],
            "varpattern": output_variables["EnsoPrMapJja"][7:9],
            "xname": "longitude",
            "yname": "latitude",
            "zname": "PRA",
            "method": "1) N3.4 SST averaged\n2) Linearly detrended\n3) Seasonal cycle removed\n" +
                      "4) Detect El Nino and La Nina\n    (NDJ N3.4 SSTA > 0.5 STD 5 cons. seasons)\n" +
                      "5) PRA regridded to 1°x1°\n6) El Nino and La Nina JJA PRA composited\n7) Mask ocean",
        },
        "dive_down06": {
            "plot_type": "map",
            "nbr_panel": 2,
            "colorbar": dict_colorbar["anomalies"],
            "label": dict_label["PRA"],
            "maskland": False,
            "maskocean": True,
            "title": ["reg(ENSO SSTA, PRA) JJA", "reg(ENSO SSTA, PRA) JJA"],
            "varpattern": output_variables["EnsoPrMapJja"][9],
            "xname": "longitude",
            "yname": "latitude",
            "zname": "regression",
            "method": "1) N3.4 SST averaged\n2) Linearly detrended\n3) Seasonal cycle removed\n" +
                      "4) PRA regridded to 1°x1°\n5) JJA PRA regressed onto JJA N3.4 SSTA\n6) Mask ocean",
        },
        "dive_down07": {
            "plot_type": "map",
            "nbr_panel": 4,
            "colorbar": dict_colorbar["anomalies"],
            "label": dict_label["SKEW"],
            "maskland": False,
            "maskocean": True,
            "title": ["La Nina PRA JJA", "El Nino PRA JJA"],
            "varpattern": output_variables["EnsoPrMapJja"][10:12],
            "xname": "longitude",
            "yname": "latitude",
            "zname": "PRA",
            "method": "1) N3.4 SST averaged\n2) Linearly detrended\n3) Seasonal cycle removed\n" +
                      "4) Detect El Nino and La Nina\n    (NDJ N3.4 SSTA > 0.5 STD 5 cons. seasons)\n" +
                      "5) PRA regridded to 1°x1°\n6) El Nino and La Nina JJA PRA composited\n7) Mask ocean",
        },
        "dive_down08": {
            "plot_type": "map",
            "nbr_panel": 2,
            "colorbar": dict_colorbar["anomalies"],
            "label": dict_label["PRA"],
            "maskland": False,
            "maskocean": True,
            "title": ["reg(ENSO SSTA, PRA) JJA", "reg(ENSO SSTA, PRA) JJA"],
            "varpattern": output_variables["EnsoPrMapJja"][12],
            "xname": "longitude",
            "yname": "latitude",
            "zname": "regression",
            "method": "1) N3.4 SST averaged\n2) Linearly detrended\n3) Seasonal cycle removed\n" +
                      "4) PRA regridded to 1°x1°\n5) JJA PRA regressed onto JJA N3.4 SSTA\n6) Mask ocean",
        },
        "dive_down09": {
            "plot_type": "map",
            "nbr_panel": 4,
            "colorbar": dict_colorbar["anomalies"],
            "label": dict_label["SKEW"],
            "maskland": False,
            "maskocean": True,
            "title": ["La Nina PRA JJA", "El Nino PRA JJA"],
            "varpattern": output_variables["EnsoPrMapJja"][13:15],
            "xname": "longitude",
            "yname": "latitude",
            "zname": "PRA",
            "method": "1) N3.4 SST averaged\n2) Linearly detrended\n3) Seasonal cycle removed\n" +
                      "4) Detect El Nino and La Nina\n    (NDJ N3.4 SSTA > 0.5 STD 5 cons. seasons)\n" +
                      "5) PRA regridded to 1°x1°\n6) El Nino and La Nina JJA PRA composited\n7) Mask ocean",
        },
        "dive_down10": {
            "plot_type": "map",
            "nbr_panel": 2,
            "colorbar": dict_colorbar["anomalies"],
            "label": dict_label["PRA"],
            "maskland": False,
            "maskocean": True,
            "title": ["reg(ENSO SSTA, PRA) JJA", "reg(ENSO SSTA, PRA) JJA"],
            "varpattern": output_variables["EnsoPrMapJja"][15],
            "xname": "longitude",
            "yname": "latitude",
            "zname": "regression",
            "method": "1) N3.4 SST averaged\n2) Linearly detrended\n3) Seasonal cycle removed\n" +
                      "4) PRA regridded to 1°x1°\n5) JJA PRA regressed onto JJA N3.4 SSTA\n6) Mask ocean",
        },
        "dive_down11": {
            "plot_type": "map",
            "nbr_panel": 4,
            "colorbar": dict_colorbar["anomalies"],
            "label": dict_label["SKEW"],
            "maskland": False,
            "maskocean": True,
            "title": ["La Nina PRA JJA", "El Nino PRA JJA"],
            "varpattern": output_variables["EnsoPrMapJja"][16:],
            "xname": "longitude",
            "yname": "latitude",
            "zname": "PRA",
            "method": "1) N3.4 SST averaged\n2) Linearly detrended\n3) Seasonal cycle removed\n" +
                      "4) Detect El Nino and La Nina\n    (NDJ N3.4 SSTA > 0.5 STD 5 cons. seasons)\n" +
                      "5) PRA regridded to 1°x1°\n6) El Nino and La Nina JJA PRA composited\n7) Mask ocean",
        },
    },
    "EnsoPrLonRmse": {
        "diagnostic": {
            "plot_type": "curve",
            "nbr_panel": 1,
            "title": "ENSO's PRA pattern",
            "varpattern": output_variables["EnsoPrLonRmse"][0],
            "xname": "longitude",
            "yname": "reg(ENSO SSTA, PRA)",
            "method": "1) N3.4 SST averaged\n2) Linearly detrended\n3) Seasonal cycle removed\n" +
                      "4) PRA regridded to 1°x1°\n5) 5S-5N meridional PRA averaged\n" +
                      "6) NDJ PRA regressed onto NDJ N3.4 SSTA\n\nMetric: RMSE$_x$",
        },
        "dive_down01": {
            "plot_type": "curve",
            "nbr_panel": 1,
            "title": "ENSO's PRA pattern",
            "varpattern": output_variables["EnsoPrLonRmse"][1:3],
            "colors": {"model": ["blue", "red"], "reference": ["blue", "red"]},
            "linestyles": {"model": ["-", "-"], "reference": ["-.", "-."]},
            "legend": ["La Nina", "El Nino"],
            "xname": "longitude",
            "yname": "ENSO PRA",
            "method": "1) N3.4 SST averaged\n2) Linearly detrended\n3) Seasonal cycle removed\n" +
                      "4) Detect El Nino and La Nina\n    (NDJ N3.4 SSTA > 0.5 STD 5 cons. seasons)\n" +
                      "5) PRA regridded to 1°x1°\n6) 5S-5N meridional PRA averaged\n" +
                      "7) El Nino and La Nina NDJ PRA composited",
        },
        "dive_down02": {
            "plot_type": "map",
            "nbr_panel": 2,
            "colorbar": dict_colorbar["anomalies"],
            "label": dict_label["REG3"],
            "maskland": True,
            "title": ["reg(ENSO SSTA, PRA)", "reg(ENSO SSTA, PRA)"],
            "varpattern": output_variables["EnsoPrLonRmse"][3],
            "xname": "longitude",
            "yname": "latitude",
            "zname": "regression",
            "method": "1) N3.4 SST averaged\n2) Linearly detrended\n3) Seasonal cycle removed\n" +
                      "4) PRA regridded to 1°x1°\n5) NDJ PRA regressed onto NDJ N3.4 SSTA",
        },
        "dive_down03": {
            "plot_type": "map",
            "nbr_panel": 4,
            "colorbar": dict_colorbar["anomalies"],
            "label": dict_label["REG3"],
            "maskland": True,
            "title": ["La Nina PRA", "El Nino PRA"],
            "varpattern": output_variables["EnsoPrLonRmse"][4:],
            "xname": "longitude",
            "yname": "latitude",
            "zname": "PRA",
            "method": "1) N3.4 SST averaged\n2) Linearly detrended\n3) Seasonal cycle removed\n" +
                      "4) Detect El Nino and La Nina\n    (NDJ N3.4 SSTA > 0.5 STD 5 cons. seasons)\n" +
                      "5) PRA regridded to 1°x1°\n6) El Nino and La Nina NDJ PRA composited",
        },
    },
    "EnsoPrTsRmse": {
        "diagnostic": {
            "plot_type": "curve",
            "nbr_panel": 1,
            "title": "ENSO's PRA life-cycle",
            "varpattern": output_variables["EnsoPrTsRmse"][0],
            "xname": "months",
            "yname": "reg(ENSO SSTA, PRA)",
            "method": "1) Horizontal averaged\n2) Linearly detrended\n3) Seasonal cycle removed\n" +
                      "4) REGION1 PRA regressed onto NDJ N3.4 SSTA\n\nMetric: RMSE$_{t}$",
        },
        "dive_down01": {
            "plot_type": "curve",
            "nbr_panel": 1,
            "title": "ENSO's PRA life-cycle",
            "varpattern": output_variables["EnsoPrTsRmse"][1:3],
            "colors": {"model": ["blue", "red"], "reference": ["blue", "red"]},
            "linestyles": {"model": ["-", "-"], "reference": ["-.", "-."]},
            "legend": ["La Nina", "El Nino"],
            "xname": "months",
            "yname": "ENSO PRA",
            "method": "1) Horizontal averaged\n2) Linearly detrended\n3) Seasonal cycle removed\n" +
                      "4) Detect El Nino and La Nina\n    (NDJ N3.4 SSTA > 0.5 STD 5 cons. seasons)\n" +
                      "5) El Nino and La Nina PRA composited",
        },
        "dive_down02": {
            "plot_type": "hovmoeller",
            "nbr_panel": 2,
            "colorbar": dict_colorbar["anomalies"],
            "label": dict_label["REG3"],
            "title": ["reg(ENSO SSTA, PRA)", "reg(ENSO SSTA, PRA)"],
            "varpattern": output_variables["EnsoPrTsRmse"][3],
            "xname": "longitude",
            "yname": "months",
            "zname": "regression",
            "method": "1) N3.4 SST averaged\n2) Linearly detrended\n3) Seasonal cycle removed\n" +
                      "4) PRA regridded to 1°x1°\n5) 5S-5N meridional PRA average\n" +
                      "6) NDJ PRA regressed onto NDJ N3.4 SSTA",
        },
        "dive_down03": {
            "plot_type": "hovmoeller",
            "nbr_panel": 4,
            "colorbar": dict_colorbar["anomalies"],
            "label": dict_label["REG5"],
            "title": ["La Nina PRA", "El Nino PRA"],
            "varpattern": output_variables["EnsoPrTsRmse"][4:],
            "xname": "longitude",
            "yname": "months",
            "zname": "PRA",
            "method": "1) N3.4 SST averaged\n2) Linearly detrended\n3) Seasonal cycle removed\n" +
                      "4) Detect El Nino and La Nina\n    (NDJ N3.4 SSTA > 0.5 STD 5 cons. seasons)\n" +
                      "5) PRA regridded to 1°x1°\n6) 5S-5N meridional PRA average\n" +
                      "7) El Nino and La Nina PRA composited",
        },
    },
    "EnsoSlpMap": {
        "diagnostic": {
            "plot_type": "map",
            "nbr_panel": 2,
            "colorbar": dict_colorbar["anomalies"],
            "label": dict_label["REG2"],
            "maskland": False,
            "title": ["reg(ENSO SSTA, SLPA)", "reg(ENSO SSTA, SLPA)"],
            "varpattern": output_variables["EnsoSlpMap"][0],
            "xname": "longitude",
            "yname": "latitude",
            "zname": "regression",
            "method": "1) N3.4 SST averaged\n2) Linearly detrended\n3) Seasonal cycle removed\n" +
                      "4) 5-month triangular running ave.\n5) SLPA regridded to 1°x1°\n" +
                      "6) Dec. SLPA regressed onto Dec. N3.4 SSTA\n7) Equatorial Pacific masked\n\nMetric: RMSE$_{xy}$",
        },
        "dive_down01": {
            "plot_type": "map",
            "nbr_panel": 2,
            "colorbar": dict_colorbar["anomalies"],
            "label": dict_label["REG2"],
            "maskland": False,
            "maskocean": True,
            "title": ["reg(ENSO SSTA, SLPA)", "reg(ENSO SSTA, SLPA)"],
            "varpattern": output_variables["EnsoSlpMap"][1],
            "xname": "longitude",
            "yname": "latitude",
            "zname": "regression",
            "method": "1) N3.4 SST averaged\n2) Linearly detrended\n3) Seasonal cycle removed\n" +
                      "4) 5-month triangular running ave.\n5) SLPA regridded to 1°x1°\n" +
                      "6) Dec. SLPA regressed onto Dec. N3.4 SSTA\n7) Mask ocean",
        },
        "dive_down02": {
            "plot_type": "map",
            "nbr_panel": 2,
            "colorbar": dict_colorbar["anomalies"],
            "label": dict_label["REG2"],
            "maskland": False,
            "maskocean": True,
            "title": ["reg(ENSO SSTA, SLPA)", "reg(ENSO SSTA, SLPA)"],
            "varpattern": output_variables["EnsoSlpMap"][2],
            "xname": "longitude",
            "yname": "latitude",
            "zname": "regression",
            "method": "1) N3.4 SST averaged\n2) Linearly detrended\n3) Seasonal cycle removed\n" +
                      "4) 5-month triangular running ave.\n5) SLPA regridded to 1°x1°\n" +
                      "6) Dec. SLPA regressed onto Dec. N3.4 SSTA\n7) Mask ocean",
        },
        "dive_down03": {
            "plot_type": "map",
            "nbr_panel": 2,
            "colorbar": dict_colorbar["anomalies"],
            "label": dict_label["REG2"],
            "maskland": False,
            "maskocean": True,
            "title": ["reg(ENSO SSTA, SLPA)", "reg(ENSO SSTA, SLPA)"],
            "varpattern": output_variables["EnsoSlpMap"][3],
            "xname": "longitude",
            "yname": "latitude",
            "zname": "regression",
            "method": "1) N3.4 SST averaged\n2) Linearly detrended\n3) Seasonal cycle removed\n" +
                      "4) 5-month triangular running ave.\n5) SLPA regridded to 1°x1°\n" +
                      "6) Dec. SLPA regressed onto Dec. N3.4 SSTA\n7) Mask ocean",
        },
        "dive_down04": {
            "plot_type": "map",
            "nbr_panel": 2,
            "colorbar": dict_colorbar["anomalies"],
            "label": dict_label["REG2"],
            "maskland": False,
            "maskocean": True,
            "title": ["reg(ENSO SSTA, SLPA)", "reg(ENSO SSTA, SLPA)"],
            "varpattern": output_variables["EnsoSlpMap"][4],
            "xname": "longitude",
            "yname": "latitude",
            "zname": "regression",
            "method": "1) N3.4 SST averaged\n2) Linearly detrended\n3) Seasonal cycle removed\n" +
                      "4) 5-month triangular running ave.\n5) SLPA regridded to 1°x1°\n" +
                      "6) Dec. SLPA regressed onto Dec. N3.4 SSTA\n7) Mask ocean",
        },
        "dive_down05": {
            "plot_type": "map",
            "nbr_panel": 2,
            "colorbar": dict_colorbar["anomalies"],
            "label": dict_label["REG2"],
            "maskland": False,
            "maskocean": True,
            "title": ["reg(ENSO SSTA, SLPA)", "reg(ENSO SSTA, SLPA)"],
            "varpattern": output_variables["EnsoSlpMap"][5],
            "xname": "longitude",
            "yname": "latitude",
            "zname": "regression",
            "method": "1) N3.4 SST averaged\n2) Linearly detrended\n3) Seasonal cycle removed\n" +
                      "4) 5-month triangular running ave.\n5) SLPA regridded to 1°x1°\n" +
                      "6) Dec. SLPA regressed onto Dec. N3.4 SSTA\n7) Mask ocean",
        },
    },
    "EnsoSlpMapDjf": {
        "diagnostic": {
            "plot_type": "map",
            "nbr_panel": 2,
            "colorbar": dict_colorbar["anomalies"],
            "label": dict_label["REG2"],
            "maskland": False,
            "title": ["reg(ENSO SSTA, SLPA) DJF", "reg(ENSO SSTA, SLPA) DJF"],
            "varpattern": output_variables["EnsoSlpMapDjf"][0],
            "xname": "longitude",
            "yname": "latitude",
            "zname": "regression",
            "method": "1) N3.4 SST averaged\n2) Linearly detrended\n3) Seasonal cycle removed\n" +
                      "4) SLPA regridded to 1°x1°\n5) DJF SLPA regressed onto DJF N3.4 SSTA\n" +
                      "6) Equatorial Pacific masked\n\nMetric: RMSE$_{xy}$",
        },
        "dive_down01": {
            "plot_type": "map",
            "nbr_panel": 4,
            "colorbar": dict_colorbar["anomalies"],
            "label": dict_label["REG3"],
            "maskland": False,
            "title": ["La Nina SLPA DJF", "El Nino SLPA DJF"],
            "varpattern": output_variables["EnsoSlpMapDjf"][1:3],
            "xname": "longitude",
            "yname": "latitude",
            "zname": "SLPA",
            "method": "1) N3.4 SST averaged\n2) Linearly detrended\n3) Seasonal cycle removed\n" +
                      "4) Detect El Nino and La Nina\n    (NDJ N3.4 SSTA > 0.5 STD 5 cons. seasons)\n" +
                      "5) SLPA regridded to 1°x1°\n6) El Nino and La Nina DJF SLPA composited\n" +
                      "6) Equatorial Pacific masked",
        },
        # ["africaSE", "americaN", "americaS", "asiaS", "oceania"]
        "dive_down02": {
            "plot_type": "map",
            "nbr_panel": 2,
            "colorbar": dict_colorbar["anomalies"],
            "label": dict_label["REG2"],
            "maskland": False,
            "maskocean": True,
            "title": ["reg(ENSO SSTA, SLPA) DJF", "reg(ENSO SSTA, SLPA) DJF"],
            "varpattern": output_variables["EnsoSlpMapDjf"][3],
            "xname": "longitude",
            "yname": "latitude",
            "zname": "regression",
            "method": "1) N3.4 SST averaged\n2) Linearly detrended\n3) Seasonal cycle removed\n" +
                      "4) SLPA regridded to 1°x1°\n5) DJF SLPA regressed onto DJF N3.4 SSTA\n6) Mask ocean",
        },
        "dive_down03": {
            "plot_type": "map",
            "nbr_panel": 4,
            "colorbar": dict_colorbar["anomalies"],
            "label": dict_label["REG3"],
            "maskland": False,
            "maskocean": True,
            "title": ["La Nina SLPA DJF", "El Nino SLPA DJF"],
            "varpattern": output_variables["EnsoSlpMapDjf"][4:6],
            "xname": "longitude",
            "yname": "latitude",
            "zname": "SLPA",
            "method": "1) N3.4 SST averaged\n2) Linearly detrended\n3) Seasonal cycle removed\n" +
                      "4) Detect El Nino and La Nina\n    (NDJ N3.4 SSTA > 0.5 STD 5 cons. seasons)\n" +
                      "5) SLPA regridded to 1°x1°\n6) El Nino and La Nina DJF SLPA composited\n7) Mask ocean",
        },
        "dive_down04": {
            "plot_type": "map",
            "nbr_panel": 2,
            "colorbar": dict_colorbar["anomalies"],
            "label": dict_label["REG2"],
            "maskland": False,
            "maskocean": True,
            "title": ["reg(ENSO SSTA, SLPA) DJF", "reg(ENSO SSTA, SLPA) DJF"],
            "varpattern": output_variables["EnsoSlpMapDjf"][6],
            "xname": "longitude",
            "yname": "latitude",
            "zname": "regression",
            "method": "1) N3.4 SST averaged\n2) Linearly detrended\n3) Seasonal cycle removed\n" +
                      "4) SLPA regridded to 1°x1°\n5) DJF SLPA regressed onto DJF N3.4 SSTA\n6) Mask ocean",
        },
        "dive_down05": {
            "plot_type": "map",
            "nbr_panel": 4,
            "colorbar": dict_colorbar["anomalies"],
            "label": dict_label["REG3"],
            "maskland": False,
            "maskocean": True,
            "title": ["La Nina SLPA DJF", "El Nino SLPA DJF"],
            "varpattern": output_variables["EnsoSlpMapDjf"][7:9],
            "xname": "longitude",
            "yname": "latitude",
            "zname": "SLPA",
            "method": "1) N3.4 SST averaged\n2) Linearly detrended\n3) Seasonal cycle removed\n" +
                      "4) Detect El Nino and La Nina\n    (NDJ N3.4 SSTA > 0.5 STD 5 cons. seasons)\n" +
                      "5) SLPA regridded to 1°x1°\n6) El Nino and La Nina DJF SLPA composited\n7) Mask ocean",
        },
        "dive_down06": {
            "plot_type": "map",
            "nbr_panel": 2,
            "colorbar": dict_colorbar["anomalies"],
            "label": dict_label["REG2"],
            "maskland": False,
            "maskocean": True,
            "title": ["reg(ENSO SSTA, SLPA) DJF", "reg(ENSO SSTA, SLPA) DJF"],
            "varpattern": output_variables["EnsoSlpMapDjf"][9],
            "xname": "longitude",
            "yname": "latitude",
            "zname": "regression",
            "method": "1) N3.4 SST averaged\n2) Linearly detrended\n3) Seasonal cycle removed\n" +
                      "4) SLPA regridded to 1°x1°\n5) DJF SLPA regressed onto DJF N3.4 SSTA\n6) Mask ocean",
        },
        "dive_down07": {
            "plot_type": "map",
            "nbr_panel": 4,
            "colorbar": dict_colorbar["anomalies"],
            "label": dict_label["REG3"],
            "maskland": False,
            "maskocean": True,
            "title": ["La Nina SLPA DJF", "El Nino SLPA DJF"],
            "varpattern": output_variables["EnsoSlpMapDjf"][10:12],
            "xname": "longitude",
            "yname": "latitude",
            "zname": "SLPA",
            "method": "1) N3.4 SST averaged\n2) Linearly detrended\n3) Seasonal cycle removed\n" +
                      "4) Detect El Nino and La Nina\n    (NDJ N3.4 SSTA > 0.5 STD 5 cons. seasons)\n" +
                      "5) SLPA regridded to 1°x1°\n6) El Nino and La Nina DJF SLPA composited\n7) Mask ocean",
        },
        "dive_down08": {
            "plot_type": "map",
            "nbr_panel": 2,
            "colorbar": dict_colorbar["anomalies"],
            "label": dict_label["REG2"],
            "maskland": False,
            "maskocean": True,
            "title": ["reg(ENSO SSTA, SLPA) DJF", "reg(ENSO SSTA, SLPA) DJF"],
            "varpattern": output_variables["EnsoSlpMapDjf"][12],
            "xname": "longitude",
            "yname": "latitude",
            "zname": "regression",
            "method": "1) N3.4 SST averaged\n2) Linearly detrended\n3) Seasonal cycle removed\n" +
                      "4) SLPA regridded to 1°x1°\n5) DJF SLPA regressed onto DJF N3.4 SSTA\n6) Mask ocean",
        },
        "dive_down09": {
            "plot_type": "map",
            "nbr_panel": 4,
            "colorbar": dict_colorbar["anomalies"],
            "label": dict_label["REG3"],
            "maskland": False,
            "maskocean": True,
            "title": ["La Nina SLPA DJF", "El Nino SLPA DJF"],
            "varpattern": output_variables["EnsoSlpMapDjf"][13:15],
            "xname": "longitude",
            "yname": "latitude",
            "zname": "SLPA",
            "method": "1) N3.4 SST averaged\n2) Linearly detrended\n3) Seasonal cycle removed\n" +
                      "4) Detect El Nino and La Nina\n    (NDJ N3.4 SSTA > 0.5 STD 5 cons. seasons)\n" +
                      "5) SLPA regridded to 1°x1°\n6) El Nino and La Nina DJF SLPA composited\n7) Mask ocean",
        },
        "dive_down10": {
            "plot_type": "map",
            "nbr_panel": 2,
            "colorbar": dict_colorbar["anomalies"],
            "label": dict_label["REG2"],
            "maskland": False,
            "maskocean": True,
            "title": ["reg(ENSO SSTA, SLPA) DJF", "reg(ENSO SSTA, SLPA) DJF"],
            "varpattern": output_variables["EnsoSlpMapDjf"][15],
            "xname": "longitude",
            "yname": "latitude",
            "zname": "regression",
            "method": "1) N3.4 SST averaged\n2) Linearly detrended\n3) Seasonal cycle removed\n" +
                      "4) SLPA regridded to 1°x1°\n5) DJF SLPA regressed onto DJF N3.4 SSTA\n6) Mask ocean",
        },
        "dive_down11": {
            "plot_type": "map",
            "nbr_panel": 4,
            "colorbar": dict_colorbar["anomalies"],
            "label": dict_label["REG3"],
            "maskland": False,
            "maskocean": True,
            "title": ["La Nina SLPA DJF", "El Nino SLPA DJF"],
            "varpattern": output_variables["EnsoSlpMapDjf"][16:],
            "xname": "longitude",
            "yname": "latitude",
            "zname": "SLPA",
            "method": "1) N3.4 SST averaged\n2) Linearly detrended\n3) Seasonal cycle removed\n" +
                      "4) Detect El Nino and La Nina\n    (NDJ N3.4 SSTA > 0.5 STD 5 cons. seasons)\n" +
                      "5) SLPA regridded to 1°x1°\n6) El Nino and La Nina DJF SLPA composited\n7) Mask ocean",
        },
    },
    "EnsoSlpMapJja": {
        "diagnostic": {
            "plot_type": "map",
            "nbr_panel": 2,
            "colorbar": dict_colorbar["anomalies"],
            "label": dict_label["REG2"],
            "maskland": False,
            "title": ["reg(ENSO SSTA, SLPA) JJA", "reg(ENSO SSTA, SLPA) JJA"],
            "varpattern": output_variables["EnsoSlpMapJja"][0],
            "xname": "longitude",
            "yname": "latitude",
            "zname": "regression",
            "method": "1) N3.4 SST averaged\n2) Linearly detrended\n3) Seasonal cycle removed\n" +
                      "4) SLPA regridded to 1°x1°\n5) JJA SLPA regressed onto JJA N3.4 SSTA\n" +
                      "6) Equatorial Pacific masked\n\nMetric: RMSE$_{xy}$",
        },
        "dive_down01": {
            "plot_type": "map",
            "nbr_panel": 4,
            "colorbar": dict_colorbar["anomalies"],
            "label": dict_label["REG2"],
            "maskland": False,
            "title": ["La Nina SLPA JJA", "El Nino SLPA JJA"],
            "varpattern": output_variables["EnsoSlpMapJja"][1:3],
            "xname": "longitude",
            "yname": "latitude",
            "zname": "SLPA",
            "method": "1) N3.4 SST averaged\n2) Linearly detrended\n3) Seasonal cycle removed\n" +
                      "4) Detect El Nino and La Nina\n    (NDJ N3.4 SSTA > 0.5 STD 5 cons. seasons)\n" +
                      "5) SLPA regridded to 1°x1°\n6) El Nino and La Nina JJA SLPA composited\n" +
                      "6) Equatorial Pacific masked",
        },
        # ["africaSE", "americaN", "americaS", "asiaS", "oceania"]
        "dive_down02": {
            "plot_type": "map",
            "nbr_panel": 2,
            "colorbar": dict_colorbar["anomalies"],
            "label": dict_label["REG2"],
            "maskland": False,
            "maskocean": True,
            "title": ["reg(ENSO SSTA, SLPA) JJA", "reg(ENSO SSTA, SLPA) JJA"],
            "varpattern": output_variables["EnsoSlpMapJja"][3],
            "xname": "longitude",
            "yname": "latitude",
            "zname": "regression",
            "method": "1) N3.4 SST averaged\n2) Linearly detrended\n3) Seasonal cycle removed\n" +
                      "4) SLPA regridded to 1°x1°\n5) JJA SLPA regressed onto JJA N3.4 SSTA\n6) Mask ocean",
        },
        "dive_down03": {
            "plot_type": "map",
            "nbr_panel": 4,
            "colorbar": dict_colorbar["anomalies"],
            "label": dict_label["REG2"],
            "maskland": False,
            "maskocean": True,
            "title": ["La Nina SLPA JJA", "El Nino SLPA JJA"],
            "varpattern": output_variables["EnsoSlpMapJja"][4:6],
            "xname": "longitude",
            "yname": "latitude",
            "zname": "SLPA",
            "method": "1) N3.4 SST averaged\n2) Linearly detrended\n3) Seasonal cycle removed\n" +
                      "4) Detect El Nino and La Nina\n    (NDJ N3.4 SSTA > 0.5 STD 5 cons. seasons)\n" +
                      "5) SLPA regridded to 1°x1°\n6) El Nino and La Nina JJA SLPA composited\n7) Mask ocean",
        },
        "dive_down04": {
            "plot_type": "map",
            "nbr_panel": 2,
            "colorbar": dict_colorbar["anomalies"],
            "label": dict_label["REG2"],
            "maskland": False,
            "maskocean": True,
            "title": ["reg(ENSO SSTA, SLPA) JJA", "reg(ENSO SSTA, SLPA) JJA"],
            "varpattern": output_variables["EnsoSlpMapJja"][6],
            "xname": "longitude",
            "yname": "latitude",
            "zname": "regression",
            "method": "1) N3.4 SST averaged\n2) Linearly detrended\n3) Seasonal cycle removed\n" +
                      "4) SLPA regridded to 1°x1°\n5) JJA SLPA regressed onto JJA N3.4 SSTA\n6) Mask ocean",
        },
        "dive_down05": {
            "plot_type": "map",
            "nbr_panel": 4,
            "colorbar": dict_colorbar["anomalies"],
            "label": dict_label["REG2"],
            "maskland": False,
            "maskocean": True,
            "title": ["La Nina SLPA JJA", "El Nino SLPA JJA"],
            "varpattern": output_variables["EnsoSlpMapJja"][7:9],
            "xname": "longitude",
            "yname": "latitude",
            "zname": "SLPA",
            "method": "1) N3.4 SST averaged\n2) Linearly detrended\n3) Seasonal cycle removed\n" +
                      "4) Detect El Nino and La Nina\n    (NDJ N3.4 SSTA > 0.5 STD 5 cons. seasons)\n" +
                      "5) SLPA regridded to 1°x1°\n6) El Nino and La Nina JJA SLPA composited\n7) Mask ocean",
        },
        "dive_down06": {
            "plot_type": "map",
            "nbr_panel": 2,
            "colorbar": dict_colorbar["anomalies"],
            "label": dict_label["REG2"],
            "maskland": False,
            "maskocean": True,
            "title": ["reg(ENSO SSTA, SLPA) JJA", "reg(ENSO SSTA, SLPA) JJA"],
            "varpattern": output_variables["EnsoSlpMapJja"][9],
            "xname": "longitude",
            "yname": "latitude",
            "zname": "regression",
            "method": "1) N3.4 SST averaged\n2) Linearly detrended\n3) Seasonal cycle removed\n" +
                      "4) SLPA regridded to 1°x1°\n5) JJA SLPA regressed onto JJA N3.4 SSTA\n6) Mask ocean",
        },
        "dive_down07": {
            "plot_type": "map",
            "nbr_panel": 4,
            "colorbar": dict_colorbar["anomalies"],
            "label": dict_label["REG2"],
            "maskland": False,
            "maskocean": True,
            "title": ["La Nina SLPA JJA", "El Nino SLPA JJA"],
            "varpattern": output_variables["EnsoSlpMapJja"][10:12],
            "xname": "longitude",
            "yname": "latitude",
            "zname": "SLPA",
            "method": "1) N3.4 SST averaged\n2) Linearly detrended\n3) Seasonal cycle removed\n" +
                      "4) Detect El Nino and La Nina\n    (NDJ N3.4 SSTA > 0.5 STD 5 cons. seasons)\n" +
                      "5) SLPA regridded to 1°x1°\n6) El Nino and La Nina JJA SLPA composited\n7) Mask ocean",
        },
        "dive_down08": {
            "plot_type": "map",
            "nbr_panel": 2,
            "colorbar": dict_colorbar["anomalies"],
            "label": dict_label["REG2"],
            "maskland": False,
            "maskocean": True,
            "title": ["reg(ENSO SSTA, SLPA) JJA", "reg(ENSO SSTA, SLPA) JJA"],
            "varpattern": output_variables["EnsoSlpMapJja"][12],
            "xname": "longitude",
            "yname": "latitude",
            "zname": "regression",
            "method": "1) N3.4 SST averaged\n2) Linearly detrended\n3) Seasonal cycle removed\n" +
                      "4) SLPA regridded to 1°x1°\n5) JJA SLPA regressed onto JJA N3.4 SSTA\n6) Mask ocean",
        },
        "dive_down09": {
            "plot_type": "map",
            "nbr_panel": 4,
            "colorbar": dict_colorbar["anomalies"],
            "label": dict_label["REG2"],
            "maskland": False,
            "maskocean": True,
            "title": ["La Nina SLPA JJA", "El Nino SLPA JJA"],
            "varpattern": output_variables["EnsoSlpMapJja"][13:15],
            "xname": "longitude",
            "yname": "latitude",
            "zname": "SLPA",
            "method": "1) N3.4 SST averaged\n2) Linearly detrended\n3) Seasonal cycle removed\n" +
                      "4) Detect El Nino and La Nina\n    (NDJ N3.4 SSTA > 0.5 STD 5 cons. seasons)\n" +
                      "5) SLPA regridded to 1°x1°\n6) El Nino and La Nina JJA SLPA composited\n7) Mask ocean",
        },
        "dive_down10": {
            "plot_type": "map",
            "nbr_panel": 2,
            "colorbar": dict_colorbar["anomalies"],
            "label": dict_label["REG2"],
            "maskland": False,
            "maskocean": True,
            "title": ["reg(ENSO SSTA, SLPA) JJA", "reg(ENSO SSTA, SLPA) JJA"],
            "varpattern": output_variables["EnsoSlpMapJja"][15],
            "xname": "longitude",
            "yname": "latitude",
            "zname": "regression",
            "method": "1) N3.4 SST averaged\n2) Linearly detrended\n3) Seasonal cycle removed\n" +
                      "4) SLPA regridded to 1°x1°\n5) JJA SLPA regressed onto JJA N3.4 SSTA\n6) Mask ocean",
        },
        "dive_down11": {
            "plot_type": "map",
            "nbr_panel": 4,
            "colorbar": dict_colorbar["anomalies"],
            "label": dict_label["REG2"],
            "maskland": False,
            "maskocean": True,
            "title": ["La Nina SLPA JJA", "El Nino SLPA JJA"],
            "varpattern": output_variables["EnsoSlpMapJja"][16:],
            "xname": "longitude",
            "yname": "latitude",
            "zname": "SLPA",
            "method": "1) N3.4 SST averaged\n2) Linearly detrended\n3) Seasonal cycle removed\n" +
                      "4) Detect El Nino and La Nina\n    (NDJ N3.4 SSTA > 0.5 STD 5 cons. seasons)\n" +
                      "5) SLPA regridded to 1°x1°\n6) El Nino and La Nina JJA SLPA composited\n7) Mask ocean",
        },
    },
    "EnsoSshLonRmse": {
        "diagnostic": {
            "plot_type": "curve",
            "nbr_panel": 1,
            "title": "ENSO's SSHA pattern",
            "varpattern": output_variables["EnsoSshLonRmse"][0],
            "xname": "longitude",
            "yname": "reg(ENSO SSTA, SSHA)",
            "method": "1) N3.4 SST averaged\n2) Linearly detrended\n3) Seasonal cycle removed\n" +
                      "4) SSHA regridded to 1°x1°\n5) 5S-5N meridional SSHA averaged\n" +
                      "6) NDJ SSHA regressed onto NDJ N3.4 SSTA\n\nMetric: RMSE$_x$",
        },
        "dive_down01": {
            "plot_type": "curve",
            "nbr_panel": 1,
            "title": "ENSO's SSHA pattern",
            "varpattern": output_variables["EnsoSshLonRmse"][1:3],
            "colors": {"model": ["blue", "red"], "reference": ["blue", "red"]},
            "linestyles": {"model": ["-", "-"], "reference": ["-.", "-."]},
            "legend": ["La Nina", "El Nino"],
            "xname": "longitude",
            "yname": "ENSO SSHA",
            "method": "1) N3.4 SST averaged\n2) Linearly detrended\n3) Seasonal cycle removed\n" +
                      "4) Detect El Nino and La Nina\n    (NDJ N3.4 SSTA > 0.5 STD 5 cons. seasons)\n" +
                      "5) SSHA regridded to 1°x1°\n6) 5S-5N meridional SSHA averaged\n" +
                      "7) El Nino and La Nina NDJ SSHA composited",
        },
        "dive_down02": {
            "plot_type": "map",
            "nbr_panel": 2,
            "colorbar": dict_colorbar["anomalies"],
            "label": dict_label["REG30"],
            "maskland": True,
            "title": ["reg(ENSO SSTA, SSHA)", "reg(ENSO SSTA, SSHA)"],
            "varpattern": output_variables["EnsoSshLonRmse"][3],
            "xname": "longitude",
            "yname": "latitude",
            "zname": "regression",
            "method": "1) N3.4 SST averaged\n2) Linearly detrended\n3) Seasonal cycle removed\n" +
                      "4) SSHA regridded to 1°x1°\n5) NDJ SSHA regressed onto NDJ N3.4 SSTA",
        },
        "dive_down03": {
            "plot_type": "map",
            "nbr_panel": 4,
            "colorbar": dict_colorbar["anomalies"],
            "label": dict_label["REG30"],
            "maskland": True,
            "title": ["La Nina SSHA", "El Nino SSHA"],
            "varpattern": output_variables["EnsoSshLonRmse"][4:],
            "xname": "longitude",
            "yname": "latitude",
            "zname": "SSHA",
            "method": "1) N3.4 SST averaged\n2) Linearly detrended\n3) Seasonal cycle removed\n" +
                      "4) Detect El Nino and La Nina\n    (NDJ N3.4 SSTA > 0.5 STD 5 cons. seasons)\n" +
                      "5) SSHA regridded to 1°x1°\n6) El Nino and La Nina NDJ SSHA composited",
        },
    },
    "EnsoSshTsRmse": {
        "diagnostic": {
            "plot_type": "curve",
            "nbr_panel": 1,
            "title": "ENSO's SSHA life-cycle",
            "varpattern": output_variables["EnsoSshTsRmse"][0],
            "xname": "months",
            "yname": "reg(ENSO SSTA, SSHA)",
            "method": "1) Horizontal averaged\n2) Linearly detrended\n3) Seasonal cycle removed\n" +
                      "4) REGION1 SSHA regressed onto Dec. N3.4 SSTA\n\nMetric: RMSE$_{t}$",
        },
        "dive_down01": {
            "plot_type": "curve",
            "nbr_panel": 1,
            "title": "ENSO's SSHA life-cycle",
            "varpattern": output_variables["EnsoSshTsRmse"][1:3],
            "colors": {"model": ["blue", "red"], "reference": ["blue", "red"]},
            "linestyles": {"model": ["-", "-"], "reference": ["-.", "-."]},
            "legend": ["La Nina", "El Nino"],
            "xname": "months",
            "yname": "ENSO SSHA",
            "method": "1) Horizontal averaged\n2) Linearly detrended\n3) Seasonal cycle removed\n" +
                      "4) Detect El Nino and La Nina\n    (NDJ N3.4 SSTA > 0.5 STD 5 cons. seasons)\n" +
                      "5) El Nino and La Nina SSHA composited",
        },
        "dive_down02": {
            "plot_type": "hovmoeller",
            "nbr_panel": 2,
            "colorbar": dict_colorbar["anomalies"],
            "label": dict_label["REG20"],
            "title": ["reg(ENSO SSTA, SSHA)", "reg(ENSO SSTA, SSHA)"],
            "varpattern": output_variables["EnsoSshTsRmse"][3],
            "xname": "longitude",
            "yname": "months",
            "zname": "regression",
            "method": "1) N3.4 SST averaged\n2) Linearly detrended\n3) Seasonal cycle removed\n" +
                      "4) SSHA regridded to 1°x1°\n5) 5S-5N meridional SSHA average\n" +
                      "6) NDJ SSHA regressed onto NDJ N3.4 SSTA",
        },
        "dive_down03": {
            "plot_type": "hovmoeller",
            "nbr_panel": 4,
            "colorbar": dict_colorbar["anomalies"],
            "label": dict_label["REG30"],
            "title": ["La Nina SSHA", "El Nino SSHA"],
            "varpattern": output_variables["EnsoSshTsRmse"][4:],
            "xname": "longitude",
            "yname": "months",
            "zname": "SSHA",
            "method": "1) N3.4 SST averaged\n2) Linearly detrended\n3) Seasonal cycle removed\n" +
                      "4) Detect El Nino and La Nina\n    (NDJ N3.4 SSTA > 0.5 STD 5 cons. seasons)\n" +
                      "5) SSHA regridded to 1°x1°\n6) 5S-5N meridional SSHA average\n" +
                      "7) El Nino and La Nina SSHA composited",
        },
    },
    "EnsoSstMap": {
        "diagnostic": {
            "plot_type": "map",
            "nbr_panel": 2,
            "colorbar": dict_colorbar["anomalies"],
            "label": dict_label["PRA"],
            "maskland": False,
            "title": ["reg(ENSO SSTA, TASA)", "reg(ENSO SSTA, TASA)"],
            "varpattern": output_variables["EnsoSstMap"][0],
            "xname": "longitude",
            "yname": "latitude",
            "zname": "regression",
            "method": "1) N3.4 SST averaged\n2) Linearly detrended\n3) Seasonal cycle removed\n" +
                      "4) 5-month triangular running ave.\n5) TASA regridded to 1°x1°\n" +
                      "6) Dec. TASA regressed onto Dec. N3.4 SSTA\n7) Equatorial Pacific masked\n\nMetric: RMSE$_{xy}$",
        },
        "dive_down01": {
            "plot_type": "map",
            "nbr_panel": 2,
            "colorbar": dict_colorbar["anomalies"],
            "label": dict_label["PRA"],
            "maskland": False,
            "maskocean": True,
            "title": ["reg(ENSO SSTA, TASA)", "reg(ENSO SSTA, TASA)"],
            "varpattern": output_variables["EnsoSstMap"][1],
            "xname": "longitude",
            "yname": "latitude",
            "zname": "regression",
            "method": "1) N3.4 SST averaged\n2) Linearly detrended\n3) Seasonal cycle removed\n" +
                      "4) 5-month triangular running ave.\n5) TASA regridded to 1°x1°\n" +
                      "6) Dec. TASA regressed onto Dec. N3.4 SSTA\n7) Mask ocean",
        },
        "dive_down02": {
            "plot_type": "map",
            "nbr_panel": 2,
            "colorbar": dict_colorbar["anomalies"],
            "label": dict_label["PRA"],
            "maskland": False,
            "maskocean": True,
            "title": ["reg(ENSO SSTA, TASA)", "reg(ENSO SSTA, TASA)"],
            "varpattern": output_variables["EnsoSstMap"][2],
            "xname": "longitude",
            "yname": "latitude",
            "zname": "regression",
            "method": "1) N3.4 SST averaged\n2) Linearly detrended\n3) Seasonal cycle removed\n" +
                      "4) 5-month triangular running ave.\n5) TASA regridded to 1°x1°\n" +
                      "6) Dec. TASA regressed onto Dec. N3.4 SSTA\n7) Mask ocean",
        },
        "dive_down03": {
            "plot_type": "map",
            "nbr_panel": 2,
            "colorbar": dict_colorbar["anomalies"],
            "label": dict_label["PRA"],
            "maskland": False,
            "maskocean": True,
            "title": ["reg(ENSO SSTA, TASA)", "reg(ENSO SSTA, TASA)"],
            "varpattern": output_variables["EnsoSstMap"][3],
            "xname": "longitude",
            "yname": "latitude",
            "zname": "regression",
            "method": "1) N3.4 SST averaged\n2) Linearly detrended\n3) Seasonal cycle removed\n" +
                      "4) 5-month triangular running ave.\n5) TASA regridded to 1°x1°\n" +
                      "6) Dec. TASA regressed onto Dec. N3.4 SSTA\n7) Mask ocean",
        },
        "dive_down04": {
            "plot_type": "map",
            "nbr_panel": 2,
            "colorbar": dict_colorbar["anomalies"],
            "label": dict_label["PRA"],
            "maskland": False,
            "maskocean": True,
            "title": ["reg(ENSO SSTA, TASA)", "reg(ENSO SSTA, TASA)"],
            "varpattern": output_variables["EnsoSstMap"][4],
            "xname": "longitude",
            "yname": "latitude",
            "zname": "regression",
            "method": "1) N3.4 SST averaged\n2) Linearly detrended\n3) Seasonal cycle removed\n" +
                      "4) 5-month triangular running ave.\n5) TASA regridded to 1°x1°\n" +
                      "6) Dec. TASA regressed onto Dec. N3.4 SSTA\n7) Mask ocean",
        },
        "dive_down05": {
            "plot_type": "map",
            "nbr_panel": 2,
            "colorbar": dict_colorbar["anomalies"],
            "label": dict_label["PRA"],
            "maskland": False,
            "maskocean": True,
            "title": ["reg(ENSO SSTA, TASA)", "reg(ENSO SSTA, TASA)"],
            "varpattern": output_variables["EnsoSstMap"][5],
            "xname": "longitude",
            "yname": "latitude",
            "zname": "regression",
            "method": "1) N3.4 SST averaged\n2) Linearly detrended\n3) Seasonal cycle removed\n" +
                      "4) 5-month triangular running ave.\n5) TASA regridded to 1°x1°\n" +
                      "6) Dec. TASA regressed onto Dec. N3.4 SSTA\n7) Mask ocean",
        },
    },
    "EnsoSstMapDjf": {
        "diagnostic": {
            "plot_type": "map",
            "nbr_panel": 2,
            "colorbar": dict_colorbar["anomalies"],
            "label": dict_label["PRA"],
            "maskland": False,
            "title": ["reg(ENSO SSTA, TASA) DJF", "reg(ENSO SSTA, TASA) DJF"],
            "varpattern": output_variables["EnsoSstMapDjf"][0],
            "xname": "longitude",
            "yname": "latitude",
            "zname": "regression",
            "method": "1) N3.4 SST averaged\n2) Linearly detrended\n3) Seasonal cycle removed\n" +
                      "4) TASA regridded to 1°x1°\n5) DJF TASA regressed onto DJF N3.4 SSTA\n" +
                      "6) Equatorial Pacific masked\n\nMetric: RMSE$_{xy}$",
        },
        "dive_down01": {
            "plot_type": "map",
            "nbr_panel": 4,
            "colorbar": dict_colorbar["anomalies"],
            "label": dict_label["REG2"],
            "maskland": False,
            "title": ["La Nina TASA DJF", "El Nino TASA DJF"],
            "varpattern": output_variables["EnsoSstMapDjf"][1:3],
            "xname": "longitude",
            "yname": "latitude",
            "zname": "TASA",
            "method": "1) N3.4 SST averaged\n2) Linearly detrended\n3) Seasonal cycle removed\n" +
                      "4) Detect El Nino and La Nina\n    (NDJ N3.4 SSTA > 0.5 STD 5 cons. seasons)\n" +
                      "5) TASA regridded to 1°x1°\n6) El Nino and La Nina DJF TASA composited\n" +
                      "6) Equatorial Pacific masked",
        },
        # ["africaSE", "americaN", "americaS", "asiaS", "oceania"]
        "dive_down02": {
            "plot_type": "map",
            "nbr_panel": 2,
            "colorbar": dict_colorbar["anomalies"],
            "label": dict_label["PRA"],
            "maskland": False,
            "maskocean": True,
            "title": ["reg(ENSO SSTA, TASA) DJF", "reg(ENSO SSTA, TASA) DJF"],
            "varpattern": output_variables["EnsoSstMapDjf"][3],
            "xname": "longitude",
            "yname": "latitude",
            "zname": "regression",
            "method": "1) N3.4 SST averaged\n2) Linearly detrended\n3) Seasonal cycle removed\n" +
                      "4) TASA regridded to 1°x1°\n5) DJF TASA regressed onto DJF N3.4 SSTA\n6) Mask ocean",
        },
        "dive_down03": {
            "plot_type": "map",
            "nbr_panel": 4,
            "colorbar": dict_colorbar["anomalies"],
            "label": dict_label["REG2"],
            "maskland": False,
            "maskocean": True,
            "title": ["La Nina TASA DJF", "El Nino TASA DJF"],
            "varpattern": output_variables["EnsoSstMapDjf"][5:6],
            "xname": "longitude",
            "yname": "latitude",
            "zname": "TASA",
            "method": "1) N3.4 SST averaged\n2) Linearly detrended\n3) Seasonal cycle removed\n" +
                      "4) Detect El Nino and La Nina\n    (NDJ N3.4 SSTA > 0.5 STD 5 cons. seasons)\n" +
                      "5) TASA regridded to 1°x1°\n6) El Nino and La Nina DJF TASA composited\n7) Mask ocean",
        },
        "dive_down04": {
            "plot_type": "map",
            "nbr_panel": 2,
            "colorbar": dict_colorbar["anomalies"],
            "label": dict_label["PRA"],
            "maskland": False,
            "maskocean": True,
            "title": ["reg(ENSO SSTA, TASA) DJF", "reg(ENSO SSTA, TASA) DJF"],
            "varpattern": output_variables["EnsoSstMapDjf"][6],
            "xname": "longitude",
            "yname": "latitude",
            "zname": "regression",
            "method": "1) N3.4 SST averaged\n2) Linearly detrended\n3) Seasonal cycle removed\n" +
                      "4) TASA regridded to 1°x1°\n5) DJF TASA regressed onto DJF N3.4 SSTA\n6) Mask ocean",
        },
        "dive_down05": {
            "plot_type": "map",
            "nbr_panel": 4,
            "colorbar": dict_colorbar["anomalies"],
            "label": dict_label["REG2"],
            "maskland": False,
            "maskocean": True,
            "title": ["La Nina TASA DJF", "El Nino TASA DJF"],
            "varpattern": output_variables["EnsoSstMapDjf"][7:9],
            "xname": "longitude",
            "yname": "latitude",
            "zname": "TASA",
            "method": "1) N3.4 SST averaged\n2) Linearly detrended\n3) Seasonal cycle removed\n" +
                      "4) Detect El Nino and La Nina\n    (NDJ N3.4 SSTA > 0.5 STD 5 cons. seasons)\n" +
                      "5) TASA regridded to 1°x1°\n6) El Nino and La Nina DJF TASA composited\n7) Mask ocean",
        },
        "dive_down06": {
            "plot_type": "map",
            "nbr_panel": 2,
            "colorbar": dict_colorbar["anomalies"],
            "label": dict_label["PRA"],
            "maskland": False,
            "maskocean": True,
            "title": ["reg(ENSO SSTA, TASA) DJF", "reg(ENSO SSTA, TASA) DJF"],
            "varpattern": output_variables["EnsoSstMapDjf"][9],
            "xname": "longitude",
            "yname": "latitude",
            "zname": "regression",
            "method": "1) N3.4 SST averaged\n2) Linearly detrended\n3) Seasonal cycle removed\n" +
                      "4) TASA regridded to 1°x1°\n5) DJF TASA regressed onto DJF N3.4 SSTA\n6) Mask ocean",
        },
        "dive_down07": {
            "plot_type": "map",
            "nbr_panel": 4,
            "colorbar": dict_colorbar["anomalies"],
            "label": dict_label["REG2"],
            "maskland": False,
            "maskocean": True,
            "title": ["La Nina TASA DJF", "El Nino TASA DJF"],
            "varpattern": output_variables["EnsoSstMapDjf"][10:12],
            "xname": "longitude",
            "yname": "latitude",
            "zname": "TASA",
            "method": "1) N3.4 SST averaged\n2) Linearly detrended\n3) Seasonal cycle removed\n" +
                      "4) Detect El Nino and La Nina\n    (NDJ N3.4 SSTA > 0.5 STD 5 cons. seasons)\n" +
                      "5) TASA regridded to 1°x1°\n6) El Nino and La Nina DJF TASA composited\n7) Mask ocean",
        },
        "dive_down08": {
            "plot_type": "map",
            "nbr_panel": 2,
            "colorbar": dict_colorbar["anomalies"],
            "label": dict_label["PRA"],
            "maskland": False,
            "maskocean": True,
            "title": ["reg(ENSO SSTA, TASA) DJF", "reg(ENSO SSTA, TASA) DJF"],
            "varpattern": output_variables["EnsoSstMapDjf"][12],
            "xname": "longitude",
            "yname": "latitude",
            "zname": "regression",
            "method": "1) N3.4 SST averaged\n2) Linearly detrended\n3) Seasonal cycle removed\n" +
                      "4) TASA regridded to 1°x1°\n5) DJF TASA regressed onto DJF N3.4 SSTA\n6) Mask ocean",
        },
        "dive_down09": {
            "plot_type": "map",
            "nbr_panel": 4,
            "colorbar": dict_colorbar["anomalies"],
            "label": dict_label["REG2"],
            "maskland": False,
            "maskocean": True,
            "title": ["La Nina TASA DJF", "El Nino TASA DJF"],
            "varpattern": output_variables["EnsoSstMapDjf"][13:15],
            "xname": "longitude",
            "yname": "latitude",
            "zname": "TASA",
            "method": "1) N3.4 SST averaged\n2) Linearly detrended\n3) Seasonal cycle removed\n" +
                      "4) Detect El Nino and La Nina\n    (NDJ N3.4 SSTA > 0.5 STD 5 cons. seasons)\n" +
                      "5) TASA regridded to 1°x1°\n6) El Nino and La Nina DJF TASA composited\n7) Mask ocean",
        },
        "dive_down10": {
            "plot_type": "map",
            "nbr_panel": 2,
            "colorbar": dict_colorbar["anomalies"],
            "label": dict_label["PRA"],
            "maskland": False,
            "maskocean": True,
            "title": ["reg(ENSO SSTA, TASA) DJF", "reg(ENSO SSTA, TASA) DJF"],
            "varpattern": output_variables["EnsoSstMapDjf"][15],
            "xname": "longitude",
            "yname": "latitude",
            "zname": "regression",
            "method": "1) N3.4 SST averaged\n2) Linearly detrended\n3) Seasonal cycle removed\n" +
                      "4) TASA regridded to 1°x1°\n5) DJF TASA regressed onto DJF N3.4 SSTA\n6) Mask ocean",
        },
        "dive_down11": {
            "plot_type": "map",
            "nbr_panel": 4,
            "colorbar": dict_colorbar["anomalies"],
            "label": dict_label["REG2"],
            "maskland": False,
            "maskocean": True,
            "title": ["La Nina TASA DJF", "El Nino TASA DJF"],
            "varpattern": output_variables["EnsoSstMapDjf"][16:],
            "xname": "longitude",
            "yname": "latitude",
            "zname": "TASA",
            "method": "1) N3.4 SST averaged\n2) Linearly detrended\n3) Seasonal cycle removed\n" +
                      "4) Detect El Nino and La Nina\n    (NDJ N3.4 SSTA > 0.5 STD 5 cons. seasons)\n" +
                      "5) TASA regridded to 1°x1°\n6) El Nino and La Nina DJF TASA composited\n7) Mask ocean",
        },
    },
    "EnsoSstMapJja": {
        "diagnostic": {
            "plot_type": "map",
            "nbr_panel": 2,
            "colorbar": dict_colorbar["anomalies"],
            "label": dict_label["PRA"],
            "maskland": False,
            "title": ["reg(ENSO SSTA, TASA) JJA", "reg(ENSO SSTA, TASA) JJA"],
            "varpattern": output_variables["EnsoSstMapJja"][0],
            "xname": "longitude",
            "yname": "latitude",
            "zname": "regression",
            "method": "1) N3.4 SST averaged\n2) Linearly detrended\n3) Seasonal cycle removed\n" +
                      "4) TASA regridded to 1°x1°\n5) JJA TASA regressed onto JJA N3.4 SSTA\n" +
                      "6) Equatorial Pacific masked\n\nMetric: RMSE$_{xy}$",
        },
        "dive_down01": {
            "plot_type": "map",
            "nbr_panel": 4,
            "colorbar": dict_colorbar["anomalies"],
            "label": dict_label["PRA"],
            "maskland": False,
            "title": ["La Nina TASA JJA", "El Nino TASA JJA"],
            "varpattern": output_variables["EnsoSstMapJja"][1:3],
            "xname": "longitude",
            "yname": "latitude",
            "zname": "TASA",
            "method": "1) N3.4 SST averaged\n2) Linearly detrended\n3) Seasonal cycle removed\n" +
                      "4) Detect El Nino and La Nina\n    (NDJ N3.4 SSTA > 0.5 STD 5 cons. seasons)\n" +
                      "5) TASA regridded to 1°x1°\n6) El Nino and La Nina JJA TASA composited\n" +
                      "6) Equatorial Pacific masked",
        },
        "dive_down02": {
            "plot_type": "map",
            "nbr_panel": 2,
            "colorbar": dict_colorbar["anomalies"],
            "label": dict_label["PRA"],
            "maskland": False,
            "maskocean": True,
            "title": ["reg(ENSO SSTA, TASA) JJA", "reg(ENSO SSTA, TASA) JJA"],
            "varpattern": output_variables["EnsoSstMapJja"][3],
            "xname": "longitude",
            "yname": "latitude",
            "zname": "regression",
            "method": "1) N3.4 SST averaged\n2) Linearly detrended\n3) Seasonal cycle removed\n" +
                      "4) TASA regridded to 1°x1°\n5) JJA TASA regressed onto JJA N3.4 SSTA\n6) Mask ocean",
        },
        "dive_down03": {
            "plot_type": "map",
            "nbr_panel": 4,
            "colorbar": dict_colorbar["anomalies"],
            "label": dict_label["PRA"],
            "maskland": False,
            "maskocean": True,
            "title": ["La Nina TASA JJA", "El Nino TASA JJA"],
            "varpattern": output_variables["EnsoSstMapJja"][3:6],
            "xname": "longitude",
            "yname": "latitude",
            "zname": "TASA",
            "method": "1) N3.4 SST averaged\n2) Linearly detrended\n3) Seasonal cycle removed\n" +
                      "4) Detect El Nino and La Nina\n    (NDJ N3.4 SSTA > 0.5 STD 5 cons. seasons)\n" +
                      "5) TASA regridded to 1°x1°\n6) El Nino and La Nina JJA TASA composited\n7) Mask ocean",
        },
        "dive_down04": {
            "plot_type": "map",
            "nbr_panel": 2,
            "colorbar": dict_colorbar["anomalies"],
            "label": dict_label["PRA"],
            "maskland": False,
            "maskocean": True,
            "title": ["reg(ENSO SSTA, TASA) JJA", "reg(ENSO SSTA, TASA) JJA"],
            "varpattern": output_variables["EnsoSstMapJja"][6],
            "xname": "longitude",
            "yname": "latitude",
            "zname": "regression",
            "method": "1) N3.4 SST averaged\n2) Linearly detrended\n3) Seasonal cycle removed\n" +
                      "4) TASA regridded to 1°x1°\n5) JJA TASA regressed onto JJA N3.4 SSTA\n6) Mask ocean",
        },
        "dive_down05": {
            "plot_type": "map",
            "nbr_panel": 4,
            "colorbar": dict_colorbar["anomalies"],
            "label": dict_label["PRA"],
            "maskland": False,
            "maskocean": True,
            "title": ["La Nina TASA JJA", "El Nino TASA JJA"],
            "varpattern": output_variables["EnsoSstMapJja"][7:9],
            "xname": "longitude",
            "yname": "latitude",
            "zname": "TASA",
            "method": "1) N3.4 SST averaged\n2) Linearly detrended\n3) Seasonal cycle removed\n" +
                      "4) Detect El Nino and La Nina\n    (NDJ N3.4 SSTA > 0.5 STD 5 cons. seasons)\n" +
                      "5) TASA regridded to 1°x1°\n6) El Nino and La Nina JJA TASA composited\n7) Mask ocean",
        },
        "dive_down06": {
            "plot_type": "map",
            "nbr_panel": 2,
            "colorbar": dict_colorbar["anomalies"],
            "label": dict_label["PRA"],
            "maskland": False,
            "maskocean": True,
            "title": ["reg(ENSO SSTA, TASA) JJA", "reg(ENSO SSTA, TASA) JJA"],
            "varpattern": output_variables["EnsoSstMapJja"][9],
            "xname": "longitude",
            "yname": "latitude",
            "zname": "regression",
            "method": "1) N3.4 SST averaged\n2) Linearly detrended\n3) Seasonal cycle removed\n" +
                      "4) TASA regridded to 1°x1°\n5) JJA TASA regressed onto JJA N3.4 SSTA\n6) Mask ocean",
        },
        "dive_down07": {
            "plot_type": "map",
            "nbr_panel": 4,
            "colorbar": dict_colorbar["anomalies"],
            "label": dict_label["PRA"],
            "maskland": False,
            "maskocean": True,
            "title": ["La Nina TASA JJA", "El Nino TASA JJA"],
            "varpattern": output_variables["EnsoSstMapJja"][10:12],
            "xname": "longitude",
            "yname": "latitude",
            "zname": "TASA",
            "method": "1) N3.4 SST averaged\n2) Linearly detrended\n3) Seasonal cycle removed\n" +
                      "4) Detect El Nino and La Nina\n    (NDJ N3.4 SSTA > 0.5 STD 5 cons. seasons)\n" +
                      "5) TASA regridded to 1°x1°\n6) El Nino and La Nina JJA TASA composited\n7) Mask ocean",
        },
        "dive_down08": {
            "plot_type": "map",
            "nbr_panel": 2,
            "colorbar": dict_colorbar["anomalies"],
            "label": dict_label["PRA"],
            "maskland": False,
            "maskocean": True,
            "title": ["reg(ENSO SSTA, TASA) JJA", "reg(ENSO SSTA, TASA) JJA"],
            "varpattern": output_variables["EnsoSstMapJja"][12],
            "xname": "longitude",
            "yname": "latitude",
            "zname": "regression",
            "method": "1) N3.4 SST averaged\n2) Linearly detrended\n3) Seasonal cycle removed\n" +
                      "4) TASA regridded to 1°x1°\n5) JJA TASA regressed onto JJA N3.4 SSTA\n6) Mask ocean",
        },
        "dive_down09": {
            "plot_type": "map",
            "nbr_panel": 4,
            "colorbar": dict_colorbar["anomalies"],
            "label": dict_label["PRA"],
            "maskland": False,
            "maskocean": True,
            "title": ["La Nina TASA JJA", "El Nino TASA JJA"],
            "varpattern": output_variables["EnsoSstMapJja"][13:15],
            "xname": "longitude",
            "yname": "latitude",
            "zname": "TASA",
            "method": "1) N3.4 SST averaged\n2) Linearly detrended\n3) Seasonal cycle removed\n" +
                      "4) Detect El Nino and La Nina\n    (NDJ N3.4 SSTA > 0.5 STD 5 cons. seasons)\n" +
                      "5) TASA regridded to 1°x1°\n6) El Nino and La Nina JJA TASA composited\n7) Mask ocean",
        },
        "dive_down10": {
            "plot_type": "map",
            "nbr_panel": 2,
            "colorbar": dict_colorbar["anomalies"],
            "label": dict_label["PRA"],
            "maskland": False,
            "maskocean": True,
            "title": ["reg(ENSO SSTA, TASA) JJA", "reg(ENSO SSTA, TASA) JJA"],
            "varpattern": output_variables["EnsoSstMapJja"][15],
            "xname": "longitude",
            "yname": "latitude",
            "zname": "regression",
            "method": "1) N3.4 SST averaged\n2) Linearly detrended\n3) Seasonal cycle removed\n" +
                      "4) TASA regridded to 1°x1°\n5) JJA TASA regressed onto JJA N3.4 SSTA\n6) Mask ocean",
        },
        "dive_down11": {
            "plot_type": "map",
            "nbr_panel": 4,
            "colorbar": dict_colorbar["anomalies"],
            "label": dict_label["PRA"],
            "maskland": False,
            "maskocean": True,
            "title": ["La Nina TASA JJA", "El Nino TASA JJA"],
            "varpattern": output_variables["EnsoSstMapJja"][16:],
            "xname": "longitude",
            "yname": "latitude",
            "zname": "TASA",
            "method": "1) N3.4 SST averaged\n2) Linearly detrended\n3) Seasonal cycle removed\n" +
                      "4) Detect El Nino and La Nina\n    (NDJ N3.4 SSTA > 0.5 STD 5 cons. seasons)\n" +
                      "5) TASA regridded to 1°x1°\n6) El Nino and La Nina JJA TASA composited\n7) Mask ocean",
        },
    },
    "EnsoSstLonRmse": {
        "diagnostic": {
            "plot_type": "curve",
            "nbr_panel": 1,
            "title": "ENSO's SSTA pattern",
            "varpattern": output_variables["EnsoSstLonRmse"][0],
            "xname": "longitude",
            "yname": "reg(ENSO SSTA, SSTA)",
            "method": "1) N3.4 SST averaged\n2) Linearly detrended\n3) Seasonal cycle removed\n" +
                      "4) SSTA regridded to 1°x1°\n5) 5S-5N meridional SSTA averaged\n" +
                      "6) NDJ SSTA regressed onto NDJ N3.4 SSTA\n\nMetric: RMSE$_x$",
        },
        "dive_down01": {
            "plot_type": "curve",
            "nbr_panel": 1,
            "title": "ENSO's SSTA pattern",
            "varpattern": output_variables["EnsoSstLonRmse"][1:3],
            "colors": {"model": ["blue", "red"], "reference": ["blue", "red"]},
            "linestyles": {"model": ["-", "-"], "reference": ["-.", "-."]},
            "legend": ["La Nina", "El Nino"],
            "xname": "longitude",
            "yname": "ENSO SSTA",
            "method": "1) N3.4 SST averaged\n2) Linearly detrended\n3) Seasonal cycle removed\n" +
                      "4) Detect El Nino and La Nina\n    (NDJ N3.4 SSTA > 0.5 STD 5 cons. seasons)\n" +
                      "5) SSTA regridded to 1°x1°\n6) 5S-5N meridional SSTA averaged\n" +
                      "7) El Nino and La Nina NDJ SSTA composited",
        },
        "dive_down02": {
            "plot_type": "map",
            "nbr_panel": 2,
            "colorbar": dict_colorbar["anomalies"],
            "label": dict_label["SKEW"],
            "maskland": True,
            "title": ["reg(ENSO SSTA, SSTA)", "reg(ENSO SSTA, SSTA)"],
            "varpattern": output_variables["EnsoSstLonRmse"][3],
            "xname": "longitude",
            "yname": "latitude",
            "zname": "regression",
            "method": "1) N3.4 SST averaged\n2) Linearly detrended\n3) Seasonal cycle removed\n" +
                      "4) SSTA regridded to 1°x1°\n5) NDJ SSTA regressed onto NDJ N3.4 SSTA",
        },
        "dive_down03": {
            "plot_type": "map",
            "nbr_panel": 4,
            "colorbar": dict_colorbar["anomalies"],
            "label": dict_label["REG25"],
            "maskland": True,
            "title": ["La Nina SSTA", "El Nino SSTA"],
            "varpattern": output_variables["EnsoSstLonRmse"][4:],
            "xname": "longitude",
            "yname": "latitude",
            "zname": "SSTA",
            "method": "1) N3.4 SST averaged\n2) Linearly detrended\n3) Seasonal cycle removed\n" +
                      "4) Detect El Nino and La Nina\n    (NDJ N3.4 SSTA > 0.5 STD 5 cons. seasons)\n" +
                      "5) SSTA regridded to 1°x1°\n6) El Nino and La Nina NDJ SSTA composited",
        },
    },
    "EnsoSstTsRmse": {
        "diagnostic": {
            "plot_type": "curve",
            "nbr_panel": 1,
            "title": "ENSO's SSTA life-cycle",
            "varpattern": output_variables["EnsoSstTsRmse"][0],
            "xname": "months",
            "yname": "reg(ENSO SSTA, SSTA)",
            "method": "1) Horizontal averaged\n2) Linearly detrended\n3) Seasonal cycle removed\n" +
                      "4) REGION1 SSTA regressed onto NDJ N3.4 SSTA\n\nMetric: RMSE$_{t}$",
        },
        "dive_down01": {
            "plot_type": "curve",
            "nbr_panel": 1,
            "title": "ENSO's SSTA life-cycle",
            "varpattern": output_variables["EnsoSstTsRmse"][1:3],
            "colors": {"model": ["blue", "red"], "reference": ["blue", "red"]},
            "linestyles": {"model": ["-", "-"], "reference": ["-.", "-."]},
            "legend": ["La Nina", "El Nino"],
            "xname": "months",
            "yname": "ENSO SSTA",
            "method": "1) Horizontal averaged\n2) Linearly detrended\n3) Seasonal cycle removed\n" +
                      "4) Detect El Nino and La Nina\n    (NDJ N3.4 SSTA > 0.5 STD 5 cons. seasons)\n" +
                      "5) El Nino and La Nina SSTA composited",
        },
        "dive_down02": {
            "plot_type": "hovmoeller",
            "nbr_panel": 2,
            "colorbar": dict_colorbar["anomalies"],
            "label": dict_label["REG12"],
            "title": ["reg(ENSO SSTA, SSTA)", "reg(ENSO SSTA, SSTA)"],
            "varpattern": output_variables["EnsoSstTsRmse"][3],
            "xname": "longitude",
            "yname": "months",
            "zname": "regression",
            "method": "1) N3.4 SST averaged\n2) Linearly detrended\n3) Seasonal cycle removed\n" +
                      "4) SSTA regridded to 1°x1°\n5) 5S-5N meridional SSTA average\n" +
                      "6) NDJ SSTA regressed onto NDJ N3.4 SSTA",
        },
        "dive_down03": {
            "plot_type": "hovmoeller",
            "nbr_panel": 4,
            "colorbar": dict_colorbar["anomalies"],
            "label": dict_label["REG2"],
            "title": ["La Nina SSTA", "El Nino SSTA"],
            "varpattern": output_variables["EnsoSstTsRmse"][4:],
            "xname": "longitude",
            "yname": "months",
            "zname": "SSTA",
            "method": "1) N3.4 SST averaged\n2) Linearly detrended\n3) Seasonal cycle removed\n" +
                      "4) Detect El Nino and La Nina\n    (NDJ N3.4 SSTA > 0.5 STD 5 cons. seasons)\n" +
                      "5) SSTA regridded to 1°x1°\n6) 5S-5N meridional SSTA average\n" +
                      "7) El Nino and La Nina TAUYA composited",
        },
    },
    "EnsoTauxLonRmse": {
        "diagnostic": {
            "plot_type": "curve",
            "nbr_panel": 1,
            "title": "ENSO's TAUXA pattern",
            "varpattern": output_variables["EnsoTauxLonRmse"][0],
            "xname": "longitude",
            "yname": "reg(ENSO SSTA, TAUXA)",
            "method": "1) N3.4 SST averaged\n2) Linearly detrended\n3) Seasonal cycle removed\n" +
                      "4) TAUXA regridded to 1°x1°\n5) 5S-5N meridional TAUXA averaged\n" +
                      "6) NDJ TAUXA regressed onto NDJ N3.4 SSTA\n\nMetric: RMSE$_x$",
        },
        "dive_down01": {
            "plot_type": "curve",
            "nbr_panel": 1,
            "title": "ENSO's TAUXA pattern",
            "varpattern": output_variables["EnsoTauxLonRmse"][1:3],
            "colors": {"model": ["blue", "red"], "reference": ["blue", "red"]},
            "linestyles": {"model": ["-", "-"], "reference": ["-.", "-."]},
            "legend": ["La Nina", "El Nino"],
            "xname": "longitude",
            "yname": "ENSO TAUXA",
            "method": "1) N3.4 SST averaged\n2) Linearly detrended\n3) Seasonal cycle removed\n" +
                      "4) Detect El Nino and La Nina\n    (NDJ N3.4 SSTA > 0.5 STD 5 cons. seasons)\n" +
                      "5) TAUXA regridded to 1°x1°\n6) 5S-5N meridional TAUXA averaged\n" +
                      "7) El Nino and La Nina NDJ TAUXA composited",
        },
        "dive_down02": {
            "plot_type": "map",
            "nbr_panel": 2,
            "colorbar": dict_colorbar["anomalies"],
            "label": dict_label["REG30"],
            "maskland": True,
            "title": ["reg(ENSO SSTA, TAUXA)", "reg(ENSO SSTA, TAUXA)"],
            "varpattern": output_variables["EnsoTauxLonRmse"][3],
            "xname": "longitude",
            "yname": "latitude",
            "zname": "regression",
            "method": "1) N3.4 SST averaged\n2) Linearly detrended\n3) Seasonal cycle removed\n" +
                      "4) TAUXA regridded to 1°x1°\n5) NDJ TAUXA regressed onto NDJ N3.4 SSTA",
        },
        "dive_down03": {
            "plot_type": "map",
            "nbr_panel": 4,
            "colorbar": dict_colorbar["anomalies"],
            "label": dict_label["REG30"],
            "maskland": True,
            "title": ["La Nina TAUXA", "El Nino TAUXA"],
            "varpattern": output_variables["EnsoTauxLonRmse"][4:],
            "xname": "longitude",
            "yname": "latitude",
            "zname": "TAUXA",
            "method": "1) N3.4 SST averaged\n2) Linearly detrended\n3) Seasonal cycle removed\n" +
                      "4) Detect El Nino and La Nina\n    (NDJ N3.4 SSTA > 0.5 STD 5 cons. seasons)\n" +
                      "5) TAUXA regridded to 1°x1°\n6) El Nino and La Nina NDJ TAUXA composited",
        },
    },
    "EnsoTauxTsRmse": {
        "diagnostic": {
            "plot_type": "curve",
            "nbr_panel": 1,
            "title": "ENSO's TAUXA life-cycle",
            "varpattern": output_variables["EnsoTauxTsRmse"][0],
            "xname": "months",
            "yname": "reg(ENSO SSTA, TAUXA)",
            "method": "1) Horizontal averaged\n2) Linearly detrended\n3) Seasonal cycle removed\n" +
                      "4) REGION1 TAUXA regressed onto NDJ N3.4 SSTA\n\nMetric: RMSE$_{t}$",
        },
        "dive_down01": {
            "plot_type": "curve",
            "nbr_panel": 1,
            "title": "ENSO's TAUXA life-cycle",
            "varpattern": output_variables["EnsoTauxTsRmse"][1:3],
            "colors": {"model": ["blue", "red"], "reference": ["blue", "red"]},
            "linestyles": {"model": ["-", "-"], "reference": ["-.", "-."]},
            "legend": ["La Nina", "El Nino"],
            "xname": "months",
            "yname": "ENSO TAUXA",
            "method": "1) Horizontal averaged\n2) Linearly detrended\n3) Seasonal cycle removed\n" +
                      "4) Detect El Nino and La Nina\n    (NDJ N3.4 SSTA > 0.5 STD 5 cons. seasons)\n" +
                      "5) El Nino and La Nina TAUXA composited",
        },
        "dive_down02": {
            "plot_type": "hovmoeller",
            "nbr_panel": 2,
            "colorbar": dict_colorbar["anomalies"],
            "label": dict_label["REG20"],
            "title": ["reg(ENSO SSTA, TAUXA)", "reg(ENSO SSTA, TAUXA)"],
            "varpattern": output_variables["EnsoTauxTsRmse"][3],
            "xname": "longitude",
            "yname": "months",
            "zname": "regression",
            "method": "1) N3.4 SST averaged\n2) Linearly detrended\n3) Seasonal cycle removed\n" +
                      "4) TAUXA regridded to 1°x1°\n5) 5S-5N meridional TAUXA average\n" +
                      "6) NDJ TAUXA regressed onto NDJ N3.4 SSTA",
        },
        "dive_down03": {
            "plot_type": "hovmoeller",
            "nbr_panel": 4,
            "colorbar": dict_colorbar["anomalies"],
            "label": dict_label["REG30"],
            "title": ["La Nina TAUXA", "El Nino TAUXA"],
            "varpattern": output_variables["EnsoTauxTsRmse"][4:],
            "xname": "longitude",
            "yname": "months",
            "zname": "TAUXA",
            "method": "1) N3.4 SST averaged\n2) Linearly detrended\n3) Seasonal cycle removed\n" +
                      "4) Detect El Nino and La Nina\n    (NDJ N3.4 SSTA > 0.5 STD 5 cons. seasons)\n" +
                      "5) TAUXA regridded to 1°x1°\n6) 5S-5N meridional TAUXA average\n" +
                      "7) El Nino and La Nina TAUXA composited",
        },
    },
    "EnsoTauyLonRmse": {
        "diagnostic": {
            "plot_type": "curve",
            "nbr_panel": 1,
            "title": "ENSO's TAUYA pattern",
            "varpattern": output_variables["EnsoTauyLonRmse"][0],
            "xname": "longitude",
            "yname": "reg(ENSO SSTA, TAUYA)",
            "method": "1) N3.4 SST averaged\n2) Linearly detrended\n3) Seasonal cycle removed\n" +
                      "4) TAUYA regridded to 1°x1°\n5) 5S-5N meridional TAUYA averaged\n" +
                      "6) NDJ TAUYA regressed onto NDJ N3.4 SSTA\n\nMetric: RMSE$_x$",
        },
        "dive_down01": {
            "plot_type": "curve",
            "nbr_panel": 1,
            "title": "ENSO's TAUYA pattern",
            "varpattern": output_variables["EnsoTauyLonRmse"][1:3],
            "colors": {"model": ["blue", "red"], "reference": ["blue", "red"]},
            "linestyles": {"model": ["-", "-"], "reference": ["-.", "-."]},
            "legend": ["La Nina", "El Nino"],
            "xname": "longitude",
            "yname": "ENSO TAUYA",
            "method": "1) N3.4 SST averaged\n2) Linearly detrended\n3) Seasonal cycle removed\n" +
                      "4) Detect El Nino and La Nina\n    (NDJ N3.4 SSTA > 0.5 STD 5 cons. seasons)\n" +
                      "5) TAUYA regridded to 1°x1°\n6) 5S-5N meridional TAUYA averaged\n" +
                      "7) El Nino and La Nina NDJ TAUYA composited",
        },
        "dive_down02": {
            "plot_type": "map",
            "nbr_panel": 2,
            "colorbar": dict_colorbar["anomalies"],
            "label": dict_label["REG30"],
            "maskland": True,
            "title": ["reg(ENSO SSTA, TAUYA)", "reg(ENSO SSTA, TAUYA)"],
            "varpattern": output_variables["EnsoTauyLonRmse"][3],
            "xname": "longitude",
            "yname": "latitude",
            "zname": "regression",
            "method": "1) N3.4 SST averaged\n2) Linearly detrended\n3) Seasonal cycle removed\n" +
                      "4) TAUYA regridded to 1°x1°\n5) NDJ TAUYA regressed onto NDJ N3.4 SSTA",
        },
        "dive_down03": {
            "plot_type": "map",
            "nbr_panel": 4,
            "colorbar": dict_colorbar["anomalies"],
            "label": dict_label["REG30"],
            "maskland": True,
            "title": ["La Nina TAUYA", "El Nino TAUYA"],
            "varpattern": output_variables["EnsoTauyLonRmse"][4:],
            "xname": "longitude",
            "yname": "latitude",
            "zname": "TAUYA",
            "method": "1) N3.4 SST averaged\n2) Linearly detrended\n3) Seasonal cycle removed\n" +
                      "4) Detect El Nino and La Nina\n    (NDJ N3.4 SSTA > 0.5 STD 5 cons. seasons)\n" +
                      "5) TAUYA regridded to 1°x1°\n6) El Nino and La Nina NDJ TAUYA composited",
        },
    },
    "EnsoTauyTsRmse": {
        "diagnostic": {
            "plot_type": "curve",
            "nbr_panel": 1,
            "title": "ENSO's TAUYA life-cycle",
            "varpattern": output_variables["EnsoTauyTsRmse"][0],
            "xname": "months",
            "yname": "reg(ENSO SSTA, TAUYA)",
            "method": "1) Horizontal averaged\n2) Linearly detrended\n3) Seasonal cycle removed\n" +
                      "4) REGION1 TAUYA regressed onto NDJ N3.4 SSTA\n\nMetric: RMSE$_{t}$",
        },
        "dive_down01": {
            "plot_type": "curve",
            "nbr_panel": 1,
            "title": "ENSO's TAUYA life-cycle",
            "varpattern": output_variables["EnsoTauyTsRmse"][1:3],
            "colors": {"model": ["blue", "red"], "reference": ["blue", "red"]},
            "linestyles": {"model": ["-", "-"], "reference": ["-.", "-."]},
            "legend": ["La Nina", "El Nino"],
            "xname": "months",
            "yname": "ENSO TAUYA",
            "method": "1) Horizontal averaged\n2) Linearly detrended\n3) Seasonal cycle removed\n" +
                      "4) Detect El Nino and La Nina\n    (NDJ N3.4 SSTA > 0.5 STD 5 cons. seasons)\n" +
                      "5) El Nino and La Nina TAUYA composited",
        },
        "dive_down02": {
            "plot_type": "hovmoeller",
            "nbr_panel": 2,
            "colorbar": dict_colorbar["anomalies"],
            "label": dict_label["REG20"],
            "title": ["reg(ENSO SSTA, TAUYA)", "reg(ENSO SSTA, TAUYA)"],
            "varpattern": output_variables["EnsoTauyTsRmse"][3],
            "xname": "longitude",
            "yname": "months",
            "zname": "regression",
            "method": "1) N3.4 SST averaged\n2) Linearly detrended\n3) Seasonal cycle removed\n" +
                      "4) TAUYA regridded to 1°x1°\n5) 5S-5N meridional TAUYA average\n" +
                      "6) NDJ TAUYA regressed onto NDJ N3.4 SSTA",
        },
        "dive_down03": {
            "plot_type": "hovmoeller",
            "nbr_panel": 4,
            "colorbar": dict_colorbar["anomalies"],
            "label": dict_label["REG30"],
            "title": ["La Nina TAUYA", "El Nino TAUYA"],
            "varpattern": output_variables["EnsoTauyTsRmse"][4:],
            "xname": "longitude",
            "yname": "months",
            "zname": "TAUYA",
            "method": "1) N3.4 SST averaged\n2) Linearly detrended\n3) Seasonal cycle removed\n" +
                      "4) Detect El Nino and La Nina\n    (NDJ N3.4 SSTA > 0.5 STD 5 cons. seasons)\n" +
                      "5) TAUYA regridded to 1°x1°\n6) 5S-5N meridional TAUYA average\n" +
                      "7) El Nino and La Nina TAUYA composited",
        },
    },
    "EnsoSeasonality": {
        "diagnostic": {
            "plot_type": "dot",
            "nbr_panel": 1,
            "title": "ENSO Seasonality",
            "varpattern": "diagnostic",
            "yname": "SSTA std (NDJ/MAM)",
            "method": "1) REGION1 averaged\n2) Linearly detrended\n3) Seasonal cycle removed\n" +
                      "4) NDJ and MAM standard deviation\n5) ratio = STD$_{NDJ}$/STD$_{MAM}$\n\n" +
                      "Metric: abs((Ratio$_{mod}$-Ratio$_{ref}$)/Ratio$_{ref}$)*100",
        },
        "dive_down01": {
            "plot_type": "curve",
            "nbr_panel": 1,
            "title": "SSTA standard deviation",
            "varpattern": output_variables["EnsoSeasonality"][0],
            "xname": "months",
            "yname": "SSTA std",
            "method": "1) REGION1 averaged\n2) Linearly detrended\n3) Seasonal cycle removed\n" +
                      "4) Standard deviation for each calendar month",
        },
        "dive_down02": {
            "plot_type": "hovmoeller",
            "nbr_panel": 2,
            "colorbar": dict_colorbar["amplitude"],
            "label": dict_label["amplitude"],
            "title": ["SSTA standard deviation", "SSTA standard deviation"],
            "varpattern": output_variables["EnsoSeasonality"][1],
            "xname": "longitude",
            "yname": "months",
            "zname": "SSTA std",
            "method": "1) Linearly detrended\n2) Seasonal cycle removed\n3) Standard deviation for each calendar month"
                      + "4) Regridded to 1°x1°\n5) 5S-5N meridional averaged",
        },
        "dive_down03": {
            "plot_type": "curve",
            "nbr_panel": 1,
            "title": "SSTA standard deviation",
            "varpattern": output_variables["EnsoSeasonality"][2:4],
            "colors": {"model": ["red", "blue"], "reference": ["red", "blue"]},
            "linestyles": {"model": ["-", "-"], "reference": ["-.", "-."]},
            "legend": ["NDJ", "MAM"],
            "xname": "longitude",
            "yname": "SSTA std",
            "method": "1) Linearly detrended\n2) Seasonal cycle removed\n" +
                      "3) NDJ and MAM standard deviation\n4) Regridded to 1°x1°\n5) 5S-5N meridional averaged",
        },
        "dive_down04": {
            "plot_type": "map",
            "nbr_panel": 4,
            "colorbar": dict_colorbar["amplitude"],
            "label": dict_label["amplitude"],
            "maskland": True,
            "title": ["NDJ", "MAM"],
            "varpattern": output_variables["EnsoSeasonality"][4:],
            "xname": "longitude",
            "yname": "latitude",
            "zname": "monthly SSTA std",
            "method": "1) Linearly detrended\n2) Seasonal cycle removed\n" +
                      "3) NDJ and MAM standard deviation\n4) Regridded to 1°x1°",
        },
    },
    "EnsoSstDiversity": {
        "diagnostic": {
            "plot_type": "dot",
            "nbr_panel": 1,
            "title": "ENSO diversity",
            "varpattern": "diagnostic",
            "yname": "IQR of min/max SSTA",
            "method": "1) N3.4 SST averaged\n2) Linearly detrended\n3) Seasonal cycle removed\n" +
                      "4) Detect El Nino and La Nina\n    (NDJ N3.4 SSTA > 0.5 STD 5 cons. seasons)\n" +
                      "5) SSTA regridded to 1°x1°\n6) 5S-5N meridional SSTA average\n" +
                      "7) 19° triangular running ave.\n" +
                      "8) Find zonal location of El Nino max(SSTA) and La Nina min(SSTA)\n" +
                      "9) IQR El Nino max(SSTA) with La Nina min(SSTA)\n\n" +
                      "Metric: abs((IQR$_{mod}$-IQR$_{ref}$)/IQR$_{ref}$)*100",
        },
        "dive_down01": {
            "plot_type": "boxplot",
            "nbr_panel": 3,
            "title": ["ENSO diversity", "La Nina diversity", "El Nino diversity"],
            "varpattern": output_variables["EnsoSstDiversity"],
            "yname": ["longitude of min/max SSTA", "longitude of min SSTA", "longitude of max SSTA"],
            "custom_label": "longitude",
            "method": "1) N3.4 SST averaged\n2) Linearly detrended\n3) Seasonal cycle removed\n" +
                      "4) Detect El Nino and La Nina\n    (NDJ N3.4 SSTA > 0.5 STD 5 cons. seasons)\n" +
                      "5) SSTA regridded to 1°x1°\n6) 5S-5N meridional SSTA average\n" +
                      "7) 19° triangular running ave.\n" +
                      "8) Find zonal location of El Nino max(SSTA) and La Nina min(SSTA)",
        },
    },
    "EnsoSstSkew": {
        "diagnostic": {
            "plot_type": "dot",
            "nbr_panel": 1,
            "title": "ENSO SSTA skewness",
            "varpattern": "diagnostic",
            "yname": "SSTA skewness",
            "method": "1) REGION1 averaged\n2) Linearly detrended\n3) Seasonal cycle removed\n4) Skewness\n\n" +
                      "Metric: abs((SKE$_{mod}$-SKE$_{ref}$)/SKE$_{ref}$)*100",
        },
        "dive_down01": {
            "plot_type": "curve",
            "nbr_panel": 1,
            "title": "SSTA skewness",
            "varpattern": output_variables["EnsoSstSkew"][0],
            "xname": "longitude",
            "yname": "SSTA skew",
            "method": "1) Linearly detrended\n2) Seasonal cycle removed\n3) Skewness\n4) Regridded to 1°x1°\n" +
                      "5) 5S-5N meridional averaged",
        },
        "dive_down02": {
            "plot_type": "map",
            "nbr_panel": 2,
            "colorbar": dict_colorbar["anomalies"],
            "label": dict_label["SKEW"],
            "maskland": True,
            "title": ["SSTA skew", "SSTA skew"],
            "varpattern": output_variables["EnsoSstSkew"][1],
            "xname": "longitude",
            "yname": "latitude",
            "zname": "SSTA skew",
            "method": "1) Linearly detrended\n2) Seasonal cycle removed\n3) Skewness\n4) Regridded to 1°x1°",
        },
    },
    "grad_lat_pr": {
        "diagnostic": {
            "plot_type": "dot",
            "nbr_panel": 1,
            "title": "meridional PR gradient",
            "varpattern": "diagnostic",
            "yname": "PR grad",
            "method": "1) REGION1 averaged\n2) REGION2 averaged\n3) Linearly detrended\n4) Off-equ minus equ\n" +
                      "5) Temporal averaged\n\nMetric: abs((STD$_{mod}$-STD$_{ref}$)/STD$_{ref}$)*100",

        },
        "dive_down01": {
            "plot_type": "curve",
            "nbr_panel": 1,
            "title": "Mean PR",
            "varpattern": output_variables["grad_lat_pr"][0],
            "xname": "latitude",
            "yname": "PR",
            "method": "1) Linearly detrended\n2) Temporal averaged\n3) Regridded to 1°x1°\n" +
                      "4) Zonal averaged (see box)",
        },
        "dive_down02": {
            "plot_type": "map",
            "nbr_panel": 2,
            "colorbar": dict_colorbar["PR"],
            "label": dict_label["PR"],
            "maskland": True,
            "title": ["Mean PR", "Mean PR"],
            "varpattern": output_variables["grad_lat_pr"][1],
            "xname": "longitude",
            "yname": "latitude",
            "zname": "PR",
            "method": "1) Linearly detrended\n2) Temporal averaged\n3) Regridded to 1°x1°",
        },
    },
    "grad_lat_sst": {
        "diagnostic": {
            "plot_type": "dot",
            "nbr_panel": 1,
            "title": "meridional SST gradient",
            "varpattern": "diagnostic",
            "yname": "SST grad",
            "method": "1) REGION1 averaged\n2) REGION2 averaged\n3) Linearly detrended\n4) Off-equ minus equ\n" +
                      "5) Temporal averaged\n\nMetric: abs((STD$_{mod}$-STD$_{ref}$)/STD$_{ref}$)*100",

        },
        "dive_down01": {
            "plot_type": "curve",
            "nbr_panel": 1,
            "title": "Mean SST",
            "varpattern": output_variables["grad_lat_sst"][0],
            "xname": "latitude",
            "yname": "SST",
            "method": "1) Linearly detrended\n2) Temporal averaged\n3) Regridded to 1°x1°\n" +
                      "4) Zonal averaged (see box)",
        },
        "dive_down02": {
            "plot_type": "map",
            "nbr_panel": 2,
            "colorbar": dict_colorbar["SST"],
            "label": dict_label["SST"],
            "maskland": True,
            "title": ["Mean SST", "Mean SST"],
            "varpattern": output_variables["grad_lat_sst"][1],
            "xname": "longitude",
            "yname": "latitude",
            "zname": "SST",
            "method": "1) Linearly detrended\n2) Temporal averaged\n3) Regridded to 1°x1°",
        },
    },
    "grad_lon_pr": {
        "diagnostic": {
            "plot_type": "dot",
            "nbr_panel": 1,
            "title": "zonal PR gradient",
            "varpattern": "diagnostic",
            "yname": "PR grad",
            "method": "1) REGION1 averaged\n2) REGION2 averaged\n3) Linearly detrended\n4) west minus east\n" +
                      "5) Temporal averaged\n\nMetric: abs((STD$_{mod}$-STD$_{ref}$)/STD$_{ref}$)*100",

        },
        "dive_down01": {
            "plot_type": "curve",
            "nbr_panel": 1,
            "title": "Mean PR",
            "varpattern": output_variables["grad_lon_pr"][0],
            "xname": "longitude",
            "yname": "PR",
            "method": "1) Linearly detrended\n2) Temporal averaged\n3) Regridded to 1°x1°\n" +
                      "4) Meridional averaged (see box)",
        },
        "dive_down02": {
            "plot_type": "map",
            "nbr_panel": 2,
            "colorbar": dict_colorbar["PR"],
            "label": dict_label["PR"],
            "maskland": True,
            "title": ["Mean PR", "Mean PR"],
            "varpattern": output_variables["grad_lon_pr"][1],
            "xname": "longitude",
            "yname": "latitude",
            "zname": "PR",
            "method": "1) Linearly detrended\n2) Temporal averaged\n3) Regridded to 1°x1°",
        },
    },
    "grad_lon_sst": {
        "diagnostic": {
            "plot_type": "dot",
            "nbr_panel": 1,
            "title": "zonal SST gradient",
            "varpattern": "diagnostic",
            "yname": "SST grad",
            "method": "1) REGION1 averaged\n2) REGION2 averaged\n3) Linearly detrended\n4) west minus east\n" +
                      "5) Temporal averaged\n\nMetric: abs((STD$_{mod}$-STD$_{ref}$)/STD$_{ref}$)*100",

        },
        "dive_down01": {
            "plot_type": "curve",
            "nbr_panel": 1,
            "title": "Mean SST",
            "varpattern": output_variables["grad_lon_sst"][0],
            "xname": "longitude",
            "yname": "SST",
            "method": "1) Linearly detrended\n2) Temporal averaged\n3) Regridded to 1°x1°\n" +
                      "4) Meridional averaged (see box)",
        },
        "dive_down02": {
            "plot_type": "map",
            "nbr_panel": 2,
            "colorbar": dict_colorbar["SST"],
            "label": dict_label["SST"],
            "maskland": True,
            "title": ["Mean SST", "Mean SST"],
            "varpattern": output_variables["grad_lon_sst"][1],
            "xname": "longitude",
            "yname": "latitude",
            "zname": "SST",
            "method": "1) Linearly detrended\n2) Temporal averaged\n3) Regridded to 1°x1°",
        },
    },
    "NinaPrMap": {
        "diagnostic": {
            "plot_type": "map",
            "nbr_panel": 2,
            "colorbar": dict_colorbar["anomalies"],
            "label": dict_label["REG2"],
            "maskland": False,
            "title": ["La Nina composite", "La Nina composite"],
            #"varpattern": "sst_over_sst_map__",
            "varpattern": "prComp_map__",
            "xname": "longitude",
            "yname": "latitude",
            "zname": "PRA",
            "method": "1) Detect La Nina\n    (5-m. tri. ave. Dec. N3.4 SSTA < -0.75 STD)\n" +
                      "2) Seasonal cycle removed\n3) Linearly detrended\n4) 5-month triangular running ave.\n" +
                      "5) PRA regridded to 1°x1°6) La Nina Dec. PRA composited\n\nMetric: RMSE$_{xy}$",
        },
    },
    "NinaSlpMap": {
        "diagnostic": {
            "plot_type": "map",
            "nbr_panel": 2,
            "colorbar": dict_colorbar["anomalies"],
            "label": dict_label["REG3"],
            "maskland": False,
            "title": ["La Nina composite", "La Nina composite"],
            #"varpattern": "sst_over_sst_map__",
            "varpattern": "slp_map__",
            "xname": "longitude",
            "yname": "latitude",
            "zname": "SLPA",
            "method": "1) Detect La Nina\n    (5-m. tri. ave. Dec. N3.4 SSTA < -0.75 STD)\n" +
                      "2) Seasonal cycle removed\n3) Linearly detrended\n4) 5-month triangular running ave.\n" +
                      "5) SLPA regridded to 1°x1°6) La Nina Dec. SLPA composited\n\nMetric: RMSE$_{xy}$",
        },
    },
    "NinaSstMap": {
        "diagnostic": {
            "plot_type": "map",
            "nbr_panel": 2,
            "colorbar": dict_colorbar["anomalies"],
            "label": dict_label["SKEW"],
            "maskland": False,
            "title": ["La Nina composite", "La Nina composite"],
            #"varpattern": "sst_over_sst_map__",
            "varpattern": "ts_map__",
            "xname": "longitude",
            "yname": "latitude",
            "zname": "TASA",
            "method": "1) Detect La Nina\n    (5-m. tri. ave. Dec. N3.4 SSTA < -0.75 STD)\n" +
                      "2) Seasonal cycle removed\n3) Linearly detrended\n4) 5-month triangular running ave.\n" +
                      "5) TASA regridded to 1°x1°\n6) La Nina Dec. TASA composited\n\nMetric: RMSE$_{xy}$",
        },
    },
    "NinaSstDur": {
        "diagnostic": {
            "plot_type": "dot",
            "nbr_panel": 1,
            "title": "La Nina duration",
            "varpattern": "diagnostic",
            "yname": "duration (SSTA<-0.5)",
            "method": "1) Detect La Nina\n    (5-m. tri. ave. Dec. N3.4 SSTA < -0.75 STD)\n" +
                      "2) Seasonal cycle removed\n3) Linearly detrended\n4) 5-month triangular running ave.\n" +
                      "5) REGION1 averaged\n6) Duration = nbr months < -0.5 ENSO STD\n7) Mean La Nina duration\n\n" +
                      "Metric: abs((DUR$_{mod}$-DUR$_{ref}$)/DUR$_{ref}$)*100",
        },
        "dive_down01": {
            "plot_type": "boxplot",
            "nbr_panel": 1,
            "title": "La Nina duration",
            "varpattern": "Nina_duration__",
            "yname": "duration (SSTA<-0.5)",
            "method": "1) Detect La Nina\n    (5-m. tri. ave. Dec. N3.4 SSTA < -0.75 STD)\n" +
                      "2) Seasonal cycle removed\n3) Linearly detrended\n4) 5-month triangular running ave.\n" +
                      "5) REGION1 averaged\n6) Duration = nbr months < -0.5 ENSO STD",
        },
    },
    "NinaSstLonRmse": {
        "diagnostic": {
            "plot_type": "curve",
            "nbr_panel": 1,
            "title": "La Nina pattern",
            "varpattern": "sst_lon__",
            "xname": "longitude",
            "yname": "SSTA",
            "method": "1) Detect La Nina\n    (5-m. tri. ave. Dec. N3.4 SSTA < -0.75 STD)\n" +
                      "2) Seasonal cycle removed\n3) Linearly detrended\n4) 5-month triangular running ave.\n" +
                      "5) SSTA regridded to 1°x1°\n6) 5S-5N meridional SSTA averaged\n" +
                      "7) La Nina Dec. SSTA composited\n\nMetric: RMSE$_x$",
        },
        "dive_down01": {
            "plot_type": "map",
            "nbr_panel": 2,
            "colorbar": dict_colorbar["anomalies"],
            "label": dict_label["dSST"],
            "maskland": True,
            "title": "La Nina SSTA",
            "varpattern": "sst_map__",
            "xname": "longitude",
            "yname": "latitude",
            "zname": "SSTA",
            "method": "1) Detect La Nina\n    (5-m. tri. ave. Dec. N3.4 SSTA < -0.75 STD)\n" +
                      "2) Seasonal cycle removed\n3) Linearly detrended\n4) 5-month triangular running ave.\n" +
                      "5) SSTA regridded to 1°x1°\n6) La Nina Dec. SSTA composited",
        },
    },
    "NinaSstTsRmse": {
        "diagnostic": {
            "plot_type": "curve",
            "nbr_panel": 1,
            "title": "La Nina life-cycle",
            "varpattern": "sst_ts__",
            "xname": "months",
            "yname": "SSTA",
            "method": "1) Detect La Nina\n    (5-m. tri. ave. Dec. N3.4 SSTA < -0.75 STD)\n" +
                      "2) Seasonal cycle removed\n3) Linearly detrended\n4) 5-month triangular running ave.\n" +
                      "5) REGION1 SSTA averaged\n6) La Nina SSTA composited\n\nMetric: RMSE$_{t}$",
        },
        "dive_down01": {
            "plot_type": "hovmoeller",
            "nbr_panel": 2,
            "colorbar": dict_colorbar["anomalies"],
            "label": dict_label["SKEW"],
            "title": "La Nina SSTA",
            "varpattern": "sst_hov__",
            "xname": "longitude",
            "yname": "months",
            "zname": "SSTA",
            "method": "1) Detect La Nina\n    (5-m. tri. ave. Dec. N3.4 SSTA < -0.75 STD)\n" +
                      "2) Seasonal cycle removed\n3) Linearly detrended\n4) 5-month triangular running ave.\n" +
                      "5) SSTA regridded to 1°x1°\n6) 5S-5N meridional SSTA average\n7) La Nina SSTA composited",
        },
    },
    "NinoPrMap": {
        "diagnostic": {
            "plot_type": "map",
            "nbr_panel": 2,
            "colorbar": dict_colorbar["anomalies"],
            "label": dict_label["SKEW"],
            "maskland": False,
            "title": ["El Nino composite", "El Nino composite"],
            #"varpattern": "sst_over_sst_map__",
            "varpattern": "pr_map__",
            "xname": "longitude",
            "yname": "latitude",
            "zname": "PRA",
            "method": "1) Detect El Nino\n    (5-m. tri. ave. Dec. N3.4 SSTA > 0.75 STD)\n2) Seasonal cycle removed\n" +
                      "3) Linearly detrended\n4) 5-month triangular running ave.\n5) PRA regridded to 1°x1°" +
                      "6) El Nino Dec. PRA composited\n\nMetric: RMSE$_{xy}$",
        },
    },
    "NinoSlpMap": {
        "diagnostic": {
            "plot_type": "map",
            "nbr_panel": 2,
            "colorbar": dict_colorbar["anomalies"],
            "label": dict_label["REG3"],
            "maskland": False,
            "title": ["El Nino composite", "El Nino composite"],
            #"varpattern": "sst_over_sst_map__",
            "varpattern": "slp_map__",
            "xname": "longitude",
            "yname": "latitude",
            "zname": "SLPA",
            "method": "1) Detect El Nino\n    (5-m. tri. ave. Dec. N3.4 SSTA > 0.75 STD)\n2) Seasonal cycle removed\n" +
                      "3) Linearly detrended\n4) 5-month triangular running ave.\n5) SLPA regridded to 1°x1°" +
                      "6) El Nino Dec. SLPA composited\n\nMetric: RMSE$_{xy}$",
        },
    },
    "NinoSstMap": {
        "diagnostic": {
            "plot_type": "map",
            "nbr_panel": 2,
            "colorbar": dict_colorbar["anomalies"],
            "label": dict_label["SKEW"],
            "maskland": False,
            "title": ["El Nino composite", "El Nino composite"],
            #"varpattern": "sst_over_sst_map__",
            "varpattern": "ts_map__",
            "xname": "longitude",
            "yname": "latitude",
            "zname": "TASA",
            "method": "1) Detect El Nino\n    (5-m. tri. ave. Dec. N3.4 SSTA > 0.75 STD)\n2) Seasonal cycle removed\n" +
                      "3) Linearly detrended\n4) 5-month triangular running ave.\n5) TASA regridded to 1°x1°" +
                      "6) El Nino Dec. TASA composited\n\nMetric: RMSE$_{xy}$",
        },
    },
    "NinoSstDiversity": {
        "diagnostic": {
            "plot_type": "dot",
            "nbr_panel": 1,
            "title": "El Nino diversity",
            "varpattern": "diagnostic",
            "yname": "IQR of max SSTA",
            "method": "1) Detect El Nino\n    (5-m. tri. ave. Dec. N3.4 SSTA > 0.75 STD)\n2) Seasonal cycle removed\n" +
                      "3) Linearly detrended\n4) 5-month triangular running ave.\n5) SSTA regridded to 1°x1°\n" +
                      "6) 5S-5N meridional SSTA averaged\n7) 5° triangular running ave.\n" +
                      "8) Find zonal location of max(SSTA)\n7) IQR El Nino max(SSTA)\n\n" +
                      "Metric: abs((IQR$_{mod}$-IQR$_{ref}$)/IQR$_{ref}$)*100",
        },
        "dive_down01": {
            "plot_type": "boxplot",
            "nbr_panel": 2,
            "title": ["La Nina diversity", "El Nino diversity"],
            "varpattern": ["Nina_lon_pos_minSSTA__", "Nino_lon_pos_maxSSTA__"],
            "yname": ["longitude of min SSTA", "longitude of max SSTA"],
            "custom_label": "longitude",
            "method": "1) Detect El Nino\n    (5-m. tri. ave. Dec. N3.4 SSTA > 0.75 STD)\n2) Seasonal cycle removed\n" +
                      "3) Linearly detrended\n4) 5-month triangular running ave.\n5) SSTA regridded to 1°x1°\n" +
                      "6) 5S-5N meridional SSTA averaged\n7) 5° triangular running ave.\n" +
                      "8) Find zonal location of max(SSTA)",
        },
    },
    "NinoSstDur": {
        "diagnostic": {
            "plot_type": "dot",
            "nbr_panel": 1,
            "title": "El Nino duration",
            "varpattern": "diagnostic",
            "yname": "duration (SSTA>0.5)",
            "method": "1) Detect El Nino\n    (5-m. tri. ave. Dec. N3.4 SSTA > 0.75 STD)\n2) Seasonal cycle removed\n" +
                      "3) Linearly detrended\n4) 5-month triangular running ave.\n5) REGION1 averaged\n" +
                      "6) Duration = nbr months > 0.5 ENSO STD\n7) Mean El Nino duration\n\n" +
                      "Metric: abs((DUR$_{mod}$-DUR$_{ref}$)/DUR$_{ref}$)*100",
        },
        "dive_down01": {
            "plot_type": "boxplot",
            "nbr_panel": 1,
            "title": "El Nino duration",
            "varpattern": "Nino_duration__",
            "yname": "duration (SSTA>0.5)",
            "method": "1) Detect El Nino\n    (5-m. tri. ave. Dec. N3.4 SSTA > 0.75 STD)\n2) Seasonal cycle removed\n" +
                      "3) Linearly detrended\n4) 5-month triangular running ave.\n5) REGION1 averaged\n" +
                      "6) Duration = nbr months > 0.5 ENSO STD",
        },
    },
    "NinoSstLonRmse": {
        "diagnostic": {
            "plot_type": "curve",
            "nbr_panel": 1,
            "title": "El Nino pattern",
            "varpattern": "sst_lon__",
            "xname": "longitude",
            "yname": "SSTA",
            "method": "1) Detect El Nino\n    (5-m. tri. ave. Dec. N3.4 SSTA > 0.75 STD)\n2) Seasonal cycle removed\n" +
                      "3) Linearly detrended\n4) 5-month triangular running ave.\n5) SSTA regridded to 1°x1°\n" +
                      "6) 5S-5N meridional SSTA averaged\n7) El Nino Dec. SSTA composited\n\nMetric: RMSE$_x$",
        },
        "dive_down01": {
            "plot_type": "map",
            "nbr_panel": 2,
            "colorbar": dict_colorbar["anomalies"],
            "label": dict_label["dSST"],
            "maskland": True,
            "title": "El Nino SSTA",
            "varpattern": "sst_map__",
            "xname": "longitude",
            "yname": "latitude",
            "zname": "SSTA",
            "method": "1) Detect El Nino\n    (5-m. tri. ave. Dec. N3.4 SSTA > 0.75 STD)\n2) Seasonal cycle removed\n" +
                      "3) Linearly detrended\n4) 5-month triangular running ave.\n5) SSTA regridded to 1°x1°\n" +
                      "6) El Nino Dec. SSTA composited",
        },
    },
    "NinoSstTsRmse": {
        "diagnostic": {
            "plot_type": "curve",
            "nbr_panel": 1,
            "title": "El Nino life-cycle",
            "varpattern": "sst_ts__",
            "xname": "months",
            "yname": "SSTA",
            "method": "1) Detect El Nino\n    (5-m. tri. ave. Dec. N3.4 SSTA > 0.75 STD)\n2) Seasonal cycle removed\n" +
                      "3) Linearly detrended\n4) 5-month triangular running ave.\n5) REGION1 SSTA averaged\n" +
                      "6) El Nino SSTA composited\n\nMetric: RMSE$_{t}$",
        },
        "dive_down01": {
            "plot_type": "hovmoeller",
            "nbr_panel": 2,
            "colorbar": dict_colorbar["anomalies"],
            "label": dict_label["SKEW"],
            "title": "El Nino SSTA",
            "varpattern": "sst_hov__",
            "xname": "longitude",
            "yname": "months",
            "zname": "SSTA",
            "method": "1) Detect El Nino\n    (5-m. tri. ave. Dec. N3.4 SSTA > 0.75 STD)\n2) Seasonal cycle removed\n" +
                      "3) Linearly detrended\n4) 5-month triangular running ave.\n5) SSTA regridded to 1°x1°\n" +
                      "6) 5S-5N meridional SSTA average\n7) El Nino SSTA composited",
        },
    },
    "SeasonalPrLatRmse": {
        "diagnostic": {
            "plot_type": "curve",
            "nbr_panel": 1,
            "title": "PR seasonal cycle std",
            "varpattern": output_variables["SeasonalPrLatRmse"][0],
            "xname": "latitude",
            "yname": "PR std",
            "method": "1) Linearly detrended\n2) Seasonal cycle computed\n3) Standard deviation\n" +
                      "4) Regridded to 1°x1°\n5) Zonal averaged (see box)\n\nMetric: RMSE$_y$",
        },
        "dive_down01": {
            "plot_type": "map",
            "nbr_panel": 2,
            "colorbar": dict_colorbar["amplitude"],
            "label": dict_label["amplitude5"],
            "maskland": True,
            "title": ["PR seasonal cycle std"],
            "varpattern": output_variables["SeasonalPrLatRmse"][1],
            "xname": "longitude",
            "yname": "latitude",
            "zname": "PR std",
            "method": "1) Linearly detrended\n2) Seasonal cycle computed\n3) Standard deviation\n" +
                      "4) Regridded to 1°x1°",
        },
        "dive_down02": {
            "plot_type": "hovmoeller",
            "nbr_panel": 2,
            "colorbar": dict_colorbar["PR"],
            "label": dict_label["amplitude15"],
            "title": ["PR seasonal cycle", "PR seasonal cycle"],
            "varpattern": output_variables["SeasonalPrLatRmse"][2],
            "xname": "latitude",
            "yname": "months",
            "zname": "PR",
            "method": "1) Linearly detrended\n2) Seasonal cycle computed\n3) Regridded to 1°x1°\n" +
                      "5) Zonal averaged (see box)",
        },
    },
    "SeasonalPrLonRmse": {
        "diagnostic": {
            "plot_type": "curve",
            "nbr_panel": 1,
            "title": "PR seasonal cycle std",
            "varpattern": output_variables["SeasonalPrLonRmse"][0],
            "xname": "longitude",
            "yname": "PR std",
            "method": "1) Linearly detrended\n2) Seasonal cycle computed\n3) Standard deviation\n" +
                      "4) Regridded to 1°x1°\n5) Meridional averaged (see box)\n\nMetric: RMSE$_x$",
        },
        "dive_down01": {
            "plot_type": "map",
            "nbr_panel": 2,
            "colorbar": dict_colorbar["amplitude"],
            "label": dict_label["amplitude5"],
            "maskland": True,
            "title": ["PR seasonal cycle std"],
            "varpattern": output_variables["SeasonalPrLonRmse"][1],
            "xname": "longitude",
            "yname": "latitude",
            "zname": "PR std",
            "method": "1) Linearly detrended\n2) Seasonal cycle computed\n3) Standard deviation\n" +
                      "4) Regridded to 1°x1°",
        },
        "dive_down02": {
            "plot_type": "hovmoeller",
            "nbr_panel": 2,
            "colorbar": dict_colorbar["PR"],
            "label": dict_label["amplitude10"],
            "title": ["PR seasonal cycle", "PR seasonal cycle"],
            "varpattern": output_variables["SeasonalPrLonRmse"][2],
            "xname": "longitude",
            "yname": "months",
            "zname": "PR",
            "method": "1) Linearly detrended\n2) Seasonal cycle computed\n3) Regridded to 1°x1°\n" +
                      "5) Meridional averaged (see box)",
        },
    },
    "SeasonalSshLatRmse": {
        "diagnostic": {
            "plot_type": "curve",
            "nbr_panel": 1,
            "title": "SSH seasonal cycle std",
            "varpattern": output_variables["SeasonalSshLatRmse"][0],
            "xname": "latitude",
            "yname": "SSH std",
            "method": "1) Linearly detrended\n2) Seasonal cycle computed\n3) Standard deviation\n" +
                      "4) Regridded to 1°x1°\n5) Zonal averaged (see box)\n\nMetric: RMSE$_y$",
        },
        "dive_down01": {
            "plot_type": "map",
            "nbr_panel": 2,
            "colorbar": dict_colorbar["amplitude"],  # YYP: I do not know yet the colobar / label needed
            "label": dict_label["amplitude"],
            "maskland": True,
            "title": ["SSH seasonal cycle std"],
            "varpattern": output_variables["SeasonalSshLatRmse"][1],
            "xname": "longitude",
            "yname": "latitude",
            "zname": "SSH std",
            "method": "1) Linearly detrended\n2) Seasonal cycle computed\n3) Standard deviation\n" +
                      "4) Regridded to 1°x1°",
        },
        "dive_down02": {
            "plot_type": "hovmoeller",
            "nbr_panel": 2,
            "colorbar": dict_colorbar["SST"],  # YYP: I do not know yet the colobar / label needed
            "label": dict_label["SST"],
            "title": ["SSH seasonal cycle", "SSH seasonal cycle"],
            "varpattern": output_variables["SeasonalSshLatRmse"][2],
            "xname": "latitude",
            "yname": "months",
            "zname": "SSH",
            "method": "1) Linearly detrended\n2) Seasonal cycle computed\n3) Regridded to 1°x1°\n" +
                      "5) Zonal averaged (see box)",
        },
    },
    "SeasonalSshLonRmse": {
        "diagnostic": {
            "plot_type": "curve",
            "nbr_panel": 1,
            "title": "SSH seasonal cycle std",
            "varpattern": output_variables["SeasonalSshLonRmse"][0],
            "xname": "longitude",
            "yname": "SSH std",
            "method": "1) Linearly detrended\n2) Seasonal cycle computed\n3) Standard deviation\n" +
                      "4) Regridded to 1°x1°\n5) Meridional averaged (see box)\n\nMetric: RMSE$_x$",
        },
        "dive_down01": {
            "plot_type": "map",
            "nbr_panel": 2,
            "colorbar": dict_colorbar["amplitude"],  # YYP: I do not know yet the colobar / label needed
            "label": dict_label["amplitude"],
            "maskland": True,
            "title": ["SSH seasonal cycle std"],
            "varpattern": output_variables["SeasonalSshLonRmse"][1],
            "xname": "longitude",
            "yname": "latitude",
            "zname": "SSH std",
            "method": "1) Linearly detrended\n2) Seasonal cycle computed\n3) Standard deviation\n" +
                      "4) Regridded to 1°x1°",
        },
        "dive_down02": {
            "plot_type": "hovmoeller",
            "nbr_panel": 2,
            "colorbar": dict_colorbar["SST"],  # YYP: I do not know yet the colobar / label needed
            "label": dict_label["SST"],
            "title": ["SSH seasonal cycle", "SSH seasonal cycle"],
            "varpattern": output_variables["SeasonalSshLonRmse"][2],
            "xname": "longitude",
            "yname": "months",
            "zname": "SSH",
            "method": "1) Linearly detrended\n2) Seasonal cycle computed\n3) Regridded to 1°x1°\n" +
                      "5) Meridional averaged (see box)",
        },
    },
    "SeasonalSstLatRmse": {
        "diagnostic": {
            "plot_type": "curve",
            "nbr_panel": 1,
            "title": "SST seasonal cycle std",
            "varpattern": output_variables["SeasonalSstLatRmse"][0],
            "xname": "latitude",
            "yname": "SST std",
            "method": "1) Linearly detrended\n2) Seasonal cycle computed\n3) Standard deviation\n" +
                      "4) Regridded to 1°x1°\n5) Zonal averaged (see box)\n\nMetric: RMSE$_y$",
        },
        "dive_down01": {
            "plot_type": "map",
            "nbr_panel": 2,
            "colorbar": dict_colorbar["amplitude"],
            "label": dict_label["amplitude"],
            "maskland": True,
            "title": ["SST seasonal cycle std"],
            "varpattern": output_variables["SeasonalSstLatRmse"][1],
            "xname": "longitude",
            "yname": "latitude",
            "zname": "SST std",
            "method": "1) Linearly detrended\n2) Seasonal cycle computed\n3) Standard deviation\n" +
                      "4) Regridded to 1°x1°",
        },
        "dive_down02": {
            "plot_type": "hovmoeller",
            "nbr_panel": 2,
            "colorbar": dict_colorbar["SST"],
            "label": dict_label["SST"],
            "title": ["SST seasonal cycle", "SST seasonal cycle"],
            "varpattern": output_variables["SeasonalSstLatRmse"][2],
            "xname": "latitude",
            "yname": "months",
            "zname": "SST",
            "method": "1) Linearly detrended\n2) Seasonal cycle computed\n3) Regridded to 1°x1°\n" +
                      "5) Zonal averaged (see box)",
        },
    },
    "SeasonalSstLonRmse": {
        "diagnostic": {
            "plot_type": "curve",
            "nbr_panel": 1,
            "title": "SST seasonal cycle std",
            "varpattern": output_variables["SeasonalSstLonRmse"][0],
            "xname": "longitude",
            "yname": "SST std",
            "method": "1) Linearly detrended\n2) Seasonal cycle computed\n3) Standard deviation\n" +
                      "4) Regridded to 1°x1°\n5) Meridional averaged (see box)\n\nMetric: RMSE$_x$",
        },
        "dive_down01": {
            "plot_type": "map",
            "nbr_panel": 2,
            "colorbar": dict_colorbar["amplitude"],
            "label": dict_label["amplitude"],
            "maskland": True,
            "title": ["SST seasonal cycle std"],
            "varpattern": output_variables["SeasonalSstLonRmse"][1],
            "xname": "longitude",
            "yname": "latitude",
            "zname": "SST std",
            "method": "1) Linearly detrended\n2) Seasonal cycle computed\n3) Standard deviation\n" +
                      "4) Regridded to 1°x1°",
        },
        "dive_down02": {
            "plot_type": "hovmoeller",
            "nbr_panel": 2,
            "colorbar": dict_colorbar["SST"],
            "label": dict_label["SST"],
            "title": ["SST seasonal cycle", "SST seasonal cycle"],
            "varpattern": output_variables["SeasonalSstLonRmse"][2],
            "xname": "longitude",
            "yname": "months",
            "zname": "SST",
            "method": "1) Linearly detrended\n2) Seasonal cycle computed\n3) Regridded to 1°x1°\n" +
                      "5) Meridional averaged (see box)",
        },
    },
    "SeasonalTauxLatRmse": {
        "diagnostic": {
            "plot_type": "curve",
            "nbr_panel": 1,
            "title": "TAUX seasonal cycle std",
            "varpattern": output_variables["SeasonalTauxLatRmse"][0],
            "xname": "latitude",
            "yname": "TAUX std",
            "method": "1) Linearly detrended\n2) Seasonal cycle computed\n3) Standard deviation\n" +
                      "4) Regridded to 1°x1°\n5) Zonal averaged (see box)\n\nMetric: RMSE$_y$",
        },
        "dive_down01": {
            "plot_type": "map",
            "nbr_panel": 2,
            "colorbar": dict_colorbar["amplitude"],
            "label": dict_label["amplitude60"],
            "maskland": True,
            "title": ["TAUX seasonal cycle std"],
            "varpattern": output_variables["SeasonalTauxLatRmse"][1],
            "xname": "longitude",
            "yname": "latitude",
            "zname": "TAUX std",
            "method": "1) Linearly detrended\n2) Seasonal cycle computed\n3) Standard deviation\n" +
                      "4) Regridded to 1°x1°",
        },
        "dive_down02": {
            "plot_type": "hovmoeller",
            "nbr_panel": 2,
            "colorbar": dict_colorbar["anomalies"],
            "label": dict_label["TAUX"],
            "title": ["TAUX seasonal cycle", "TAUX seasonal cycle"],
            "varpattern": output_variables["SeasonalTauxLatRmse"][2],
            "xname": "latitude",
            "yname": "months",
            "zname": "TAUX",
            "method": "1) Linearly detrended\n2) Seasonal cycle computed\n3) Regridded to 1°x1°\n" +
                      "5) Zonal averaged (see box)",

        },
    },
    "SeasonalTauxLonRmse": {
        "diagnostic": {
            "plot_type": "curve",
            "nbr_panel": 1,
            "title": "TAUX seasonal cycle std",
            "varpattern": output_variables["SeasonalTauxLonRmse"][0],
            "xname": "longitude",
            "yname": "TAUX std",
            "method": "1) Linearly detrended\n2) Seasonal cycle computed\n3) Standard deviation\n" +
                      "4) Regridded to 1°x1°\n5) Meridional averaged (see box)\n\nMetric: RMSE$_x$",
        },
        "dive_down01": {
            "plot_type": "map",
            "nbr_panel": 2,
            "colorbar": dict_colorbar["amplitude"],
            "label": dict_label["amplitude60"],
            "maskland": True,
            "title": ["TAUX seasonal cycle std"],
            "varpattern": output_variables["SeasonalTauxLonRmse"][1],
            "xname": "longitude",
            "yname": "latitude",
            "zname": "TAUX std",
            "method": "1) Linearly detrended\n2) Seasonal cycle computed\n3) Standard deviation\n" +
                      "4) Regridded to 1°x1°",
        },
        "dive_down02": {
            "plot_type": "hovmoeller",
            "nbr_panel": 2,
            "colorbar": dict_colorbar["anomalies"],
            "label": dict_label["REG80"],
            "title": ["TAUX seasonal cycle", "TAUX seasonal cycle"],
            "varpattern": output_variables["SeasonalTauxLonRmse"][2],
            "xname": "longitude",
            "yname": "months",
            "zname": "TAUX",
            "method": "1) Linearly detrended\n2) Seasonal cycle computed\n3) Regridded to 1°x1°\n" +
                      "5) Meridional averaged (see box)",
        },
    },
    "SeasonalTauyLatRmse": {
        "diagnostic": {
            "plot_type": "curve",
            "nbr_panel": 1,
            "title": "TAUY seasonal cycle std",
            "varpattern": output_variables["SeasonalTauyLatRmse"][0],
            "xname": "latitude",
            "yname": "TAUY std",
            "method": "1) Linearly detrended\n2) Seasonal cycle computed\n3) Standard deviation\n" +
                      "4) Regridded to 1°x1°\n5) Zonal averaged (see box)\n\nMetric: RMSE$_y$",
        },
        "dive_down01": {
            "plot_type": "map",
            "nbr_panel": 2,
            "colorbar": dict_colorbar["amplitude"],
            "label": dict_label["amplitude60"],
            "maskland": True,
            "title": ["TAUY seasonal cycle std"],
            "varpattern": output_variables["SeasonalTauyLatRmse"][1],
            "xname": "longitude",
            "yname": "latitude",
            "zname": "TAUY std",
            "method": "1) Linearly detrended\n2) Seasonal cycle computed\n3) Standard deviation\n" +
                      "4) Regridded to 1°x1°",
        },
        "dive_down02": {
            "plot_type": "hovmoeller",
            "nbr_panel": 2,
            "colorbar": dict_colorbar["anomalies"],
            "label": dict_label["TAUY"],
            "title": ["TAUY seasonal cycle", "TAUY seasonal cycle"],
            "varpattern": output_variables["SeasonalTauyLatRmse"][2],
            "xname": "latitude",
            "yname": "months",
            "zname": "TAUY",
            "method": "1) Linearly detrended\n2) Seasonal cycle computed\n3) Regridded to 1°x1°\n" +
                      "5) Zonal averaged (see box)",

        },
    },
    "SeasonalTauyLonRmse": {
        "diagnostic": {
            "plot_type": "curve",
            "nbr_panel": 1,
            "title": "TAUY seasonal cycle std",
            "varpattern": output_variables["SeasonalTauyLonRmse"][0],
            "xname": "longitude",
            "yname": "TAUY std",
            "method": "1) Linearly detrended\n2) Seasonal cycle computed\n3) Standard deviation\n" +
                      "4) Regridded to 1°x1°\n5) Meridional averaged (see box)\n\nMetric: RMSE$_x$",
        },
        "dive_down01": {
            "plot_type": "map",
            "nbr_panel": 2,
            "colorbar": dict_colorbar["amplitude"],
            "label": dict_label["amplitude60"],
            "maskland": True,
            "title": ["TAUY seasonal cycle std"],
            "varpattern": output_variables["SeasonalTauyLonRmse"][1],
            "xname": "longitude",
            "yname": "latitude",
            "zname": "TAUY std",
            "method": "1) Linearly detrended\n2) Seasonal cycle computed\n3) Standard deviation\n" +
                      "4) Regridded to 1°x1°",
        },
        "dive_down02": {
            "plot_type": "hovmoeller",
            "nbr_panel": 2,
            "colorbar": dict_colorbar["anomalies"],
            "label": dict_label["REG80"],
            "title": ["TAUY seasonal cycle", "TAUY seasonal cycle"],
            "varpattern": output_variables["SeasonalTauyLonRmse"][2],
            "xname": "longitude",
            "yname": "months",
            "zname": "TAUY",
            "method": "1) Linearly detrended\n2) Seasonal cycle computed\n3) Regridded to 1°x1°\n" +
                      "5) Meridional averaged (see box)",
        },
    },
}


reference_observations = {
    "ssh": "AVISO", "pr": "GPCPv2.3", "sst": "Tropflux", "lhf": "Tropflux", "lwr": "Tropflux", "shf": "Tropflux",
    "slp": "ERA-Interim", "swr": "Tropflux", "taux": "Tropflux", "thf": "Tropflux"
}

def metric_variable_names(mc=True):
    if isinstance(mc, str) is True and mc in list(output_variables.keys()):
        dict_out = output_variables[mc]
    else:
        dict_out = deepcopy(output_variables)
    return dict_out

def plot_param(metric_collection, metric):
    dict_MC = defCollection(metric_collection)
    dict_MCm = dict_MC["metrics_list"][metric]
    # get plot parameters
    dict_out = plot_parameters[metric.replace("_1", "").replace("_2", "").replace("_3", "")]
    # get metric computation
    if metric_collection in ["ENSO_tel", "test_tel"] and "Map" in metric:
        computation = ["CORR", "RMSE"]
    elif "rmse" in metric.lower():
        computation = "RMSE"
    elif "corr" in metric.lower():
        computation = "CORR"
    else:
        try:
            computation = dict_MCm["metric_computation"]
        except:
            try:
                computation = dict_MC["common_collection_parameters"]["metric_computation"]
            except:
                computation = default_arg_values("metric_computation")
    dict_out["metric_computation"] = computation
    # get metric variables
    variables = dict_MCm["variables"]
    dict_out["metric_variables"] = variables
    # get metric reference
    references = dict((var, reference_observations[var]) for var in variables)
    if "sst" in variables and len(variables) > 1:
        references["sst"] = "Tropflux"
    refname = references[variables[0]]
    for var in variables[1:]:
        refname = refname + "_" + references[var]
    if metric_collection in ["ENSO_tel", "test_tel"] and metric in\
            ["EnsoSstMap", "NinaSstMap", "NinoSstMap", "EnsoSstMapDjf", "NinoSstMapDjf", "NinaSstMapDjf",
             "EnsoSstMapJja", "NinoSstMapJja", "NinaSstMapJja"]:
        refname = "ERA-Interim"
    dict_out["metric_reference"] = refname
    # get variable regions
    dict_out["metric_regions"] = dict_MCm["regions"]
    return dict_out
