import numpy as np
import pandas as pd
from pytest import approx
import statsmodels.formula.api as smf
import statsmodels.api as sm
from utils import estim_prob
from utils import potencia
from utils import deflacion
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

# Lectura de base de datos
df = pd.read_csv('data_t_final.csv')
df = df.dropna(subset=['time','orig_time','first_time']).copy()

# Transformacion de base de datos para Metodo de potencia y deflacion
defaultrates_states1 = df.groupby(['time','state_orig_time'])['default_time'].mean().unstack(level=1).add_prefix('defaultrate_').fillna(0).reset_index(drop=False)
scaler = StandardScaler()
defaultrates_states = scaler.fit_transform(defaultrates_states1)
cov = np.cov(defaultrates_states.T)

### Regresion Logistica ###

# Regresion Logistica con metodos de optimizacion
fitted_values, beta = estim_prob(df,['time','orig_time','first_time','default_time'])

# Regresion Logistica con paqueteria python
model_lr = smf.glm('default_time ~ time + orig_time + first_time', 
family = sm.families.Binomial(), data = df).fit()

# Evaluacion de la precision con metodo de optimizacion y con paqueteria de python

print(beta == approx(np.array(model_lr.params), abs=1e-5, rel=1e-5))

### Metodo de potencia y deflacion ###

# PCA con metodos de optimizacion

eigenvalor,eigenvector = potencia(cov,MAX=1000)
eigenvalor2,eigenvector2 = deflacion(cov,MAX=1000)
cp1 = eigenvector@defaultrates_states.T
cp2 = eigenvector2@defaultrates_states.T

# PCA con paqueteria de python
pca=PCA()
pca.fit(defaultrates_states)
z = pca.transform(defaultrates_states)

# Evaluacion de la precision con metodo de optimizacion y con paqueteria de python

print(cp1 == approx(z[:,0], abs=1e-1, rel=1e-1))
print(-cp2 == approx(z[:,1], abs=1e-1, rel=1e-1))
