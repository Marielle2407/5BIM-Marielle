# Système de Détection d'Ordinateur et de Souris à l'aide de OpenCV & YOLO

## Contexte
Ce projet a pour but de développer un système capable de détecter des ordinateurs et des souris sur des images ou 
des flux vidéo en utilisant OpenCV et le modèle de détection d'objets YOLO (You Only Look Once). Le code est structuré 
en utilisant une approche de programmation orientée objet (POO) et est bien commenté pour en expliquer les fonctionnalités et la logique.

## Objectifs
1. Faire fonctionner OpenCV
2. Utiliser le modèle YOLO
3. Intégrer les fonctionnalités d'OpenCV et YOLO pour traiter l'image ou le flux vidéo
4. Bonus: Utilisation de la POO et ajout de commentaires/documentation

## Installation des dépendances

Assurez-vous d'avoir Python installé sur votre machine. Puis, installez les dépendances nécessaires en utilisant le fichier `requirements.txt`.

```bash
pip install -r requirements.txt

## Exécution du projet

Pour exécuter le projet, lancez le fichier yolo.py:

```bash
python yolo.py

## Fonctionnalités

Détection en temps réel: Utilise la webcam pour détecter des objets en temps réel.
Annotation des objets: Affiche des cadres colorés et des étiquettes sur les objets détectés.
Affichage des FPS: Affiche le nombre d'images par seconde en temps réel.

## Structure du Code

ObjectDetection : Classe principale pour la détection d'objets utilisant YOLOv5 et OpenCV.

__init__(self, model_name='yolov5s') : Initialise le modèle YOLOv5 pré-entraîné.
access_camera(self) : Méthode pour accéder à la caméra et effectuer la détection en temps réel.
annotate_frame(self, frame, results) : Méthode pour annoter l'image avec les résultats de la détection.
get_color(self, class_id) : Méthode pour obtenir une couleur pour annoter les objets détectés.
main() : Fonction principale pour exécuter la détection d'objets.

## Commentaires
Le code est bien commenté pour expliquer les parties critiques et les méthodes utilisées.

## Documentation
Pour plus d'informations sur l'utilisation et la compréhension du code, veuillez consulter les commentaires dans le fichier yolo.py.

## Exigences Techniques
Utilisez Python pour le développement.
La version d'OpenCV recommandée est 4.5 ou supérieure.
Utilisez YOLOv3 ou une version ultérieure.
Documentez les dépendances et les instructions pour exécuter le projet dans un fichier README.
## Contribution
Les contributions sont les bienvenues. Veuillez ouvrir une issue pour discuter de ce que vous souhaitez changer.
