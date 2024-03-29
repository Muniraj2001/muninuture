# Generated by Django 4.2.7 on 2024-01-09 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0125_alter_customer_state_alter_orderplaced_status_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='state',
            field=models.CharField(choices=[('Chattisgarh', 'Chattisgarh'), ('Goa', 'Goa'), ('Assam', 'Assam'), ('Himachal Pradesh', 'Himachal Pradesh'), ('Jammu & Kashmir', 'Jammu & Kashmir'), ('Andaman & Nicobar Islands', 'Andaman & Nicobar Islands'), ('Chandigarh', 'Chandigarh'), ('Andhra Pradesh', 'Andhra Pradesh'), ('Arunachal Pradesh', 'Arunachal Pradesh'), ('Dadra & Nagar Haveli', 'Dadra & Nagar Haveli'), ('Bihar', 'Bihar'), ('Delhi', 'Delhi'), ('Gujrat', 'Gujrat'), ('Haryana', 'Haryana'), ('Daman and Diu', 'Daman and Diu')], max_length=100),
        ),
        migrations.AlterField(
            model_name='orderplaced',
            name='status',
            field=models.CharField(choices=[('Packed', 'packed'), ('Cancel', 'Cancel'), ('Delivered', 'Delivered'), ('Accepted', 'Accepted'), ('Pending', 'Pending'), ('On The Wey', 'On The Way')], default='pending', max_length=50),
        ),
        migrations.AlterField(
            model_name='popular',
            name='category',
            field=models.CharField(choices=[('D3', 'Vitamin D3'), ('GH', 'General Health'), ('MH', 'Men Health'), ('OG', 'Organic'), ('AN', 'Antioxidants'), ('DH', 'Digestive Health'), ('E', 'Vitamin E'), ('SH', 'Sexual health'), ('K', 'Vitamin K'), ('C', 'Vitamin C'), ('HS', 'Herbal, Specialty Supplements'), ('AV', 'Ayurvedic'), ('VM', 'Vitamins&Minerals'), ('WH', 'Women health'), ('PC', 'Personal Care'), ('A', 'Vitamin A'), ('B12', 'Vitamin B12'), ('IH', 'Immune Health')], max_length=3),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('D3', 'Vitamin D3'), ('GH', 'General Health'), ('MH', 'Men Health'), ('OG', 'Organic'), ('AN', 'Antioxidants'), ('DH', 'Digestive Health'), ('E', 'Vitamin E'), ('SH', 'Sexual health'), ('K', 'Vitamin K'), ('C', 'Vitamin C'), ('HS', 'Herbal, Specialty Supplements'), ('AV', 'Ayurvedic'), ('VM', 'Vitamins&Minerals'), ('WH', 'Women health'), ('PC', 'Personal Care'), ('A', 'Vitamin A'), ('B12', 'Vitamin B12'), ('IH', 'Immune Health')], max_length=3),
        ),
        migrations.AlterField(
            model_name='product1',
            name='category',
            field=models.CharField(choices=[('D3', 'Vitamin D3'), ('GH', 'General Health'), ('MH', 'Men Health'), ('OG', 'Organic'), ('AN', 'Antioxidants'), ('DH', 'Digestive Health'), ('E', 'Vitamin E'), ('SH', 'Sexual health'), ('K', 'Vitamin K'), ('C', 'Vitamin C'), ('HS', 'Herbal, Specialty Supplements'), ('AV', 'Ayurvedic'), ('VM', 'Vitamins&Minerals'), ('WH', 'Women health'), ('PC', 'Personal Care'), ('A', 'Vitamin A'), ('B12', 'Vitamin B12'), ('IH', 'Immune Health')], max_length=3),
        ),
        migrations.AlterField(
            model_name='shopnow',
            name='category',
            field=models.CharField(choices=[('D3', 'Vitamin D3'), ('GH', 'General Health'), ('MH', 'Men Health'), ('OG', 'Organic'), ('AN', 'Antioxidants'), ('DH', 'Digestive Health'), ('E', 'Vitamin E'), ('SH', 'Sexual health'), ('K', 'Vitamin K'), ('C', 'Vitamin C'), ('HS', 'Herbal, Specialty Supplements'), ('AV', 'Ayurvedic'), ('VM', 'Vitamins&Minerals'), ('WH', 'Women health'), ('PC', 'Personal Care'), ('A', 'Vitamin A'), ('B12', 'Vitamin B12'), ('IH', 'Immune Health')], max_length=3),
        ),
        migrations.AlterField(
            model_name='specialoffer',
            name='category',
            field=models.CharField(choices=[('D3', 'Vitamin D3'), ('GH', 'General Health'), ('MH', 'Men Health'), ('OG', 'Organic'), ('AN', 'Antioxidants'), ('DH', 'Digestive Health'), ('E', 'Vitamin E'), ('SH', 'Sexual health'), ('K', 'Vitamin K'), ('C', 'Vitamin C'), ('HS', 'Herbal, Specialty Supplements'), ('AV', 'Ayurvedic'), ('VM', 'Vitamins&Minerals'), ('WH', 'Women health'), ('PC', 'Personal Care'), ('A', 'Vitamin A'), ('B12', 'Vitamin B12'), ('IH', 'Immune Health')], max_length=3),
        ),
        migrations.DeleteModel(
            name='ProductPack',
        ),
    ]
