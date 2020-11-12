def create_phone_number(lst):

    #iterasi elemen dalam lst
    for i in lst: 
        #lst diubah menjadi string tanpa spasi dimasukkan kedalam li1
        li1 = ''.join(map(str, lst)) 
        #return hasil string tanpa spasi ditambah tanda kurung dan strip
        return '(' + li1[:3] + ') ' + li1[3:6] + '-' + li1[6:] 

print(create_phone_number([1,2,3,4,5,6,7,8,9,0]))

