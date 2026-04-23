# Comparativa final — seis Case Projects

## Propósito
Comparar los seis casos realizados para identificar qué tipo de señal aporta cada uno, en qué condiciones Codex rinde mejor y qué hipótesis conviene probar a continuación.

## Caso 1 — mi-primer-repo
Este repositorio funcionó como sandbox inicial para validar el método base de trabajo con Codex en condiciones controladas.

### Qué se probó
- PRs pequeñas y de una sola intención.
- Cambios pequeños de código, tests y documentación.
- Bugfixes y mejoras de UX de bajo riesgo.
- Refactors pequeños, incluyendo un caso multiarchivo.

### Qué señal aportó
`mi-primer-repo` confirmó que el método base funciona bien cuando:
- el contexto es simple,
- el riesgo es bajo,
- la validación es barata,
- y el alcance está claramente delimitado.

También sirvió para fijar un patrón operativo:
- contrato claro,
- PR pequeña,
- checks explícitos,
- microevaluación humana al cierre.

## Caso 2 — csvtools-case
Este repositorio funcionó como primer Case Project de cleanup arquitectónico pequeño en un entorno más real que el sandbox inicial.

### Qué se probó
- PR1 documental para delimitar alcance y hotspots.
- Cleanup local mínimo.
- Cleanup multiarchivo real.
- Blindaje con tests sobre una frontera tratada.
- Mejora mínima del entorno de tests.
- Documentación reutilizable del método.

### Qué señal aportó
`csvtools-case` confirmó que Codex puede trabajar con control en un repo más real cuando:
- el hotspot está bien delimitado,
- el cambio sigue siendo pequeño y reversible,
- la validación mínima del repo es suficiente,
- y la revisión humana mantiene disciplina de alcance.

También mostró que mejorar pronto la infraestructura mínima de validación aumenta la calidad de las PRs posteriores.

## Caso 3 — timesheet-case
Este repositorio funcionó como caso para medir una hipótesis distinta: elección entre varias alternativas plausibles de cleanup.

### Qué se probó
- PR1 de selección explícita entre alternativas.
- Rechazo de una primera dirección menos conservadora.
- Reformulación de PR2 hacia una opción más prudente.
- Blindaje con tests.
- Ajuste mínimo de entorno para hacer ejecutable el blindaje.
- Retrospectiva breve de cierre.

### Qué señal aportó
`timesheet-case` añadió una señal nueva respecto a los casos anteriores:
no solo que Codex puede ejecutar cambios pequeños, sino que puede participar en una decisión local entre varias opciones plausibles, siempre que existan:
- alcance explícito,
- criterio conservador,
- revisión humana disciplinada,
- y validación mínima suficiente.

También mostró que la revisión humana no solo valida ejecución, sino calidad de decisión.

## Caso 4 — har-file-sanitiser-case
Este repositorio funcionó como caso para medir una hipótesis de dependencias internas más ricas entre módulos (`cli`, `core`, `utils`) sin abandonar el marco de PRs pequeñas.

### Qué se probó
- PR1 documental para delimitar la frontera bajo observación.
- PR2 técnica mínima sobre un ajuste conservador de límites entre CLI y core.
- PR3 de blindaje explícito de la delegación a streaming sin prelectura redundante.
- PR4 mínima de compatibilidad para hacer ejecutable el test objetivo en Python 3.10, sin abrir un frente amplio.

### Qué señal aportó
`har-file-sanitiser-case` aportó una señal útil sobre un contexto con dependencias internas más ricas:
- Codex puede mantener criterio conservador en una frontera más densa,
- puede sostener el cambio con blindaje específico,
- y puede aceptar una corrección mínima de compatibilidad cuando esa corrección sigue siendo local, explícita y de una sola intención.

También confirmó que no toda fricción de entorno justifica abrir una reforma amplia: a veces existe una salida pequeña y suficiente.

## Caso 5 — pytest-fastapi-crud-example-case
Este repositorio funcionó como caso para medir una ruta multicapa más explícita: API → lógica intermedia → acceso a base de datos, manteniendo PRs pequeñas.

### Qué se probó
- PR1 documental para delimitar la ruta multicapa bajo observación.
- PR2 técnica mínima con extracción local y conservadora de una operación repetida dentro de `app/user.py`.
- PR3 de blindaje específico sobre reutilización del helper compartido en `get_user` y `update_user`.
- PR4 documental de cierre, dejando explícito el límite de validación por entorno.

### Qué señal aportó
`pytest-fastapi-crud-example-case` añadió una señal distinta:
- Codex puede sostener un cambio pequeño dentro de una ruta que atraviesa varias capas internas,
- puede evitar un salto prematuro a una arquitectura más ambiciosa,
- y puede mantener disciplina de PR pequeña incluso en una ruta más densa que las tratadas antes.

El límite principal fue que la validación dinámica final quedó condicionada por fricción de entorno ajena al hotspot trabajado.

## Caso 6 — fastapi-onion-architecture-case
Este repositorio funcionó como caso para medir una ruta multicapa más profunda, con coordinación entre router, service y repository, y con dependencias internas más densas que en los casos anteriores.

### Qué se probó
- PR1 documental para delimitar la ruta bajo observación.
- PR2 técnica mínima de alineación de contrato interno entre `UserService.get_users_by_filters(...)` y `UserRepository.get_users_by_filters(...)`.
- PR3 de blindaje pequeño con test focalizado sobre `GET /user/filters/` para fijar la delegación del contrato interno.
- Evaluación explícita de viabilidad de PR4 mínima, concluyendo que corregir la fricción de entorno excedía el perímetro acordado.
- Cierre del caso sin expandir alcance.

### Qué señal aportó
`fastapi-onion-architecture-case` añadió una señal útil sobre un nivel más alto de densidad interna:
- Codex puede sostener una decisión conservadora en una ruta con varias capas más profundas,
- puede alinear un contrato interno pequeño sin rediseño de arquitectura,
- y puede blindar esa decisión con un test focalizado.

También aportó una señal metodológica importante:
cuando la fricción final pertenece al entorno y la corrección mínima real excede el perímetro experimental, la decisión correcta puede ser cerrar el caso con trazabilidad en lugar de seguir abriendo PRs.

## Diferencias clave entre los seis casos

### mi-primer-repo
- mayor control,
- menor complejidad,
- señal rápida,
- mejor para fijar el método base.

### csvtools-case
- más real que el sandbox,
- útil para medir cleanup multiarchivo pequeño,
- buena base para consolidar método reusable.

### timesheet-case
- mejor para medir elección entre alternativas plausibles,
- más dependiente de revisión humana para distinguir una solución válida de la opción más conservadora,
- buena señal sobre reformulación prudente.

### har-file-sanitiser-case
- mejor para medir criterio conservador en una frontera con dependencias internas más ricas,
- buena señal sobre correcciones mínimas de compatibilidad sin expansión innecesaria.

### pytest-fastapi-crud-example-case
- mejor para medir disciplina conservadora dentro de una ruta multicapa más explícita,
- buena señal sobre coordinación local entre API, lógica intermedia y acceso a datos,
- con límite claro de validación condicionado por el entorno.

### fastapi-onion-architecture-case
- mejor para medir coordinación en una ruta multicapa más profunda y con mayor densidad entre capas,
- buena señal sobre alineación mínima de contrato interno entre service y repository,
- y buena señal de gobernanza experimental al cerrar el caso sin forzar una expansión de alcance.

## Aprendizajes operativos comunes
En los seis casos, Codex rindió mejor cuando se mantuvieron estas condiciones:
- una sola intención por PR,
- cambios pequeños y revisables,
- restricciones explícitas,
- checks claros,
- separación entre fallo del entorno y efecto del cambio,
- microevaluación humana breve tras cada revisión.

## Qué parece funcionar mejor
Codex aporta más valor cuando trabaja como:
- operador técnico de ejecución,
- sobre hotspots acotados,
- con decisiones reversibles,
- en repos con validación razonablemente barata,
- y con revisión humana que discipline alcance y criterio.

## Límites observados
- El valor cae cuando la PR aporta más higiene local que señal estructural.
- La señal empeora cuando el entorno de validación introduce demasiado ruido.
- Ya hay evidencia sólida sobre cleanup pequeño, multiarchivo pequeño, elección conservadora local, fronteras con dependencias internas más ricas y rutas multicapa explícitas.
- También hay evidencia de que la gobernanza del experimento importa: no toda fricción merece una PR adicional.
- Aún no se ha probado con suficiente claridad una situación donde una decisión pequeña atraviese varias capas con dependencias más profundas y, además, compita contra varias alternativas conservadoras realmente fuertes a la vez.

## Conclusión
Los seis casos, en conjunto, sugieren que Codex funciona bien en cambios pequeños, acotados, reversibles y bien revisados.

La evidencia acumulada es especialmente sólida en seis planos:
1. ejecución disciplinada de PRs pequeñas,
2. cleanup multiarchivo pequeño con validación suficiente,
3. elección conservadora entre alternativas plausibles,
4. mantenimiento del criterio en fronteras con dependencias internas más ricas,
5. disciplina de alcance dentro de rutas multicapa explícitas,
6. capacidad de cerrar un caso correctamente cuando el entorno ya no justifica expandir alcance.

## Recomendación de la siguiente hipótesis experimental
No seguir por inercia en ninguno de estos seis repositorios.

La siguiente hipótesis debería subir un nivel y probar esto:

**Codex puede mantener criterio conservador en un repo con coordinación entre varias capas internas y dependencias más profundas, enfrentando además 2 o 3 alternativas pequeñas realmente competitivas, sin perder disciplina de PR pequeña ni claridad de validación.**

## Qué debería tener el siguiente repo
- entrypoint claro,
- coordinador o capa intermedia explícita,
- lógica central distinguible,
- adaptador o persistencia ligera,
- tests locales suficientes para validar una ruta concreta,
- ausencia de infraestructura pesada o dependencias externas dominantes,
- y un hotspot donde existan varias alternativas conservadoras plausibles, no una sola obvia.

## Recomendación final
Usar esta comparativa como documento de cierre del bloque actual y como base para seleccionar el siguiente repositorio candidato, evitando repetir hipótesis ya suficientemente medidas y priorizando ahora un caso con más densidad estructural y más competencia real entre alternativas pequeñas.
