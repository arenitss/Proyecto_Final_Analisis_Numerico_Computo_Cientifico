# Modelos para la estimación de probabilidades de incumplimiento

## Introducción

La obtención de probabilidades de incumplimiento es una parte fundamental en la toma de decisiones en las instituciones de crédito. La **probabilidad de incumplimiento** se define en general como la probabilidad de que un acreditado no cumpla con las obligaciones de su crédito durante 90 días o más. Generalmente se cree que la probabilidad de incumplimiento es una cantidad que puede ser tomada como una etiqueta y que esa misma etiqueta puede usarse para definir tasas de productos (*pricing*), análisis temporal o credit scoring. En este trabajo se mostrarán 2 metodologías para calcular la probabilidad de incumplimiento en el tiempo.

### 1. Objetivo:

Comparar modelos obtenidos por metodologías distintas, las cuales son las vistas en el curso *vs* las metodologías implementadas en módulos de `Python`. Ambos permiten calcular la estimación de probabilidades de incumplimiento. Se tomará como referencia los modelos obtenidos 
del módulo [`statsmodel.api`](https://www.statsmodels.org/stable/examples/notebooks/generated/glm_formula.html).

### 2. Datos:

Se utilizará la información de 60 trimestres de 5000 créditos hipotecarios de Estados Unidos tomada de portafolios bursatilizado (RMBSs) a partir del año 2000 hasta 2015. El proveedor de la base es el [**International Financial Reasearch**](http://www.internationalfinancialresearch.org/), y se tiene acceso a ella por la adquisición del libro *Deep Credit Risk de Daniel Rosch y Harald Scheule*, que es la principal fuente de este trabajo.


### 3. Temas

a. Análisis exploratorio de la base de datos.

b. Selección de variables usando distintas herramientas: "Feature Enginering".
	
	b.1 Análisis de Probabilidades de incumplimiento en el tiempo : PCA.
	
	b.2 Credit Scoring: Mapeo WOE (weight of evidence) para obtención de Information Value.
	
c. Modelo de Regresión Logística para obtención de Probabilidades de incumplimiento en el tiempo.
	
	c.1 Selección de Técnica.
	
	c.2 Obtención de Parámetros.
	
	c.3 Análisis de medidas de validación.
	
d. Modelo de Regresión para uso en Credit Scoring (sobre el mapeo de WOEś).
	
	d.1 Selección de Técnica.
	
	d.2 Obtención de Parámetros.
	
	d.3 Análisis de medidas de validación.
	
e. Conclusiones

### 4. Software
Python y AWS

### 5. Bibliografía:
Rosch Daniel, Scheule Harald. Deep Credit Risk. 2020. Amazon Fulfillment, Polonia.
Siddiqi, Naeem. Credit Risk Scorecards, Developing and Implementing Credit Scoring. 2006. Wiley, New Jersey 

### Integrantes y asignación de tareas del equipo

|User | Nombre Completo| Tarea |
|:---:|:---:|:---:|
|@oaperez3|Oscar Perez|Project manager, levantamiento de instancia en AWS, implementación de metodología, responder preguntas
|@Eduardo-Moreno|Eduardo Moreno|Investigación de variables, implementación metodología, responder preguntas
|@yefovar|Yedam Fortiz|Testing, estudio de parte matemática, expositor
|@arenitss|Nayeli Arenas|Redacción, revisón de resultados, expositor


