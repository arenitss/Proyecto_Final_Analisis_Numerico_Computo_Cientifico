import numpy as np
import cvxpy as cp

def logistic_model(data, variables, default = "default_time"):
    """
    Obtención del modelo de regresión logística resolviendo un problema de optimización (minimización) convexo
    :param data(dataframe): dataframe con variables a analizar
    :param variables(list): variables a incluir en el modelo de regresión logística, debe incluir variable dependiente
                      e independientes
    :param default(str): variable dependiente
    :return beta(array): vector de parámetros obtenidos del problema de optimización convexa
    """

    # Selección de features
    data = data[variables]

    # Selección de variable dependiente (para este proyecto siempre es default_time
    classes = data[default].copy()

    # Quitar variable dependiente al dataset
    data = data.drop([default], axis=1)
    m, n = data.shape
    print(m)

    # Agregamos columna de 1's para el intercepto (beta_0)
    data = np.column_stack((np.ones((m, 1)), data))

    # Número de variables (se agrega beta_0 o intercepto)
    n = n + 1

    # Variable de optimización
    beta = cp.Variable(n)

    # Planteamos y resolvemos problema de optimización convexo
    fo_cvxpy = 2 * cp.sum(cp.logistic(data @ beta) - cp.multiply(classes, data @ beta))
    obj = cp.Minimize(fo_cvxpy)
    prob = cp.Problem(obj)

    print('Evaluación de valor óptimo al resolver problema de optimización', prob.solve())

    return beta.value, data

def estim_prob(data, variables, default = 'default_time'):
    """
    Obtención de estimación de probabilidades utilizando un modelo de regresión logístico y metodología de
    optimización convexa
    :param data: dataframe con variables a analizar
    :param variables: variables a incluir en el modelo de regresión logística, debe incluir variable dependiente
                      e independientes
    :param default: variable dependiente
    :return fitted_values: estimación de probabilidadees
    """

    # Obtención de parámetros estimados
    model, data = logistic_model(data, variables)

    # Evaluación lineal del modelo
    linear_value = -data.dot(model)

    # Estimación de probabilidad
    fitted_values = 1 / (1 + np.exp(linear_value))

    return fitted_values, model



def potencia(d, sim=False, MAX=100):
    """
    Método de la potencia para encontrar eigenvector de máximo módulo matrices cuadradas (simétricas) o no
    - input:
    - d(dataframe): matriz
    - simetrica(boolean): indica si la matriz input es cuadrada y simétrica
    - MAX(int): máximas evaluaciones del método de la potencia
    - output(array):
    - eil(array): evolución hacia el eigenvalor de máximo módulo
    - v(vector): eigenvector asociado a eigenvalor máximo modulo asociado
    Pseudoalgoritmo obtenido de la nota 2.3
    """

    # Definimos los parámetros de entrada y las dimensiones de nuestro data set
    if not sim:
        X = d @ d.T
    else:
        X = d
    n = X.shape[0]

    # Condiciones iniciales
    np.random.seed(2020)
    q_k = np.random.rand(n)
    lambda_k_iter = np.zeros(MAX)

    # Método de la potencia
    for k in range(MAX):
        # Paso de la potencia
        z_k = X @ q_k

        # Normalizamos el vector
        q_k = z_k / np.linalg.norm(z_k)

        # Calculamos eigenvalor de máximo módulo
        lambda_k = q_k.T @ X @ q_k
        lambda_k_iter[k] = lambda_k

    return q_k




def second_potencia(d, MAX=100):
    """
    Método de la potencia para encontrar eigenvector asociado al segundo eigenvalor de
    máximo módulo para matrices simétricas
    - input:
    - d(dataframe): matriz no cuadrada
    - MAX(int): máximas evaluaciones del método de la potencia
    - output(array):
    - v(vector): eigenvector asociado a eigenvalor máximo modulo asociado
    Pseudoalgoritmo obtenido de la nota 2.3
    """

    # Eliminamos el eigenvalor de máximo módulo
    eig_1, eiv_1 = potencia(d)

    # Definimos los parámetros de entrada y las dimensiones de nuestro data set
    X = d @ d.T

    # Calculamos matriz actualizada sin el eigenvalor de máximo módulo
    X = X - eig_1[-1] * np.outer(eiv_1, eiv_1)

    # Calculamos eigenvector de máximo módulo
    eig_2, eiv_2 = potencia(X, True)

    return eiv_2
