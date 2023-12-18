from services import koreksi_service as CorrectionService

def correcting(fileName):
    try:
        return CorrectionService.correction(fileName)
    except Exception as Err:
        return Err
