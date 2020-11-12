def hashtag(string):

    #jika panjang elemen di string lebih dari 140 maka return False
    if len(string) > 140:
        return False
    #jika panjang elemen di string adalah 0 maka return False
    elif len(string) == 0:
        return False
    #jika elemen string tidak memenuhi kriteria diatas maka masuk ke else
    else:
        #mengubah string menjadi list li1 dan membesarkan huruf awal masing-masing elemen
        li1 = (string.title()).split()
        #mengubah list menjadi string kembali tanpa spasi
        li2 = ''.join(map(str, li1))
        #menambahkan hastag diawal string li2
        return '#' + li2

print(hashtag('halo ini ujian modul 1 kak'))