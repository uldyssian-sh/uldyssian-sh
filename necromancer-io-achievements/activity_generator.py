#!/usr/bin/env python3
"""
Activity Generator for Achievement System
Generates automated activities to unlock achievements

Use of this code is at your own risk.
Author bears no responsibility for any damages caused by the code.
"""

import json
import time
import random
from datetime import datetime
from achievements import AchievementSystem

class ActivityGenerator:
    def __init__(self):
        self.achievement_system = AchievementSystem()
        
    def generate_security_activities(self, count=5):
        """Generate security scan activities"""
        print(f"🛡️ Generating {count} security activities...")
        for i in range(count):
            self.achievement_system.check_achievement("security_scan")
            print(f"   Security scan {i+1}/{count} completed")
            time.sleep(0.1)
    
    def generate_monitoring_activities(self, count=3):
        """Generate monitoring activities"""
        print(f"👁️ Generating {count} monitoring activities...")
        for i in range(count):
            self.achievement_system.check_achievement("system_monitor")
            print(f"   Monitoring session {i+1}/{count} completed")
            time.sleep(0.1)
    
    def generate_deployment_activities(self, count=2):
        """Generate deployment activities"""
        print(f"🚀 Generating {count} deployment activities...")
        for i in range(count):
            self.achievement_system.check_achievement("deployment")
            print(f"   Deployment {i+1}/{count} completed")
            time.sleep(0.1)
    
    def generate_performance_activities(self, count=5):
        """Generate performance optimization activities"""
        print(f"⚡ Generating {count} performance activities...")
        for i in range(count):
            self.achievement_system.check_achievement("performance_opt")
            print(f"   Performance optimization {i+1}/{count} completed")
            time.sleep(0.1)
    
    def generate_night_activity(self):
        """Generate night usage activity"""
        print("🌙 Generating night activity...")
        self.achievement_system.check_achievement("night_usage")
        print("   Night activity completed")
    
    def generate_combo_activity(self):
        """Generate combo activity for automation lord"""
        print("🎯 Generating combo activity...")
        tools_used = ["security_scanner", "monitor", "deployer", "optimizer"]
        self.achievement_system.check_achievement("combo_usage", tools_used=tools_used)
        print("   Combo activity completed")
    
    def run_full_activity_cycle(self):
        """Run complete activity cycle for maximum achievements"""
        print("🚀 Starting full activity cycle...")
        print("=" * 50)
        
        # Generate various activities
        self.generate_security_activities(10)
        self.generate_monitoring_activities(5)
        self.generate_deployment_activities(3)
        self.generate_performance_activities(8)
        self.generate_night_activity()
        self.generate_combo_activity()
        
        print("=" * 50)
        print("✅ Full activity cycle completed!")
        
        # Show final progress
        self.achievement_system.show_progress()

def main():
    """Main function"""
    generator = ActivityGenerator()
    
    print("🎮 Necromancer Activity Generator")
    print("Generating activities for achievement unlocking...")
    print()
    
    generator.run_full_activity_cycle()

if __name__ == "__main__":
    main()