# Concilio

## Rol

Procedimiento para convocar agentes en gates importantes del método.

El concilio existe para que decisiones difíciles se tomen con presión real, no solo con la opinión del que está al volante. Como en un equipo de IDEO, mezclamos perfiles que no suelen pensar igual: un economista que mira incentivos, una artista que cuestiona la forma, un filósofo que pelea por las definiciones, un dueño de pyme que aporta la calle, e incluso un taxista que baja la abstracción cuando todo se pone demasiado experto. Cada voz trae una tensión distinta. No reemplaza el criterio del Guía ni el del usuario. Muestra los ángulos que solo no se ven.

## Flujo

1. El Guía formula una pregunta neutral.
2. **El Guía propone 3-5 agentes relevantes con una justificación corta de cada uno. El usuario confirma, suma o saca antes de convocar.** La regla: combinar al menos tres lentes distintos (técnico-analítico, humano-cualitativo, divergente o crítico, opcionalmente lateral no experta).
3. Cada agente responde independiente siguiendo su archivo: tensión, inputs, preguntas, output y success metrics.
4. Si hay desacuerdo importante, el Guía puede pedir una segunda ronda corta.
5. El Guía sintetiza:
   - acuerdos,
   - desacuerdos,
   - riesgos,
   - supuestos a registrar,
   - métricas de calidad que no se están cumpliendo,
   - recomendación,
   - acción sugerida.
6. El Guía actualiza `state.yaml`, `decision-log.md` o `assumptions.md`.

## Prompt de convocatoria

```text
Actuá como el agente convocado dentro del Concilio.

Pregunta neutral:
Voy a darte una pregunta neutral.

Contexto disponible:
Voy a darte el contexto disponible del proyecto.

Respondé desde tu tensión específica. No busques consenso. No inventes datos. Separá evidencia, inferencias y dudas. Marcá cualquier supuesto que debería registrarse.

Formato:
- Lectura principal
- Desacuerdo o tensión
- Evidencia usada
- Supuestos o dudas
- Preguntas que conviene hacer
- Recomendación concreta
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

## Síntesis del Guía

- Acuerdos:
- Desacuerdos:
- Riesgos:
- Supuestos a registrar:
- Success metrics en riesgo:
- Recomendación:
- Acción sugerida:
```

## Criterio de calidad

Un buen concilio no busca consenso rápido. Tiene que:

- Mostrar desacuerdos útiles.
- Identificar qué evidencia falta.
- Recomendar una acción, no una lista infinita.
- Actualizar documentos si cambia el estado del proceso.
- Mantener las voces distinguibles sin convertirlas en teatro.
