nums = ["w","w","w","l","l","d","l","w","w","l"]

#maximum streak
max=1
current=1
cur_char=nums[0]


for i in range(1,len(nums)):
    if nums[i]==nums[i-1]:
        current+=1
        if current>max:
            max=current
            cur_char=nums[i]
    else:
        current=1
        
print(f'{cur_char} : {max}')

#all streaks
freq=[]
current=1
cur_char=nums[0]

for i in range(1,len(nums)):
    if nums[i]==nums[i-1]:
        current+=1
    else:
        freq.append((cur_char,current))
        current=1
        cur_char=nums[i]
        
freq.append((cur_char,current))
print(freq)

#count only "w"
count=0
char="w"
for i in range(len(nums)):
    if nums[i]==char:
        count+=1
    
print(char,count)

        
    
    
    
    
    
    
    