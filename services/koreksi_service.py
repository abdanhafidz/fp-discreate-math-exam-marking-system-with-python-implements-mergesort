from services import readexcel_service as readExcel
from models import mergesort_model as sort
from repositories import kunci_jawaban as key
import numpy as np
def correction(fileName):
    data = readExcel.read(fileName).tolist()
    kunci = key.answer_key
    total_soal = len(kunci)
    B = [0] * len(data)
    S = [0] * len(data)
    K = [0] * len(data)

    for i in range(len(data)):
        for no in range(total_soal):
            if data[i][2][no] == kunci[no]:
                B[i] += 1
            elif (data[i][2][no] == 0 or data[i][2][no] == '0' or data[i][2][no] == "0"):
                K[i] += 1
            else:
                S[i] += 1
    for k in range(0,len(data)):
        score = B[k]*4 - S[k]
        data[k][2] = (B[k])
        data[k].append(S[k])
        data[k].append(K[k])
        data[k].append(score)
    sort.merge_sort_score(data)
    return data

# data = [
#     ['021', 'Abdan', ['A', 'A', 'A', 'C', 'C', 'D']],
#     # Tambahkan data peserta lain jika diperlukan
# ]

# kunci_jawaban = ['A', 'B', 'A', 'C', 'C', 'D']

