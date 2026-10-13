text = input()
pattern = input()

def find_pattern():
    for i in range(len(text)):
        if text[i:i+len(pattern)] == pattern:
            ans = i
            break
        else:
            ans = -1
    
    return ans

print(find_pattern())