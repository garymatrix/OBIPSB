import chardet
with open('spam.csv', 'rb') as rawdata: ##input the required filename 
    result = chardet.detect(rawdata.read(100000))
print (result)
