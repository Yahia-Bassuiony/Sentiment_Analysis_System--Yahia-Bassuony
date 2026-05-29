import re
from lexicon import (
    ALL_WORDS,
    NEGATION_WORDS,
    INTENSIFIERS
)

#---------------------------------------------------------
# display functions

def display_welcome():
    """Display welcome message"""
    print("=" * 55)
    print("   SENTIMENT ANALYSIS SYSTEM")
    print("   DecodeLabs AI Internship | Project 4")
    print("=" * 55)


def display_result(text, sentiment, score, confidence):
    """Display the analysis result"""
    print("\n" + "-" * 55)
    print(f"  Text       : {text}")
    print(f"  Sentiment  : {sentiment}")
    print(f"  Score      : {score:.2f}")
    print(f"  Confidence : {confidence:.1f}%")
    print("-" * 55)

#---------------------------------------------------------------
# text preprocessing

def preprocess_text(text):
    """
    Clean and tokenize the input text.
    Returns a list of lowercase words.
    """
    # Convert to lowercase
    text = text.lower()

    # Remove punctuation using regex
    text = re.sub(r'[^\w\s]', '', text)

    # Split into words (tokenize)
    words = text.split()

    return words

#--------------------------------------------------------------------
# scoring engine

def calculate_score(words):
    """
    Calculate sentiment score for a list of words.
    Handles negation and intensifiers.
    Returns total score and word details.
    """
    total_score  = 0.0
    word_details = []
    negation_active     = False
    intensifier_value   = 1.0

    for i, word in enumerate(words):

        # Check if word is a negation
        if word in NEGATION_WORDS:
            negation_active = True
            word_details.append((word, "negation", 0))
            continue

        # Check if word is an intensifier
        if word in INTENSIFIERS:
            intensifier_value = INTENSIFIERS[word]
            word_details.append((word, "intensifier",
                                  intensifier_value))
            continue

        # Check if word has sentiment
        if word in ALL_WORDS:
            base_score = ALL_WORDS[word]

            # Apply intensifier
            score = base_score * intensifier_value

            # Apply negation — flip the score
            if negation_active:
                score = score * -1
                negation_active = False

            total_score += score
            word_details.append((word, "sentiment", score))

            # Reset intensifier after use
            intensifier_value = 1.0

        else:
            word_details.append((word, "neutral", 0))

    return total_score, word_details

#------------------------------------------------------------------
# sentiment label

def get_sentiment_label(score):
    """
    Convert numeric score to sentiment label.
    Returns label and confidence percentage.
    """
    # Calculate confidence (cap at 100%)
    confidence = min(abs(score) * 20, 100)

    if score >= 1.0:
        return "POSITIVE ", confidence
    elif score <= -1.0:
        return "NEGATIVE ", confidence
    else:
        return "NEUTRAL  ", confidence


def analyze(text):
    """
    Main function — full pipeline.
    Takes raw text, returns sentiment.
    """
    # Step 1: Preprocess
    words = preprocess_text(text)

    # Step 2: Score
    score, details = calculate_score(words)

    # Step 3: Label
    sentiment, confidence = get_sentiment_label(score)

    return sentiment, score, confidence, details

#--------------------------------------------------------------
# batch analysis

import json
import datetime


def analyze_batch(texts):
    """
    Analyze a list of texts.
    Returns list of results.
    """
    results = []

    print("\n" + "=" * 55)
    print("  BATCH ANALYSIS RESULTS")
    print("=" * 55)

    for i, text in enumerate(texts, 1):
        sentiment, score, confidence, _ = analyze(text)

        result = {
            "id":         i,
            "text":       text,
            "sentiment":  sentiment,
            "score":      round(score, 2),
            "confidence": round(confidence, 1)
        }
        results.append(result)

        print(f"\n  [{i}] {text}")
        print(f"      → {sentiment} | "
              f"Score: {score:.2f} | "
              f"Confidence: {confidence:.1f}%")

    return results


def show_statistics(results):
    """
    Show summary statistics for batch results.
    """
    total    = len(results)
    positive = sum(1 for r in results
                   if "POSITIVE" in r['sentiment'])
    negative = sum(1 for r in results
                   if "NEGATIVE" in r['sentiment'])
    neutral  = sum(1 for r in results
                   if "NEUTRAL"  in r['sentiment'])

    avg_score = sum(r['score'] for r in results) / total

    print("\n" + "=" * 55)
    print("  STATISTICS")
    print("=" * 55)
    print(f"  Total Analyzed : {total}")
    print(f"  Positive       : {positive} "
          f"({positive/total*100:.1f}%)")
    print(f"  Negative       : {negative} "
          f"({negative/total*100:.1f}%)")
    print(f"  Neutral        : {neutral}  "
          f"({neutral/total*100:.1f}%)")
    print(f"  Average Score  : {avg_score:.2f}")
    print("=" * 55)


def save_results(results, filename="results.json"):
    """
    Save analysis results to a JSON file.
    """
    output = {
        "timestamp": datetime.datetime.now().strftime(
                     "%Y-%m-%d %H:%M:%S"),
        "total":     len(results),
        "results":   results
    }

    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(output, f, indent=4, ensure_ascii=False)

    print(f"\n  Results saved to '{filename}' ")

#--------------------------------------------------------------------
# main loop

def main():
    display_welcome()
    print("\n  Options:")
    print("  1. Analyze single text")
    print("  2. Analyze batch")
    print("  Type 'exit' to quit.\n")

    while True:
        user_input = input("\nYou: ").strip()

        if not user_input:
            continue

        if user_input.lower() == "exit":
            print("\n  Goodbye! 👋")
            break

        # Batch mode
        if user_input.lower() == "2":
            print("\n  Enter texts one by one.")
            print("  Type 'done' when finished.\n")
            texts = []
            while True:
                text = input("  Text: ").strip()
                if text.lower() == "done":
                    break
                if text:
                    texts.append(text)

            if texts:
                results = analyze_batch(texts)
                show_statistics(results)
                save_results(results)
            continue

        # Debug mode
        debug_mode = False
        if user_input.lower().startswith("debug "):
            debug_mode = True
            user_input = user_input[6:]

        # Single analysis
        sentiment, score, confidence, details = analyze(
            user_input)
        display_result(user_input, sentiment, score, confidence)

        if debug_mode:
            print("\n  [ Word Analysis ]")
            for word, word_type, word_score in details:
                if word_type != "neutral":
                    print(f"    {word:<15} {word_type:<12}"
                          f" {word_score:+.2f}")


if __name__ == "__main__":
    main()