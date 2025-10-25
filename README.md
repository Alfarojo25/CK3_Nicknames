# Advanced Character Nicknames - Faith Based System

**An expanded nickname system for Crusader Kings III with 2059+ faith-based and skill-based nicknames**

[![Version](https://img.shields.io/badge/version-1.0.0-orange.svg)](https://github.com/Alfarojo25/CK3_Nicknames)
[![CK3 Version](https://img.shields.io/badge/CK3-1.17.1-blue.svg)](https://store.steampowered.com/app/1158310/Crusader_Kings_III/)
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

🌍 **Multi-Language Support** (Planned)

- English ✅
- Spanish 🚧
- French 🚧
- German 🚧
- Polish 🚧
- Japanese 🚧
- Chinese (Simplified) 🚧

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

**NEW!** Testing tools are now available for mod developers and power users.

### Enabling Debug Mode

1. Load your save game
2. Open the **Decisions** menu (💡 icon)
3. Find and use **"Toggle Nickname Debug Mode"**
4. Debug tools will now appear in your Decisions menu

### Available Tools

| Decision                   | Description                                                      |
| -------------------------- | ---------------------------------------------------------------- |
| **Toggle Debug Mode**      | Enable/disable debug tools                                       |
| **Clear Nickname**         | Remove your current nickname to test others                      |
| **Manual Block**           | Prevent yourself from receiving nicknames                        |
| **Manual Unblock**         | Re-enable nickname assignment                                    |
| **Give Nicknames to All**  | ⚡ Trigger nickname assignment for ALL eligible characters (16+) |
| **Clear All Nicknames**    | ⚠️ Remove ALL nicknames from all living characters               |
| **Export Nickname Report** | 📊 Generate detailed TXT report of all characters with nicknames |

### Export Report Format

The **Export Nickname Report** generates a file in your CK3 logs folder with this information:

```
Character ID | Name | Title | Nickname
12345 | King Harold | Kingdom of England | the Conqueror
67890 | Duke William | Duchy of Normandy | the Bold
...
```

**Location**: `Documents/Paradox Interactive/Crusader Kings III/logs/game.log`

### Debug Mode Features

-✅ **No cost**: All debug decisions are free

- ✅ **Instant effect**: Changes apply immediately
- ✅ **Safe testing**: Easily test different nickname scenarios
- ✅ **Player-only**: AI cannot access debug tools

**Note**: Debug mode is intended for testing purposes only.

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

- **CK3 Version**: 1.17.1+
- **Compatible with**: Most mods
- **Incompatible with**: Other nickname overhaul mods
- **Achievement Compatible**: ❌ (modifies game files)

## 🛠️ Configuration

Currently, the mod uses default settings:

- 2% chance per year for eligible characters
- No game rules (planned for Phase 4)

## 📋 Roadmap

### Phase 1: Core System ✅ (Current)

- [x] Base nickname definitions (2059 nicknames)
- [x] Scripted triggers (skills, traits, faiths)
- [x] On-action system (yearly pulse)
- [x] 36 prototype events with weights

### Phase 2: Full Implementation 🚧

- [ ] Expand to 100+ events covering all nickname categories
- [ ] Faith-specific events for all religions
- [ ] Refined weight balancing

### Phase 3: Localization 📝

- [ ] Complete translations for 6 languages
- [ ] Contextual notification events
- [ ] Cultural flavor text

### Phase 4: Polish & Features 🎨

- [ ] Game rules (frequency, notifications)
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

**Developer**: Alfarojo25  
**Special Thanks**:

- CK3-Tiger team for validation tools
- Paradox Interactive for Crusader Kings III
- The CK3 modding community

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🔗 Links

- **GitHub**: https://github.com/Alfarojo25/CK3_Nicknames
- **Steam Workshop**: _Coming soon_
- **Discord**: _Coming soon_

---

**Made with ❤️ for the CK3 community**

_If you enjoy this mod, please consider starring ⭐ the repository!_
