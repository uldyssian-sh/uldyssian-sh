#!/bin/bash
# Achievement System Cleanup Script
# Removes temporary files and organizes achievement system

echo "🧹 Cleaning up achievement system..."

# Remove Python cache files
find . -name "__pycache__" -type d -exec rm -rf {} + 2>/dev/null || true
find . -name "*.pyc" -delete 2>/dev/null || true

# Remove system files
find . -name ".DS_Store" -delete 2>/dev/null || true

# Clean achievement logs
if [ -f "necromancer-io-achievements/achievements.json" ]; then
    echo "📊 Achievement data preserved"
else
    echo "⚠️ Achievement data not found"
fi

echo "✅ Cleanup completed!"
echo "🏆 Achievement system ready for use"