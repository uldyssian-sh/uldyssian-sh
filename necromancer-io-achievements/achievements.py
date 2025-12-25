#!/usr/bin/env python3
"""
Necromancer-IO Achievement System
Tracks and rewards user progress across dark automation tools
"""

import json
import os
import sys
from datetime import datetime
from pathlib import Path

class AchievementSystem:
    def __init__(self):
        self.achievements_file = Path("achievements.json")
        self.user_progress = self.load_progress()
        
    def load_progress(self):
        """Load user achievement progress"""
        if self.achievements_file.exists():
            with open(self.achievements_file, 'r') as f:
                return json.load(f)
        return {"unlocked": [], "stats": {}}
    
    def save_progress(self):
        """Save achievement progress"""
        with open(self.achievements_file, 'w') as f:
            json.dump(self.user_progress, f, indent=2)
    
    def get_achievements(self):
        """Define all available achievements"""
        return {
            "first_scan": {
                "name": "First Blood",
                "description": "Run your first security scan",
                "icon": "🩸",
                "points": 10
            },
            "system_master": {
                "name": "System Overlord",
                "description": "Complete 10 system monitoring sessions",
                "icon": "👁️",
                "points": 25
            },
            "deployment_wizard": {
                "name": "Dark Deployment Master",
                "description": "Successfully deploy 5 infrastructure setups",
                "icon": "🧙‍♂️",
                "points": 50
            },
            "security_expert": {
                "name": "Guardian of Shadows",
                "description": "Pass 20 security assessments",
                "icon": "🛡️",
                "points": 75
            },
            "automation_lord": {
                "name": "Lord of Automation",
                "description": "Use all necromancer tools in one session",
                "icon": "⚡",
                "points": 100
            },
            "performance_guru": {
                "name": "Performance Necromancer",
                "description": "Optimize system performance 15 times",
                "icon": "🚀",
                "points": 40
            },
            "night_warrior": {
                "name": "Night Shift Warrior",
                "description": "Run tools between 22:00-06:00",
                "icon": "🌙",
                "points": 30
            },
            "marathon_runner": {
                "name": "Dark Marathon",
                "description": "Keep monitoring active for 24 hours",
                "icon": "🏃‍♂️",
                "points": 80
            }
        }
    
    def check_achievement(self, action, **kwargs):
        """Check if action triggers an achievement"""
        achievements = self.get_achievements()
        unlocked = []
        
        # Initialize stats if not exists
        if "stats" not in self.user_progress:
            self.user_progress["stats"] = {}
        
        stats = self.user_progress["stats"]
        
        # Update stats based on action
        if action == "security_scan":
            stats["scans"] = stats.get("scans", 0) + 1
            if "first_scan" not in self.user_progress["unlocked"] and stats["scans"] >= 1:
                unlocked.append("first_scan")
            if "security_expert" not in self.user_progress["unlocked"] and stats["scans"] >= 20:
                unlocked.append("security_expert")
                
        elif action == "system_monitor":
            stats["monitoring"] = stats.get("monitoring", 0) + 1
            if "system_master" not in self.user_progress["unlocked"] and stats["monitoring"] >= 10:
                unlocked.append("system_master")
                
        elif action == "deployment":
            stats["deployments"] = stats.get("deployments", 0) + 1
            if "deployment_wizard" not in self.user_progress["unlocked"] and stats["deployments"] >= 5:
                unlocked.append("deployment_wizard")
                
        elif action == "performance_opt":
            stats["optimizations"] = stats.get("optimizations", 0) + 1
            if "performance_guru" not in self.user_progress["unlocked"] and stats["optimizations"] >= 15:
                unlocked.append("performance_guru")
                
        elif action == "night_usage":
            current_hour = datetime.now().hour
            if (current_hour >= 22 or current_hour <= 6) and "night_warrior" not in self.user_progress["unlocked"]:
                unlocked.append("night_warrior")
        
        # Check for combo achievements
        tools_used = kwargs.get("tools_used", [])
        if len(tools_used) >= 3 and "automation_lord" not in self.user_progress["unlocked"]:
            unlocked.append("automation_lord")
        
        # Add newly unlocked achievements
        for achievement_id in unlocked:
            if achievement_id not in self.user_progress["unlocked"]:
                self.user_progress["unlocked"].append(achievement_id)
                self.show_achievement_unlocked(achievement_id, achievements[achievement_id])
        
        self.save_progress()
        return unlocked
    
    def show_achievement_unlocked(self, achievement_id, achievement):
        """Display achievement unlock notification"""
        print(f"\n🎉 ACHIEVEMENT UNLOCKED! 🎉")
        print(f"{achievement['icon']} {achievement['name']}")
        print(f"📝 {achievement['description']}")
        print(f"⭐ +{achievement['points']} points")
        print("=" * 40)
    
    def show_progress(self):
        """Display current achievement progress"""
        achievements = self.get_achievements()
        unlocked = self.user_progress.get("unlocked", [])
        stats = self.user_progress.get("stats", {})
        
        print("\n🏆 NECROMANCER ACHIEVEMENTS 🏆")
        print("=" * 50)
        
        total_points = 0
        for achievement_id, achievement in achievements.items():
            status = "✅" if achievement_id in unlocked else "🔒"
            print(f"{status} {achievement['icon']} {achievement['name']}")
            print(f"   {achievement['description']}")
            if achievement_id in unlocked:
                total_points += achievement['points']
            print()
        
        print(f"📊 STATISTICS:")
        print(f"   Security Scans: {stats.get('scans', 0)}")
        print(f"   Monitoring Sessions: {stats.get('monitoring', 0)}")
        print(f"   Deployments: {stats.get('deployments', 0)}")
        print(f"   Optimizations: {stats.get('optimizations', 0)}")
        print(f"\n⭐ Total Points: {total_points}")
        print(f"🏅 Achievements Unlocked: {len(unlocked)}/{len(achievements)}")
    
    def get_next_achievements(self):
        """Show progress toward next achievements"""
        achievements = self.get_achievements()
        unlocked = self.user_progress.get("unlocked", [])
        stats = self.user_progress.get("stats", {})
        
        print("\n🎯 NEXT ACHIEVEMENTS:")
        print("=" * 30)
        
        # Show progress for locked achievements
        if "system_master" not in unlocked:
            current = stats.get('monitoring', 0)
            print(f"👁️ System Overlord: {current}/10 monitoring sessions")
        
        if "security_expert" not in unlocked:
            current = stats.get('scans', 0)
            print(f"🛡️ Guardian of Shadows: {current}/20 security scans")
        
        if "deployment_wizard" not in unlocked:
            current = stats.get('deployments', 0)
            print(f"🧙‍♂️ Dark Deployment Master: {current}/5 deployments")
        
        if "performance_guru" not in unlocked:
            current = stats.get('optimizations', 0)
            print(f"🚀 Performance Necromancer: {current}/15 optimizations")

def main():
    """CLI interface for achievement system"""
    import argparse
    
    parser = argparse.ArgumentParser(description='Necromancer Achievement System')
    parser.add_argument('--action', help='Track achievement action')
    parser.add_argument('--show', action='store_true', help='Show achievements')
    parser.add_argument('--progress', action='store_true', help='Show progress')
    
    args = parser.parse_args()
    
    system = AchievementSystem()
    
    if args.action:
        system.check_achievement(args.action)
    elif args.show or args.progress or len(sys.argv) == 1:
        system.show_progress()
        system.get_next_achievements()
    else:
        # Demo mode
        print("🌟 Necromancer-IO Achievement System Demo")
        print("=" * 45)
        
        # Simulate some actions
        system.check_achievement("security_scan")
        system.check_achievement("system_monitor")
        system.check_achievement("deployment")
        system.check_achievement("night_usage")
        
        # Show current progress
        system.show_progress()
        system.get_next_achievements()

if __name__ == "__main__":
    main()