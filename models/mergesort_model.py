def merge_sort_score(result):
    if len(result) > 1:
        mid = len(result) // 2
        left_side = result[:mid]
        right_side = result[mid:]
        merge_sort_score(left_side)
        merge_sort_score(right_side)
        i = j = k = 0

        while i < len(left_side) and j < len(right_side):
            # Kriteria sorting: nilai terbesar DESC, benar terbanyak DESC, Salah Terdikit ASC, NRP ASC
            # Urutan array adalah [NRP,NAMA,JUMLAH_BENAR,JUMLAH_SALAH,JUMLAH_KOSONG,NILAI]
            # leftside[5] / rightside[5] = Nilai Siswa
            # leftside[4] / rightside[4] = Jumlah Kosong
            # leftside[3] / rightside[3] = Jumlah Salah
            # leftside[2] / rightside[2] = Jumlah Benar
            # leftside[1] / rightside[1] = NAMA
            # leftside[0] / rightside[0] = NRP
            # salah paling sedikit ASC, kosong paling sedikit ASC, NRP ASC
                # Urutkan berdasarkan Nilai terbesar
            if (left_side[i][5] > right_side[j][5] or
                    # Jika Nilai sama maka urutkan berdasarkan Jumlah benar paling banyak
                    (left_side[i][5] == right_side[j][5] and left_side[i][2] > right_side[j][2]) 
                    or 
                    # Jika Nilai dan Jumlah benar sama maka urutkan berdasarkan Jumlah 
                    # Salah paling sedikit
                    (left_side[i][5] == right_side[j][5] and 
                     left_side[i][2] == right_side[j][2] and 
                     left_side[i][3] < right_side[j][3]) 
                     or 
                     # Jika Nilai, Jumlah benar, Jumlah Salah sama maka urutkan 
                     # berdasarkan NRP / ID SISWA
                    (left_side[i][5] == right_side[j][5] and 
                     left_side[i][2] == right_side[j][2] and 
                     left_side[i][3] == right_side[j][3] and 
                     left_side[i][0] < right_side[j][0])): 
                result[k] = left_side[i]
                i += 1
            else:
                result[k] = right_side[j]
                j += 1
            k += 1

        while i < len(left_side):
            result[k] = left_side[i]
            i += 1
            k += 1

        while j < len(right_side):
            result[k] = right_side[j]
            j += 1
            k += 1

