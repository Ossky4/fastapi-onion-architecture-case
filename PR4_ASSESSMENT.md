# PR4 mínima - evaluación de viabilidad

## Objetivo
Determinar si existe una PR4 mínima, local y conservadora para ejecutar el test agregado en PR3 (delegación de `GET /user/filters/`), sin abrir un frente amplio de compatibilidad.

## Hallazgo técnico exacto
La fricción de ejecución en este entorno (Python 3.10.19) se debe a imports directos de `Never` desde `typing`, símbolo disponible en Python 3.11+.

Error observado al correr el test focalizado:
- `ImportError: cannot import name 'Never' from 'typing'`

Archivo que dispara primero:
- `src/utils/service.py`

Además, el mismo patrón se repite en:
- `src/utils/repository.py`
- `src/utils/unit_of_work.py`

## Evaluación de tamaño de solución
Para que el test de PR3 ejecute en Python 3.10, el cambio mínimo real debe corregir este import en toda la cadena de carga.

Conclusión de alcance técnico:
- No alcanza con 1 archivo.
- Lo razonablemente mínimo son **3 archivos** (service/repository/unit_of_work) con una sola intención: compatibilidad de typing para `Never`.

## Decisión respecto al criterio del caso
Con el criterio explícito del caso (1 archivo, o como mucho 2), **no existe una PR4 mínima viable**.

Aunque el cambio sería pequeño y local en términos técnicos, **rebasa el umbral definido para continuar**.

## Recomendación
Cerrar el caso aquí, documentando la limitación de entorno (Python 3.10 + `typing.Never`) y evitando abrir una PR4 que ya nace fuera del perímetro acordado.
