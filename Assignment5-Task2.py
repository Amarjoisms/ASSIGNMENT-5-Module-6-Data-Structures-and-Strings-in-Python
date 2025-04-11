from Tools.scripts.pdeps import inverse

olist = [1,2,3,4,5,6,7,8,9,10]
print('Original list: ', olist)
list = olist[0:5]
print('Extracted first five elements: ', list)
invlist = list[::-1]
print('Reversed extracted elements: ', invlist)
