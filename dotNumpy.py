import numpy as np
import time

# Generamos datos simulados
np.random.seed(42)
x = np.random.rand(1000000)
y = 3.5 * x + 2 + np.random.randn(1000000) * 0.5  # y = 3.5x + 2 + ruido

# Agregamos una columna de unos para el término independiente
X = np.vstack((np.ones_like(x), x)).T

# -------------------------------
# Método 1: Usando bucle for
# -------------------------------
start_time = time.time()

# Calculamos X^T * X manualmente
XtX = np.zeros((2, 2))
for i in range(len(x)):
    xi = np.array([1, x[i]])
    XtX += np.outer(xi, xi)

# Calculamos X^T * y manualmente
Xty = np.zeros(2)
for i in range(len(x)):
    xi = np.array([1, x[i]])
    Xty += xi * y[i]

# Resolvemos para los coeficientes: (X^T X)^(-1) X^T y
beta_for = np.linalg.inv(XtX) @ Xty

time_for = time.time() - start_time

# -------------------------------
# Método 2: Usando numpy.dot
# -------------------------------
start_time = time.time()

XtX_dot = X.T.dot(X)
Xty_dot = X.T.dot(y)
beta_dot = np.linalg.inv(XtX_dot).dot(Xty_dot)

time_dot = time.time() - start_time

# -------------------------------
# Resultados
# -------------------------------
print("Coeficientes usando for loop:", beta_for)
print("Tiempo usando for loop:", time_for, "segundos\n")

print("Coeficientes usando numpy.dot:", beta_dot)
print("Tiempo usando numpy.dot:", time_dot, "segundos\n")

# Comparación de precisión
print("Diferencia entre métodos:", np.linalg.norm(beta_for - beta_dot))