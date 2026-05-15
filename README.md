# Empat.ia

> Método instalable para **guiarte en un proyecto de descubrimiento de usuarios**, usando [Claude](https://claude.com/claude-code) o Codex. Un Tandem entre VOS + Inteligencia Artificial para llevar adelante un proyecto de Design Thinking.

Empat.ia es un copiloto que te guía en un proceso de diseño empático siguiendo la metodología de Design Thinking. El entregable final son **principios de diseño** rastreables a evidencia, que vas a usar para decidir producto, comunicación con usuarios y estrategia.

## ⚠️ Antes de usarlo

- **Es un copiloto.** No reemplaza el trabajo de campo. Si no hablás con usuarios reales, el método no sirve.
- **Requiere tiempo: mínimo una semana de dedicación seria + 10-12 entrevistas hechas por vos.** El Guía te arma las guías, te ayuda a reclutar y te ordena la evidencia, pero no entrevista por vos.
- **No reemplaza criterio profesional en research con stakes altos** (médico, legal, financiero, vulnerabilidad de usuarios). Consultá con un researcher senior.


## Qué hace

- Te lleva a construir **principios de diseño** rastreables a evidencia. Ese es el entregable central.
- Crea una carpeta `descubrimiento/` dentro de tu proyecto con documentos persistentes (state, supuestos, decisiones, entrevistas, síntesis).
- Te guía paso a paso por 10 etapas, de alineación inicial a síntesis con evidencia.
- Separa hechos, supuestos e inferencias. No te deja confundir.
- Convierte material crudo de entrevistas en evidencia atómica trazable antes de escribir insights y principios.
- Te ofrece un concilio de agentes (economista, socióloga, filósofo, artista, dueño de pyme, taxista y otros) cuando una decisión necesita más presión.
- Mantiene el estado del proyecto visible en todo momento: dónde estás, qué hiciste, qué sigue.

## Para quién es

Para cualquiera con ganas de aprender de sus usuarios y dispuesto a hacer el trabajo. En particular: founders early-stage, Product Managers, UX Researchers, dueños de PyMEs repensando un servicio, estudiantes y equipos de innovación.

Requisitos mínimos:

| Lo que necesitás                      | Para qué                                      |
| ------------------------------------- | --------------------------------------------- |
| Cuenta paga de Claude o Codex         | Para que un asistente corra el método con vos |
| 10-12 entrevistas con usuarios reales | El campo lo hacés vos, no se delega           |
| Mínimo 1 semana de dedicación         | Sin tiempo, el método no rinde                |

## Cómo se usa

Decile a tu asistente (Claude o Codex), copiando este mensaje:

```text
Instalame este repo: https://github.com/brunogiel/Empat.ia
```

Tu asistente baja el método, te explica de qué se trata y arranca con vos.

En cualquier momento podés pedir _"cómo va"_ o _"status"_ y te muestra dónde estás.

### Instalación como skill global

Opcional, si querés tenerlo disponible en todos tus proyectos sin pegar el link cada vez:

```bash
./install.sh claude   # copia el skill a ~/.claude/skills/descubrimiento-guia
./install.sh codex    # copia el skill a ~/.codex/skills/descubrimiento-guia
```

Después invocás con _"usá Empat.ia"_ desde cualquier proyecto.

## Las 10 etapas

| Etapa | Qué se hace | Tiempo estimado | Entregable |
|---|---|---|---|
| 1. Inicio | Alineación, contexto, decisión a destrabar | 30-60 min | `documento-discovery.md` inicial |
| 2. Design Challenge | Encuadre del problema sin meter solución | 30-90 min | Challenge en el documento principal |
| 3. Research de mercado | Categoría, sustitutos, referentes (cuando aplica) | 1-3 hs | `research-mercado.md` con fuentes |
| 4. Base de conocimiento | Qué sabemos, qué asumimos, qué falta aprender | 30-60 min | `base-conocimiento.md` |
| 5. Usuarios y muestra | Roles, perfiles y muestra cualitativa | 30-90 min | `usuarios-y-muestra.md` |
| 6. Guías de entrevista | Una guía por perfil, machete no cuestionario | 1-2 hs | `guias-entrevista.md` |
| 7. Reclutamiento | Canales, mensajes, tracker | 2-5 días | `reclutamiento.md` actualizándose |
| 8. Checklist de campo | Antes, durante, después de cada entrevista | 30 min | `checklist-campo.md` |
| 9. Captura de entrevistas | Transcripts, notas, consentimientos, evidencia atómica | 1-3 semanas | `interviews/` poblado |
| 10. Síntesis | De evidencia a **principios de diseño** + insights, patrones y HMW | 3-5 hs | `sintesis.md` |

**Entregable final**: un set de **principios de diseño** rastreables a citas y evidencia de entrevistas. Reglas de decisión que vas a usar después para guiar:

- **Producto**: qué construir y qué dejar afuera, cómo priorizar features, cómo resolver dilemas de diseño cuando aparecen.
- **Comunicación con usuarios**: qué palabras usar, qué prometer, qué no prometer, cómo hablarles a los distintos perfiles.
- **Estrategia**: dónde apostar, qué segmento priorizar, qué oportunidades vale la pena perseguir y cuáles no.

Los principios vienen acompañados de patrones, insights, citas top y preguntas "Cómo podríamos..." (HMW) que abren la siguiente fase de ideación. Los principios son lo que se queda con vos cuando termina el método.

Las etapas con gate (1, 2, 3, 4, 5, 6, 9, 10) requieren actualizar el estado antes de avanzar. El método no te deja saltar.

También podés usar Empat.ia por etapa suelta. Si ya tenés entrevistas hechas y solo querés síntesis, podés arrancar directo en la etapa 10.

## Las cuatro acciones del Guía

En cada gate, el Guía recomienda una acción:

- **Avanzar**: el material es suficiente, pasamos a la próxima etapa.
- **Profundizar**: hay base pero falta espesor antes de seguir.
- **Cuestionar**: hay supuestos peligrosos o definiciones flojas, vamos a tensionar antes de avanzar.
- **Concilio**: la decisión amerita traer voces externas con lentes distintos.

El Guía propone. Vos elegís. Siempre podés sobreescribir la recomendación, y el Guía te muestra los riesgos de hacerlo.

## El concilio

Cuando una decisión es difícil, podés convocar al concilio: un equipo multidisciplinario que te tensiona desde lentes distintos. Como en un equipo de IDEO, mezclamos perfiles que no piensan igual:

- Un **economista** que mira incentivos y costos.
- Una **socióloga** que cuestiona el contexto cultural.
- Un **filósofo** que pelea por las definiciones y los supuestos.
- Una **artista** que abre analogías y posibilidades no obvias.
- Un **dueño de pyme** que aporta la realidad operativa.
- Un **especialista en growth** que mira canales y lenguaje.
- Y otros: tecnologo, experto en industria, uxer, researcher cualitativo, e incluso un **taxista** para cuando el equipo se pone demasiado experto y hace falta una mirada lateral.

El Guía te propone 3-5 según el proyecto y el gate, y te ayuda a elegir. Vos también podés sumar o sacar agentes a mano. La regla: combinar al menos tres lentes distintos para forzar desacuerdo útil. El concilio te muestra los ángulos que solo no ves.

## Privacidad y fuentes

El repositorio público contiene solo archivos genéricos del método. Proyectos privados, trabajo con clientes y ejemplos específicos quedan fuera.

El método se construyó sobre material propio de facilitación, referencias externas de human-centered design (IDEO, Acumen y otros) y **años de experiencia corriendo este método de forma manual, pre-IA**. Las referencias se listan en [`docs/reference-map.md`](docs/reference-map.md). Los documentos fuente permanecen con sus dueños originales.

## Licencia

MIT, ver [`LICENSE`](LICENSE).
