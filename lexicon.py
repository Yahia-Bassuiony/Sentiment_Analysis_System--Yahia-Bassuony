# Positive words with intensity scores
POSITIVE_WORDS = {
    # Strong positive (score: 2.0)
    "amazing":      2.0,
    "excellent":    2.0,
    "outstanding":  2.0,
    "fantastic":    2.0,
    "superb":       2.0,
    "brilliant":    2.0,
    "perfect":      2.0,
    "wonderful":    2.0,
    "love":         2.0,

    # Medium positive (score: 1.0)
    "good":         1.0,
    "great":        1.0,
    "nice":         1.0,
    "happy":        1.0,
    "glad":         1.0,
    "helpful":      1.0,
    "recommend":    1.0,
    "enjoyed":      1.0,
    "impressive":   1.0,
    "pleased":      1.0,

    # Weak positive (score: 0.5)
    "okay":         0.5,
    "fine":         0.5,
    "decent":       0.5,
    "acceptable":   0.5,
    "average":      0.3,
}

# Negative words with intensity scores
NEGATIVE_WORDS = {
    # Strong negative (score: -2.0)
    "terrible":     -2.0,
    "horrible":     -2.0,
    "awful":        -2.0,
    "disgusting":   -2.0,
    "hate":         -2.0,
    "worst":        -2.0,
    "useless":      -2.0,
    "pathetic":     -2.0,

    # Medium negative (score: -1.0)
    "bad":          -1.0,
    "poor":         -1.0,
    "disappointing":-1.0,
    "annoying":     -1.0,
    "frustrated":   -1.0,
    "broken":       -1.0,
    "failed":       -1.0,
    "slow":         -1.0,

    # Weak negative (score: -0.5)
    "mediocre":     -0.5,
    "lacking":      -0.5,
    "boring":       -0.5,
    "overpriced":   -0.5,
}

# Negation words — reverse the sentiment
NEGATION_WORDS = [
    "not", "never", "no", "neither",
    "nobody", "nothing", "nor", "barely",
    "hardly", "scarcely", "doesnt",
    "dont", "cant", "wont", "isnt",
    "wasnt", "couldnt", "shouldnt"
]

# Intensifier words — boost the score
INTENSIFIERS = {
    "very":       1.5,
    "extremely":  2.0,
    "absolutely": 2.0,
    "really":     1.5,
    "incredibly": 2.0,
    "so":         1.3,
    "quite":      1.2,
    "totally":    1.5,
}

# Merge all sentiment words
ALL_WORDS = {**POSITIVE_WORDS, **NEGATIVE_WORDS}