import hashlib 

key = "yzbqklnj"

i = 0
not_found = True
while (not_found):
    new_key = key + str(i)
    h = hashlib.md5(new_key.encode())
    if (str(h.hexdigest()).startswith('00000')):
        not_found = False
    else:
        i+=1
    
print(i)
    
