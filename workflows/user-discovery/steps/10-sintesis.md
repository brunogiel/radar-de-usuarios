# 10, Sintesis

## Objetivo

Convertir material de entrevistas en conocimiento accionable y trazable.

## Input de Bruno incorporado

- Del dato al insight: no resumir por resumir.
- Cada insight debe nacer de facts o citas.
- Cruzar perfiles.
- Identificar patrones fuertes, senales debiles, outliers y contradicciones.
- Derivar design principles y HMW desde evidencia.
- No inventar.

## Documentos a tocar

- `radar/sintesis.md`
- `radar/interviews/index.md`
- `radar/interviews/evidence-ledger.md`
- `radar/documento-discovery.md`
- `radar/state.yaml`
- `radar/decision-log.md`
- `radar/assumptions.md`

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
