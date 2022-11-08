## simple hashing function

# create a hash table of size 10
hash_table = [None]* 10
print(hash_table)
# [None, None, None, None, None, None, None, None, None, None]

# Modulo operator (%) is used in the hashing function

def hashing_func(key):
    return key % len(hash_table)

print (hashing_func(10)) # Output: 0
print (hashing_func(20)) # Output: 0
print (hashing_func(25)) # Output: 5

# insert elements in hash table
def insert(hash_table,key,value):
    hash_key = hashing_func(key)
    hash_table[hash_key] = value 

insert(hash_table, 10, 'India')
print (hash_table)
# Output: 
# ['India', None, None, None, None, None, None, None, None, None]

insert(hash_table, 25, 'USA')
print (hash_table)
# Output: 
# ['Nepal', None, None, None, None, 'USA', None, None, None, None]



## Collision Resolution

hash_table = [[] for _ in range(10)]
print (hash_table)
# Output: 
# [[], [], [], [], [], [], [], [], [], []]

def insert(hash_table, key, value):
    hash_key = hashing_func(key)
    hash_table[hash_key].append(value)

insert(hash_table, 10, 'Nepal')
print (hash_table)
# Output: 
# [['Nepal'], [], [], [], [], [], [], [], [], []]

insert(hash_table, 25, 'USA')
print (hash_table)
# Output: 
# [['Nepal'], [], [], [], [], ['USA'], [], [], [], []]

insert(hash_table, 20, 'India')
print (hash_table)
# Output: 
# [['Nepal', 'India'], [], [], [], [], ['USA'], [], [], [], []]


## hash function

hash_key = hash(25) % len(hash_table)
print (hash_key) # Output: 5

hash_key = hash('20') % len(hash_table)
print (hash_key) # Output: 4

# Create empty Hash Table
hash_table = [[] for _ in range(10)]

def insert(hash_table, key, value):
    hash_key = hash(key) % len(hash_table)
    key_exists = False
    bucket = hash_table[hash_key]   
    for i, kv in enumerate(bucket):
        k, v = kv
        if key == k:
            key_exists = True 
            break
    if key_exists:
        bucket[i] = ((key, value))
    else:
        bucket.append((key, value))

insert(hash_table,10,'India')
insert(hash_table,20,'USA')
print(hash_table)
# [[(10, 'India'), (20, 'USA')], [], [], [], [], [], [], [], [], []]

# Search Data from the Hash Table

def search(hash_table,key):
    hash_key = hash(key) % len(hash_table)
    bucket = hash_table[hash_key]

    for i , kv in enumerate(bucket):
        k, v = kv
        if key == k :
            return v

print (search(hash_table, 10)) # Output: India
print (search(hash_table, 30)) # Output: None

# Delete Data from the Hash Table
def delete(hash_table, key):
    hash_key = hash(key) % len(hash_table)  
    key_exists = False
    bucket = hash_table[hash_key]
    for i, kv in enumerate(bucket):
        k, v = kv 
        if key == k:
            key_exists = True 
            break
    if key_exists:
        del bucket[i]
        print ('Key {} deleted'.format(key))
    else:
        print ('Key {} not found'.format(key))

delete(hash_table, 100)
delete(hash_table, 10)
print(hash_table)
