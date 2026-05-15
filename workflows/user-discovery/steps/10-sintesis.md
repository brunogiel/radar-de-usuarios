# 10, Sintesis

## Objetivo

Convertir material de entrevistas en **principios de diseño** trazables a evidencia. Los principios son el entregable central de Empat.ia: reglas de decisión que el usuario va a usar para producto, comunicación y estrategia.

Insights, patrones, HMW y top citas son material que sostiene a los principios, no son el output final. Si un principio no se rastrea a facts o citas, no es un principio: es una opinión.

## Notas del método

- Del dato al insight, del insight al principio: cada salto se sostiene en evidencia.
- Cada insight y cada principio deben nacer de facts o citas.
- Cruzar perfiles.
- Identificar patrones fuertes, senales debiles, outliers y contradicciones.
- Derivar design principles y HMW desde evidencia.
- Los principios son reglas de diseño accionables, no features ni opiniones.
- No inventar.

## Documentos a tocar

- `descubrimiento/sintesis.md`
- `descubrimiento/interviews/index.md`
- `descubrimiento/interviews/evidence-ledger.md`
- `descubrimiento/documento-discovery.md`
- `descubrimiento/state.yaml`
- `descubrimiento/decision-log.md`
- `descubrimiento/assumptions.md`

## Proceso

1. Revisar `interviews/index.md` para saber que material esta listo y que gaps hay.
2. Revisar `interviews/evidence-ledger.md`.
3. Completar resumen por entrevistado solo con entrevistas procesadas.
4. Agrupar evidencia por temas.
5. Cruzar perfiles.
6. Identificar patrones, outliers y contradicciones.
7. Escribir insights como lectura, no como resumen.
8. Derivar design principles.
9. Formular HMW.
10. Listar preguntas abiertas.

## Criterios de calidad

- Un insight no es resumen: es una nueva perspectiva sobre el problema.
- Cada insight necesita fact o cita rastreable al `evidence-ledger.md`.
- Los principles son reglas de diseno, no features.
- Los HMW no deben traer una solucion escondida.
- Un HMW justo permite imaginar varias soluciones rapidamente.
- Si falta evidencia, decirlo en vez de rellenar.

## Tablas obligatorias

| Evidencia IDs | Patron | Insight | Design Principle | HMW |
|---|---|---|---|---|

| Gap de evidencia | Impacto en la sintesis | Accion sugerida |
|---|---|---|

## Concilio

Sugerir `Concilio` antes de cerrar si:

- Hay insights debiles.
- Hay contradicciones relevantes.
- Hay principios de diseno sin evidencia.
- El `evidence-ledger.md` muestra gaps importantes.
- El usuario quiere priorizar oportunidades.

## Gate

Accion sugerida:

- `Avanzar` si los insights son trazables y utiles.
- `Profundizar` si faltan citas o entrevistas.
- `Cuestionar` si se estan inventando conclusiones.
- `Concilio` si hace falta tensionar la sintesis.
