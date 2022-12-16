from PyP100 import PyP110
import pandas as pd
from dotenv import load_dotenv
import os

load_dotenv()

# connect to tapo device
p110 = PyP110.P110(os.environ['tapo_url_1'], os.environ['tapo_email'], os.environ['tapo_password'])

# create cookies required for further methods
p110.handshake()

# send credentials and create AES Key and IV for further methods
p110.login()

# get info from the connected plug
energy = p110.getEnergyUsage()
name = p110.getDeviceName()
info = p110.getDeviceInfo()
energy_df = pd.DataFrame.from_dict(energy)
energy_df.loc['device_name'] = name
energy_final = energy_df.drop(columns=['error_code']).T


