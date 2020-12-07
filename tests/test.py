import numpy as np
import pandas as pd
from pytest import approx
import statsmodels.formula.api as smf
import statsmodels.api as sm
from logisticregression_pca import estim_prob

# Lectura de base de datos
df = pd.read_csv('data_t_final.csv')
df = df.dropna(subset=['time','orig_time','first_time']).copy()

# Regresion Logistica con metodos de optimizacion
fitted_values, beta = estim_prob(df,['time','orig_time','first_time','default_time'])

# Regresion Logistica con paqueteria python
model_lr = smf.glm('default_time ~ time + orig_time + first_time', 
family = sm.families.Binomial(), data = df).fit()

print(beta == approx(np.array(model_lr.params), abs=1e-5, rel=1e-5))
