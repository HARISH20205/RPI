# will update within tmrw morning
# also tried onnx, will explore later
# for tomorrow's demo, just gonna use ollama,
# dont chnage any code for now, if you want to please do it as a pull request, dont commit directly

#!/bin/bash

read -p "Enter the prompt: " PROMPT

start_time=$(date +%s.%3N)
echo "Start time: $start_time"

python3 main.py "$PROMPT"

COMPLEXITY=$(grep -o '"complexity": *"[^"]*"' data/test.txt | sed 's/"complexity": "//; s/"$//')
# PROMPT=$(grep -o '"prompt": *"[^"]*"' data/test.txt | sed 's/"prompt": "//; s/"$//')

echo "Complexity: $COMPLEXITY"
echo "Prompt: $PROMPT"

# python prompt.py $PROMPT

case "$COMPLEXITY" in
    "Low")
        echo start="$(date +%s)"
        echo "Running low complexity model..."
        ollama run tinyllama "$PROMPT"
        echo end="$(date +%s)"
        ;;
    "Mid")
        echo "Running medium complexity model..."
        ollama run tinydolphin "$PROMPT"
        ;;
    "High")
        echo "Running high complexity model..."
        ollama run gemma2:2b "$PROMPT"
        ;;
    *)
        echo "Unkown complexity level: $COMPLEXITY"
        echo "Running on highly inefficient model..."
        ollama run phi "$PROMPT"
        ;;
esac

end_time=$(date +%s.%3N)
echo "End time: $end_time"
time_diff_ms=$(bc -l <<< "scale=0; ($end_time - $start_time) * 1000")
echo "Time taken: $time_diff_ms ms"
echo "Done!!"
# now the remaining process is to capture and store it in the vector db or direct storage

