
def count_bob(s):
    count = 0
    while len(s) > 0:
        if s[0:3] == "bob":
            count += 1
        s = s[1:]
    return "Number of times 'bob' occurs is: ", count

    
            
                           

print(count_bob('eybonbobobmbobbobbbobobob'))
