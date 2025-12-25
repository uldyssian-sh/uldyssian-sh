# 🏆 Necromancer-IO Achievement System

Gamifikovaný systém odmeňovania pre necromancer-io projekt, ktorý sleduje pokrok používateľa a odomkýna achievementy za používanie dark automation nástrojov.

## ✨ Funkcie

- **Automatické sledovanie**: Sleduje aktivity vo všetkých necromancer nástrojoch
- **Progresívne odomykanie**: Achievementy sa odomykajú na základe používania
- **Štatistiky**: Detailné štatistiky o používaní nástrojov
- **Bodový systém**: Každý achievement má pridelenú hodnotu bodov
- **Vizuálne notifikácie**: Pekné zobrazenie odomknutých achievementov

## 🎯 Dostupné Achievementy

| Achievement | Popis | Podmienka | Body |
|-------------|-------|-----------|------|
| 🩸 **First Blood** | Prvý bezpečnostný sken | 1 sken | 10 |
| 👁️ **System Overlord** | Majster monitoringu | 10 monitoring sessions | 25 |
| 🧙♂️ **Dark Deployment Master** | Deployment expert | 5 deploymentov | 50 |
| 🛡️ **Guardian of Shadows** | Bezpečnostný expert | 20 skenov | 75 |
| ⚡ **Lord of Automation** | Použitie všetkých nástrojov | Všetky nástroje v jednej session | 100 |
| 🚀 **Performance Necromancer** | Optimalizácia výkonu | 15 optimalizácií | 40 |
| 🌙 **Night Shift Warrior** | Nočný bojovník | Použitie medzi 22:00-06:00 | 30 |
| 🏃♂️ **Dark Marathon** | Dlhodobé monitorovanie | 24h monitoring | 80 |

## 🚀 Použitie

### Automatická integrácia

Achievement systém je automaticky integrovaný do:
- `necromancer-toolkit/necromancer.sh` - Bash nástroje
- `dark-automation/deploy.py` - Python deployment nástroj

### Manuálne sledovanie

```bash
# Zobrazenie achievementov
python3 achievements.py

# Sledovanie konkrétnej akcie
python3 achievements.py --action security_scan

# Zobrazenie len progressu
python3 achievements.py --progress
```

### Programatické použitie

```python
from achievements import AchievementSystem

# Inicializácia
system = AchievementSystem()

# Sledovanie akcie
system.check_achievement("security_scan")

# Zobrazenie progressu
system.show_progress()
```

## 📊 Sledované akcie

- `security_scan` - Bezpečnostné skenovanie
- `system_monitor` - Monitorovanie systému
- `deployment` - Deployment infraštruktúry
- `performance_opt` - Optimalizácia výkonu
- `night_usage` - Používanie v noci
- `combo_usage` - Kombinované používanie nástrojov

## 💾 Úložisko dát

Achievementy a štatistiky sa ukladajú do `achievements.json`:

```json
{
  "unlocked": ["first_scan", "system_master"],
  "stats": {
    "scans": 25,
    "monitoring": 12,
    "deployments": 3,
    "optimizations": 8
  }
}
```

## 🔧 Inštalácia

1. Skopírujte `achievements.py` do root adresára necromancer-io projektu
2. Systém sa automaticky aktivuje pri používaní nástrojov
3. Žiadne dodatočné závislosti nie sú potrebné

## 🎮 Príklady použitia

### Zobrazenie aktuálneho stavu
```bash
cd necromancer-io
python3 achievements.py
```

### Spustenie necromancer nástrojov s achievementmi
```bash
cd necromancer-toolkit
./necromancer.sh
# Vyberte možnosť 4 pre zobrazenie achievementov
```

### Deployment s achievementmi
```bash
cd dark-automation
python3 deploy.py
# Achievementy sa zobrazia na konci
```

## 🏅 Motivačný systém

- **Začiatočník**: 0-50 bodov
- **Pokročilý**: 51-150 bodov  
- **Expert**: 151-300 bodov
- **Majster**: 301+ bodov

## 🔮 Budúce rozšírenia

- [ ] Týždenné výzvy
- [ ] Leaderboard pre tímy
- [ ] Export achievementov
- [ ] Integrácia s GitHub
- [ ] Vlastné achievementy
- [ ] Achievement badges

---

*Vytvorené pre necromancer-io projekt - Dark Arts Automation Toolkit* 🌙