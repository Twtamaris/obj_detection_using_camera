import os
if 'VIRTUAL_ENV' in os.environ and os.environ['VIRTUAL_ENV'] != '':
    print("Virtual environment is activated.")
else:
    print("Virtual environment is not activated.")
