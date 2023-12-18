from services import readexcel_service as RExcelService

def read(fileName):
    try:
        return RExcelService.read(fileName)
    except Exception as Err:
        return Err

