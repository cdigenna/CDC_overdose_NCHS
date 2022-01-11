#
# READ THIS
#   This tools is NOT coded with safety, efficiency, or elegance in mind. Use at your own risk. 
#
# VS13MORT Parser.py
# Author tommaho
# Hosted at https://github.com/tommaho/VS13MORT.DUSMCPUB-Parser
#
# About
#   Converts the 2013 Mortality file located here: http://www.cdc.gov/nchs/data_access/vitalstatsonline.htm
#   to a CSV, based on data file documentation here: http://www.cdc.gov/nchs/data/dvs/Record_Layout_2013.pdf
# Edits
#
# 11-2-2015
#  - removed space from filename. 
#
# Directions
#
# 1. Have Python installed.
# 2. Get & unzip mortality file
# 3. Tweak fileObj and FileOutObj to point to the source and destination of your choosing.
#


fileObj = open("VS20MORT.DUSMCPUB_r20220105",'r')
fileOutObj = open("Data\mort2020.csv","a")

fileOutObj.write('Resident_Status, Education, Month_Of_Death, sex, Age_Key, age, Age_Sub_Flag, ager52, Age_Recode_27, ' + \
                 'Age_Recode_12, Infant_Age_Recode_22, placdth, Marital_Status, DOW_of_Death, year, Injured_At_Work, ' + \
                 'Manner_Of_Death, Method_Of_Disposition, Autopsy, Activity_Code, Place_Of_Causal_Injury,  ucod, Cause_Recode_358, ' + \
                 'Cause_Recode_113, Infant_Cause_Recode_130, Cause_Recode_39, Entity_Axis_Conditions, EAC1, EAC2, EAC3, EAC4, EAC5, ' + \
                 'EAC6, EAC7, EAC8, EAC9, EAC10, EAC11, EAC12, EAC13, EAC14, EAC15, EAC16, EAC17, EAC18, EAC19, EAC20, ' + \
                 'Record_Axis_Conditions, record_1, record_2, record_3, record_4, record_5, record_6, record_7, record_8, record_9, ' + \
				 'record_10, record_11, record_12, record_13, record_14, record_15, record_16, record_17, record_18, record_19, record_20, ' + \
				 'race, Race_Bridged, Race_Imputation, Race_Recode_3, Race_Recode_5, ' + \
                 'hispanic, Hispanic_Origin_Recode\n')

outStr = ""

for line in fileObj:

               Resident_Status = line[19].strip()
               Education = line[60:62].strip()
               Month_Of_Death = line[63:67].strip()
               sex = line[68].strip()
               Age_Key = line[69].strip()
               age = line[70:73].strip()
               Age_Sub_Flag = line[73].strip()
               ager52 = line[74:76].strip()
               Age_Recode_27 = line[76:78].strip()
               Age_Recode_12 = line[78:80].strip()
               Infant_Age_Recode_22 = line[80:82].strip()
               placdth = line[82].strip()
               Marital_Status = line[83].strip()
               DOW_of_Death = line[84].strip()
               year = line[101:105].strip()
               Injured_At_Work = line[105].strip()
               Manner_Of_Death = line[106].strip()
               Method_Of_Disposition = line[107].strip()
               Autopsy = line[108].strip()
               Activity_Code = line[143].strip()
               Place_Of_Causal_Injury = line[144].strip()
               ucod = line[145:149].strip()
               Cause_Recode_358 = line[149:152].strip()
               Cause_Recode_113 = line[153:156].strip()
               Infant_Cause_Recode_130 = line[156:159].strip()
               Cause_Recode_39 = line[159:161].strip()
               Entity_Axis_Conditions = line[162:164].strip()
               EAC1 = line[164:171].strip()
               EAC2 = line[171:178].strip()
               EAC3 = line[178:185].strip()
               EAC4 = line[185:192].strip()
               EAC5 = line[192:199].strip()
               EAC6 = line[199:206].strip()
               EAC7 = line[206:213].strip()
               EAC8 = line[213:220].strip()
               EAC9 = line[220:227].strip()
               EAC10 = line[227:234].strip()
               EAC11 = line[234:241].strip()
               EAC12 = line[241:248].strip()
               EAC13 = line[248:255].strip()
               EAC14 = line[255:262].strip()
               EAC15 = line[262:269].strip()
               EAC16 = line[269:276].strip()
               EAC17 = line[276:283].strip()
               EAC18 = line[283:290].strip()
               EAC19 = line[290:297].strip()
               EAC20 = line[297:304].strip()
               Record_Axis_Conditions = line[340:342]
               record_1 = line[343:348].strip()
               record_2 = line[348:353].strip()
               record_3 = line[353:358].strip()
               record_4 = line[358:363].strip()
               record_5 = line[363:368].strip()
               record_6 = line[368:373].strip()
               record_7 = line[373:378].strip()
               record_8 = line[378:383].strip()
               record_9 = line[383:388].strip()
               record_10 = line[388:393].strip()
               record_11 = line[393:398].strip()
               record_12 = line[398:403].strip()
               record_13 = line[403:408].strip()
               record_14 = line[408:413].strip()
               record_15 = line[413:418].strip()
               record_16 = line[418:423].strip()
               record_17 = line[423:428].strip()
               record_18 = line[428:433].strip()
               record_19 = line[433:438].strip()
               record_20 = line[438:443].strip()
               race = line[444:446].strip()
               Race_Bridged = line[446].strip()
               Race_Imputation = line[447].strip()
               Race_Recode_3 = line[448].strip()
               Race_Recode_5 = line[449].strip()
               hispanic = line[483:486].strip()
               Hispanic_Origin_Recode = line[487].strip()
               
               
               
               
               
               outStr = (Resident_Status +              ', ' + Education +              ', ' + Month_Of_Death +         ', ' + sex + \
                         ', ' + Age_Key +               ', ' + age +              		', ' + Age_Sub_Flag +           ', ' + ager52 + \
                         ', ' + Age_Recode_27 +         ', ' + Age_Recode_12 +          ', ' + Infant_Age_Recode_22 +   ', ' + placdth + \
                         ', ' + Marital_Status +        ', ' + DOW_of_Death +           ', ' + year +              		', ' + Injured_At_Work +  \
                         ', ' + Manner_Of_Death +       ', ' + Method_Of_Disposition +  ', ' + Autopsy +                ', ' + Activity_Code + \
                         ', ' + Place_Of_Causal_Injury +', ' + ucod +                  	', ' + Cause_Recode_358 +       ', ' + Cause_Recode_113 +  \
                         ', ' + Infant_Cause_Recode_130 + ', ' + Cause_Recode_39 +      ', ' + Entity_Axis_Conditions + ', ' + EAC1 + \
                         ', ' + EAC2 +                  ', ' + EAC3 +                   ', ' + EAC4 +                   ', ' + EAC5 + \
                         ', ' + EAC6 +                  ', ' + EAC7 +                   ', ' + EAC8 +                   ', ' + EAC9 + \
                         ', ' + EAC10 +                 ', ' + EAC11 +                  ', ' + EAC12 +                  ', ' + EAC13 + \
                         ', ' + EAC14 +                 ', ' + EAC15 +                  ', ' + EAC16 +                  ', ' + EAC17 + \
                         ', ' + EAC18 +                 ', ' + EAC19 +                  ', ' + EAC20 +                  ', ' + Record_Axis_Conditions + \
                         ', ' + record_1 +              ', ' + record_2 +               ', ' + record_3 +               ', ' + record_4 + \
                         ', ' + record_5 +              ', ' + record_6 +               ', ' + record_7 +               ', ' + record_8 + \
                         ', ' + record_9 +              ', ' + record_10 +         		', ' + record_11 +              ', ' + record_12 + \
                         ', ' + record_13 +             ', ' + record_14 +          	', ' + record_15 +              ', ' + record_16 + \
                         ', ' + record_17 +             ', ' + record_18 +              ', ' + record_19 +             	', ' + record_20 + \
                         ', ' + race +                  ', ' + Race_Bridged +           ', ' + Race_Imputation +        ', ' + Race_Recode_3 + \
                         ', ' + Race_Recode_5 +         ', ' + hispanic +        		', ' + Hispanic_Origin_Recode + '\n')


               
               fileOutObj.write(outStr)



print("Parse complete.")
fileOutObj.close()
fileObj.close()

