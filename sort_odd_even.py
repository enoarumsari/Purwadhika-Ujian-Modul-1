def sort_odd_even(lst):
    odd = []
    index_odd = []
    even = []
    index_even = []

    #iterasi loop elemen didalam lst selama panjang lst
    for i in range (len(lst)):
        #jika elemen i didalam list habis di mod 2
        if lst[i] % 2 == 0:
            #masukkan elemen kedalam list even
            even.append(lst[i])
            #masukkan index elemen kedalam list index_even
            index_even.append(i)
            #sort list even dari terbesar sampai terkecil
            even.sort(reverse=True)
        else:
            #jika elemen tidak habis dimod 2, masukkan elemen kedalam list odd
            odd.append(lst[i])
            #masukkan index elemen kedalam list index_odd
            index_odd.append(i)
            #sort list odd dari kecil sampai terbesar
            odd.sort()

    for i in range ((len(index_even))):
        #masukkan elemen even kedalam list lst sesuai dengan nomor list di index_even
        lst[index_even[i]] = even[i]

    for i in range ((len(index_odd))):
        #masukkan elemen odd kedalam list lst sesuai dengan nomor list di index_odd
        lst[index_odd[i]] = odd[i]

    # print(even)
    # print(odd)
    print(lst)

sort_odd_even([5, 3, 2, 8, 1, 4])