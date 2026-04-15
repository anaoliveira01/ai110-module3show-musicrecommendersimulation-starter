"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

from recommender import load_songs, recommend_songs


def main() -> None:
    
    songs = load_songs("data/songs.csv") 
    print(f"Loaded songs: {len(songs)}")

    # Starter example profile
    user_prefs = {"genre": "pop", "mood": "happy", "energy": 0.8}
    taste_profile = {"genre": "rock", "mood": "intense", "energy": 0.9, "tempo": 120, "valence": 0.4, "danceability": 0.3, "acousticness": 0.2, "liveness": 0.4, "speechiness": 0.1, "instrumentalness": 0.8}

    high_energy_pop = {
        "genre": "pop",
        "mood": "happy",
        "energy": 0.9,
        "tempo": 120,
        "valence": 0.8,
        "danceability": 0.8,
    }
    chill_lofi = {
        "genre": "lofi",
        "mood": "chill",
        "energy": 0.4,
        "tempo": 78,
        "valence": 0.6,
        "danceability": 0.6,
        "acousticness": 0.7,
    }
    deep_intense_rock = {
        "genre": "rock",
        "mood": "intense",
        "energy": 0.95,
        "tempo": 140,
        "valence": 0.45,
        "danceability": 0.5,
    }

    profiles = [
        ("Starter example", user_prefs),
        ("High energy pop", high_energy_pop),
        ("Chill lofi", chill_lofi),
        ("Deep intense rock", deep_intense_rock),
    ]

    for profile_name, profile in profiles:
        recommendations = recommend_songs(profile, songs, k=5)
        print(f"\n{profile_name} recommendations:\n")
        print("Rank  Title                             Score   Reasons")
        print("----  -------------------------------  ------  --------------------------------------------------")
        for index, rec in enumerate(recommendations, start=1):
            song, score, explanation = rec
            title = song.get("title", "Unknown title")
            print(f"{index:>2}.   {title:<31.31}  {score:>6.2f}  {explanation}")


if __name__ == "__main__":
    main()
