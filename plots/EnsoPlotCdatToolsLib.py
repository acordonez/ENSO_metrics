# -*- coding:UTF-8 -*-
# ---------------------------------------------------#
# Aim of the program:
#      Provide functions based on CDAT (https://cdat.llnl.gov/) used for plots
# ---------------------------------------------------#


# ---------------------------------------------------#
# Import packages
# ---------------------------------------------------#
from copy import deepcopy
from inspect import stack as INSPECTstack
# CDAT
from cdms2 import setAutoBounds as CDMS2setAutoBounds
from cdms2 import open as CDMS2open
from MV2 import maximum as MV2maximum
from MV2 import minimum as MV2minimum
# ENSO_metrics package functions:
from EnsoMetrics import EnsoErrorsWarnings


# ---------------------------------------------------#


# ---------------------------------------------------#
# Parameters
# ---------------------------------------------------#
# Colors for prints
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
# ---------------------------------------------------#


# ---------------------------------------------------------------------------------------------------------------------#
# Functions
# ---------------------------------------------------------------------------------------------------------------------#
def minimaxi(array, mini=1e20, maxi=-1e20):
    """
    #################################################################################
    Description:
    Find the minimum and the maximum
    #################################################################################

    :param array: masked_array
        masked_array for which the minimum and maximum values are wanted
    :param mini: float, optional
        preset minimum value
        default is 1e20
    :param maxi: float, optional
        preset maximum value
        default is -1e20

    :return: list
        minimum and maximum values
    """
    if isinstance(array, list) is True:
        for tmp in array:
            v1, v2 = float(MV2minimum(tmp)), float(MV2maximum(tmp))
            if v1 < mini:
                mini = deepcopy(v1)
            if v2 > maxi:
                maxi = deepcopy(v2)
    else:
        v1, v2 = float(MV2minimum(array)), float(MV2maximum(array))
        if v1 < mini:
            mini = deepcopy(v1)
        if v2 > maxi:
            maxi = deepcopy(v2)
    return mini, maxi

def read_data(netcdf_file, netcdf_var, mod_name, ref_name, dict_diagnostic, dict_metric, member=None,
              netcdf_var_extra=None):
    """
    #################################################################################
    Description:
    Read and organize the given variables and associated metadata from the given netCDF file
    Select diagnostic and metric values
    #################################################################################

    :param netcdf_file: string
        path and file name of the netcdf file to read
        e.g., '/path/to/file/file_name.nc'
    :param netcdf_var: list
        list of the variable patterns to read
        e.g., ['var1__', 'var2__']
    :param mod_name: string
        name of the model
        e.g., 'ACCESS1-0'
    :param ref_name: string
        name of the reference observational dataset
        e.g., 'ERA-Interim'
    :param dict_diagnostic: dictionary
        dictionary containing the diagnostic values of the model and the observational datasets
        e.g., {'ACCESS1-0': 1., 'ERA-Interim': 1.}
    :param dict_metric: dictionary
        dictionary containing the metric values comparing the model to the observational datasets
        e.g., {'ERA-Interim': 1.}
    :param member: string, optional
        name of the model's member
        e.g., 'r1i1p1'
        default is None
    :param netcdf_var_extra: list
        list of the extra variable patterns to read if available
        e.g., ['extra_var1__', 'extra_var2__']

    :return:
    """
    # open netcdf file
    CDMS2setAutoBounds("on")
    ff = CDMS2open(netcdf_file)
    # global attributes
    att_glo = read_global_attributes(ff)
    # list the variables in the file
    list_variables = sorted(ff.listvariables(), key=lambda v: v.upper())
    # read netcdf
    dict_mod, dict_mod_extra, dict_ref, dict_ref_extra = dict(), dict(), dict(), dict()
    for var in netcdf_var:
        var_name1 = str(var) + str(mod_name)
        var_name2 = str(var_name1) + "_" + str(member) if isinstance(member, str) is True else None
        if var_name1 not in list_variables and (var_name2 is None or var_name2 not in list_variables):
            arr, att = None, None
            my_name = deepcopy(var_name1)
            if isinstance(member, str) is True:
                my_name += " or " + str(var_name2)
            list_strings = [
                "ERROR" + EnsoErrorsWarnings.message_formating(INSPECTstack()) + ": cannot find given variable",
                str().ljust(5) + "cannot find " + str(my_name) + " in " + str(netcdf_file),
                str().ljust(5) + "variables in file: " + str(list_variables)]
            EnsoErrorsWarnings.my_error(list_strings)
        elif var_name1 in list_variables:
            arr, att = read_variable_and_attributes(ff, var_name1)
        else:
            arr, att = read_variable_and_attributes(ff, var_name2)
        dict_mod[var] = {"array": arr, "attributes": att}
        del arr, att, var_name1, var_name2
        var_name1 = str(var) + str(ref_name)
        var_name2 = str(var_name1) + "_" + str(ref_name)
        if var_name1 not in list_variables and var_name2 not in list_variables:
            arr, att = None, None
            list_strings = [
                "ERROR" + EnsoErrorsWarnings.message_formating(INSPECTstack()) + ": cannot find given variable",
                str().ljust(5) + "cannot find " + str(var_name1) + " or " + str(var_name2) + " in " + str(netcdf_file),
                str().ljust(5) + "variables in file: " + str(list_variables)]
            EnsoErrorsWarnings.my_error(list_strings)
        elif var_name1 in list_variables:
            arr, att = read_variable_and_attributes(ff, var_name1)
        else:
            arr, att = read_variable_and_attributes(ff, var_name2)
        dict_ref[var] = {"array": arr, "attributes": att}
        del arr, att, var_name1, var_name2
    if isinstance(netcdf_var_extra, list) is True:
        for var in netcdf_var_extra:
            var_name1 = str(var) + str(mod_name)
            var_name2 = str(var_name1) + "_" + str(member) if isinstance(member, str) is True else None
            if var_name1 not in list_variables and (var_name2 is None or var_name2 not in list_variables):
                arr, att = None, None
            elif var_name1 in list_variables:
                arr, att = read_variable_and_attributes(ff, var_name1)
            else:
                arr, att = read_variable_and_attributes(ff, var_name2)
            if arr is not None:
                dict_mod_extra[var] = {"array": arr, "attributes": att}
            del arr, att, var_name1, var_name2
            var_name1 = str(var) + str(ref_name)
            var_name2 = str(var_name1) + "_" + str(ref_name)
            if var_name1 not in list_variables and var_name2 not in list_variables:
                arr, att = None, None
            elif var_name1 in list_variables:
                arr, att = read_variable_and_attributes(ff, var_name1)
            else:
                arr, att = read_variable_and_attributes(ff, var_name2)
            if arr is not None:
                dict_ref_extra[var] = {"array": arr, "attributes": att}
            del arr, att, var_name1, var_name2
    # read diagnostic value
    list_keys = sorted(list(dict_diagnostic.keys()), key=lambda v: v.upper())
    var_name1 = deepcopy(mod_name)
    var_name2 = str(var_name1) + "_" + str(member) if isinstance(member, str) is True else None
    if var_name1 not in list_keys and (var_name2 is None or var_name2 not in list_keys):
        dia_mod = None
        my_name = deepcopy(var_name1)
        if isinstance(member, str) is True:
            my_name += " or " + str(var_name2)
        list_strings = [
            "ERROR" + EnsoErrorsWarnings.message_formating(INSPECTstack()) + ": cannot find diagnostic for given model",
            str().ljust(5) + "cannot find " + str(my_name) + " in given dictionary",
            str().ljust(5) + "dictionary keys: " + str(list_keys)]
        EnsoErrorsWarnings.my_error(list_strings)
    elif var_name1 in list_keys:
        dia_mod = dict_diagnostic[var_name1]
    else:
        dia_mod = dict_diagnostic[var_name2]
    var_name1 = deepcopy(ref_name)
    var_name2 = str(var_name1) + "_" + str(ref_name)
    if var_name1 not in list_keys and var_name2 not in list_keys:
        dia_ref = None
        list_strings = [
            "ERROR" + EnsoErrorsWarnings.message_formating(INSPECTstack()) +
            ": cannot find diagnostic for given reference",
            str().ljust(5) + "cannot find " + str(var_name1) + " or " + str(var_name2) + " in given dictionary",
            str().ljust(5) + "dictionary keys: " + str(list_keys)]
        EnsoErrorsWarnings.my_error(list_strings)
    elif var_name1 in list_keys:
        dia_ref = dict_diagnostic[var_name1]
    else:
        dia_ref = dict_diagnostic[var_name2]
    # read metric value
    list_keys = sorted(list(dict_metric.keys()), key=lambda v: v.upper())
    if var_name1 not in list_keys and var_name2 not in list_keys:
        met_val = None
        list_strings = [
            "ERROR" + EnsoErrorsWarnings.message_formating(INSPECTstack()) + ": cannot find metric for given reference",
            str().ljust(5) + "cannot find " + str(var_name1) + " or " + str(var_name2) + " in given dictionary",
            str().ljust(5) + "dictionary keys: " + str(list_keys)]
        EnsoErrorsWarnings.my_error(list_strings)
    elif var_name1 in list_keys:
        met_val = dict_metric[var_name1]
    else:
        met_val = dict_metric[var_name2]
    return dict_mod, dict_ref, dia_mod, dia_ref, met_val, att_glo, dict_mod_extra, dict_ref_extra


def read_global_attributes(opened_file):
    attributes = dict()
    for att in opened_file.listglobal():
        tmp = opened_file.attributes[att]
        if isinstance(tmp, list) is True and len(tmp) == 1:
            tmp = tmp[0]
        attributes[att] = tmp
        del tmp
    return attributes


def read_variable_and_attributes(opened_file, variable_name):
    array = opened_file(variable_name)
    attributes = dict()
    for att in opened_file.listattribute(variable_name):
        tmp = opened_file.getattribute(variable_name, att)
        if isinstance(tmp, list) is True and len(tmp) == 1:
            tmp = tmp[0]
        attributes[att] = tmp
        del tmp
    return array, attributes
# ---------------------------------------------------------------------------------------------------------------------#