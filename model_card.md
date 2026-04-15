# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name  

Give your model a short, descriptive name.  
Example: **VibeFinder 1.0**  

---

## 2. Intended Use  

Describe what your recommender is designed to do and who it is for. 

Prompts:  

- What kind of recommendations does it generate  
- What assumptions does it make about the user  
- Is this for real users or classroom exploration  

---

## 3. How the Model Works  

Explain your scoring approach in simple language.  

Prompts:  

- What features of each song are used (genre, energy, mood, etc.)  
- What user preferences are considered  
- How does the model turn those into a score  
- What changes did you make from the starter logic  

Avoid code here. Pretend you are explaining the idea to a friend who does not program.

---

## 4. Data  

Describe the dataset the model uses.  

Prompts:  

- How many songs are in the catalog  
- What genres or moods are represented  
- Did you add or remove data  
- Are there parts of musical taste missing in the dataset  

---

## 5. Strengths  

Where does your system seem to work well  

Prompts:  

- User types for which it gives reasonable results  
- Any patterns you think your scoring captures correctly  
- Cases where the recommendations matched your intuition  

---

## 6. Limitations and Bias 

Where the system struggles or behaves unfairly. 

One weakness discovered during experiments for this system is that the new mood weight dominance creates a single-song bias because most of the moods listed are unique and not repeated. This means a user whose favorite_mood matches one of those rare moods will effectively always receive the same song as their top result, because no combination of genre, energy, or other numeric similarities can overcome a 4.0-point head start for the mood. For example, a user preferring "soulful" music will always see "Blue Velvet" ranked first, even if its tempo, valence, and energy are a poor fit.

- Chill lofi had the most dramatic change — 4 out of 5 songs are completely different, and all 5 now fit the genre/mood/acoustic profile.
- Starter and High energy pop share the same top 3, confirming the earlier finding that genre+mood lock in the ranking before numeric features can differentiate.
- Deep intense rock now surfaces Storm Runner (#1) and Midnight Ember (#3) where before it had no genre-relevant songs at all.
- The "before" list (Sunrise City through Gym Hero) was hardcoded CSV insertion order — it was the same for every user, making the system useless for personalization.


Prompts:  

- Features it does not consider 
    - 
- Genres or moods that are underrepresented  
- Cases where the system overfits to one preference  
- Ways the scoring might unintentionally favor some users  

---

## 7. Evaluation  

How you checked whether the recommender behaved as expected. 

Prompts:  

- Which user profiles you tested
    - Four user profiles were tested with the 18-song catalog: a minimal "starter" profile with genre, mood, and energy only, a "high energy pop" profile, "chill lofi", and "deep intense rock". The most unexpected result came from the "deep intense rock" profile. Despite preferring rock music, "Gym Hero" - a pop song - ranked in 2nd place, beating out "Midnight Ember" - metal - because both share the "intense" mood tag.

- What you looked for in the recommendations  
- What surprised you  
- Any simple tests or comparisons you ran  

No need for numeric metrics unless you created some.

---

## 8. Future Work  

Ideas for how you would improve the model next.  

Prompts:  

- Additional features or preferences  
- Better ways to explain recommendations  
- Improving diversity among the top results  
- Handling more complex user tastes  

---

## 9. Personal Reflection  

A few sentences about your experience.  

Prompts:  

- What you learned about recommender systems  
- Something unexpected or interesting you discovered  
- How this changed the way you think about music recommendation apps  
