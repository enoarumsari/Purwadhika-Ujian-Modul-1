def hollowTriangle(x):

    #iterasi baris sebanyak x kali
    for i in range(x):
        #iterasi j mulai dari 1 sampai x dikurang iterasi baris keberapa
        for j in range(1,x-i):
            #print - untuk membuat segitiga kiri atas pertama
            print('-', end='')
    
        #iterasi j sebanyak x ditambah iterasi baris keberapa
        for j in range(x+i):
            #jika j sebesar 0 atau j sama dengan 2 dikali iterasi baris atau iterasi baris sama dengan x-1
            if j==0 or j==2*i or i==x-1:
                #maka print *
                print('*',end='')
                #jika persyaratan iterasi j tidak memenuhi syarat maka masuk ke else
            else:
                #maka print -
                print('-', end='')
        #ganti baris iterasi i berikutnya
        print()

hollowTriangle(5)
