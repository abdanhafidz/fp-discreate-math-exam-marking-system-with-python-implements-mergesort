from repositories import readerfiles_repository as rf
from controller import koreksi_controller as KoreksiController
import pandas
def main_view():
    print("======= PROGRAM KOREKSI JAWABAN SISWA =======")
    print("Silahkan pilih nama file data excel :")
    i = 1
    for x in rf.showFile():
        print(i,'>',x)
        i+=1
    f = int(input("Masukkan Nomor file yang ingin dibaca: [1/2/3/...] :"))
    # Mengkoreksi jawaban siswa
    data = KoreksiController.correcting(rf.showFile()[f-1]) 
    df = pandas.DataFrame(data)
    df.columns = ["STUDENT ID","NAME","B","S","K","SCORE"]
    print(df)



