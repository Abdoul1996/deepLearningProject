import os 
import sys 

def error_message_detail(error: Exception, error_detail:sys) -> str:
    _, _, exc_tb = error_detail.exc_info()
    
    file_name: str = os.path.split