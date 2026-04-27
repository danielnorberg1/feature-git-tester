import random
import textwrap
import datetime

# This program demonstrates several random features in one small CLI.
# Each feature is annotated using the requested &[FeatureX] markers.

# &begin[FeatureA]
def feature_greeting():
    """FeatureA: Print a random greeting and a positive message."""
    greetings = [
        "Hello, explorer!",
        "Welcome to the random feature generator.",
        "Hi there — ready for something unexpected?",
    ]
    compliments = [
        "You're doing great.",
        "Your curiosity is your best feature.",
        "This program thinks you're awesome.",
    ]
    print(random.choice(greetings))
    print(random.choice(compliments))
# &end[FeatureA]

# &begin[FeatureB]
def feature_number_fun():
    """FeatureB: Generate a random number and describe it."""
    value = random.randint(1, 100)
    parity = "even" if value % 2 == 0 else "odd"
    print(f"Your random number is {value}, which is {parity}.")
    if value % 5 == 0:
        print("It is also divisible by 5 — nice pattern!")
# &end[FeatureB]

# &begin[FeatureC]
def feature_story_prompt():
    """FeatureC: Build a tiny story prompt from random pieces."""
    heroes = ["a wandering musician", "a curious scientist", "a daring coder"]
    quests = ["find a hidden library", "tame a wildfire of ideas", "decode a secret message"]
    settings = ["in a neon city", "under the ocean", "inside a mountain"]
    print("Story prompt:")
    print(f"{random.choice(heroes)} must {random.choice(quests)} {random.choice(settings)}.")
# &end[FeatureC]

# &begin[FeatureD]
def feature_ascii_art():
    """FeatureD: Display a small, random ASCII art shape."""
    art = [
        r"""
  /\_/\
 ( o.o )
  > ^ <
""",
        r"""
  .-.
 (o o)
  |=|
 __|__
""",
        r"""
   *
  ***
 *****
*******
  ***
  ***
""",
    ]
    print("Here's a little ASCII surprise:")
    print(random.choice(art).strip())
# &end[FeatureD]

# &begin[FeatureE]
def feature_time_magic():
    """FeatureE: Show the current time and a quick time-based tip."""
    now = datetime.datetime.now()
    print(f"The current time is {now:%Y-%m-%d %H:%M:%S}.")
    if now.hour < 12:
        print("Morning is perfect for planning a new experiment.")
    elif now.hour < 18:
        print("Afternoon is great for pushing through a creative sprint.")
    else:
        print("Evening is ideal for reflecting and relaxing.")
# &end[FeatureE]

FEATURES = [
    ("FeatureA", feature_greeting),
    ("FeatureB", feature_number_fun),
    ("FeatureC", feature_story_prompt),
    ("FeatureD", feature_ascii_art),
    ("FeatureE", feature_time_magic),
]


def main():
    print("=== Random Feature Program ===")
    chosen = random.sample(FEATURES, k=random.randint(2, 4))
    print(f"Running {len(chosen)} random feature(s): {', '.join(name for name, _ in chosen)}")
    print("""
This program selects a small set of features at random each time it runs.
The feature blocks are annotated with &[FeatureX] markers.
""")
    for name, func in chosen:
        print("\n---")
        print(f"{name}")
        func()


if __name__ == "__main__":
    main()
