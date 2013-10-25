s1 = "hellolovely"
s2 = "world"
s3 = ""
x = 0

if len(s1) == len(s2):    
    while x < len(s1):
        s3 += s3.join([s1[x]])
        s3 += s3.join([s2[x]])
        x += 1
        
else:
    if len(s1) < len(s2):
        shorter_str = s1
        longer_str = s2
    else:
        shorter_str = s2
        longer_str = s1

    while x < len(shorter_str):    
        s3 += s3.join([s1[x]])
        s3 += s3.join([s2[x]])
        x += 1
   
    while x < len(longer_str):
        s3 += s3.join([longer_str[x]])
        x += 1
 
