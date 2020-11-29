# Estimación de probabilidades de incumplimiento en el tiempo

## Introducción

La obtención de probabilidades de incumplimiento es una parte fundamental en la toma de decisiones en las instituciones de crédito. La **probabilidad de incumplimiento** se define en general como la probabilidad de que un acreditado no cumpla con las obligaciones de su crédito durante 90 días o más. Generalmente se cree que la probabilidad de incumplimiento es una cantidad que puede ser como una etiqueta y que esa misma etiqueta puede usarse para definir tasas de productos (pricing), análisis temporal o credit scoring. En este trabajo se mostrará una forma de calcular probabilidad de incumplimiento en el tiempo y contrastarla con la forma de calcularlas para realizar Credit Scoring de créditos hipotecarios.




### 1. Objetivo:

Identificar **periodos de crisis* y propuesta de **credit scoring** mediante el análisis de probabilidad de default (o de incumplimiento) de créditos hipotecarios de Estados Unidos, mediante el uso de las herramientas vistas en el curso de Análisis Numérico y Computo Científico.



### 2. Datos:

Se utilizará la información de 60 trimestres de 5,000 créditos hipotecarios de Estados Unidos tomada de protafolios bursatilizado (RMBSs) a partir del año 2000 (hasta 2015). El proveedor de la base es la instutición estadounidense (**International Financial Reasearch**)[www.internationalfinancialreaserch.org]. Cabe mencionar, que se  tiene acceso a ella por la adquisición del libro *Deep Credit Risk de Daniel Rosch y Harald Scheule*, el cual es la principal fuente de este proyecto.

A continuación, se enunciará y describirán las variables:

Dentro de la base de datos cada observación (*renglón*) corresponde a un préstamo otorgado por la institución hipotecaria.

1. *id*.- clave única por respondiente, dado que los préstamos se otorgan por distintos periodos de tiempo, el valor de esta variable se repite por varias préstamos (*renglones*).

1. *time*.- periodo observado identificado como trimestres deade el año 2000 hasta **IDENTIFICAR AÑO FINAL**, de tal manera que, 0 corresponde al 2000, 1 al primer trimestre del 2000, 2 al segundo trimestre del año 2000, ...

1. *orig_time*.- periodo en el que se otorgó el crédito. Si se otorgó previo al 2000, el número es negativo.

1. *first_time*.- primer periodo de tiempo en el que aparece el crédito en la base.

1. *mat_time*.- plazo del crédito	

1. *res_time*.- periodo en el que se recuperó la vivienda.

1. *balance_time*.- saldo en el periodo de observación

1. *LTV_time*.- Loan to Value a la originación (endeudamiento de un activo en relación con su valor real y actual). Para obtener una descripción más detallada se recomienda visitar el siguiente (link)[https://www.ilpabogados.com/que-es-el-loan-to-value-ltv-y-por-que-es-relevante/].

1. *interest_rate_time*.- tasa de interés en el periodo de observación

1. *rate_time*.- tasa libre de riesgo en el periodo de observación

1. *hpi_time*.- índice de precios de casas en el periodo de observación

1. *gdp_time*.- tasa de crecimiento del PIB en el periodo de observación

1. *uer_time*.- tasa de desempleo en el momento de la valuación

1. *REtype_CO_orig_time*.- identificador de condominio (condominio 1, en otro caso 0)

1. *REtype_PU_orig_time*.- identificador de desarrollo urbano (desarrollo urbano 1, en otro caso 0)

1. *REtype_SF_orig_time*.- identificador de vivienda familia unitaria (vivienda para una sola familia 1, en otro caso 0)

1. *investor_orig_time*.- desarrollador 1, otherwise 0

1. *balance_orig_time*.- monto del crédito

1. *FICO_orig_time*.- (FICO score)[https://www.ficoscore.com/ficoscore/pdf/Understanding-FICO-Scores-SPANISH.pdf] en el momento de originar

1. *LTV_orig_time*.- Loan to Value en el momento de la orriginación

1. *Interest_Rate_orig_time*.- tasa de interés en el momento de la originación

1. *state_orig_time*.- Estado de la unión americana donde se encuentra la vivienda

1. *hpi_orig_time*.- índice de precios de casa en el momento de la originación

1. *default_time*.- indicadora de incumplimiento de pago (default 1, en otro caso 0)

1. *payoff_time*.- indicadora de liquidación (liquidación 1, en otro caso 0) 

1. *status_time*.- 1 default, 2 payoff, 0 en otro caso

1. *lgd_time*.- (Loss given default)[https://www.investopedia.com/terms/l/lossgivendefault.asp#:~:text=Loss%20given%20default%20(LGD)%20is,at%20the%20time%20of%20default.] o severidad  al momento del default

1. *recovery_res*.- suma de los flujos recibidos durante el periodo de resolución


### 3. Temas

a. Análisis exploratorio de la base de datos: **EDA/GEDA**

	a.1 Describir la estructura de los datos
	
	a.2 Describir relaciones entre variables
	
	a.3 Mostrar gráficas y resultados (tablas) relevantes
	
	a.3 Identificar, analizar y describir Insights importantes


b. Selección de variables usando distintas herramientas: **Feature Enginering**
	
	b.1 Análisis de Probabilidades de incumplimiento en el tiempo: PCA.
	
	b.2 Credit Scoring: Mapeo WOE (weight of evidence) para obtención de Information Value.
	
c. Modelo de Regresión Logística para obtención de Probabilidades de incumplimiento en el tiempo: **Modelling**
	
	c.1 Selección de Técnica.
	
	c.2 Obtención de Parámetros.
	
	c.3 Análisis de medidas de validación.
	
	c.4 Proyección o estimación.
	
d. Modelo de Regresión para uso en Credit Scoring (sobre el mapeo de WOEś): **Modelling**
	
	d.1 Selección de Técnica.
	
	d.2 Obtención de Parámetros.
	
	d.3 Análisis de medidas de validación.
	
	d.5 Transformación a scorecards.
	
e. Conclusiones



### 4. Software
Python y AWS



### 5. Bibliografía:
*Rosch Daniel*, Scheule Harald. Deep Credit Risk. 2020. Amazon Fulfillment, Polonia.
*Siddiqi, Naeem*. Credit Risk Scorecards, Developing and Implementing Credit Scoring. 2006. Wiley, New Jersey 



## Integrantes del equipo

|User | Nombre Completo|
|:---:|:---:|:---:|
|@oaperez3|Oscar Perez|

|@yefovar|Yedam Fortiz|

|@arenitss|Nayeli Arenas|

|@Eduardo-Moreno|Eduardo Moreno|


