# -*- coding: utf-8 -*-
"""
Created on Mon Oct 19 20:56:04 2020

@author: chinmay.bhelke
"""

# Class Company: Represents a company
#-------------------------------------------------
class Company:
    def __init__(self, n, t, s):
        self.__name = n
        self.ticker = t
        self.__value = ""
        self.sector = s

    def __repr__(self):
        return "{} {} {}={}".format(  self.__name, self.ticker, self.sector, self.__value)
    
    def __str__(self):
        return " {} ({}) : {}".format( self.__name, self.ticker, self.__value)
    
    def IsInSectorList(self,sectorList):
        return self.sector in sectorList
    
    def IsInSector(self,sector):
        return self.sector == sector
    
    def SetValue (self,value):
        self.__value = value
        
    def GetValue(self):
        return self.__value

# Class Sector: Represents a sector for company
#-------------------------------------------------
class Sector:
    def __init__(self, idx, name):
        self.idx = idx
        self.name = name
    def __repr__(self):
        return"{} {}".format(self.idx, self.name)    


# Class Sector: Represents a colletion of companies
#-------------------------------------------------
class CompanyStore:
    def __init__ (self, input_file_name):
        self.__all_companies = self.__load_companies_from_file(input_file_name)
        assert self.__all_companies is not None, "Can not read data file"
              
    def __load_companies_from_file(self,input_file_name):
        try:
            input_file = open(input_file_name, "r")
            companies = []
            for line in input_file:
                line = line.strip()
                arr = line.split(',')
                if arr[2] != 'Sector':
                    c = Company(arr[1],arr[0],arr[2])
                    companies.append(c)
        
            input_file.close()
            return companies
        except:
            return None
        
    def get_sectors(self):
        dictionary = dict()
        for c in self.__all_companies:
            if not c.IsInSectorList ( dictionary.keys()):
                dictionary[c.sector]= Sector(len(dictionary)+1,c.sector)
        return dictionary.values()
    
    def get_companies_by_sector(self,sector):
        selected_companies = []
        for c in self.__all_companies:
            if c.IsInSector(sector):
                selected_companies.append(c)
        return selected_companies

#Unit Testing Block

if __name__ == '__main__':

# Company
    c=Company('name','tkr','dummy')
    assert c.ticker == 'tkr', "Wrong ticker for company"
    c.SetValue(12345)
    assert c.GetValue()== 12345, "can not set value for company"
    assert c.__repr__() =="name tkr dummy=12345", "wrong attibute for company"
    
    assert c.IsInSector('dummy'), "wrong IsInSector dummy"
    assert not c.IsInSector('one'), "wrong IsInSector one"

    assert c.IsInSectorList(['dummy','one']), "wrong IsInSectorList dummy"
    assert not c.IsInSector(['one','two']), "wrong IsInSectorList one"

# Sector
    s=Sector(1,'Test Sector')
    assert s.idx == 1, "Wrong index for sector"
    assert s.name == 'Test Sector', "Wrong name for sector"
    assert s.__repr__() == "1 Test Sector"

# CompanyStore
    store = CompanyStore("sp500.txt")
    list = store.get_sectors()
    assert list is not None, "Can not get sector list from store"
    assert len(list)>0, "Got empty sector list from store"
    firstSector = ""
    for s in list:
        if s.idx==1:
            firstSector=s.name
    assert firstSector != "", "Dod not find first sector value"
    companies = store.get_companies_by_sector(firstSector)
    assert companies is not None, "Can not get company list from store"
    assert len(companies)>0, "Got empty company list from store"
    
    
    