# Advanced Character Nicknames - Faith Based System

**An expanded nickname system for Crusader Kings III with 2059+ faith-based and skill-based nicknames**

[![Version](https://img.shields.io/badge/version-2.0.0-orange.svg)](https://github.com/Alfarojo25/CK3_Nicknames)
[![CK3 Version](https://img.shields.io/badge/CK3-1.18.0.1-blue.svg)](https://store.steampowered.com/app/1158310/Crusader_Kings_III/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

## 📖 Description

**Advanced Character Nicknames** is a comprehensive overhaul of the nickname system in Crusader Kings III, featuring over **2059 unique nicknames** that characters can earn based on their traits, skills, faith, and achievements. This mod emphasizes faith-based and cultural diversity while maintaining historical authenticity.

### Features

✨ **2059+ Unique Nicknames**

- 136 faith-specific nicknames (Christian, Muslim, Norse, Hindu, Buddhist, Zoroastrian, etc.)
- 1923 generic nicknames (warriors, scholars, beauty, disabilities, achievements, etc.)
- Faith-based system that respects religious and cultural context

⚖️ **Intelligent Assignment System**

- Weight-based probability system for balanced distribution
- Skill-based nicknames (Diplomacy, Martial, Stewardship, Intrigue, Learning)
- Trait-based nicknames (Physical, Congenital, Personality)
- Faith-based nicknames (unique to each religion family)
- Age-gated: 16+ for all nickname types

🎲 **Dynamic & Balanced**

- 20% chance per year for eligible characters (AI and players)
- Requires: Age 16+, at least one qualifying skill range, and a title
- Weight multipliers ensure appropriate distribution
- Respects character context and history

🌍 **Multi-Language Support**

- English ✅
- Spanish ✅
- Chinese (Simplified) ✅
- Japanese ✅ **NEW in v1.18.0.1**
- Korean ✅ **NEW in v1.18.0.1**

All 2,055 nicknames have been manually translated to ensure cultural appropriateness and contextual accuracy in each language.

## 📥 Installation

### Steam Workshop (Recommended)

_Coming soon_

### Manual Installation

1. Download the latest release from [Releases](https://github.com/Alfarojo25/CK3_Nicknames/releases)
2. Extract the folder to your CK3 mod directory:
   - **Windows**: `C:\Users\[YourUsername]\Documents\Paradox Interactive\Crusader Kings III\mod\`
   - **macOS**: `~/Documents/Paradox Interactive/Crusader Kings III/mod/`
   - **Linux**: `~/.local/share/Paradox Interactive/Crusader Kings III/mod/`
3. Launch CK3 and enable the mod in the Launcher

## 🛠️ Debug Mode

**⚠️ NOTA IMPORTANTE:** Las decisiones de debug están implementadas pero **los eventos asociados aún no funcionan completamente**. Actualmente solo funciona la activación/desactivación del modo debug. Las demás funcionalidades se completarán en futuras actualizaciones.

### Enabling Debug Mode

1. Load your save game
2. Open the **Decisions** menu (💡 icon)
3. Find and use **"Toggle Nickname Debug Mode"**
4. Debug tools will now appear in your Decisions menu (pero los eventos no están implementados aún)

### Available Tools (En Desarrollo)

| Decision                   | Estado | Description                                                      |
| -------------------------- | ------ | ---------------------------------------------------------------- |
| **Toggle Debug Mode**      | ✅     | Enable/disable debug tools                                       |
| **Clear Nickname**         | 🚧     | Remove your current nickname to test others                      |
| **Manual Block**           | 🚧     | Prevent yourself from receiving nicknames                        |
| **Manual Unblock**         | 🚧     | Re-enable nickname assignment                                    |
| **Give Nicknames to All**  | 🚧     | ⚡ Trigger nickname assignment for ALL eligible characters (16+) |
| **Clear All Nicknames**    | 🚧     | ⚠️ Remove ALL nicknames from all living characters               |
| **Export Nickname Report** | 🚧     | 📊 Generate detailed TXT report of all characters with nicknames |

**Note**: Debug mode is intended for testing purposes only and is currently under development.

## 🎮 How It Works

### Nickname Categories

**Physical/Congenital Traits** (Age 16+)

- Size: "the Giant", "the Dwarf"
- Beauty: "the Fair", "the Ugly"
- Strength: "the Strong", "the Weak"
- Intelligence: "the Wise", "the Simple"
- Disabilities: "the One-Eyed", "the Scarred"

**Skill-Based** (Age 20+)

- **Martial** (17+): "the Conqueror", "the Invincible", "the Hammer"
- **Diplomacy** (17+): "the Just", "the Peacemaker", "the Silver Tongue"
- **Stewardship** (17+): "the Builder", "the Rich", "the Merchant"
- **Intrigue** (17+): "the Shadow", "the Spider", "the Knife"
- **Learning** (17+): "the Scholar", "the Philosopher", "the Wise"

**Faith-Specific** (Age 20+)

- **Christian**: "the Saint", "the Crusader", "the Pilgrim"
- **Norse Pagan**: "Son of Thor", "Daughter of Freya"
- **Muslim**: "the Martyr", "the Faithful"
- **Buddhist**: "the Enlightened", "the Ascetic"
- **Zoroastrian**: "Fire-touched", "the Flame"

### Skill Ranges

| Skill Level | Nickname Type      | Examples                     |
| ----------- | ------------------ | ---------------------------- |
| 0-8         | None               | Too mediocre                 |
| 9-11        | Bad/Incompetent    | "the Weak", "the Simple"     |
| 12-16       | Competent          | "the Wise", "the Builder"    |
| 17+         | Glorious/Legendary | "the Conqueror", "the Great" |

## ⚙️ Compatibility

- **CK3 Version**: 1.18.0+ (Fully compatible with latest version)
- **DLC Compatibility**:
  - ✅ Compatible with ALL DLCs (Roads to Power, Royal Court, All Under Heaven, etc.)
  - ✅ Works with new v1.18.0 features (Diarchies, Confederations, House Aspirations)
  - ✅ No DLC required - works with base game
- **Mod Compatibility**:
  - ✅ Compatible with most mods (100% additive, no vanilla overwrites)
  - ❌ Incompatible with other nickname overhaul mods
- **Achievement Compatible**: ❌ (modifies game files)

### Version 1.18.0 Features Support

This mod is fully compatible with CK3 v1.18.0 and its new features:

- **Diarchies**: Apodos work normally for both rulers and diarchs
- **Confederations**: Characters in confederations can receive nicknames
- **House Aspirations**: Nickname system respects house goals and traits
- **Great Projects**: No conflicts with monument construction
- **Landless Adventurers**: Adventurers can earn nicknames based on their deeds

## 🛠️ Configuration

Currently, the mod uses default settings:

- 2% chance per year for eligible characters
- No game rules (planned for Phase 4)

## 📋 Roadmap

### Phase 1: Core System ✅ COMPLETE

- [x] Base nickname definitions (2059 nicknames)
- [x] Scripted triggers (skills, traits, faiths)
- [x] On-action system (yearly pulse)
- [x] 36 prototype events with weights

### Phase 2: Full Implementation ✅ COMPLETE

- [x] Expand to 100+ events covering all nickname categories
- [x] Faith-specific events for all religions
- [x] Refined weight balancing

### Phase 3: Localization ✅ COMPLETE

- [x] Complete translations for 5 languages (English, Spanish, Chinese, Japanese, Korean)
- [x] All 2,055 nicknames fully translated
- [x] UI elements and game rules translated
- [x] Contextual notification events
- [x] Cultural flavor text

### Phase 4: Polish & Features 🚧 IN PROGRESS

- [x] Game rules (frequency, notifications)
- [x] Debug tools (partially implemented)
- [ ] Compatibility patches
- [ ] Steam Workshop release

### Phase 5: Future Enhancements 🔮

- [ ] More language support (French, German, Russian)
- [ ] Additional nickname categories
- [ ] Dynasty-specific nicknames
- [ ] Historical character nickname assignments
- [ ] Debug tools
- [ ] Compatibility patches
- [ ] Steam Workshop release

## 🐛 Bug Reports

Found a bug? Please report it on [GitHub Issues](https://github.com/Alfarojo25/CK3_Nicknames/issues) with:

- Your game version
- Steps to reproduce
- Screenshots if applicable
- `error.log` file from your CK3 directory

## 🤝 Contributing

Contributions are welcome! Please:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📜 Credits

**Developer**: Alfarojo  
**GitHub**: https://github.com/Alfarojo25  
**Steam**: [Alfarojo](https://steamcommunity.com/profiles/76561198085829278/) (ID: 76561198085829278)  
**Discord**: alfarojo / Latamsquad - IFT (Clan)

**Special Thanks**:

- CK3-Tiger team for validation tools
- Paradox Interactive for Crusader Kings III
- The CK3 modding community

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🔗 Links

- **GitHub Repository**: https://github.com/Alfarojo25/CK3_Nicknames
- **Steam Profile**: https://steamcommunity.com/profiles/76561198085829278/
- **Steam Workshop**: _Coming soon_

---

**Made with ❤️ for the CK3 community**

_If you enjoy this mod, please consider starring ⭐ the repository!_
