#!/bin/bash

echo "🎮 AI Hunter 3D - Game Jam Edition"
echo "=================================="
echo ""

# Check if Python 3 is available
if command -v python3 &> /dev/null; then
    echo "✅ Python 3 found - Starting local server..."
    python3 run-game.py
elif command -v python &> /dev/null; then
    echo "✅ Python found - Starting local server..."
    python run-game.py
else
    echo "⚠️  Python not found. Trying to open HTML file directly..."
    if command -v open &> /dev/null; then
        open ai-game-3d.html
        echo "✅ Game opened in your default browser"
        echo "💡 If the game doesn't work, install Python and run: python3 run-game.py"
    else
        echo "❌ Could not open the game automatically"
        echo "💡 Please manually open ai-game-3d.html in your web browser"
        echo "💡 Or install Python and run: python3 run-game.py"
    fi
fi