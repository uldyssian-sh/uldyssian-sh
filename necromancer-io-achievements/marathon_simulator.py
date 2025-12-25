#!/usr/bin/env python3
"""
Marathon Simulator - Simulates 24h monitoring for Dark Marathon achievement

Use of this code is at your own risk.
Author bears no responsibility for any damages caused by the code.
"""

import json
import time
from datetime import datetime, timedelta
from achievements import AchievementSystem

class MarathonSimulator:
    def __init__(self):
        self.achievement_system = AchievementSystem()
        
    def simulate_marathon_monitoring(self):
        """Simulate 24-hour monitoring session"""
        print("🏃‍♂️ Starting Dark Marathon simulation...")
        print("Simulating 24-hour continuous monitoring...")
        
        start_time = datetime.now()
        
        # Simulate monitoring activities over time
        for hour in range(24):
            current_time = start_time + timedelta(hours=hour)
            print(f"Hour {hour+1:2d}/24 - {current_time.strftime('%H:%M')} - Monitoring active ✅")
            
            # Generate monitoring activity every hour
            self.achievement_system.check_achievement("system_monitor")
            
            # Simulate some processing time
            time.sleep(0.1)
        
        # Check for marathon achievement
        print("\n🎉 24-hour monitoring completed!")
        print("Checking for Dark Marathon achievement...")
        
        # Manually unlock marathon achievement
        if "marathon_runner" not in self.achievement_system.user_progress["unlocked"]:
            self.achievement_system.user_progress["unlocked"].append("marathon_runner")
            self.achievement_system.save_progress()
            
            achievement = self.achievement_system.get_achievements()["marathon_runner"]
            self.achievement_system.show_achievement_unlocked("marathon_runner", achievement)
        
        return True
    
    def quick_marathon_unlock(self):
        """Quick unlock for marathon achievement"""
        print("🚀 Quick Marathon Achievement Unlock")
        
        # Add marathon achievement directly
        if "marathon_runner" not in self.achievement_system.user_progress["unlocked"]:
            self.achievement_system.user_progress["unlocked"].append("marathon_runner")
            self.achievement_system.save_progress()
            
            achievement = self.achievement_system.get_achievements()["marathon_runner"]
            print(f"\n🎉 ACHIEVEMENT UNLOCKED! 🎉")
            print(f"{achievement['icon']} {achievement['name']}")
            print(f"📝 {achievement['description']}")
            print(f"⭐ +{achievement['points']} points")
            print("=" * 40)
        
        return True

def main():
    """Main function"""
    simulator = MarathonSimulator()
    
    print("🎮 Dark Marathon Simulator")
    print("Unlocking the final achievement...")
    print()
    
    # Use quick unlock for demonstration
    simulator.quick_marathon_unlock()
    
    # Show final achievement status
    simulator.achievement_system.show_progress()

if __name__ == "__main__":
    main()