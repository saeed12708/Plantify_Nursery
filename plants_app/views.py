from django.shortcuts import render
from rest_framework import viewsets
from .models import (
    Plant,
    IndoorPlant,
    OutdoorPlant,
    SeasonalFlower,
    FlowerPlant,
    Tree,
    GroundCover,
    BonsaiPlant,
    Fertilizer, GardenFertilizer, MicroNutri, OrganicFertilizer,
    Pesticide, SeedStarter, Fungicide, WateringSolution, PlantFood,Seed,GardenTools,Pots,Soil, Perlite, OrganicCompost, SweetSoilRiverSoil,GardenDecoration,Services, Landscaping, LawnRestoration, Plantation, Pebbles 

)
from .serializers import (
    PlantSerializer,
    IndoorPlantSerializer,
    OutdoorPlantSerializer,
    SeasonalFlowerSerializer,
    FlowerPlantSerializer,
    TreeSerializer,
    GroundCoverSerializer,
    BonsaiPlantSerializer,
    FertilizerSerializer, GardenFertilizerSerializer, MicroNutriSerializer,
    OrganicFertilizerSerializer, PesticideSerializer, SeedStarterSerializer,
    FungicideSerializer, WateringSolutionSerializer, PlantFoodSerializer, SeedSerializer,GardenToolsSerializer, PotsSerializer, SoilSerializer, PerliteSerializer, OrganicCompostSerializer, SweetSoilRiverSoilSerializer,GardenDecorationSerializer,ServicesSerializer, LandscapingSerializer, LawnRestorationSerializer, PlantationSerializer,PebblesSerializer
)
from django_filters.rest_framework import DjangoFilterBackend



class PlantViewSet(viewsets.ModelViewSet):
    queryset = Plant.objects.all()
    serializer_class = PlantSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name', 'category', 'price']

class IndoorPlantViewSet(viewsets.ModelViewSet):
    queryset = IndoorPlant.objects.all()
    serializer_class = IndoorPlantSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['plant','light_requirement']
    
class OutdoorPlantViewSet(viewsets.ModelViewSet):
    queryset = OutdoorPlant.objects.all()
    serializer_class = OutdoorPlantSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['plant','climate']

class SeasonalFlowerViewSet(viewsets.ModelViewSet):
    queryset = SeasonalFlower.objects.all()
    serializer_class = SeasonalFlowerSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['plant','season']

class FlowerPlantViewSet(viewsets.ModelViewSet):
    queryset = FlowerPlant.objects.all()
    serializer_class = FlowerPlantSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['plant','color']


class TreeViewSet(viewsets.ModelViewSet):
    queryset = Tree.objects.all()
    serializer_class = TreeSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['plant','age']

class GroundCoverViewSet(viewsets.ModelViewSet):
    queryset = GroundCover.objects.all()
    serializer_class = GroundCoverSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['plant','spread_rate']

class BonsaiPlantViewSet(viewsets.ModelViewSet):
    queryset = BonsaiPlant.objects.all()
    serializer_class = BonsaiPlantSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['plant','age','style']

# Fertilizer ViewSet
class FertilizerViewSet(viewsets.ModelViewSet):
    queryset = Fertilizer.objects.all()
    serializer_class = FertilizerSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['fertilizer_id','name']


# GardenFertilizer ViewSet
class GardenFertilizerViewSet(viewsets.ModelViewSet):
    queryset = GardenFertilizer.objects.all()
    serializer_class = GardenFertilizerSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['id','fertilizer']

# MicroNutri ViewSet
class MicroNutriViewSet(viewsets.ModelViewSet):
    queryset = MicroNutri.objects.all()
    serializer_class = MicroNutriSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['id','fertilizer']


# OrganicFertilizer ViewSet
class OrganicFertilizerViewSet(viewsets.ModelViewSet):
    queryset = OrganicFertilizer.objects.all()
    serializer_class = OrganicFertilizerSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['id','fertilizer']

# Pesticide ViewSet
class PesticideViewSet(viewsets.ModelViewSet):
    queryset = Pesticide.objects.all()
    serializer_class = PesticideSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['id','fertilizer']

# SeedStarter ViewSet
class SeedStarterViewSet(viewsets.ModelViewSet):
    queryset = SeedStarter.objects.all()
    serializer_class = SeedStarterSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['id','fertilizer']

# Fungicide ViewSet
class FungicideViewSet(viewsets.ModelViewSet):
    queryset = Fungicide.objects.all()
    serializer_class = FungicideSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['id','fertilizer']

# WateringSolution ViewSet
class WateringSolutionViewSet(viewsets.ModelViewSet):
    queryset = WateringSolution.objects.all()
    serializer_class = WateringSolutionSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['id','fertilizer']

# PlantFood ViewSet
class PlantFoodViewSet(viewsets.ModelViewSet):
    queryset = PlantFood.objects.all()
    serializer_class = PlantFoodSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['id','fertilizer']

class SeedViewSet(viewsets.ModelViewSet):
    queryset = Seed.objects.all()
    serializer_class = SeedSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['favorite','name']

class GardenToolsViewSet(viewsets.ModelViewSet):
    queryset = GardenTools.objects.all()
    serializer_class = GardenToolsSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['tool_id','name']

class PotsViewSet(viewsets.ModelViewSet):
    queryset = Pots.objects.all()
    serializer_class = PotsSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['favorite','price']


class SoilViewSet(viewsets.ModelViewSet):
    queryset = Soil.objects.all()
    serializer_class = SoilSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['soil_id','price']

class PerliteViewSet(viewsets.ModelViewSet):
    queryset = Perlite.objects.all()
    serializer_class = PerliteSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['soil','texture']

class OrganicCompostViewSet(viewsets.ModelViewSet):
    queryset = OrganicCompost.objects.all()
    serializer_class = OrganicCompostSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['soil','compost_type']

class SweetSoilRiverSoilViewSet(viewsets.ModelViewSet):
    queryset = SweetSoilRiverSoil.objects.all()
    serializer_class = SweetSoilRiverSoilSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['soil','source']

class GardenDecorationViewSet(viewsets.ModelViewSet):
    queryset = GardenDecoration.objects.all()
    serializer_class = GardenDecorationSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['decor_id','name']

class ServicesViewSet(viewsets.ModelViewSet):
    queryset = Services.objects.all()
    serializer_class = ServicesSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['service_id','name']

class LandscapingViewSet(viewsets.ModelViewSet):
    queryset = Landscaping.objects.all()
    serializer_class = LandscapingSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['service','area_size']


class LawnRestorationViewSet(viewsets.ModelViewSet):
    queryset = LawnRestoration.objects.all()
    serializer_class = LawnRestorationSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['service','lawn_condition']


class PlantationViewSet(viewsets.ModelViewSet):
    queryset = Plantation.objects.all()
    serializer_class = PlantationSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['service','plant_type']



class PebblesViewSet(viewsets.ModelViewSet):
    queryset = Pebbles.objects.all()
    serializer_class = PebblesSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['pebble_id','color']