
def split(word):
    return [char for char in word]

#file_text = "VIMMZNYMNMNGpEtjfWlWym5m5jiDhD0AFZZIIFJdFAQkVMdJMFVgqHfTtDlTmj5zlmjTyTkDZdMMMMYMZZZYMZNZNONNWzTtTtzjGjG1Tkjzz0zl1gUFRQNMYR"

#file_text = "VIMMMYZNONYGpEtjfW2zjz1TkT3W2jmwFZZIIJFMUNZkMdYIIMQRqHfTtDmmxzjT5TyWzD1TZdMMMMNNONNZNMNMNNYMWzTtTtDiGhTiTlD0jz2x1kUZRldgkQ"
file_text = "VIMOYYNNZYNGpEtjfTm2wT4Gwz3Tmz3AFZZIIFQFRMAQIIMEMNgkqHfTtD3jhjzmzDwT5mzDZdMMNMZNYNZNYNOZZMZZWzTtDtDljlmim1T3TiT21kUhdNMcZA"



#VIMOYYNNZYNGpEtjfTm2wT4Gwz3Tmz3AFZZIIFQFRMAQIIMEMNgkqHfTtD3jhjzmzDwT5mzDZdMMNMZNYNZNYNOZZMZZWzTtDtDljlmim1T3TiT21gUhdNMcZA
#VIMNNNMOYYNGpEtjf2jz3T12zT1ThzywFZZIMFYRFMIEQAgIUlQYqHfTtD1jiDzD5j1mzjzWZdMMMMNMYNZNNYMYYZMOWzTtTt25j5mkzmj1W0Tl1gUQIFdMEF
#VIMNMONMONNGpEtjfmxG2D4Dkj5Ti25QFZZIMFUEIIQQUBcQhdMMqHfTtDzj5G1D0jxmmzxWZdMMNMOZYOMMNZZNMMYZWzTtDtWz2mDmD0Dy2kzz1gUUNNMENY
#VIMNYNZMONYGpEtDfTxj1WkG3jlTzjkQFZZIAFIkEkNlUMkZMQQdqHfTtD5T5DjD1mymzmyjZdMMMMNOMZNZZZYZONNMWzTtTtDjj4D0D3z2WkGl1kUNgIAEVZ
#VIMONZYNONNGpEtDfWlz2m0jlTyD4TwAFZZIAJMZYIYMMFEcZgEUqHfTtDxGxzxm2z3zkj2TZdMMNMOMNMMZYYMMOZONWzTtDtWhT1z3T42kDwWw1kUJYUgJEU

#Tajemstvi F_19-12-22-15-00_
base_text = "VGFqZW1zdHZpIEZfMTgtMTItMjItMTUtMDBf"

dict = {
0 : 0, #V
11 : 1, #G
32 : 2, #F
52 : 3, #q
33 : 4, #Z
92 : 5,  # W
112 : 6, #1
93 : 7,#z
73 : 8,#d
53 : 9,#H
34 : 10,#Z
12 : 11,#p
1 : 12,#I
13 : 13,#E
72 : 14,#Z
16 : 15,#f
2 : 16,#M
55 : 17,#T
113 : 18, #daily c
56 : 19,#t
74 : 20,#M
94 : 21,#T
35 : 22,#I
14 : 23, #t
75 : 24,#M
15 : 25, ##daily c
36 : 26, #hourly
95 : 27, #t
76 : 28, # 15 - minutes change
96 : 29 ,# 15 -minut
114 : 30, #U
97 : 31,#     : 30#t
77 : 32,#M
57 : 33,#D
37 : 34, #F
54 : 35#f

}

file_text_list = split(file_text)
print(file_text_list[34])

position = 0
result = [0] * 36
hash = ""
for char in file_text_list:
    print(char + "," + str(position))

    try:
        # part of Tajemstvi F_19-12-22-15-02_
        dict_position_in_result = dict[position]
        print(dict_position_in_result)
        result[dict_position_in_result] = char
        position += 1
    except KeyError: # part of hash
        hash += char
        position += 1
        print("\n")

print(result)
result_str = ''.join(result)
print(result_str + hash)
