# -*- coding: utf-8 -*-
"""Untitled2.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1vGQ6rI3JAMdv-BfrWepbAEfhhl6tA7J_
"""

def kasallik_tashxis(alomat):
  if alomat=="bosh ogrig'i,istima" :
   return "Sizda grip belgilari bor"
  elif alomat=="qorin og'rig'i":
    return "sizda spazma bor"
  elif alomat=="yutal,burun oqishi":
    return "sizda grip bor"
  elif alomat=="tish og'tig'i":
   return "sizda kares bulishi mumkin"
  elif alomat=="bosh aylanishi ":
   return "siz garen bulib turgan bulishiz mumkin"
  elif alomat=="ich qotishi ":
   return "sizda qabziyat bulishi mumkin"
  elif alomat=="bug'imlar  og'tig'i":
   return "sizda kalsiy yetish movchiligi bulishi mumkin"
  elif alomat== "tish g'irchillatish ":
   return "sizga gijjalar bulishi mumlin "
  elif alomat== "kungil aynishi ":
   return "sizda ovqatdan zaxarlanish bulishi mumkin"
  else:
    return "Shifokorga murojaat qiling"
alomat=input("belgini kiriting")
natija=kasallik_tashxis(alomat)
print(natija)

def Telefon_narxi(turi):
  if turi=="Xiaomi Redmi Note 13 Pro" :
   return "2978000 so'mdan"
  elif turi=="Xiaomi Redmi Note 13":
    return "2360000 so'mdan"
  elif turi=="Xiaomi Redmi Note 13 Pro+":
    return "5015400 so'mdan"
  elif turi=="Xiaomi Redmi Note 13C":
   return "1765000 so'mdan"
  elif turi=="Xiaomi Redmi Note 11T Pro ":
   return "4583000 so'mdan"
  elif turi=="Xiaomi Redmi Note A3":
   return "1172000 so'mdan"
  elif turi=="Xiaomi Redmi Note 12":
   return "1999000 so'mdan"
  elif turi== "Xiaomi Redmi Note 11E Pro":
   return "2790000 so'mdan "
  elif turi== "Xiaomi Redmi K50 Ultra ":
   return "7101000 so'mdan"
  else:
    return "Sotuvchiga Murojaat qiling "
turi=input("turini kiritin")
natija=Telefon_narxi(turi)
print(natija)