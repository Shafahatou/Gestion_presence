from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from hierarchie.models import Direction, Departement

User = get_user_model()

class Command(BaseCommand):
    help = "Crée un directeur, crée une direction liée et affiche toutes les directions existantes."

    def handle(self, *args, **options):
        directions = []
        for directionData in directions:
            director_data = directionData.get("director", None)
            name = directionData.get("name", None)
            director = User.objects.filter(email=director_data.get("email", "")).first()
            if not director:
                director = User.objects.create_user(**director_data, password="123456788")

            direction = Direction.objects.create(name=name, director=director)
        
        departements = directionData.get([])
        name = []
        

