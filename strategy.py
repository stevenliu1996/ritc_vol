import numpy as np
import pandas as pd
from api import RitClient

C2P_1m = {'RTM1C'+str(i):'RTM1P'+str(i) for i in range(45, 55)}
C2P_2m = {'RTM2C'+str(i):'RTM2P'+str(i) for i in range(45, 55)}
P2C_1m = {'RTM1P'+str(i):'RTM1C'+str(i) for i in range(45, 55)}
P2C_2m = {'RTM2P'+str(i):'RTM2C'+str(i) for i in range(45, 55)}
tickers_1m = ['RTM1C'+str(i) for i in range(45, 55)]+['RTM1P'+str(i) for i in range(45, 55)]
tickers_2m = ['RTM2C'+str(i) for i in range(45, 55)]+['RTM2P'+str(i) for i in range(45, 55)]
ticker = 'RTM'
