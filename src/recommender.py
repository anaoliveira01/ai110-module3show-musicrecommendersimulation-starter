import csv
from typing import List, Dict, Tuple, Optional
from dataclasses import dataclass

@dataclass
class Song:
    """
    Represents a song and its attributes.
    Required by tests/test_recommender.py
    """
    id: int
    title: str
    artist: str
    genre: str
    mood: str
    energy: float
    tempo_bpm: float
    valence: float
    danceability: float
    acousticness: float

@dataclass
class UserProfile:
    """
    Represents a user's taste preferences.
    Required by tests/test_recommender.py
    """
    favorite_genre: str
    favorite_mood: str
    target_energy: float
    likes_acoustic: bool
    target_tempo: Optional[float] = None
    target_valence: Optional[float] = None
    target_danceability: Optional[float] = None
    target_liveness: Optional[float] = None
    target_speechiness: Optional[float] = None
    target_instrumentalness: Optional[float] = None

class Recommender:
    """
    OOP implementation of the recommendation logic.
    Required by tests/test_recommender.py
    """
    def __init__(self, songs: List[Song]):
        self.songs = songs

    def _profile_to_prefs(self, user: UserProfile) -> Dict:
        """Map UserProfile fields to the dict keys expected by score_song."""
        prefs: Dict = {
            "genre": user.favorite_genre,
            "mood": user.favorite_mood,
            "energy": user.target_energy,
        }
        if user.likes_acoustic:
            prefs["acousticness"] = 1.0
        optional_numeric = {
            "tempo_bpm": user.target_tempo,
            "valence": user.target_valence,
            "danceability": user.target_danceability,
            "liveness": user.target_liveness,
            "speechiness": user.target_speechiness,
            "instrumentalness": user.target_instrumentalness,
        }
        for key, value in optional_numeric.items():
            if value is not None:
                prefs[key] = value
        return prefs

    def recommend(self, user: UserProfile, k: int = 5) -> List[Song]:
        prefs = self._profile_to_prefs(user)
        scored = [(song_obj, score_song(prefs, vars(song_obj))[0]) for song_obj in self.songs]
        scored.sort(key=lambda x: x[1], reverse=True)
        return [s for s, _ in scored[:k]]

    def explain_recommendation(self, user: UserProfile, song: Song) -> str:
        prefs = self._profile_to_prefs(user)
        _, reasons = score_song(prefs, vars(song))
        return "; ".join(reasons)

def load_songs(csv_path: str) -> List[Dict]:
    """Load song data from the specified CSV file."""
    print(f"Loading songs from {csv_path}...")
    songs: List[Dict] = []
    numeric_fields = {
        "id": int,
        "energy": float,
        "tempo_bpm": float,
        "valence": float,
        "danceability": float,
        "acousticness": float,
        "liveness": float,
        "speechiness": float,
        "instrumentalness": float,
    }

    with open(csv_path, newline="", encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            parsed_row: Dict = {}
            for key, value in row.items():
                if value is None:
                    parsed_row[key] = value
                    continue
                value = value.strip()
                if key in numeric_fields and value != "":
                    parsed_row[key] = numeric_fields[key](value)
                else:
                    parsed_row[key] = value
            songs.append(parsed_row)

    return songs

def score_song(user_prefs: Dict, song: Dict) -> Tuple[float, List[str]]:
    """Score a single song against user preferences, returning its score and reasons."""
    score = 0.0
    reasons: List[str] = []

    genre_weight = 2.5
    mood_weight = 4.0
    energy_weight = 2.0

    if user_prefs.get("genre") and song.get("genre"):
        if user_prefs["genre"].strip().lower() == song["genre"].strip().lower():
            score += genre_weight
            reasons.append(f"genre match (+{genre_weight:.1f})")

    if user_prefs.get("mood") and song.get("mood"):
        if user_prefs["mood"].strip().lower() == song["mood"].strip().lower():
            score += mood_weight
            reasons.append(f"mood match (+{mood_weight:.1f})")

    numeric_keys = {
        "energy": "energy",
        "tempo": "tempo_bpm",
        "tempo_bpm": "tempo_bpm",
        "valence": "valence",
        "danceability": "danceability",
        "acousticness": "acousticness",
        "liveness": "liveness",
        "speechiness": "speechiness",
        "instrumentalness": "instrumentalness",
    }

    seen_song_keys: set = set()
    for pref_key, song_key in numeric_keys.items():
        if song_key in seen_song_keys:
            continue
        if pref_key in user_prefs and song_key in song:
            try:
                user_value = float(user_prefs[pref_key])
                song_value = float(song[song_key])
            except (TypeError, ValueError):
                continue

            seen_song_keys.add(song_key)
            diff = abs(user_value - song_value)
            similarity = max(0.0, 1.0 - diff)
            if similarity > 0:
                weight = energy_weight if pref_key == "energy" else 1.0
                score += similarity * weight
                reasons.append(f"{song_key} similarity (+{similarity * weight:.2f})")

    if not reasons:
        reasons.append("no strong match")

    return score, reasons

def recommend_songs(user_prefs: Dict, songs: List[Dict], k: int = 5) -> List[Tuple[Dict, float, str]]:
    """Rank songs by score and return the top k recommendations."""
    scored_songs: List[Tuple[Dict, float, str]] = []

    for song in songs:
        score, reasons = score_song(user_prefs, song)
        explanation = "; ".join(reasons)
        scored_songs.append((song, score, explanation))

    scored_songs.sort(key=lambda item: item[1], reverse=True)
    return scored_songs[:k]
