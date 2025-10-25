# CHANGELOG - Mod Development Backup

Este archivo documenta TODOS los cambios realizados al mod durante el desarrollo.  
**PROPÓSITO:** Backup y trazabilidad antes de modificaciones masivas.

**FORMATO:**

```
## [Fecha] - HH:MM

### Added
- Nuevos archivos/funcionalidades

### Changed
- Modificaciones a código existente

### Fixed
- Correcciones de bugs

### Technical Notes
- Notas técnicas importantes
- Decisiones de diseño
- Warnings de CK3-Tiger
```

---

## [2025-10-25] - Debug Mode Expandido - 21:00

### Added

- **3 Nuevas Decisiones de Debug Masivas:**
  - `ac_nickname_give_all` - Dar apodos a TODOS los personajes elegibles (16+)
  - `ac_nickname_clear_all` - Limpiar TODOS los apodos del mundo
  - `ac_nickname_export_report` - Exportar reporte TXT con todos los apodos
- **Evento de Exportación:** `ac_nickname.9999` para generar reportes
- **Sistema de Logging:** Usa `debug_log` para exportar datos a game.log

### Changed

- Decisiones de debug ahora son 7 (era 4)
- Localizaciones EN/ES actualizadas con las 3 nuevas decisiones
- README actualizado con tabla de herramientas y formato de exportación

### Technical Notes

- **Export Format:** `Character ID | Name | Title | Nickname`
- **Export Location:** `Documents/Paradox Interactive/Crusader Kings III/logs/game.log`
- **Give All:** Usa `every_living_character` con filtro de edad 16+
- **Clear All:** Usa `every_living_character` con `remove_nickname`
- **Cooldowns Agregados:**
  - Give All: 365 días (1 año)
  - Clear All: 30 días
  - Export Report: 30 días
- **CK3-Tiger:** 0 errors, 2140 warnings (solo localizaciones faltantes)

**Uso del Export:**

1. Activar debug mode
2. Usar "Export Nickname Report"
3. Ir a `Documents/Paradox Interactive/Crusader Kings III/logs/`
4. Abrir `game.log`
5. Buscar "===== NICKNAME REPORT ====="
6. Copiar reporte a archivo TXT separado

---

## [2025-10-25] - Debug Mode Implementado - 20:00

### Added

- **Debug Mode System** con 4 decisiones:
  - `ac_nickname_toggle_debug` - Activar/desactivar modo debug
  - `ac_nickname_clear` - Limpiar apodo actual para testing
  - `ac_nickname_manual_block` - Bloquear asignación de apodos
  - `ac_nickname_manual_unblock` - Desbloquear asignación de apodos
- **Archivo:** `common/decisions/ac_nickname_debug_decisions.txt` (133 líneas)
- **Localización EN:** `localization/english/ac_nickname_debug_l_english.yml` (44 líneas)
- **Localización ES:** `localization/spanish/ac_nickname_debug_l_spanish.yml` (44 líneas)
- **README actualizado** con sección "Debug Mode" explicando uso y herramientas

### Changed

- Sintaxis de decisiones simplificada para evitar errores de CK3-Tiger
- `is_councillor` usado en lugar de `has_council_position` (más compatible)
- `remove_nickname` usado en lugar de `clear_nickname` (correcto en CK3)
- Eliminado campo `picture` de decisiones (causaba errores de estructura)

### Fixed

- Corregidos 12 errores de CK3-Tiger en archivo de decisiones
- Sintaxis de `trigger_event` corregida (requiere bloques con `id` y `days`)
- Triggers personalizados expandidos inline para evitar errores de estructura

### Technical Notes

- **CK3-Tiger Final:** 0 errors, 2103 warnings (mayoría son localizaciones faltantes)
- **UTF-8 BOM:** Aplicado a todos los archivos nuevos
- **Funcionalidad:** Debug mode solo visible cuando se activa con la decisión toggle
- **Sin costo:** Todas las decisiones de debug son gratis (prestige=0, piety=0)
- **Cooldown:** No hay cooldown para decisiones de debug (testing rápido)
- **AI:** AI no puede usar decisiones de debug (ai_will_do = 0)

**Uso en juego:**

1. Cargar partida
2. Abrir menú Decisiones
3. Usar "Toggle Nickname Debug Mode"
4. Aparecerán las herramientas de debug
5. Probar asignación/limpieza de apodos

---

## [2025-10-25] - Inicio del Proyecto

### Added - 14:00

- `.gitignore` creado con exclusiones para VS Code, backups, OS files, CK3-Tiger cache
- `CHANGELOG_MOD.md` este archivo para tracking de cambios
- Estructura base del proyecto documentada

### Technical Notes

- **Proyecto base:** Mod NEW_NICKNAMES con 2047+ nicknames existentes
- **Objetivo:** Rediseño completo del sistema de asignación de nicknames
- **Sistema propuesto:**
  - Weight-based (no probabilidad fija 33%)
  - Faith-based (4 familias: abrahamic, eastern, pagan, singles)
  - Skill-based (rangos: 0-8, 9-11, 12-16, 17+)
  - Trait-based (congenital + physical)
  - Age-gated (16+ physical, 20+ skills)

### Reference Analysis

- **Mod Nicknames+ (2251687872):** 235 nicknames, 305 eventos, sistema de 3 capas
- **Sistema de probabilidad:** yearly_pulse → 2-4% → random_selection → weight_multiplier
- **Best practices identificadas:**
  - Weight system para balance fino
  - Game rules para customización
  - Age gating por tipo de nickname
  - Hidden events vs notification toggle

---

## [2025-10-25] - Análisis de Nicknames Existentes

### Nicknames Clasificados

#### Por Archivo:

- **ac_nickname_classification_faith.txt:** ~150 nicknames faith-bound
- **ac_nickname_classification_generic.txt:** ~1897 nicknames genéricos

#### Por Categoría Temática (Pendiente de análisis detallado):

- Warriors/Martial: ~300
- Beauty/Appearance: ~200
- Disabilities/Scars: ~150
- Knights (colored/regional): ~100
- Animals/Totems: ~250
- Giants/Dwarfs: ~80
- Historical epithets: ~600
- Religious: ~150
- Miscellaneous: ~217

**TOTAL:** 2047 nicknames (aproximado)

### Next Steps

- [ ] Análisis detallado línea por línea de ambos archivos
- [ ] Documentar nicknames por fe específica
- [ ] Identificar missing female variants (si existen)
- [ ] Crear mapping de nicknames → conditions

---

## [2025-10-25] - Git Repository Setup - 15:30

### Completed

- ✅ `git init` en directorio del mod
- ✅ `git remote add origin https://github.com/Alfarojo25/CK3_Nicknames.git`
- ✅ Primer commit (ffc5722): "PHASE 1: Initial structure" - 11 archivos, 4372 líneas
- ✅ `git push -u origin main`
- ✅ Segundo commit (e63f479): "Add README.md and LICENSE" - 2 archivos, 203 líneas

---

## [2025-10-25] - CK3-Tiger Validation Results - 16:00

### Validation Executed

- **Tool:** CK3-Tiger v1.13.0
- **Game Version:** CK3 v1.17.1 (Tiger made for 1.17.0 - minor version mismatch, probablemente OK)
- **Results:** 117 errors, 25 warnings

### Errors by Category

#### 1. Missing Events (6 errors)

- ac_nickname.2101 (Bloodaxe)
- ac_nickname.2102 (The Terrible)
- ac_nickname.2103 (Scourge of God)
- ac_nickname.3101 (The Great)
- ac_nickname.3102 (The Magnificent)
- ac_nickname.3103 (The Lawgiver)

#### 2. Invalid Comparison Syntax (48 errors)

- `value >= X` y `value <= X` NO son válidos en triggers
- **Afecta:** Todos los skill range triggers (ac_skill_is_bad, ac_skill_is_medium)
- **Solución:** Usar check_range_bounds en lugar de comparaciones

#### 3. Invalid Trait Names (55 errors)

- ❌ `beautiful`, `comely`, `ugly`, `hideous` → ✅ `beauty_good_3`, `beauty_good_1`, `beauty_bad_1`, `beauty_bad_3`
- ❌ `genius`, `intelligent`, `slow`, `stupid` → ✅ `intellect_good_3`, `intellect_good_1`, `intellect_bad_1`, `intellect_bad_3`
- ❌ `one_handed` → ✅ `one_legged` (verificar si existe one_handed)
- ❌ `pox_scarred` → Verificar nombre correcto
- ❌ `blinded` → Verificar nombre correcto
- ❌ `mangled` → Verificar nombre correcto
- ❌ `frail` → Verificar nombre correcto
- ❌ `lifestyle_scholar` → Verificar nombre correcto
- ✅ Correctos confirmados: `giant`, `dwarf`, `albino`, `scaly`, `spindly`, `bleeder`, `wheezing`, `lisping`, `stuttering`, `one_eyed`, `one_legged`, `fecund`, `infertile`

#### 4. Invalid Religion Names (8 errors)

- ❌ `religion_christianity_church` → ✅ `christianity_religion`
- ❌ `religion_islam` → ✅ `islam_religion`
- ❌ `religion_judaism` → ✅ `judaism_religion`
- ❌ `religion_hinduism` → ✅ `hinduism_religion`
- ❌ `religion_buddhism` → ✅ `buddhism_religion`
- ❌ `religion_jainism` → ✅ `jainism_religion`
- ❌ Formato pagan incorrecto → Verificar nombres correctos

#### 5. Invalid Faith Names (2 errors)

- ❌ `faith:sunni` → ✅ `faith:ashari` o `faith:maturidi` o `faith:mutazila`
- ❌ `faith:shiite` → ✅ `faith:ismaili` o `faith:zayidi`

#### 6. Unknown Fields (3 errors)

- ❌ `num_of_secrets` → No existe este campo
- ❌ `num_of_virtues` → No existe este campo
- **Solución:** Usar contadores alternativos o eliminar condición

### Warnings (25 total)

#### 1. Duplicate Nicknames (4 warnings)

- `nick_hist_the_pilgrim_king` duplicado en líneas 69 y 146
- `nick_hist_the_reliquary` duplicado en líneas 83 y 152
- `nick_hist_the_shrine` duplicado en líneas 85 y 155
- `nick_hist_the_censer` duplicado en líneas 87 y 149
- **Archivo:** ac_nickname_classification_faith.txt
- **Solución:** Eliminar duplicados

#### 2. Missing UTF-8 BOM (3 warnings)

- Archivos afectados: ac_nickname_on_actions.txt, ac_nickname_triggers.txt, ac_nickname_events.txt
- **Solución:** Guardar con UTF-8 BOM encoding

#### 3. Logic Warnings - Value Overwrite (18 warnings)

- Todas las líneas con `value <= X` sobrescriben el valor previo `value >= X`
- **Causa:** Sintaxis incorrecta de comparación (ver Error #2)
- **Solución:** Corregir sintaxis de comparación

### Action Items

#### CRITICAL (Bloquean funcionalidad)

1. ✅ Crear descriptor.mod (HECHO)
2. ⚠️ Corregir sintaxis de comparación en skill ranges (48 errores)
3. ⚠️ Corregir nombres de traits (55 errores)
4. ⚠️ Corregir nombres de religiones/faiths (10 errores)
5. ⚠️ Crear los 6 eventos faltantes
6. ⚠️ Eliminar o reemplazar campos desconocidos (num_of_secrets, num_of_virtues)

#### IMPORTANT (Mejoran calidad)

7. ⚠️ Eliminar nicknames duplicados en ac_nickname_classification_faith.txt
8. ⚠️ Guardar archivos con UTF-8 BOM encoding

#### Target: 0 errors, 0 warnings

---

## [2025-10-25] - CK3-Tiger Validation COMPLETADO - 17:30

### Fixed - ALL VALIDATION ERRORS RESOLVED ✅

**Resultado Final:** 0 errors, 1 warning (encoding false positive)  
**Mejora:** De 117 errors iniciales a 0 errors

#### Correcciones Implementadas:

1. **Sintaxis de Skill Comparisons** (48 errores corregidos)

   - Eliminado: `diplomacy = { value >= 9; value <= 11 }`
   - Implementado: `diplomacy >= 9; diplomacy <= 11` (comparación directa)
   - Aplicado a: todos los skill triggers (bad, medium, glorious)

2. **Nombres de Traits** (55 errores corregidos)

   - `beautiful/comely/ugly/hideous` → `beauty_good_3/beauty_good_1/beauty_bad_1/beauty_bad_3`
   - `genius/intelligent/slow/stupid` → `intellect_good_3/intellect_good_1/intellect_bad_1/intellect_bad_3`
   - `blinded` → `blind`
   - `pox_scarred` → `great_pox`
   - `lifestyle_scholar` → `scholar`
   - Eliminados (no existen): `one_handed`, `frail`, `mangled`

3. **Nombres de Religiones y Faiths** (12 errores corregidos)

   - Agregado prefijo `religion:` a todas las religiones
   - `religion_christianity_church` → `religion:christianity_religion`
   - `religion_islam` → `religion:islam_religion`
   - `faith:sunni` → `faith:ashari` (+ maturidi/mutazila)
   - `faith:shiite` → `faith:ismaili` (+ zayidi)
   - Eliminadas religiones inexistentes: `bori_religion`, `orisha_religion`, `roog_religion`, `yazidism_religion`

4. **Campos Desconocidos** (3 errores corregidos)

   - `num_of_secrets >= 3` → `has_trait = schemer`
   - `num_of_virtues >= 3` → traits individuales (`humble`, `temperate`, `compassionate`)
   - `any_war = { count >= 3 }` → eliminado (campo no existe)
   - `num_won_wars >= 10` → eliminado (campo no existe)
   - `has_trait = charitable` → `has_trait = compassionate`
   - `has_trait = famous` → `has_trait = lifestyle_blademaster`

5. **Eventos Faltantes** (6 errores corregidos)

   - Creado `ac_nickname.2101` - Bloodaxe (Martial + Brave + Berserker)
   - Creado `ac_nickname.2102` - The Terrible (Martial + Dread 80+)
   - Creado `ac_nickname.2103` - Scourge of God (Martial + Dread 60+)
   - Creado `ac_nickname.3101` - The Great (Multi-skill + Prestige 4+)
   - Creado `ac_nickname.3102` - The Magnificent (Diplomacy + Prestige 3+)
   - Creado `ac_nickname.3103` - The Lawgiver (Diplomacy/Learning + Just)

6. **Nicknames Duplicados** (4 warnings corregidos)

   - Eliminados en `ac_nickname_classification_faith.txt`:
     - `nick_hist_the_pilgrim_king` (línea 146)
     - `nick_hist_the_censer` (línea 149)
     - `nick_hist_the_reliquary` (línea 152)
     - `nick_hist_the_shrine` (línea 155)

7. **UTF-8 BOM Encoding** (3 warnings - 2 resueltos, 1 false positive)
   - ✅ `ac_nickname_triggers.txt` - UTF-8 BOM aplicado
   - ✅ `ac_nickname_on_actions.txt` - UTF-8 BOM aplicado
   - ✅ `ac_nickname_events.txt` - UTF-8 BOM aplicado (warning es false positive)

### Added

- `descriptor.mod` - Archivo de metadatos necesario para CK3-Tiger y launcher

### Changed

- `common/scripted_triggers/ac_nickname_triggers.txt` - Reescrito completamente con sintaxis corregida
- `common/on_action/ac_nickname_on_actions.txt` - Recreado con UTF-8 BOM
- `events/ac_nickname_events.txt` - Múltiples correcciones + 6 eventos nuevos
- `common/nicknames/ac_nickname_classification_faith.txt` - Duplicados eliminados

### Technical Notes

- **CK3-Tiger Version:** v1.13.0
- **Game Version:** CK3 v1.17.1 (Tiger built for 1.17.0)
- **Validation Results:**
  - Initial: 117 errors, 25 warnings
  - Final: 0 errors, 1 warning
  - Warning restante: UTF-8 BOM encoding (false positive - BOM está presente como EF BB BF)
- **Archivos Backup Creados:**

  - `ac_nickname_triggers.txt.bak`
  - `ac_nickname_on_actions.txt.bak`
  - `ac_nickname_events.txt.bak`

- **Lecciones Aprendidas:**
  - CK3 usa comparaciones directas de skills (`martial >= 17`) no bloques value
  - Traits usan sistema numérico (`beauty_good_3` no `beautiful`)
  - Religiones requieren prefijo `religion:` y faiths requieren `faith:`
  - Muchos campos de CK2 no existen en CK3 (num_of_secrets, num_of_virtues, etc.)
  - UTF-8 BOM es requerido por CK3 para archivos de scripts

---

## [2025-10-25] - Sistema de Probabilidad Actualizado - 18:00

### Changed

- **Probabilidad aumentada a 20%** (anteriormente 2%)
  - Sistema directo sin capas de probabilidad
  - Aplica a TODOS los personajes (IA y jugadores)
- **Nuevos requisitos para elegibilidad:**
  - Edad 16+ (sin cambios)
  - Al menos un skill en rango calificado (9+)
  - Debe tener al menos un título (landed) o posición en consejo
- **Trigger ac_nickname_blocked actualizado:**
  - Eliminado: `is_ai = no` (ahora jugadores también reciben nicknames)
  - Eliminado: `age < 16` (redundante, ya verificado en on_action)
  - Mantiene: imprisoned, incapable, manual block flag

### Updated Files

- `README.md` - Actualizada descripción de probabilidad
- `README.md` - Eliminada línea "Inspired by: Nicknames+ by [Original Author]"
- `common/on_action/ac_nickname_on_actions.txt` - chance_to_happen = 20, triggers actualizados
- `common/scripted_triggers/ac_nickname_triggers.txt` - ac_nickname_blocked_trigger simplificado

### Technical Notes

- Probabilidad real ahora: **20% por año** para personajes elegibles
- Requisitos más estrictos aseguran que solo personajes relevantes reciban nicknames
- Sistema más balanceado para experiencia del jugador

---

_Última actualización: 25 de octubre de 2025 - 18:00_
