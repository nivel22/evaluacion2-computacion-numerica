# Evaluacion 2: La raiz que se esconde

**Universidad:** Universidad Catolica del Maule  
**Evaluacion:** Laboratorio evaluado 2

## Integrantes

- **Paloma Norambuena** - GitHub: [nivel22](https://github.com/nivel22)
- **Jeremy Orellana** - GitHub: [JAOC-03](https://github.com/JAOC-03)

## Descripcion del proyecto

Este proyecto corresponde a la Evaluacion 2 de la Universidad Catolica del Maule.

El objetivo es implementar y comparar seis metodos numericos de busqueda de raices, utilizando distintas funciones matematicas.

Los metodos implementados son:

1. Biseccion
2. Falsa posicion
3. Punto fijo
4. Secante
5. Newton-Raphson
6. Newton-Raphson mejorado

Se utilizaron funciones polinomicas, logaritmicas, exponenciales, trigonometricas y mixtas, incluyendo una funcion con raiz doble.

## Requisitos

Para ejecutar este proyecto se necesita:

- Python 3
- Visual Studio Code o un editor similar
- NumPy
- Matplotlib

Las bibliotecas necesarias se encuentran en el archivo `requirements.txt`.

## Instalacion del entorno

Primero se debe descargar el repositorio y abrir su carpeta en Visual Studio Code.

Todos los comandos se deben ejecutar desde la carpeta principal del proyecto.

### 1. Crear el entorno virtual

En Windows, ejecutar:

```powershell
python -m venv .venv
```

### 2. Activar el entorno virtual

En PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

### 3. Instalar las bibliotecas

Ejecutar:

```powershell
python -m pip install -r requirements.txt
```

## Ejecucion del proyecto

### 1. Generar los datos CSV

```powershell
python src\scripts\generar_datos.py
```

Este programa genera seis archivos CSV con valores de `x` y `f(x)`.

Los archivos se guardan en `src/data`.

### 2. Generar el resumen de convergencia

```powershell
python src\scripts\generar_resumen.py
```

Este programa ejecuta los seis metodos con las funciones seleccionadas y guarda los resultados en:

`src/data/resumen_convergencia.csv`

El archivo contiene los metodos, iteraciones, raices, errores, valores de la funcion y estados de convergencia.

### 3. Generar los graficos de funciones

```powershell
python src\scripts\graficar_funciones.py
```

Genera seis graficos donde se muestra cada funcion con su raiz marcada.

Los graficos se guardan en `src/assets`.

### 4. Generar los graficos de convergencia

```powershell
python src\scripts\graficar_convergencia.py
```

Genera seis graficos que muestran el error entre aproximaciones frente al numero de iteraciones, utilizando escala logaritmica.

### 5. Generar el grafico comparativo de iteraciones

```powershell
python src\scripts\graficar_iteraciones.py
```

Genera el archivo:

`src/assets/comparacion_iteraciones.png`

La marca NC indica que un metodo no alcanzo la tolerancia establecida.

### 6. Ejecutar los experimentos

```powershell
python src\scripts\experimentos.py
```

Compara distintos intervalos en biseccion y diferentes valores iniciales en Newton-Raphson.

Los resultados se guardan en:

`src/data/experimentos.csv`

## Organizacion de archivos

```text
evaluacion2-busqueda-raices/
    README.md
    informe.md
    requirements.txt
    src/
        assets/
        data/
        scripts/
            funciones.py
            biseccion.py
            falsa_posicion.py
            punto_fijo.py
            secante.py
            newton_raphson.py
            newton_mejorado.py
            pruebas.py
            generar_datos.py
            generar_resumen.py
            graficar_funciones.py
            graficar_convergencia.py
            graficar_iteraciones.py
            experimentos.py
```

## Descripcion de los archivos Python

| Archivo | Descripcion |
|---|---|
| funciones.py | Contiene las funciones matematicas y sus derivadas |
| biseccion.py | Implementa el metodo de biseccion |
| falsa_posicion.py | Implementa el metodo de falsa posicion |
| punto_fijo.py | Implementa el metodo de punto fijo |
| secante.py | Implementa el metodo de secante |
| newton_raphson.py | Implementa Newton-Raphson |
| newton_mejorado.py | Implementa Newton-Raphson mejorado |
| pruebas.py | Contiene pruebas individuales de los metodos |
| generar_datos.py | Genera los CSV de las funciones |
| generar_resumen.py | Genera el resumen de convergencia |
| graficar_funciones.py | Genera los graficos de las funciones |
| graficar_convergencia.py | Genera los graficos de error por iteracion |
| graficar_iteraciones.py | Genera la comparacion de iteraciones |
| experimentos.py | Compara diferentes intervalos y valores iniciales |

## Funciones utilizadas

| Categoria | Funcion | Intervalo o valor inicial |
|---|---|---|
| Polinomica simple | x³ - x - 2 | [1, 2] |
| Polinomica doble | (x - 2)² | x0 = 1.2 |
| Logaritmica | ln(x) + x - 4 | [2, 3] |
| Exponencial | e^(-x) - x | [0, 1] |
| Trigonometrica | cos(x) - x | [0, 1] |
| Mixta | √x - cos(x) | [0.1, 1] |

## Condiciones de las pruebas

Se utilizo una tolerancia de `0.000001` y un maximo de `100` iteraciones.

Los metodos cerrados se aplicaron cuando existia cambio de signo en el intervalo.

Los metodos abiertos utilizaron estimaciones iniciales.

En la funcion con raiz doble se estudio el comportamiento de los metodos cuando la curva toca el eje horizontal sin atravesarlo.

Para el criterio de parada se considero el valor absoluto de la funcion o la diferencia entre aproximaciones, segun el metodo implementado.

Los datos numericos se encuentran en la carpeta `src/data`.

Los graficos se encuentran en la carpeta `src/assets`.

El analisis de los resultados y las conclusiones se presentan en `informe.md`.

## Resultados generales

Newton-Raphson y Newton-Raphson mejorado necesitaron pocas iteraciones en varias funciones.

Biseccion presento un comportamiento seguro cuando existia cambio de signo.

Falsa posicion y secante tambien obtuvieron buenos resultados en distintas funciones.

Punto fijo dependio de la funcion utilizada para obtener las aproximaciones y no alcanzo la tolerancia en algunos casos.

Newton-Raphson mejorado encontro la raiz doble exactamente en una iteracion.

Los resultados completos se encuentran en los archivos CSV, los graficos y el informe de la evaluacion.