#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script para corregir el orden de los apodos compuestos en español.
En español, el adjetivo generalmente va DESPUÉS del sustantivo.
"""

import re

# Archivo a corregir
file_path = r'localization\spanish\ac_nickname_l_spanish.yml'

# Diccionario de correcciones: clave_apodo -> traducción_correcta
corrections = {
    # Casos donde sustantivo + adjetivo está al revés
    'nick_hist_bulgar_slayer': 'el Asesino de Búlgaros',
    'nick_hist_bulgar_slayer_f': 'la Asesina de Búlgaros',
    'nick_hist_stupor_mundi': 'el Estupor del Mundo',
    'nick_hist_stupor_mundi_f': 'la Estupor del Mundo',
    'nick_hist_snake_in_the_eye': 'la Serpiente en el Ojo',
    'nick_hist_snake_in_the_eye_f': 'la Serpiente en el Ojo',
    'nick_hist_the_soldier_king': 'el Rey Soldado',
    
    # Otros que suenan mal y necesitan artículos o preposiciones
    'nick_hist_scourge_of_god_f': 'el Azote de Dios',  # "Diosa" está mal, siempre es "Azote de Dios"
}

print("Corrigiendo orden de apodos en español...")
print("=" * 60)

# Leer el archivo
with open(file_path, 'r', encoding='utf-8-sig') as f:
    content = f.read()

# Aplicar correcciones
changes_made = 0
for key, correct_translation in corrections.items():
    # Buscar patrón: key:0 "traducción_actual"
    pattern = rf'({key}:0 ")[^"]+(")'
    replacement = rf'\1{correct_translation}\2'
    
    new_content, count = re.subn(pattern, replacement, content)
    if count > 0:
        print(f"✓ {key}: '{correct_translation}'")
        content = new_content
        changes_made += count

print("=" * 60)

# Guardar cambios
if changes_made > 0:
    with open(file_path, 'w', encoding='utf-8-sig') as f:
        f.write(content)
    print(f"✓ {changes_made} correcciones aplicadas exitosamente")
else:
    print("⚠ No se encontraron cambios para aplicar")

print("\n" + "=" * 60)
print("REVISIÓN MANUAL RECOMENDADA:")
print("=" * 60)
print("""
Los siguientes apodos pueden necesitar revisión manual:

1. nick_hist_bluetooth: "el Diente Azul"
   → Sugerencia: "el de Diente Azul" o mantener "Bluetooth" sin traducir

2. nick_hist_hairy_breeches: "el Peludo Calzones"
   → Sugerencia: "el de los Calzones Peludos"

3. nick_hist_longshanks: "el Zancas Largas"
   → Sugerencia: "el Zanquilargo" o "el de las Piernas Largas"

4. nick_hist_curtmantle: "el Manto Corto"
   → Sugerencia: "el Cortomanto" o "el de Manto Corto"

5. nick_hist_ironside: "el Costado de Hierro"
   → Sugerencia: "el de Costado de Hierro"

Verifica estos en el juego para decidir si suenan naturales.
""")
