import numpy as np
import pandas as pd
from pytest import approx
import statsmodels.formula.api as smf
import statsmodels.api as sm
from logisticregression_pca import estim_prob
from logisticregression_pca import potencia
from logisticregression_pca import second_potencia

# Lectura de base de datos
df = pd.read_csv('data_t_final.csv')
df = df.dropna(subset=['time','orig_time','first_time']).copy()

# Lectura de base de datos para PCA
defaultrates_states1 = df.groupby(['time','state_orig_time'])['default_time'].mean().unstack(level=1).add_prefix('defaultrate_').fillna(0).reset_index(drop=False)
scaler = StandardScaler()
defaultrates_states = scaler.fit_transform(defaultrates_states1)


# Regresion Logistica con metodos de optimizacion
fitted_values, beta = estim_prob(df,['time','orig_time','first_time','default_time'])

# Regresion Logistica con paqueteria python
model_lr = smf.glm('default_time ~ time + orig_time + first_time', 
family = sm.families.Binomial(), data = df).fit()

print(beta == approx(np.array(model_lr.params), abs=1e-5, rel=1e-5))



# PCA con paqueteria de python
pca=PCA()
pca.fit(defaultrates_states)
z = pca.transform(defaultrates_states)


print(z[:,0]== approx(np.array(potencia(defaultrates_states, sim=False, MAX=100)))
print(z[:,1]== approx(np.array(second_potencia(defaultrates_states, MAX=100)))
