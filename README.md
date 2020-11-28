# Estimación de probabilidades de incumplimiento en el tiempo

## Introducción

La obtención de probabilidades de incumplimiento es una parte fundamental en la toma de decisiones en las instituciones de crédito. La probabilidad de incumplimiento se define en general como la probabilidad de que un acreditado no cumpla con las obligaciones de su crédito durante 90 días o más. Generalmente se cree que la probabilidad de incumplimiento es una cantidad que puede ser como una etiqueta y que esa misma etiqueta puede usarse para definir tasas de productos (pricing), análisis temporal o credit scoring. En este trabajo se mostrará una forma de calcular probabilidades en el tiempo y contrastarla con la forma de calcular probabilidades de incumplimento para realizar Credit Scoring de créditos hipotecarios.



### 1. Objetivo:

Análisis de las Probabilidades de Incumplimiento de créditos hipotecarios de Estados Unidos para identificar periodos de crisis y propuesta de credit scoring, mediante el uso de las herramientas vistas en el curso de Análisis Numérico y Computo Científico.



### 2. Datos:

Se utilizará la información de 60 trimestres de 5000 créditos hipotecarios de Estados Unidos tomada de protafolios bursatilizado (RMBSs) a partir del año 2000 (hasta 2015). El proveedor de la base es el International Financial Reasearch (www.internationalfinancialreaserch.org), y se tiene acceso a ella por la adquisición del libro Deep Credit Risk de Daniel Rosch y Harald Scheule, que es la principal fuente de este trabajo.


La base tiene los siguientes campos:


id = Identificador

time = Periodo observado (0 corresponde al 2000, 1 al primer trimestre del 2000, etc, etc)

orig_time = Periodo en el que se originó el crédito (si se originó antes del 2000, el número es negativo)

first_time = Primer periodo en el que aparece el crédito en la base

mat_time = Plazo del crédito	

res_time = Periodo en el que se recuperó la vivienda

balance_time = Saldo en el periodo de observación

LTV_time = Loan to Value a la originación

interest_rate_time = Tasa de interés en el periodo de observación

rate_time = Tasa libre de riesgo en el periodo de observación

hpi_time = Indice de precios de casas en el periodo de observación

gdp_time = Tasa de crecimiento del PIB en el periodo de observación

uer_time = Tasa de desempleo en el momento de la valuación

REtype_CO_orig_time = Real state type (condominio 1, otherwise 0)

REtype_PU_orig_time = Real state type	(desarrollo urbano 1, othrwise 0)

REtype_SF_orig_time = Real state type	(vivienda para una sola familia 1, otherwise 0)

investor_orig_time = desarrollador 1, otherwise 0

balance_orig_time = Monto del crédito	

FICO_orig_time = FICO score en el momento de originar	

LTV_orig_time = Loan to Value en el momento de la orriginación	

Interest_Rate_orig_time = Tasa de interés en el momento de la originación

state_orig_time = Estado de la unión americana donde sse encuentra la vivienda	

hpi_orig_time = Indice de precios de casa en el momento de la originación

default_time = 1 se es default	

payoff_time = 1 si es liquidación

status_time = 1 default, 2 payoff, 0 otherwise

lgd_time = Loss given default al momento del default

recovery_res = Suma de los flujos recibidos durante el periodo de resolución



### 3. Temas

a. Análisis exploratorio de la base de datos.

b. Selección de variables usando distintas herramientas: "Feature Enginering".
	b.1 Análisis de Probabilidades de incumplimiento en el tiempo : PCA.
	
	b.2 Credit Scoring: Mapeo WOE (weight of evidence) para obtención de Information Value.
	
c. Modelo de Regresión Logística para obtención de Probabilidades de incumplimiento en el tiempo.
	c.1 Selección de Técnica.
	
	c.2 Obtención de Parámetros.
	
	c.3 Análisis de medidas de validación.
	
	c.4 Proyección o estimación.
	
d. Modelo de Regresión para uso en Credit Scoring (sobre el mapeo de WOEś).
	d.1 Selección de Técnica.
	
	d.2 Obtención de Parámetros.
	
	d.3 Análisis de medidas de validación.
	
	d.5 Transformación a scorecards.
	
e. Conclusiones



### 4. Software
Python y AWS



### 5. Bibliografía:
Rosch Daniel, Scheule Harald. Deep Credit Risk. 2020. Amazon Fulfillment, Polonia.
Siddiqi, Naeem. Credit Risk Scorecards, Developing and Implementing Credit Scoring. 2006. Wiley, New Jersey 



## Integrantes del equipo

|User | Nombre Completo|Tarea|
|:---:|:---:|:---:|
|@oaperez3|Oscar Perez|Programacion y resolucion de problema de optimización|
|@Eduardo-Moreno|Eduardo Moreno|Por determinar|
|@yefovar|Yedam Fortiz|Por determinar|
|@arenitss|Nayeli Arenas|Por determinar|


