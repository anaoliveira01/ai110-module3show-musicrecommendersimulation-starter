# 🎵 Music Recommender Simulation

## Project Summary

This project is a music recommender system that uses weighted scoring to rank 18 songs based on users with UserProfile, which is a structured taste profile that includes optional numerical targets for tempo, valence, danceability, liveness, speechiness, instrumentalness, preferred, genre, mood, energy, level, and acoustic preference. Each song is given a score by adding continuous similarity scores for any numerical preferences specified by the user and rewarding genre and mood matches with fixed bonuses (2.5 and 4.0 respectively). The system provides two interfaces: an object-oriented Recommender class that takes UserProfile objects, converts them internally, and returns ranked Song objects with human-readable explanations, and a dictionary-based recommend_songs function for flexible scripting. Through testing, the system discovered that mood weight predominates scoring heavily enough to elevate off-genre songs above on-genre ones and that sparse genre coverage (13 out of 15 genres have only one song) creates filter bubbles where most users receive the same top result regardless of their other preferences. These patterns are similar to those found in real-world recommender systems which likewise amplify popularity bias and lock users into narrow taste clusters when training data is uneven.

---

## How The System Works

Explain your design in plain language.
- Real-world recommendation systems combine user preferences with item characteristics, then score each candidate for how well it matches those preferences.
- This system reads every song from `data/songs.csv`, compares each song to the user profile, and assigns a score based on how well the song matches the preferred genre, mood, and energy shape.
- Genre and mood matches are the strongest signals, while numeric audio features like tempo, valence, and danceability refine the score.
- The ranked output is the top songs sorted from best match to worst match.
- Algorithm recipe: score each song by genre/mood match and feature similarity, then sort the catalog by score and return the top results.
- Potential bias: the small catalog can favor more common genres and moods, so less frequent styles may be under-represented.

Some prompts to answer:

- What features does each `Song` use in your system
  - For example: genre, mood, energy, tempo
    - Each song includes: id, title, artist, genre, mood, energy, tempo_bpm, valence, danceability, acousticness, liveness, speechiness, and instrumentalness.

- What information does your `UserProfile` store
  - Each UserProfile includes favorite_genre, favorite_mood, target_energy, and preferences for acoustic or instrumental qualities.

- How does your `Recommender` compute a score for each song
  - It computes a score by comparing each song's attributes to the user's preferences.
    - Exact genre match gets a high weight.
    - Exact mood match gets a slightly lower (but still strong) weight.
    - Numeric feature differences are converted into smaller similarity scores.

- How do you choose which songs to recommend
  - The recommender scores every song, sorts them by descending score, and returns the top k songs as the final recommendation list.

You can include a simple diagram or bullet list if helpful.

---

## Getting Started

### Setup

1. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv .venv
   source .venv/bin/activate      # Mac or Linux
   .venv\Scripts\activate         # Windows

2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Run the app:

```bash
python -m src.main
```

### Running Tests

Run the starter tests with:

```bash
pytest
```

You can add more tests in `tests/test_recommender.py`.

---

## Experiments You Tried

Use this section to document the experiments you ran. For example:

- What happened when you changed the weight on genre from 2.0 to 0.5
  - Rooftop Lights (indie pop, happy mood) outranked Gym Hero (pop, intense mood) because the mood bonus alone outweighed the genre bonus.
- What happened when you added tempo or valence to the score
  - On a pop/happy profile: the top 3 (Sunrise City, Rooftop Lights, Gym Hero) were identical. Only positions 4 and 5 changed — Storm Runner and Dream City swapped, because Dream City's danceability (0.80) was a closer match to the target (0.8) than Storm Runner's (0.66).
- How did your system behave for different types of users
  - For niche genre users (jazz, classical, reggae), the single matching song always ranked #1. The remaining slots filled in reasonably with acoustically similar songs from other genres.

---

## Limitations and Risks

Summarize some limitations of your recommender.

Examples:

- It only works on a tiny catalog
- It does not understand lyrics or language
- It might over favor one genre or mood

You will go deeper on this in your model card.

---

## Reflection

Read and complete `model_card.md`:

[**Model Card**](model_card.md)

Write 1 to 2 paragraphs here about what you learned:

- about how recommenders turn data into predictions
- about where bias or unfairness could show up in systems like this


---

## 7. `model_card_template.md`

Combines reflection and model card framing from the Module 3 guidance. :contentReference[oaicite:2]{index=2}  

```markdown
# 🎧 Model Card - Music Recommender Simulation

## 1. Model Name

Give your recommender a name, for example:

> VibeFinder 1.0

---

## 2. Intended Use

- What is this system trying to do
- Who is it for

Example:

> This model suggests 3 to 5 songs from a small catalog based on a user's preferred genre, mood, and energy level. It is for classroom exploration only, not for real users.

---

## 3. How It Works (Short Explanation)

Describe your scoring logic in plain language.

- What features of each song does it consider
- What information about the user does it use
- How does it turn those into a number

Try to avoid code in this section, treat it like an explanation to a non programmer.

---

## 4. Data

Describe your dataset.

- How many songs are in `data/songs.csv`
- Did you add or remove any songs
- What kinds of genres or moods are represented
- Whose taste does this data mostly reflect

---

## 5. Strengths

Where does your recommender work well

You can think about:
- Situations where the top results "felt right"
- Particular user profiles it served well
- Simplicity or transparency benefits

---

## 6. Limitations and Bias

Where does your recommender struggle

Some prompts:
- Does it ignore some genres or moods
- Does it treat all users as if they have the same taste shape
- Is it biased toward high energy or one genre by default
- How could this be unfair if used in a real product

---

## 7. Evaluation

How did you check your system

Examples:
- You tried multiple user profiles and wrote down whether the results matched your expectations
- You compared your simulation to what a real app like Spotify or YouTube tends to recommend
- You wrote tests for your scoring logic

You do not need a numeric metric, but if you used one, explain what it measures.

---

## 8. Future Work

If you had more time, how would you improve this recommender

Examples:

- Add support for multiple users and "group vibe" recommendations
- Balance diversity of songs instead of always picking the closest match
- Use more features, like tempo ranges or lyric themes

---

## 9. Personal Reflection

A few sentences about what you learned:

- What surprised you about how your system behaved
- How did building this change how you think about real music recommenders
- Where do you think human judgment still matters, even if the model seems "smart"

