from django.shortcuts import render
from django.views import View
from .models import Bakings, ProportionBaking, ProcessBaking, EquipmentBaking
from django.forms.models import model_to_dict
import math

# Create your views here.
class HomeView(View):

    bakings = Bakings.objects.all().order_by('name')

    def get(self, request):
        return render(request, 'home.html', {"bakings": HomeView.bakings})


class RecipeView(View):

    TRANSLATE_INGREDIENTS = {"water_to_flour": "woda",
                 "milk_to_flour": "mleko",
                 "salt_to_flour": "sól",
                 "oil_to_flour": "olej",
                 "butter_to_flour": "masło",
                 "sourdough_to_flour": "zakwas żytni",
                 "poolish_to_flour": "pomłoda",
                 "wheat550_to_whole": "mąka pszenna typ 550",
                 "wheat00_to_whole": "mąka pszenna typ 00",
                 "wheat650_to_whole": "mąka pszenna typ 650",
                 "wheat2000_to_whole": "mąka pszenna typ 2000",
                 "rye720_to_whole": "mąka żytnia typ 720",
                 "rye2000_to_whole": "mąka żytnia typ 2000",
                 "spelt650_to_whole": "mąka orkiszowa typ 650"}

    TRANSLATE_EQUIPMENT = {"bowl": "miska",
                           "silicone_spatula": "szpatułka silikonowa lub inna łyżka do mieszania",
                           "oven": "piekarnik",
                           "food_foil": "folia spożywcza lub ściereczka",
                           "scale": "waga"}

    TRANSLATE_PROCESS = {"preparing_prefermentor_first": "czas trwania fermentacji",
                         "preparing_prefermentor_second": "czas trwania drugiej fermentacji",
                         "stretch_fold_count": "liczba składań",
                         "growing": "czas wyrastania",
                         "time_of_baking": "czas pieczenia",
                         "temperature_of_baking": "temperatura pieczenia"}

    @staticmethod
    def remove_id_from_dict(object_dict):
        del object_dict['id']
        del object_dict['baking']
        return object_dict

    def get(self, request, id):

        baking = Bakings.objects.get(pk=id)

        proportions = RecipeView.remove_id_from_dict(model_to_dict(ProportionBaking.objects.get(baking=baking)))
        proportions = {RecipeView.TRANSLATE_INGREDIENTS[k]: math.ceil(v*500) for (k, v) in proportions.items()}

        process = RecipeView.remove_id_from_dict(model_to_dict(ProcessBaking.objects.get(baking=baking)))
        process = {RecipeView.TRANSLATE_PROCESS[k]: v if k == "stretch_fold_count" or v == 0
                                                    else str(v) + "°C" if k == "temperature_of_baking"
                                                    else str(v) + " min" if v/60 < 1
                                                    else str(math.ceil(v/60)) + " h" for (k, v) in process.items()}

        equipment = RecipeView.remove_id_from_dict(model_to_dict(EquipmentBaking.objects.get(baking=baking)))
        equipment = {RecipeView.TRANSLATE_EQUIPMENT[k]: v for (k, v) in equipment.items()}

        return render(request, 'recipe.html', {'baking': baking,
                                               'proportions': proportions,
                                               'process': process,
                                               'equipment': equipment})

    