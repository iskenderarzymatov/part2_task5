classroom1 = int(input("davai 4islo: ")) 
classroom2 = int(input("davai ewe: "))    
classroom3 = int(input("ewe: "))

tab1=classroom1 // 2
tab11=classroom1 % 2
if tab11 == True:
    tab1 += 1

tab2=classroom2 // 2
tab22=classroom2 % 2
if tab22 == True:
    tab2 += 1

tab3=classroom3 // 2
tab33=classroom3 % 2
if tab33 == True:
    tab3 += 1

sms = tab1 + tab2 + tab3
print(sms)




