from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import (
    PlantViewSet,
    IndoorPlantViewSet,
    OutdoorPlantViewSet,
    SeasonalFlowerViewSet,
    FlowerPlantViewSet,
    TreeViewSet,
    GroundCoverViewSet,
    BonsaiPlantViewSet,
    FertilizerViewSet, GardenFertilizerViewSet, MicroNutriViewSet,
    OrganicFertilizerViewSet, PesticideViewSet, SeedStarterViewSet,
    FungicideViewSet, WateringSolutionViewSet, PlantFoodViewSet,SeedViewSet,GardenToolsViewSet,PotsViewSet,SoilViewSet, PerliteViewSet, OrganicCompostViewSet, SweetSoilRiverSoilViewSet,GardenDecorationViewSet,ServicesViewSet, LandscapingViewSet, LawnRestorationViewSet, PlantationViewSet,PebblesViewSet
)

router = DefaultRouter()
router.register(r'plants', PlantViewSet)
router.register(r'indoor-plants', IndoorPlantViewSet)
router.register(r'outdoor-plants', OutdoorPlantViewSet)
router.register(r'seasonal-flowers', SeasonalFlowerViewSet)
router.register(r'flower-plants', FlowerPlantViewSet)
router.register(r'trees', TreeViewSet)
router.register(r'ground-covers', GroundCoverViewSet)
router.register(r'bonsai-plants', BonsaiPlantViewSet)
router.register(r'fertilizers', FertilizerViewSet)
router.register(r'garden-fertilizers', GardenFertilizerViewSet)
router.register(r'micronutri', MicroNutriViewSet)
router.register(r'organic-fertilizers', OrganicFertilizerViewSet)
router.register(r'pesticides', PesticideViewSet)
router.register(r'seed-starters', SeedStarterViewSet)
router.register(r'fungicides', FungicideViewSet)
router.register(r'watering-solutions', WateringSolutionViewSet)
router.register(r'plant-food', PlantFoodViewSet)
router.register(r'seeds', SeedViewSet)
router.register(r'garden-tools', GardenToolsViewSet)
router.register(r'pots', PotsViewSet)
router.register(r'soil', SoilViewSet)
router.register(r'perlite', PerliteViewSet)
router.register(r'organic-compost', OrganicCompostViewSet)
router.register(r'sweet-soil', SweetSoilRiverSoilViewSet)
router.register(r'garden-decorations', GardenDecorationViewSet)
router.register(r'services', ServicesViewSet)
router.register(r'landscaping', LandscapingViewSet)
router.register(r'lawn-restoration', LawnRestorationViewSet)
router.register(r'plantation', PlantationViewSet)
router.register(r'pebbles', PebblesViewSet)



urlpatterns = [
    path('', include(router.urls)),
]