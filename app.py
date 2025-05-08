import streamlit as st
import random
import json
import os

def charger_donnees():
    if os.path.exists("data.json"):
        with open("data.json", "r") as f:
            return json.load(f)
    else:
        return {"niveau": 1, "xp": 0}

def sauvegarder_donnees(niveau, xp):
    with open("data.json", "w") as f:
        json.dump({"niveau": niveau, "xp": xp}, f)



# Charger données depuis le fichier
donnees = charger_donnees()

if "xp" not in st.session_state:
    st.session_state.xp = donnees["xp"]
if "niveau" not in st.session_state:
    st.session_state.niveau = donnees["niveau"]





    

st.title("Solo Coach IA 🎮")
st.write("Bienvenue, aventurier ! Prêt pour ta mission du jour ?")
st.write(f"Ton niveau actuel : {st.session_state.niveau} ⭐")
st.write(f"XP : {st.session_state.xp}/100")
st.progress(st.session_state.xp)



# Liste de quêtes
quetes = [
    "Bois un grand verre d'eau 💧",
    "Fais 10 pompes 💪",
    "Écris 3 choses dont tu es fier aujourd’hui ✍️",
    "Range un coin de ta chambre 🧹",
    "Éteins ton téléphone 30 min 📵",
    "Fais 10 minutes de respiration 🧘"
]


if st.button("Lancer une quête aléatoire"):
    mission = random.choice(quetes)
    st.success(f"✨ Mission : {mission}")





if st.button("✅ J'ai terminé ma mission !"):
    st.session_state.xp += 25
    if st.session_state.xp >= 100:
        st.session_state.niveau += 1
        st.session_state.xp = 0
        st.success(f"Niveau UP ! 🆙 Tu es maintenant niveau {st.session_state.niveau} 🎉")
    else:
        st.success("Bien joué ! Tu gagnes +25 XP ✨")
        
sauvegarder_donnees(st.session_state.niveau, st.session_state.xp)
