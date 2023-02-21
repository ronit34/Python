def merge_the_tools(s, k):
    
    substrings = [s[i:i+k] for i in range(0, len(s), k)]
    
    
    for substring in substrings:
        
        seen = set()
        
        for char in substring:
            
            if char not in seen:
                print(char, end='')
                seen.add(char)
        
        print()
merge_the_tools("AABCAAADA",3)