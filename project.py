kodepasien =['1a','1b','1c','0a']
nama =['Kelvin','Anita','Cyntia','Raelyn']
jenis=['L','P','P','P']
usia =[27,29,26,2]
berat =[100,62,45,10]
tinggi =[175,158,160,100]
noHp =['089532977853','089532966728','089530019927','0225422398']

# Command Header Data Pasien
def header() :
    print(f"{'Kode' : <10}{'Nama' : <10}{'Jenis': <8}{'Usia': ^8}{'Berat': ^10}{'Tinggi': ^10}{'No Hp': <15}")

# Command Tabel Data Pasien
def datapasien (j) :
    print(f"{kodepasien[j] :<10}{nama[j] : <10}{jenis[j] : ^8}{usia[j] : ^8}{berat[j] : ^10}{tinggi[j] : ^10}{noHp[j] : <15}")

# Command Menu 4 (Delete Data)
def menu4():
    k=0
    while k==0 :
        print('''
++++++++++++ Menghapus data pasien ++++++++++++

    1. Hapus data pasien
    2. Kembali ke menu utama
    ''')
        global inputmenu1
        inputmenu1=input('Masukkan menu yang dipilih [1-2]: ')
        j=0
        index=0
        if inputmenu1=='1' :
            b=0
            kodechg=input('Masukkan kode pasien yang ingin dihapus: ')
            for a in kodepasien :
                if a == kodechg :
                    b=1
                    break
            if b == 1 :
                index=kodepasien.index(kodechg)
                n=0
                while n==0 :
                    cek=input('Apakah data akan dihapus (Y/N)?')
                    if cek=='Y':
                        del kodepasien[index]
                        del nama[index]
                        del jenis[index]
                        del usia[index]
                        del berat[index]
                        del tinggi[index]
                        del noHp[index]
                        print('Data berhasil terhapus !')
                        n=1
                    elif cek=='N':
                        print('Data tidak jadi dihapus')
                        n=1
            else :
                print('Kode pasien tidak ditemukan !')
        if inputmenu1=='2' :
            k=1
            menu0()

# Command Menu 3 (Update Data)
def menu3():
    k=0
    while k==0 :
        print('''
++++++++++++ Mengubah data pasien ++++++++++++

    1. Ubah data pasien
    2. Kembali ke menu utama
    ''')
        global inputmenu1
        inputmenu1=input('Masukkan menu yang dipilih [1-2]: ')
        j=0
        index=0
        if inputmenu1=='1' :
            b=0
            kodechg=input('Masukkan kode pasien yang ingin diubah: ')
            for a in kodepasien :
                if a == kodechg :
                    b=1
                    break
            if b == 1 :
                index=kodepasien.index(kodechg)
                header()
                datapasien(index)
                l=0
                m=0
                while l==0 :
                    cek=input('Lanjut Update (Y/N)?')
                    if cek=='Y':
                        ubah=input('Apa yang ingin diubah ?')
                        ubah=ubah.lower()
                        ubah1=input('Masukkan {} baru :'.format(ubah))
                        while m==0 :
                                cek=input('Data akan diupdate (Y/N)? ')
                                if cek=='Y':
                                    if ubah =='nama':
                                        nama[index]=ubah1
                                    elif ubah =='kode':
                                        kodepasien[index]=ubah1
                                    elif ubah =='jenis':
                                        jenis[index]=ubah1
                                    elif ubah =='usia':
                                        usia[index]=ubah1
                                    elif ubah =='berat':
                                        berat[index]=ubah1
                                    elif ubah =='tinggi':
                                        tinggi[index]=ubah1
                                    elif ubah =='no hp':
                                        noHp[index]=ubah1
                                    print('Data berhasil diupdate !')
                                    m=1
                                elif cek=='N':
                                    print('Data tidak jadi diupdate')
                                    m=1
                        l=1
                    if cek=='N':
                        print('Data tidak jadi terupdate')
                        l=1
            else :
                print('Kode pasien tidak ditemukan !')
        if inputmenu1=='2' :
            k=1
            menu0()

# Command Menu 2 (Create Data)
def menu2():
    global kodepasien
    global nama
    global jenis
    global usia
    global berat
    global tinggi
    global noHp
    k=0
    while k==0 :
        print('''
++++++++++++ Menambahkan data pasien ++++++++++++

    1. Tambahkan data pasien
    2. Kembali ke menu utama
    ''')
        global inputmenu1
        inputmenu1=input('Masukkan menu yang dipilih [1-2]: ')
        j=0
        if inputmenu1=='1' :
            b=0
            kodeadd=input('Masukkan kode pasien baru : ')
            for a in kodepasien :
                if a == kodeadd :
                    b=1
                    break
            if b == 1 :
                print('Kode pasien telah digunakan !')
            else :
                namaadd = input('Masukkan Nama :')
                jenisadd = input('Masukkan Jenis Kelamin (L/P):')
                usiaadd = int(input('Masukkan Usia :'))
                beratadd = int(input('Masukkan Berat :'))
                tinggiadd = int(input('Masukkan Tinggi :'))
                noHpadd = input('Masukkan No Hp :')
                l=0
                while l==0 :
                    cek=input('Apakah anda sudah yakin (Y/N)? ')
                    if cek =='Y':
                        kodepasien=kodepasien+[kodeadd]
                        nama=nama+[namaadd]
                        jenis=jenis+[jenisadd]
                        usia=usia+[usiaadd]
                        berat=berat+[beratadd]
                        tinggi=tinggi+[tinggiadd]
                        noHp=noHp+[noHpadd]
                        print('Data sudah tersimpan !')
                        l=1
                    if cek=='N':
                        l=1
        if inputmenu1=='2' :
            k=1
            menu0()

# Command Menu 1 (Read Data)
def menu1():
    k=0
    while k==0 :
        print('''
++++++++++++ Daftar Pasien Rumah Sakit ++++++++++++

    1. Tampilkan semua daftar pasien
    2. Tampilkan daftar pasien spesifik
    3. Kembali ke menu utama
    ''')
        global inputmenu1
        inputmenu1=input('Masukkan menu yang dipilih [1-3]: ')
        j=0
        if inputmenu1=='1' :
            jkodepasien=len(kodepasien)
            if jkodepasien != 0 :
                print('\nDaftar Pasien :')
                header()
                while j<jkodepasien :
                    datapasien(j)
                    j+=1
            else :
                print('!!!!!!!!!!! Tidak ada data pasien !!!!!!!!!!!')

        if inputmenu1=='2' :
            b=0
            inputmenu11=input('Masukkan kode pasien: ')
            for a in kodepasien :
                if a == inputmenu11 :
                    b=1
                    break
            if b == '1' :
                print('Data pasien dengan kode {} :'.format(inputmenu11))
                header ()
                j=kodepasien.index(inputmenu11)
                datapasien(j)
            else :
                print('Data Pasien tidak ditemukan!')
        if inputmenu1=='3' :
            k=1
            menu0()

# Command Looping Main Menu
def menu0() :
    i=0
    while i == 0 :
            print('''============ Data Pasien Rumah Sakit ============

        1. Daftar pasien rumah sakit
        2. Menambahkan data pasien
        3. Mengubah data pasien
        4. Menghapus data pasien
        5. Exit
        ''')
            global inputmenu
            inputmenu=input('Masukkan menu yang dipilih [1-5]: ')
            if inputmenu=='1' :
                menu1()
                i=1
                break
            elif inputmenu=='2' :
                menu2()
                i=1
                break
            elif inputmenu=='3' :
                menu3()
                i=1
                break
            elif inputmenu=='4' :
                menu4()
                i=1
                break
            elif inputmenu=='5' :
                print('Anda telah mengakhiri sesi program ini. Terima kasih & Sehat selalu !')
                i=1
                break
            else : 
                print('''****** Pilihan yang anda masukkan salah :( , silahkan input kembali ! ******
                ''')

menu0()
