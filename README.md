La regresión lineal es una técnica clave en análisis de datos y machine learning, que nos ayuda a ajustar una recta a un conjunto de puntos, y también podemos resolverla usando álgebra lineal.

En lugar de resolver la ecuación ![image](https://github.com/user-attachments/assets/89db3c3e-3704-4279-a86a-f7a76026e33c)
y=mx+b usando sumatorias, podemos usar matrices y vectores para hacerlo mucho más eficiente, especialmente cuando trabajamos con grandes volúmenes de datos.

**Fórmula clásica vs. Matricial**:
La fórmula clásica de regresión lineal simple es: ![image](https://github.com/user-attachments/assets/b21a1896-82ba-4443-8518-45f976e3cf06)
donde m es la pendiente y b el intercepto.

Pero si representamos todo con matrices, la fórmula se convierte en: ![image](https://github.com/user-attachments/assets/1718295e-5369-46c6-8154-5defa27e8e89)
Donde X es la matriz de datos, y 𝛽 es el vector que contiene los coeficientes 𝑏 y 𝑚.

**¿Por qué esto importa?**
Usar álgebra lineal permite resolver la regresión lineal de manera más eficiente, especialmente cuando hay muchas variables.

Las bibliotecas como NumPy utilizan estas fórmulas matriciales para hacer los cálculos de forma rápida y optimizada.

Así que, aunque la fórmula clásica es fácil de entender, el enfoque matricial es esencial para escalar el análisis de datos y es el que usan las herramientas modernas.
