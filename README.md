# discord-bot-cosfr

# Bot « Co Scratch Francophone »
# =============================

## Commandes :
- /vérifier                | active la vérification de son compte - voir section « vérifier son compte » pour en savoir plus
- /supprimer vérification  | supprime le lien entre un user discord et scratch
- /scratcheur user:[]         | si un utilisateur a été vérifié, retourne des infos vers son compte scratch (mais en le sélectionnant depuis Discord avec le @)

## Vérifier son compte

- utiliser /vérifier pour activer la vérification (le résultat final ne doit pas marcher sans l'utilisation de cette commande)
- se rendre sur scratch, dans un projet dédié fonctionnant avec scratchattach
- le projet demande un nom d'utilisateur (pas celui d'affichage), l'encrypte et utilise scratchattach pour l'envoyer vers le programme du bot
- le bot reçoit les données, si un utilisateur ayant ce nom d'utilisateur ayant utilisé /vérifier dans les 5 dernières minutes, lie le compte scratch et le compte utilisateur

## Scratcheur

- informe de :
 - nom d'utilisateur sur scratch
 - nombre de projets, vues, j'aimes, favs, suiveurs, posts
 - classement vues, j'aimes, favs, suiveurs, posts, forum francophone
 - pp de l'utilisateur (pq pas) ?

# =============================
