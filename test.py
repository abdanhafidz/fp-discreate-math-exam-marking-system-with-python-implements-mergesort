from repositories import readerfiles_repository as rf
from controller import koreksi_controller as KoreksiController
import numpy as np
import pandas as pd
import sys



print("Data Test With : data_test_sorting.xlsx Expected data : data_test_sorting.xlsx")
resTest = KoreksiController.correcting('data_test_sorting.xlsx')
test_result_data = pd.DataFrame(resTest) 
expected_data = pd.read_excel('repositories/data_expected_sorting.xlsx')
expected_data = expected_data.to_numpy()
expected_data = expected_data.tolist()
testing_status = []
pass_test = []
for i in range(0,len(resTest)):
    pass_test.append(0)
    for j in range(0,5):
        if(resTest[i][j] == expected_data[i][j] ):
            pass_test[i] +=1
    if(pass_test[i] == 5):
        testing_status.append("OK")
    else:
        testing_status.append("WA")
pass_test = pd.DataFrame(pass_test)
testing_status = pd.DataFrame(testing_status)
expected_data = pd.DataFrame(expected_data)
test_result_data.columns = ["STUDENT ID_TEST_RESULT",
                            "NAME_TEST_RESULT",
                            "B_TEST_RESULT",
                            "S_TEST_RESULT",
                            "K_TEST_RESULT",
                            "SCORE_TEST_RESULT",
                            ]
expected_data.columns = ["STUDENT ID_EXPECTED",
                            "NAME_EXPECTED",
                            "B_EXPECTED",
                            "S_EXPECTED",
                            "K_EXPECTED",
                            "SCORE_EXPECTED"]
sys.stdout = open('test/data_test.test', 'w')
print("====  TEST DATA : ==== ")
print(test_result_data)


print("==== EXPECTED DATA : ==== ")
print(expected_data)


print("==== PASS TEST POINT : ==== ")
print(pass_test)

print("==== PASS TEST STATUS : ==== ")
print(testing_status)

