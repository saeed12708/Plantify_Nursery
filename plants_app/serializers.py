from rest_framework import serializers
from .models import Plant, IndoorPlant,OutdoorPlant, SeasonalFlower, FlowerPlant,  Tree, GroundCover,BonsaiPlant,Fertilizer, GardenFertilizer, MicroNutri, OrganicFertilizer, Pesticide, SeedStarter, Fungicide, WateringSolution, PlantFood,GardenTools,Pots,Soil, Perlite, OrganicCompost, SweetSoilRiverSoil,GardenDecoration 

from .models import Seed,Services, Landscaping, LawnRestoration, Plantation,Pebbles

class PlantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plant
        fields = '__all__'

class IndoorPlantSerializer(serializers.ModelSerializer):
    class Meta:
        model = IndoorPlant
        fields = '__all__'

class OutdoorPlantSerializer(serializers.ModelSerializer):
    class Meta:
        model = OutdoorPlant
        fields = '__all__'

class SeasonalFlowerSerializer(serializers.ModelSerializer):
    class Meta:
        model = SeasonalFlower
        fields = '__all__'

class FlowerPlantSerializer(serializers.ModelSerializer):
    class Meta:
        model = FlowerPlant
        fields = '__all__'

class TreeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tree
        fields = '__all__'

class GroundCoverSerializer(serializers.ModelSerializer):
    class Meta:
        model = GroundCover
        fields = '__all__'

class BonsaiPlantSerializer(serializers.ModelSerializer):
    class Meta:
        model = BonsaiPlant
        fields = '__all__'

# Fertilizer Serializer
class FertilizerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fertilizer
        fields = '__all__'  # All fields from Fertilizer model

# GardenFertilizer Serializer
class GardenFertilizerSerializer(serializers.ModelSerializer):
   # Nested Fertilizer Serializer

    class Meta:
        model = GardenFertilizer
        fields = '__all__'  # All fields from GardenFertilizer model

# MicroNutri Serializer
class MicroNutriSerializer(serializers.ModelSerializer):
    
 class Meta:
        model = MicroNutri
        fields = '__all__'  # All fields from MicroNutri model

# OrganicFertilizer Serializer
class OrganicFertilizerSerializer(serializers.ModelSerializer):
     # Nested Fertilizer Serializer

    class Meta:
        model = OrganicFertilizer
        fields = '__all__'  # All fields from OrganicFertilizer model

# Pesticide Serializer
class PesticideSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pesticide
        fields = '__all__'  # All fields from Pesticide model

# SeedStarter Serializer
class SeedStarterSerializer(serializers.ModelSerializer):
   

    class Meta:
        model = SeedStarter
        fields = '__all__'  # All fields from SeedStarter model

# Fungicide Serializer
class FungicideSerializer(serializers.ModelSerializer):

    class Meta:
        model = Fungicide
        fields = '__all__'  # All fields from Fungicide model

# WateringSolution Serializer
class WateringSolutionSerializer(serializers.ModelSerializer):

    class Meta:
        model = WateringSolution
        fields = '__all__'  # All fields from WateringSolution model

# PlantFood Serializer
class PlantFoodSerializer(serializers.ModelSerializer):

    class Meta:
        model = PlantFood
        fields = '__all__'  # All fields from PlantFood model


class SeedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seed
        fields = '__all__'

class GardenToolsSerializer(serializers.ModelSerializer):
    class Meta:
        model = GardenTools
        fields = '__all__'

class PotsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pots
        fields = '__all__'


class PerliteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Perlite
        fields = '__all__'

class OrganicCompostSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrganicCompost
        fields = '__all__'

class SweetSoilRiverSoilSerializer(serializers.ModelSerializer):
    class Meta:
        model = SweetSoilRiverSoil
        fields = '__all__'

class SoilSerializer(serializers.ModelSerializer):
    perlite = PerliteSerializer(many=True, read_only=True)
    organic_compost = OrganicCompostSerializer(many=True, read_only=True)
    sweet_soil_river_soil = SweetSoilRiverSoilSerializer(many=True, read_only=True)

    class Meta:
        model = Soil
        fields = '__all__'



class GardenDecorationSerializer(serializers.ModelSerializer):
    class Meta:
        model = GardenDecoration
        fields = '__all__'



class LandscapingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Landscaping
        fields = '__all__'

class LawnRestorationSerializer(serializers.ModelSerializer):
    class Meta:
        model = LawnRestoration
        fields = '__all__'

class PlantationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plantation
        fields = '__all__'

class ServicesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Services
        fields = '__all__'



class PebblesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pebbles
        fields = '__all__'
