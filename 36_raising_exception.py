# raising exception

def increment(num):
    try:
        return int(num)+1
    except:
        raise ValueError(" Inavlid value")
    
a = increment('def34')
print(a)