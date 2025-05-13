from django.db import models
from users_app.models import Order,Cart,Favorite


class Plant(models.Model):
    plant_id = models.AutoField(primary_key=True)
    order = models.ForeignKey(Order,on_delete=models.CASCADE,related_name="plant_order",null=True)
    cart = models.ForeignKey(Cart,on_delete=models.CASCADE,related_name="plant_cart",null=True)
    fav_id = models.ForeignKey(Favorite,on_delete=models.CASCADE,related_name="plant_favorite",null=True)


    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='plants/', null=True, blank=True)
    stock = models.IntegerField()
    category = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class IndoorPlant(models.Model):
    plant = models.ForeignKey(Plant, on_delete=models.CASCADE)
    light_requirement = models.CharField(max_length=100)
    water_schedule = models.CharField(max_length=100) 
    def __str__(self):
        return self.name   

class OutdoorPlant(models.Model):
    plant = models.ForeignKey(Plant, on_delete=models.CASCADE)
    climate = models.CharField(max_length=100)
    growth_rate = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class SeasonalFlower(models.Model):
    plant = models.ForeignKey(Plant, on_delete=models.CASCADE)
    season = models.CharField(max_length=100)
    blooming_time = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class FlowerPlant(models.Model):
    plant = models.ForeignKey(Plant, on_delete=models.CASCADE)
    color = models.CharField(max_length=100)
    fragrance = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Tree(models.Model):
    plant = models.ForeignKey(Plant, on_delete=models.CASCADE)
    height = models.CharField(max_length=100)
    age = models.IntegerField()
    def __str__(self):
        return self.name

class GroundCover(models.Model):
    plant = models.ForeignKey(Plant, on_delete=models.CASCADE)
    spread_rate = models.CharField(max_length=100)
    use_case = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class BonsaiPlant(models.Model):
    plant = models.ForeignKey(Plant, on_delete=models.CASCADE)
    style = models.CharField(max_length=100)
    age = models.IntegerField() 
    def __str__(self):
        return self.name  

class Fertilizer(models.Model):
    fertilizer_id = models.AutoField(primary_key=True)
    order = models.ForeignKey(Order,on_delete=models.CASCADE,related_name="fertilizer_order",null=True)
    cart = models.ForeignKey(Cart,on_delete=models.CASCADE,related_name="fertilizer_cart",null=True)
    fav_id = models.ForeignKey(Favorite,on_delete=models.CASCADE,related_name="fertilizer_favorite",null=True)
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='fertilizers/')
    stock = models.IntegerField()
    description = models.TextField()

    def __str__(self):
        return self.name


# GardenFertilizer Model (Subentity)
class GardenFertilizer(models.Model):
    id = models.AutoField(primary_key=True)
    fertilizer = models.ForeignKey(Fertilizer, on_delete=models.CASCADE)
    nitrogen_content = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f"{self.fertilizer.name} - Garden Fertilizer"


# MicroNutri Model (Subentity)
class MicroNutri(models.Model):
    id = models.AutoField(primary_key=True)
    fertilizer = models.ForeignKey(Fertilizer, on_delete=models.CASCADE)
    mineral_type = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.fertilizer.name} - MicroNutri"


# OrganicFertilizer Model (Subentity)
class OrganicFertilizer(models.Model):
    id = models.AutoField(primary_key=True)
    fertilizer = models.ForeignKey(Fertilizer, on_delete=models.CASCADE)
    origin = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.fertilizer.name} - Organic Fertilizer"


# Pesticide Model (Subentity)
class Pesticide(models.Model):
    id = models.AutoField(primary_key=True)
    fertilizer = models.ForeignKey(Fertilizer, on_delete=models.CASCADE)
    pest_type = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.fertilizer.name} - Pesticide"


# SeedStarter Model (Subentity)
class SeedStarter(models.Model):
    id = models.AutoField(primary_key=True)
    fertilizer = models.ForeignKey(Fertilizer, on_delete=models.CASCADE)
    use_method = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.fertilizer.name} - Seed Starter"


# Fungicide Model (Subentity)
class Fungicide(models.Model):
    id = models.AutoField(primary_key=True)
    fertilizer = models.ForeignKey(Fertilizer, on_delete=models.CASCADE)
    fungus_type = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.fertilizer.name} - Fungicide"


# WateringSolution Model (Subentity)
class WateringSolution(models.Model):
    id = models.AutoField(primary_key=True)
    fertilizer = models.ForeignKey(Fertilizer, on_delete=models.CASCADE)
    frequency = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.fertilizer.name} - Watering Solution"


# PlantFood Model (Subentity)
class PlantFood(models.Model):
    id = models.AutoField(primary_key=True)
    fertilizer = models.ForeignKey(Fertilizer, on_delete=models.CASCADE)
    nutrients = models.TextField()

    def __str__(self):
        return f"{self.fertilizer.name} - Plant Food"    

class Seed(models.Model):
    seed_id = models.AutoField(primary_key=True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='seed_orders')
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='seed_carts')
    favorite = models.ForeignKey(Favorite, on_delete=models.CASCADE, related_name='seed_favorites')
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    season = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    image = models.ImageField(upload_to='seed_images/', blank=True)

    def __str__(self):
        return self.name

class GardenTools(models.Model):
    tool_id = models.AutoField(primary_key=True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    favorite = models.ForeignKey(Favorite, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='tools/')
    stock = models.PositiveIntegerField()
    description = models.TextField()

    def __str__(self):
        return self.name

class Pots(models.Model):
    pot_id = models.AutoField(primary_key=True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    favorite = models.ForeignKey(Favorite, on_delete=models.CASCADE)
    type = models.CharField(max_length=100)
    size = models.CharField(max_length=50)
    material = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='pots/')
    stock = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.type} - {self.size}"

class Soil(models.Model):
    soil_id = models.AutoField(primary_key=True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    favorite = models.ForeignKey(Favorite, on_delete=models.CASCADE)
    type = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    description = models.TextField()

class Perlite(models.Model):
    soil = models.ForeignKey(Soil, on_delete=models.CASCADE, related_name="perlite")
    texture = models.CharField(max_length=100)
    application = models.TextField()

class OrganicCompost(models.Model):
    soil = models.ForeignKey(Soil, on_delete=models.CASCADE, related_name="organic_compost")
    compost_type = models.CharField(max_length=100)
    nutrient_level = models.CharField(max_length=100)

class SweetSoilRiverSoil(models.Model):
    soil = models.ForeignKey(Soil, on_delete=models.CASCADE, related_name="sweet_soil_river_soil")
    source = models.CharField(max_length=100)
    texture = models.CharField(max_length=100)



class GardenDecoration(models.Model):
    decor_id = models.AutoField(primary_key=True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    favorite = models.ForeignKey(Favorite, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    image = models.ImageField(upload_to='garden_decorations/')
    
    def __str__(self):
        return self.name



class Services(models.Model):
    service_id = models.AutoField(primary_key=True)
    order_id = models.ForeignKey(Order,on_delete=models.CASCADE,null=True,blank=True)
    cart_id = models.ForeignKey(Cart,on_delete=models.CASCADE,null=True,blank=True)
    favorite_id = models.ForeignKey(Favorite,on_delete=models.CASCADE,null=True,blank=True)
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()

    def __str__(self):
        return self.name

class Landscaping(models.Model):
    service = models.ForeignKey(Services, on_delete=models.CASCADE, related_name='landscaping_services')
    area_size = models.CharField(max_length=100)
    design_type = models.CharField(max_length=100)

    def __str__(self):
        return f"Landscaping for {self.service.name}"

class LawnRestoration(models.Model):
    service = models.ForeignKey(Services, on_delete=models.CASCADE, related_name='lawn_restorations')
    lawn_condition = models.CharField(max_length=100)
    restoration_method = models.CharField(max_length=100)

    def __str__(self):
        return f"Lawn Restoration for {self.service.name}"

class Plantation(models.Model):
    service = models.ForeignKey(Services, on_delete=models.CASCADE, related_name='plantations')
    plant_type = models.CharField(max_length=100)
    soil_preference = models.CharField(max_length=100)

    def __str__(self):
        return f"Plantation for {self.service.name}"

class Pebbles(models.Model):
    pebble_id = models.AutoField(primary_key=True)
    order_id = models.ForeignKey(Order,on_delete=models.CASCADE)
    cart_id = models.ForeignKey(Cart,on_delete=models.CASCADE)
    favorite_id = models.ForeignKey(Favorite,on_delete=models.CASCADE)
    color = models.CharField(max_length=50)
    size = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='pebbles/', null=True, blank=True)
    stock = models.IntegerField()

    def __str__(self):
        return f"{self.color} Pebble - {self.size}"

# Create your models here.
