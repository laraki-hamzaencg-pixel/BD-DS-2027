import pandas as pd
import matplotlib.pyplot as plt

# 1. Import des données
evolution = pd.read_csv("dataset_chomage_national.csv")
categories = pd.read_csv("dataset_chomage_2025_categories.csv")

# 2. Quelques calculs simples
debut = evolution.loc[evolution["annee"] == 2019, "taux_chomage"].iloc[0]
pic = evolution["taux_chomage"].max()
annee_pic = evolution.loc[evolution["taux_chomage"].idxmax(), "annee"]
print(f"Taux en 2019 : {debut} %")
print(f"Taux maximum : {pic} % en {annee_pic}")
print(f"Hausse 2019 -> {annee_pic} : {round(pic - debut, 1)} points")

# 3. Graphiques
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(13, 5))

ax1.plot(evolution["annee"], evolution["taux_chomage"], marker="o", color="tab:red")
for x, y in zip(evolution["annee"], evolution["taux_chomage"]):
    ax1.text(x, y + 0.25, str(y), ha="center", fontsize=9)
ax1.set_title("Taux de chômage au Maroc (2018-2025)")
ax1.set_xlabel("Année")
ax1.set_ylabel("Taux de chômage (%)")
ax1.set_ylim(8, 15)
ax1.grid(alpha=0.3)

ax2.barh(categories["categorie"], categories["taux_chomage"], color="tab:blue")
for i, v in enumerate(categories["taux_chomage"]):
    ax2.text(v + 0.5, i, f"{v} %", va="center", fontsize=9)
ax2.set_title("Qui est le plus touché ? (2025)")
ax2.set_xlabel("Taux de chômage (%)")
ax2.set_xlim(0, 45)
ax2.invert_yaxis()

plt.tight_layout()
plt.savefig("graphique_chomage.png", dpi=150)
plt.show()
