# 03, Research de Mercado

## Objetivo

Hacer deep research de mercado cuando aplique, usando web actual y fuentes citables.

## Input de Bruno incorporado

- El research de mercado ayuda a responder parcialmente el design challenge.
- Puede mirar reportes, tendencias, tamano de mercado, players, benchmarks y geografias relevantes.
- No reemplaza hablar con usuarios.

## Documentos a tocar

- `radar/research-mercado.md`
- `radar/documento-discovery.md`
- `radar/state.yaml`
- `radar/decision-log.md`

## Regla de web

Este paso requiere busqueda web actual. Si no hay web, dejar status `not_started` o `capturing` y explicar el bloqueo.

## Agente responsable

Delegar a `deep-researcher-mercado`.

Output minimo:

- Scope.
- Preguntas de investigacion.
- Mercado y tendencias.
- Players y alternativas.
- Comportamiento de clientes/usuarios.
- Riesgos y restricciones.
- Implicancias para entrevistas.
- Fuentes.

## Usar el template

Completar `research-mercado.md` con tablas de:

- Hallazgos con dato, fuente e implicancia.
- Players, sustitutos y benchmarks.
- Supuestos a validar con usuarios.

No cerrar la etapa hasta convertir el research en preguntas nuevas para entrevistas.

## Gate

Accion sugerida:

- `Avanzar` si el research ya orienta preguntas de usuario.
- `Profundizar` si faltan fuentes o scope.
- `Cuestionar` si el research empuja solucion sin evidencia de usuarios.
- `Concilio` si hay industria compleja o datos contradictorios.

Si el mercado objetivo son pymes, sumar `dueno-pyme` al concilio para traducir datos de mercado a realidad operativa.
