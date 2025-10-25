# Faith Reference - CK3 v1.17.1

Este documento lista TODAS las fes (faiths) de Crusader Kings III versión 1.17.1, organizadas por familia religiosa.

## Estructura del Sistema

El mod clasifica las fes en 4 categorías principales basadas en la estructura vanilla:

1. **rf_abrahamic** - Religiones abrahámicas
2. **rf_eastern** - Religiones orientales (dhármicas)
3. **rf_pagan** - Religiones paganas
4. **singles** - Religiones únicas sin familia

---

## 1. RF_ABRAHAMIC - Religiones Abrahámicas

### Christianity (religion_christianity_church)

**Denominaciones principales:**

- `catholic` - Catolicismo Romano
- `orthodox` - Iglesia Ortodoxa Oriental
- `coptic` - Cristianismo Copto
- `armenian_apostolic` - Iglesia Apostólica Armenia
- `nestorian` - Nestorianismo
- `insular_celtic` - Cristianismo Celta Insular

**Herejías y variantes:**

- `iconoclast` - Iconoclasta
- `paulician` - Paulicianismo
- `bogomilist` - Bogomilismo
- `messalian` - Mesalianismo
- `adoptionist` - Adopcionismo
- `cathar` - Catarismo
- `waldensian` - Valdensianismo
- `lollard` - Lolardismo
- `hussite` - Hussitismo

### Islam (religion_islam)

**Ramas principales:**

- `sunni` - Islam Sunní
- `shiite` - Islam Chiíta
- `muhakkima` - Muhakkima (Jarijismo)
- `muwalladi` - Muwalladí

**Sectas:**

- `ashari` - Asharismo
- `maturidi` - Maturidismo
- `mutazila` - Mutazilismo
- `zayidi` - Zaidismo
- `ismaili` - Ismailismo (Chiíta Ismaelita)
- `druze` - Druzos
- `qarmatian` - Qarmatismo

### Judaism (religion_judaism)

- `rabbinism` - Judaísmo Rabínico
- `kabarism` - Kabarismo (Judaísmo Jázaro)
- `karaism` - Caraísmo
- `samaritan` - Samaritanismo

---

## 2. RF_EASTERN - Religiones Orientales

### Indian Religions (religion_hinduism)

**Hinduismo:**

- `hinduism` - Hinduismo general
- `advaita` - Advaita Vedanta
- `vaishnavism` - Vaisnavismo
- `shaivism` - Shivaísmo
- `smartism` - Smartismo
- `kalikula` - Kalikula
- `kapalika` - Kapalika

### Buddhism (religion_buddhism)

- `theravada` - Budismo Theravada
- `mahayana` - Budismo Mahayana
- `vajrayana` - Budismo Vajrayana (Tibetano)
- `ari_buddhism` - Budismo Ari (Myanmar)

### Other Eastern

- `jainism` - Jainismo
  - `digambara` - Digambara
  - `svetambara` - Svetambara

---

## 3. RF_PAGAN - Religiones Paganas

### Germanic/Norse (religion_germanic)

- `norse_pagan` - Paganismo Nórdico (Asatru)

### Slavic (religion_slavic_pagan)

- `slovianska_pravda` - Paganismo Eslavo
- `west_slavic` - Eslavo Occidental

### Baltic (religion_baltic_pagan)

- `baltic_pagan` - Paganismo Báltico

### Finno-Ugric (religion_finno_ugric)

- `finnish_pagan` - Paganismo Finlandés
- `sami_pagan` - Paganismo Sami
- `komi_pagan` - Paganismo Komi
- `mari_pagan` - Paganismo Mari
- `mordvin_pagan` - Paganismo Mordvino

### West African (religion_west_african_pagan)

- `bori` - Bori
- `west_african_pagan` - Paganismo Africano Occidental genérico

### Berber/North African (religion_berber_pagan)

- `kushitism` - Cushitismo

### Others Pagan

- `tengri_pagan` - Tengrismo
- `bon` - Bön (Tibet)
- `zunism` - Zunismo
- `hellenic_pagan` - Paganismo Helénico
- `egyptian_pagan` - Paganismo Egipcio
- `atenism` - Atenismo
- `canaanite_pagan` - Paganismo Cananeo
- `chaldean_pagan` - Paganismo Caldeo
- `atenism_pagan` - Atenismo (duplicado?)

---

## 4. SINGLES - Religiones sin Familia

### Ancient/Dualist

- `zoroastrianism` - Zoroastrismo

  - `mazdayasna` - Mazdayasna (Zoroastrismo Ortodoxo)
  - `zurvanism` - Zurvanismo
  - `khurmazta` - Khurramitas
  - `gayomartian` - Gayomartianismo

- `manichaeism` - Maniqueísmo

### Syncretic/Other

- `taoism` - Taoísmo
- `priscillianism` - Priscilianismo
- `dualism` - Dualismo (genérico)

---

## Nicknames Específicos por Fe

### Fes con Nicknames Religiosos Exclusivos:

**Christianity:**

- Catholic: `nick_hist_the_saint`, `nick_hist_the_crusader`, `nick_hist_the_templar`, `nick_hist_the_hospitaller`
- Orthodox: `nick_hist_the_iconoclast`, `nick_hist_the_catholic` (irónico)
- Coptic: nicknames de santos coptos
- Insular Celtic: `nick_hist_the_pilgrim_king`

**Norse Pagan:**

- `nick_son_of_thor`, `nick_son_of_odin`, `nick_son_of_balder`, `nick_son_of_loki`
- `nick_daughter_freya`, `nick_daughter_frigg`

**Islam:**

- `nick_hist_the_martyr`, `nick_hist_the_jihadist` (posible)

**Zoroastrianism:**

- Nicknames relacionados con fuego sagrado

**Judaism:**

- Nicknames relacionados con la Torá

### Fes sin Nicknames Específicos:

La mayoría de fes paganas y orientales NO tienen nicknames específicos en el archivo `ac_nickname_classification_faith.txt`. Usarán el pool genérico.

---

## Mapping: Fe → Familia Religiosa

```python
FAITH_TO_FAMILY = {
    # Abrahamic
    "catholic": "rf_abrahamic",
    "orthodox": "rf_abrahamic",
    "coptic": "rf_abrahamic",
    # ... (total ~30 fes)

    # Eastern
    "hinduism": "rf_eastern",
    "theravada": "rf_eastern",
    # ... (total ~15 fes)

    # Pagan
    "norse_pagan": "rf_pagan",
    "finnish_pagan": "rf_pagan",
    # ... (total ~20 fes)

    # Singles
    "zoroastrianism": "singles",
    "manichaeism": "singles",
    # ... (total ~8 fes)
}
```

**Total de Fes en CK3 v1.17.1:** ~70-80 fes

---

## Notas de Implementación

### Para scripted_effects:

1. **ac_nickname_effects_abrahamic.txt**

   - Triggers para Christianity (todos los flavors)
   - Triggers para Islam (todos los madhhabs)
   - Triggers para Judaism

2. **ac_nickname_effects_eastern.txt**

   - Triggers para Hinduism (todos los sampradayas)
   - Triggers para Buddhism (todos los schools)
   - Triggers para Jainism

3. **ac_nickname_effects_pagan.txt**

   - Triggers para Germanic/Norse
   - Triggers para Slavic
   - Triggers para Baltic
   - Triggers para Finno-Ugric
   - Triggers para African

4. **ac_nickname_effects_singles.txt**
   - Triggers para Zoroastrianism (todos los variants)
   - Triggers para Manichaeism
   - Triggers para Taoism
   - Triggers para Dualism

### Ejemplo de Trigger:

```ck3
ac_is_abrahamic_faith_trigger = {
    OR = {
        religion = religion_christianity_church
        religion = religion_islam
        religion = religion_judaism
    }
}

ac_is_catholic_trigger = {
    faith = catholic
}

ac_is_christian_trigger = {
    religion = religion_christianity_church
}
```

---

_Documento creado: 25 de octubre de 2025_
_Última actualización: Fase 1 - Setup inicial_
