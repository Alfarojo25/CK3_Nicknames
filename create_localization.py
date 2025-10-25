#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script para generar localizaciones completas de nicknames en español e inglés.
Traduce palabra por palabra usando diccionario JSON externo.
"""

import re
import json
from pathlib import Path
from typing import Dict, List, Tuple

def load_translations(json_file: Path) -> Dict[str, str]:
    """
    Carga el diccionario de traducciones desde archivo JSON.
    
    Args:
        json_file: Ruta al archivo JSON con traducciones
    
    Returns:
        Diccionario de traducciones inglés → español
    """
    with open(json_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    # Eliminar comentarios (claves que empiezan con _)
    return {k: v for k, v in data.items() if not k.startswith('_')}

def get_gender_variant(word: str, is_feminine: bool) -> str:
    """
    Obtiene la variante de género correcta de una palabra.
    
    Args:
        word: Palabra con formato "Masculino/Femenino" o palabra sin género
        is_feminine: True si necesita versión femenina
    
    Returns:
        Palabra en el género apropiado
    """
    if "/" in word:
        parts = word.split("/")
        return parts[1] if is_feminine else parts[0]
    return word

def translate_nickname_key(key: str, translations: Dict[str, str]) -> Tuple[str, str]:
    """
    Traduce una clave de nickname al español e inglés.
    
    Args:
        key: Clave del nickname (ej: "nick_the_gentle_giant")
        translations: Diccionario de traducciones
    
    Returns:
        Tupla (traducción_español, traducción_inglés)
    """
    # Determinar si es femenino (ANTES de modificar la clave)
    is_feminine = key.endswith("_f")
    
    # Limpiar la clave
    clean_key = key.replace("nick_", "")
    # Solo remover "_f" si está al FINAL
    if clean_key.endswith("_f"):
        clean_key = clean_key[:-2]  # Remover los últimos 2 caracteres (_f)
    
    # Separar en palabras
    words = clean_key.split("_")
    
    # Traducir cada palabra
    spanish_words = []
    english_words = []
    
    for word in words:
        # Saltar palabras vacías o marcadores internos
        if word in ["hist", ""]:
            continue
            
        # Traducir al español
        if word in translations:
            translation = translations[word]
            if translation:  # Si no está vacío
                spanish_word = get_gender_variant(translation, is_feminine)
                spanish_words.append(spanish_word)
        else:
            # Si no está en el diccionario, capitalizar y dejar en inglés
            spanish_words.append(word.capitalize())
        
        # Inglés (capitalizar todas las palabras excepto artículos y preposiciones)
        if word not in ["the", "of", "a", "an", "and", "for", "in", "on"]:
            english_words.append(word.capitalize())
        elif word == "the":
            # "the" al inicio se capitaliza
            if len(english_words) == 0:
                english_words.append("the")
            else:
                english_words.append(word)
        else:
            english_words.append(word)
    
    # Construir traducciones
    spanish_text = " ".join(spanish_words)
    english_text = " ".join(english_words)
    
    # Agregar artículo español
    article = "la" if is_feminine else "el"
    spanish_final = f"{article} {spanish_text}"
    
    # Capitalizar "the" al inicio en inglés
    if not english_text.startswith("the "):
        english_final = f"the {english_text}"
    else:
        english_final = english_text
    
    return spanish_final, english_final

def extract_all_nicknames(nicknames_dir: Path) -> List[str]:
    """
    Extrae todas las claves de nicknames de los archivos .txt
    
    Args:
        nicknames_dir: Directorio con archivos de nicknames
    
    Returns:
        Lista de claves de nicknames
    """
    nicknames = []
    pattern = re.compile(r'(nick_[a-z_]+)\s*=\s*\{')
    
    for file in nicknames_dir.glob("*.txt"):
        content = file.read_text(encoding="utf-8")
        matches = pattern.findall(content)
        nicknames.extend(matches)
    
    return sorted(set(nicknames))

def generate_localization_file(nicknames: List[str], language: str, output_file: Path, translations: Dict[str, str]):
    """
    Genera archivo de localización YML.
    
    Args:
        nicknames: Lista de claves de nicknames
        language: Código de idioma ("spanish" o "english")
        output_file: Ruta del archivo de salida
        translations: Diccionario de traducciones
    """
    lines = [f"l_{language}:"]
    
    for nickname in nicknames:
        spanish, english = translate_nickname_key(nickname, translations)
        
        if language == "spanish":
            translation = spanish
        else:  # english
            translation = english
        
        lines.append(f' {nickname}:0 "{translation}"')
    
    # Escribir con BOM UTF-8
    content = "\n".join(lines) + "\n"
    output_file.parent.mkdir(parents=True, exist_ok=True)
    output_file.write_bytes(b'\xef\xbb\xbf' + content.encode('utf-8'))
    
    print(f"✓ Generado {output_file.name} con {len(nicknames)} nicknames")

def main():
    """Función principal"""
    # Rutas
    base_dir = Path(__file__).parent
    nicknames_dir = base_dir / "common" / "nicknames"
    loc_dir = base_dir / "localization"
    translations_file = base_dir / "translations_complete.json"
    
    # Cargar diccionario de traducciones
    print("Cargando diccionario de traducciones...")
    translations = load_translations(translations_file)
    print(f"✓ Cargadas {len(translations)} palabras")
    
    # Extraer todos los nicknames
    print("\nExtrayendo nicknames...")
    nicknames = extract_all_nicknames(nicknames_dir)
    print(f"✓ Encontrados {len(nicknames)} nicknames")
    
    # Generar localización en español
    print("\nGenerando localización en español...")
    spanish_file = loc_dir / "spanish" / "ac_nickname_l_spanish.yml"
    generate_localization_file(nicknames, "spanish", spanish_file, translations)
    
    # Generar localización en inglés
    print("\nGenerando localización en inglés...")
    english_file = loc_dir / "english" / "ac_nickname_l_english.yml"
    generate_localization_file(nicknames, "english", english_file, translations)
    
    print("\n✓ Proceso completado exitosamente")
    print(f"Total de nicknames procesados: {len(nicknames)}")

if __name__ == "__main__":
    main()
