#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Jan  9 20:56:30 2017

@author: Sri
"""

from GetData import get_data
import pandas as pd


#TODO: what is advisory committee description

def number_of_devices():
    """
    Function returns the number of devices in Pre Market Approval
    """
    api = "https://api.fda.gov/device/pma.json?search=medical_specialty_description:ophthalmic"
    data = get_data(api)
    number_of_devices = data[0]["results"]["total"]
    return number_of_devices


def device_PMA_by_date_received():
    """
    Functiont to analyze the number of PMA devices by date received"""
    
    api = "https://api.fda.gov/device/pma.json?search=advisory_committee_description:ophthalmic&count=date_received"
    data = get_data(api)
    data_f = pd.DataFrame(data[1])

    data_f = data_f.rename(columns={"count": "Number of PMA devices", "time": "time"})
    data_f["time"] = pd.to_datetime(data_f["time"])
    data_f["year"] = data_f["time"].dt.year

    data_f_grouped_year= data_f.groupby("year").sum()

    plot1 = data_f_grouped_year.plot(figsize=(8,8), title="Number of PMA devices over time")
    plot1.set_ylabel("Number of PMA devices")
    
    ###################
    data_f_grouped_year = data_f_grouped_year.reset_index()
    data_f_1971 = data_f_grouped_year[data_f_grouped_year["year"]>=1971]
    print data_f_1971
    
    
    plot2 = data_f_1971.plot(x="year", y="Number of PMA devices", title="Number of PMA devices since 1971", 
                             figsize=(8,8))
    plot2.set_ylabel("Number of PMA devices")
    
    


def device_PMA_by_decision_date():
    api = "https://api.fda.gov/device/pma.json?search=advisory_committee_description:ophthalmic&count=decision_date"
    data = get_data(api)
    data_f = pd.DataFrame(data[1])

    data_f = data_f.rename(columns={"count": "Number of PMA devices", "time": "time"})
    data_f["time"] = pd.to_datetime(data_f["time"])
    data_f["year"] = data_f["time"].dt.year

    data_f_grouped_year= data_f.groupby("year").sum()

    plot1 = data_f_grouped_year.plot(kind="line",figsize=(8,8), 
                                     title="Number of PMA devices by decision date over time")
    plot1.set_ylabel("Number of PMA devices")
    

def device_PMA_by_expedited_review_flag():
    api = "https://api.fda.gov/device/pma.json?search=advisory_committee_description:ophthalmic+AND+expedited_review_flag:Y&count=decision_date"
    data = get_data(api)
    data_f = pd.DataFrame(data[1])
    
    data_f =data_f.rename(columns={"count": "Number of PMA approvals expedited", "time": "time"})
    data_f["time"] = pd.to_datetime(data_f["time"])
    data_f["year"] = data_f["time"].dt.year
    data_f_grouped_year= data_f.groupby("year").sum()
    plot1 = data_f_grouped_year.plot(kind="bar", y= "Number of PMA approvals expedited",
                                     figsize=(8,8), title="Number of PMA devices approvals that are expedited")
    plot1.set_ylabel("Number of PMA devices")
    
    ###################################
    api2 = "https://api.fda.gov/device/pma.json?search=advisory_committee_description:ophthalmic+AND+expedited_review_flag:Y&count=device_class"
    data2 = get_data(api2)
    print data2[1]

    ##################################
    
    #expedited PMA by state
    api3 = "https://api.fda.gov/device/pma.json?search=advisory_committee_description:ophthalmic+AND+expedited_review_flag:Y&count=state"
    data3 = get_data(api3)
    data_f3 = pd.DataFrame(data3[1])
    print data_f3
    data_f3 =data_f3.rename(columns={"count": "Number of PMA approvals expedited", "term": "state"})
    plot2 = data_f3.plot(kind="bar", x= "state", y= "Number of PMA approvals expedited",
                        figsize=(8,8), title="Number of PMA devices approvals that are expedited by state")
    plot2.set_ylabel("Number of PMA devices")
    

def device_PMA_by_product_code():
    api = ""
    pass


def device_PMA_by_state():
    api = "https://api.fda.gov/device/pma.json?search=advisory_committee_description:ophthalmic&count=state"
    data = get_data(api)
    data_f = pd.DataFrame(data[1])
    print data_f
    data_f =data_f.rename(columns={"count": "Number of PMA approvals expedited", "term": "state"})
    plot = data_f.plot(kind="barh", x= "state", y= "Number of PMA approvals expedited",
                        figsize=(8,8), title="Number of PMA devices approvals by state")
    plot.set_ylabel("State")



def device_class():
    api = "https://api.fda.gov/device/pma.json?search=advisory_committee_description:ophthalmic&count=device_class"
    data = get_data(api)
    data_f = pd.DataFrame(data[1])
    print data_f
    data_f =data_f.rename(columns={"count": "Number of PMA approvals expedited", "term": "device class"})
    plot1 = data_f.plot.pie(subplots=True, figsize=(6,6), 
                                                       title="Number of PMA devices by device class", autopct='%0.2f',
                                                      fontsize = 13, labels = ["class 3", "class2", "class 1"])



    


def main():
    device_PMA_by_state()


if __name__ == "__main__":
    main()