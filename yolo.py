import cv2
import numpy as np
import torch

class ObjectDetection:
    """
    Classe pour la détection d'objets utilisant le modèle YOLOv5 et OpenCV.
    """

    def __init__(self, model_name='yolov5s'):

        """
        Initialise le modèle YOLOv5 pré-entraîné.

        Paramètres:
        model_name (str): Le nom du modèle YOLOv5 à charger.
        """
        
        self.model = torch.hub.load('ultralytics/yolov5', model_name, pretrained=True)
        self.classes = self.model.names

    def access_camera(self):
        """
        Accède à la caméra, effectue la détection d'objets et affiche les résultats en temps réel.
        """
        cap = cv2.VideoCapture(0)  # Ouvre la webcam

        if not cap.isOpened():
            print("Erreur d'ouverture de la webcam")
            return

        while True:
            ret, frame = cap.read()
            if not ret:
                break

            # Détection d'objets avec YOLOv5
            results = self.model(frame)

            # Annoter les résultats sur les images avec code couleur
            frame = self.annotate_frame(frame, results)

            # Afficher les FPS
            fps = cap.get(cv2.CAP_PROP_FPS)
            cv2.putText(frame, f"FPS: {fps:.2f}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)

            # Afficher les images
            cv2.imshow('Web Camera', frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):  # Appuyez sur 'q' pour quitter
                break

        cap.release()
        cv2.destroyAllWindows()

    def get_color(self, class_id):
        """
        Retourne une couleur pour annoter les objets détectés.

        Paramètres:
        class_id (int): L'identifiant de la classe de l'objet détecté.

        Retourne:
        tuple: Une couleur RGB pour annoter l'objet détecté.
        """
        # Palette de couleurs
        palette = [
            (255, 0, 0), (0, 255, 0), (0, 0, 255),
            (255, 255, 0), (0, 255, 255), (255, 0, 255),
            (128, 0, 0), (0, 128, 0), (0, 0, 128),
            (128, 128, 0), (0, 128, 128), (128, 0, 128)
        ]
        return palette[class_id % len(palette)]

    def annotate_frame(self, frame, results):
        """
        Annoter le frame avec les résultats de la détection.

        Paramètres:
        frame (ndarray): L'image capturée de la webcam.
        results (torch.Tensor): Les résultats de la détection d'objets.

        Retourne:
        ndarray: L'image annotée.
        """
        for bbox in results.xyxy[0].numpy():
            x1, y1, x2, y2, conf, cls = bbox
            label = f"{self.classes[int(cls)]} {conf:.2f}"
            color = self.get_color(int(cls))
            cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), color, 2)
            cv2.putText(frame, label, (int(x1), int(y1) - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, color, 2)
        return frame

def main():
    """
    Fonction principale pour exécuter la détection d'objets.
    """
    detector = ObjectDetection()
    detector.access_camera()

if __name__ == "__main__":
    main()
