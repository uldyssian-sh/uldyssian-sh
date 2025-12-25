#!/usr/bin/env python3
"""
Night Warrior - Unlocks Night Shift Warrior achievement

Use of this code is at your own risk.
Author bears no responsibility for any damages caused by the code.
"""

import json
from datetime import datetime
from achievements import AchievementSystem

class NightWarrior:
    def __init__(self):
        self.achievement_system = AchievementSystem()
        
    def unlock_night_warrior(self):
        """Unlock Night Shift Warrior achievement"""
        print("🌙 Night Shift Warrior Activation")
        print("Simulating night-time usage (22:00-06:00)...")
        
        # Manually unlock night warrior achievement
        if "night_warrior" not in self.achievement_system.user_progress["unlocked"]:
            self.achievement_system.user_progress["unlocked"].append("night_warrior")
            self.achievement_system.save_progress()
            
            achievement = self.achievement_system.get_achievements()["night_warrior"]
            print(f"\n🎉 ACHIEVEMENT UNLOCKED! 🎉")
            print(f"{achievement['icon']} {achievement['name']}")
            print(f"📝 {achievement['description']}")
            print(f"⭐ +{achievement['points']} points")
            print("=" * 40)
        
        return True

def main():
    """Main function"""
    warrior = NightWarrior()
    
    print("🎮 Night Shift Warrior Unlock")
    print("Activating final achievement...")
    print()
    
    warrior.unlock_night_warrior()
    
    # Show final achievement status
    warrior.achievement_system.show_progress()
    
    print("\n🎊 CONGRATULATIONS! 🎊")
    print("ALL ACHIEVEMENTS UNLOCKED!")
    print("You are now a true Necromancer Master! 🧙‍♂️")

if __name__ == "__main__":
    main()