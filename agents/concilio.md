# Concilio Radar

## Rol

Procedimiento para convocar agentes de Radar en gates importantes.

## Flujo

1. Bruno formula una pregunta neutral.
2. Bruno selecciona 3-5 agentes relevantes.
3. Cada agente responde independiente siguiendo su archivo: tension, inputs, preguntas, output y success metrics.
4. Si hay desacuerdo importante, Bruno puede pedir una segunda ronda corta.
5. Bruno sintetiza:
   - acuerdos,
   - desacuerdos,
   - riesgos,
   - supuestos a registrar,
   - metricas de calidad que no se estan cumpliendo,
   - recomendacion,
   - accion sugerida.
6. Bruno actualiza `state.yaml`, `decision-log.md` o `assumptions.md`.

## Prompt de convocatoria

```text
Actua como el agente convocado dentro del Concilio Radar.

Pregunta neutral:
Voy a darte una pregunta neutral.

Contexto disponible:
Voy a darte el contexto disponible del proyecto.

Responde desde tu tension especifica. No busques consenso. No inventes datos. Separa evidencia, inferencias y dudas. Marca cualquier supuesto que deberia registrarse.

Formato:
- Lectura principal
- Desacuerdo o tension
- Evidencia usada
- Supuestos o dudas
- Preguntas que conviene hacer
- Recomendacion concreta
- Confianza: baja/media/alta
```

## Output

```markdown
## Pregunta

...

## Agentes convocados

- ...

## Perspectivas

### Agente

...

## Sintesis de Bruno

- Acuerdos:
- Desacuerdos:
- Riesgos:
- Supuestos a registrar:
- Success metrics en riesgo:
- Recomendacion:
- Accion sugerida:
```

## Criterio de calidad

Un buen concilio no busca consenso rapido. Tiene que:

- Mostrar desacuerdos utiles.
- Identificar que evidencia falta.
- Recomendar una accion, no una lista infinita.
- Actualizar documentos si cambia el estado del proceso.
- Mantener las voces distinguibles sin convertirlas en teatro.
