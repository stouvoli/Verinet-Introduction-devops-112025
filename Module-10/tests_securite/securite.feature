Feature: Sécurité Réseau du Serveur Web
  En tant qu'ingénieur sécurité
  Je veux m'assurer que seuls les ports autorisés sont ouverts
  Pour réduire la surface d'attaque

Scenario: Le serveur web doit exposer le port HTTP
  Given L'adresse cible est "localhost"
  When Je scanne le port 80
  Then Le port doit être "open"
 
Scenario: Le port SSH ne doit pas être exposé
  Given L'adresse cible est "localhost"
  When Je scanne le port 22
  Then Le port doit être "closed"
