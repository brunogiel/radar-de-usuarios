# Interviews

Esta carpeta es la bandeja de trabajo para todo el material de campo: transcripciones, notas, audios, fotos, documentos compartidos, consentimientos y observaciones.

Regla central: el material crudo se preserva. La sintesis se hace despues, con trazabilidad.

## Estructura

```text
interviews/
├── README.md
├── index.md
├── evidence-ledger.md
├── incoming/
├── transcripts/
├── notes/
│   └── _template-notas.md
├── artifacts/
├── consent/
└── processed/
```

## Para quien lleva el proceso

Cuando termines entrevistas o recibas material, bajalo en `incoming/` sin preocuparte por dejarlo perfecto. Puede entrar como:

- transcripcion completa,
- notas sueltas,
- resumen del entrevistador,
- audio o video,
- fotos del contexto,
- screenshots,
- documentos compartidos por el entrevistado,
- consentimiento o autorizacion.

Despues Bruno ordena ese material sin perder origen.

## Naming recomendado

Usar un ID unico por entrevista.

```text
INT-001_nombre-o-alias_perfil_fecha.ext
```

Ejemplos:

```text
INT-001_maria_admin-pyme_2026-05-14_transcript.md
INT-001_maria_admin-pyme_2026-05-14_notas.md
INT-001_maria_admin-pyme_2026-05-14_foto-proceso.jpg
```

Si hay privacidad sensible, usar alias:

```text
INT-003_alias-a_dueno-comercio_2026-05-18_transcript.md
```

## Flujo de procesamiento

1. Ingresar material en `incoming/`.
2. Registrar cada entrevista en `index.md`.
3. Mover o copiar transcripciones limpias a `transcripts/`.
4. Crear una nota estructurada en `notes/` usando `_template-notas.md`.
5. Guardar fotos, documentos o capturas en `artifacts/`.
6. Guardar consentimiento o restricciones en `consent/`.
7. Extraer evidencia atomica en `evidence-ledger.md`.
8. Recien despues cruzar patrones en `../sintesis.md`.

## Que cuenta como evidencia

- Cita textual.
- Hecho reportado por el entrevistado.
- Observacion del entrevistador.
- Workaround concreto.
- Momento de emocion, tension o sorpresa.
- Contradiccion.
- Material compartido con permiso.
- Pregunta abierta que surge del campo.

## Reglas

- No mezclar entrevistas sin ID.
- No convertir notas sueltas en insight sin fuente.
- No borrar contradicciones.
- No completar silencios con inferencias.
- Si Bruno interpreta algo, marcarlo como `Lectura del copiloto`.
- Si falta consentimiento, no usar citas identificables.
