import os
import django
import random

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'homefood_connect.settings')
django.setup()

from django.contrib.auth import get_user_model
from dishes.models import Dish
from users.models import HomemakerProfile

User = get_user_model()

def seed_data():
    # Create a homemaker if not exists
    homemaker_user, created = User.objects.get_or_create(
        username='chef_anjali',
        email='anjali@example.com',
        defaults={'is_homemaker': True}
    )
    if created:
        homemaker_user.set_password('password123')
        homemaker_user.save()
        HomemakerProfile.objects.get_or_create(
            user=homemaker_user,
            delivery_radius=10,
            phone='9876543210',
            address='123, Heritage Lane, Jaipur'
        )

    dishes_data = [
        # Indian
        {'name': 'Butter Chicken', 'price': 350, 'category': 'Indian', 'description': 'Creamy, rich tomato-based gravy with tender chicken pieces.', 'ingredients': 'Chicken, Tomato, Cream, Butter, Spices', 'image_url': 'https://images.unsplash.com/photo-1603894584373-5ac82b2ae398?auto=format&fit=crop&w=800&q=80'},
        {'name': 'Paneer Butter Masala', 'price': 280, 'category': 'Indian', 'description': 'Soft paneer cubes in a classic Indian buttery gravy.', 'ingredients': 'Paneer, Tomato, Butter, Cashews, Cream', 'image_url': 'https://images.unsplash.com/photo-1631452180519-c014fe946bc7?auto=format&fit=crop&w=800&q=80'},
        {'name': 'Biryani (Veg)', 'price': 250, 'category': 'Indian', 'description': 'Fragrant basmati rice cooked with vegetables and aromatic spices.', 'ingredients': 'Basmati Rice, Mixed Veggies, Saffron, Spices', 'image_url': 'https://images.unsplash.com/photo-1563379091339-03b21bc4a6f8?auto=format&fit=crop&w=800&q=80'},
        
        # Breakfast
        {'name': 'Idli & Sambar', 'price': 80, 'category': 'Breakfast', 'description': 'Steamed rice cakes served with flavorful lentil soup.', 'ingredients': 'Rice, Urad Dal, Turmeric, Vegetables', 'image_url': 'https://images.unsplash.com/photo-1589301760014-d929f3979dbc?auto=format&fit=crop&w=800&q=80'},
        {'name': 'Dosa', 'price': 100, 'category': 'Breakfast', 'description': 'Crispy fermented crepe made from rice and lentils.', 'ingredients': 'Rice, Lentils, Oil, Potato Filling', 'image_url': 'https://images.unsplash.com/photo-1541014741259-df529411b96a?auto=format&fit=crop&w=800&q=80'},
        
        # Meals
        {'name': 'South Indian Meals', 'price': 180, 'category': 'Meals', 'description': 'A complete platter with rice, sambar, rasam, and poriyal.', 'ingredients': 'Rice, Sambar, Curd, Pickles, Appalam', 'image_url': 'https://images.unsplash.com/photo-1512621776951-a57141f2eefd?auto=format&fit=crop&w=800&q=80'},
        {'name': 'North Indian Thali', 'price': 220, 'category': 'Meals', 'description': 'Full meal with Roti, Dal, Paneer Sabzi, and Rice.', 'ingredients': 'Roti, Dal, Paneer, Rice, Gulab Jamun', 'image_url': 'https://images.unsplash.com/photo-1546833999-b9f581a1996d?auto=format&fit=crop&w=800&q=80'},
        
        # Chinese
        {'name': 'Hakka Noodles', 'price': 150, 'category': 'Chinese', 'description': 'Stir-fried noodles with crisp vegetables and soy sauce.', 'ingredients': 'Noodles, Capsicum, Carrot, Cabbage, Soy Sauce', 'image_url': 'https://images.unsplash.com/photo-1585032226651-759b368d7246?auto=format&fit=crop&w=800&q=80'},
        {'name': 'Fried Rice', 'price': 140, 'category': 'Chinese', 'description': 'Classic vegetable fried rice with a smoky flavor.', 'ingredients': 'Rice, Veggies, Spring Onion, Garlic', 'image_url': 'https://images.unsplash.com/photo-1603133872878-684f208fb84b?auto=format&fit=crop&w=800&q=80'},
        
        # Italian
        {'name': 'Margherita Pizza', 'price': 300, 'category': 'Italian', 'description': 'Simple yet divine with fresh tomatoes and mozzarella.', 'ingredients': 'Pizza Base, Tomato Sauce, Cheese, Basil', 'image_url': 'https://images.unsplash.com/photo-1574071318508-1cdbad80ad38?auto=format&fit=crop&w=800&q=80'},
        {'name': 'White Sauce Pasta', 'price': 260, 'category': 'Italian', 'description': 'Penne pasta tossed in a rich, creamy Alfredo sauce.', 'ingredients': 'Penne, Milk, Cheese, Garlic, Herbs', 'image_url': 'https://images.unsplash.com/photo-1645112481338-3560e7740212?auto=format&fit=crop&w=800&q=80'},
    ]

    for data in dishes_data:
        # We'll use the image_url as a placeholder or download it in a real scenario
        # Since we use ImageField, we might need to handle this differently if we want actual files.
        # But for the sake of this demo, we'll try to save it. 
        # Alternatively, we can use a URLField if we want to refer to external images easily.
        # However, the model uses ImageField.
        
        # Let's check how to save from URL to ImageField in Django
        # For now, I'll just create the Dish objects. 
        # NOTE: If we want to use the images, we should have them in media/dishes/
        
        dish, created = Dish.objects.get_or_create(
            name=data['name'],
            homemaker=homemaker_user,
            defaults={
                'price': data['price'],
                'category': data['category'],
                'description': data['description'],
                'ingredients': data['ingredients'],
                # For ImageField we'll use a dummy for now or just skip if we don't have the file
            }
        )
        if created:
             print(f"Created dish: {dish.name}")

if __name__ == '__main__':
    seed_data()
