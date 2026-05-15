# 09, Captura y Orden de Entrevistas

## Objetivo

Ordenar notas, transcripciones y observaciones sin sintetizar prematuramente.

Esta etapa existe para que el usuario pueda bajar todo el material real de campo y el Guía lo convierte en una base procesable, sin perder origen ni inventar cierres.

## Notas del método

- Buscar una forma comoda de bajar y leer fotos, ideas, entrevistas y notas.
- Poner todo de manera visible persona a persona.
- Primero ordenar por entrevistado; despues cruzar perfiles.

## Documentos a tocar

- `descubrimiento/interviews/`
- `descubrimiento/interviews/README.md`
- `descubrimiento/interviews/index.md`
- `descubrimiento/interviews/evidence-ledger.md`
- `descubrimiento/base-conocimiento.md`
- `descubrimiento/state.yaml`
- `descubrimiento/assumptions.md`

## Estructura de carpetas

- `incoming/`: material crudo que trae el usuario.
- `transcripts/`: transcripciones limpias por entrevista.
- `notes/`: notas estructuradas por entrevista.
- `artifacts/`: fotos, capturas, documentos o materiales compartidos.
- `consent/`: consentimiento, restricciones y notas de privacidad.
- `processed/`: derivados auxiliares si hacen falta.

## Reglas

- Preservar citas textuales.
- No mezclar usuarios sin identificar origen.
- Marcar observaciones del entrevistador separadas de dichos del usuario.
- Guardar nombre, fecha, perfil y contexto.
- Usar `_template-notas.md` para cada entrevista.
- Registrar momentos de tension, sorpresa o emocion.
- Capturar herramientas, documentos, espacios y workarounds.

## Proceso

1. Pedir al usuario que baje todo el material en `incoming/`.
2. Asignar un ID por entrevista: `INT-001`, `INT-002`, etc.
3. Completar `index.md` con metadata, archivos y estado.
4. Copiar o mover transcripciones limpias a `transcripts/`.
5. Crear una nota estructurada en `notes/` usando `_template-notas.md`.
6. Guardar materiales en `artifacts/` y consentimientos en `consent/`.
7. Extraer evidencia atomica en `evidence-ledger.md`.
8. Marcar gaps antes de pasar a sintesis.

## Como procesar cada entrevista

Por entrevista, separar:

- Citas textuales.
- Facts reportados.
- Observaciones del entrevistador.
- Workarounds.
- Momentos de emocion, tension o sorpresa.
- Contradicciones.
- Preguntas nuevas.
- `Lectura del copiloto` cuando haya inferencia.

No cruzar patrones hasta haber procesado entrevista por entrevista.

## Gate

Accion sugerida:

- `Avanzar` si hay material suficiente para cruzar patrones.
- `Profundizar` si faltan entrevistas clave.
- `Cuestionar` si hay sesgo evidente de muestra o captura.
- `Concilio` si aparecen contradicciones fuertes.

## Checklist antes de sintetizar

- Cada entrevista tiene metadata.
- Hay citas textuales.
- Las observaciones estan separadas de interpretaciones.
- `index.md` lista archivos, consentimiento y gaps.
- `evidence-ledger.md` tiene evidencia por entrevista.
- Hay suficientes perfiles para cruzar patrones o se registran gaps.
