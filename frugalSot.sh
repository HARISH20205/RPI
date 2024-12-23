# #!/bin/bash
# filename=data/output.txt
# # read -p "Enter file name: " $filename
# # data=$(<"$filename")
# # echo "$data"
# data1=$(<"$filename")
# PROMPT=$(grep -o '"prompt": *"[^"]*"' data/test.txt | sed 's/"prompt": "//; s/"$//')

# echo "Prompt: $PROMPT"
# echo "Data: $data1"

# similarity_score=$(python3 textSimilarity.py "$data1" "$PROMPT")

# echo "Similarity score: $similarity_score"

# this is where the final execution is gonna happen, so copying the file form main.sh and using it here and keeping that as a backup

#!/bin/bash

read -p "Enter the prompt: " PROMPT

start_time=$(date +%s.%3N)
echo "Start time: $start_time"

python main.py "$PROMPT"

COMPLEXITY=$(grep -o '"complexity": *"[^"]*"' data/test.txt | sed 's/"complexity": "//; s/"$//')

echo "Complexity: $COMPLEXITY"
echo "Prompt: $PROMPT"

run_model(){
    local $PROMPT = "$1"
    local COMPLEXITY = "${2:-Low}"

    case "$COMPLEXITY" in
        "Low")
            echo "Running low complexity model (tinyllama)..."
            ollama run tinyllama "$PROMPT" | tee data/output.txt
            ;;
        "Mid")
            echo "Running medium complexity model (tinydolphin)..."
            ollama run tinydolphin "$PROMPT" | tee data/output.txt
            ;;
        "High")
            echo "Running high complexity model (gemma2 2b)..."
            ollama run gemma2:2b "$PROMPT" | tee data/output.txt
            ;;
        *)
            echo "Unknown complexity level: $COMPLEXITY"
            echo "Running on highly inefficient model (phi-2.7b)..."
            ollama run phi "$PROMPT" | tee data/output.txt
            ;;
    esac
}
# case "$COMPLEXITY" in
#     "Low")
#         echo "Running low complexity model..."
#         ollama run tinyllama "$PROMPT" | tee data/output.txt
#         ;;
#     "Mid")
#         echo "Running medium complexity model..."
#         ollama run tinydolphin "$PROMPT" | tee data/output.txt
#         ;;
#     "High")
#         echo "Running high complexity model..."
#         ollama run gemma2:2b "$PROMPT" | tee data/output.txt
#         ;;
#     *)
#         echo "Unknown complexity level: $COMPLEXITY"
#         echo "Running on highly inefficient model..."
#         ollama run phi "$PROMPT" | tee data/output.txt
#         ;;
# esac

check_relevance() {
    while true; do
        python textSimilarity.py
        RELEVANT=$(grep -o '"relevant": *"[^"]*"' data/test.txt | sed 's/"relevant": "//; s/"$//')

        if [[ "$RELEVANT" == "true" ]]; then
            echo "The response generated is relevant."
            break
        else
            echo "The response generated is irrelevant. Increasing model complexity..."

            case "$COMPLEXITY" in
                "Low")
                    COMPLEXITY="Mid"
                    run_model "$PROMPT" "Mid"
                    ;;
                "Mid")
                    COMPLEXITY="High"
                    run_model "$PROMPT" "High"
                    ;;
                "High")
                    COMPLEXITY="Inefficient"
                    run_model "$PROMPT" "Inefficient"
                    ;;
                "Inefficient")
                    echo "No more complex models available. Exiting loop."
                    break
                    ;;
            esac
        fi
    done
}

run_model "$PROMPT" "$COMPLEXITY"
check_relevance

end_time=$(date +%s.%3N)
echo "End time: $end_time"
time_diff_ms=$(awk "BEGIN {printf \"%.0f\", ($end_time - $start_time) * 1000}")
echo "Time taken: $time_diff_ms ms"

# python textSimilarity.py

# RELEVANT=$(grep -o '"relevant": *"[^"]*"' data/test.txt | sed 's/"relevant": "//; s/"$//')

echo "Done!!"
