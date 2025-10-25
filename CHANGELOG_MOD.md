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

## [Pendiente] - Git Repository Setup

### To Do

- [ ] `git init` en directorio del mod
- [ ] `git remote add origin https://github.com/Alfarojo25/CK3_Nicknames.git`
- [ ] Primer commit: "Initial structure + existing nicknames"
- [ ] `git push -u origin master`

---

_Última actualización: 25 de octubre de 2025 - 14:00_
