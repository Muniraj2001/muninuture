# Generated by Django 4.2.7 on 2023-11-21 05:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0021_product2_delete_product1_alter_customer_state_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('category', models.CharField(choices=[('GH', 'General Health'), ('MH', 'Men Health'), ('AN', 'Antioxidants'), ('HS', 'Herbal, Specialty Supplements'), ('OG', 'Organic'), ('PC', 'Personal Care'), ('IH', 'Immune Health'), ('VM', 'Vitamins&Minerals'), ('SH', 'Sexual health'), ('WH', 'Women health'), ('AV', 'Ayurvedic'), ('DH', 'Digestive Health')], max_length=2)),
                ('main_image', models.ImageField(upload_to='product_images/')),
                ('thumb1', models.ImageField(upload_to='product_images/')),
                ('thumb2', models.ImageField(upload_to='product_images/')),
                ('thumb3', models.ImageField(upload_to='product_images/')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.DeleteModel(
            name='Product2',
        ),
        migrations.AlterField(
            model_name='customer',
            name='state',
            field=models.CharField(choices=[('Daman and Diu', 'Daman and Diu'), ('Bihar', 'Bihar'), ('Andaman & Nicobar Islands', 'Andaman & Nicobar Islands'), ('Andhra Pradesh', 'Andhra Pradesh'), ('Arunachal Pradesh', 'Arunachal Pradesh'), ('Jammu & Kashmir', 'Jammu & Kashmir'), ('Chattisgarh', 'Chattisgarh'), ('Assam', 'Assam'), ('Haryana', 'Haryana'), ('Himachal Pradesh', 'Himachal Pradesh'), ('Goa', 'Goa'), ('Dadra & Nagar Haveli', 'Dadra & Nagar Haveli'), ('Chandigarh', 'Chandigarh'), ('Delhi', 'Delhi'), ('Gujrat', 'Gujrat')], max_length=100),
        ),
        migrations.AlterField(
            model_name='orderplaced',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Cancel', 'Cancel'), ('Accepted', 'Accepted'), ('Packed', 'packed'), ('Delivered', 'Delivered'), ('On The Wey', 'On The Way')], default='pending', max_length=50),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('GH', 'General Health'), ('MH', 'Men Health'), ('AN', 'Antioxidants'), ('HS', 'Herbal, Specialty Supplements'), ('OG', 'Organic'), ('PC', 'Personal Care'), ('IH', 'Immune Health'), ('VM', 'Vitamins&Minerals'), ('SH', 'Sexual health'), ('WH', 'Women health'), ('AV', 'Ayurvedic'), ('DH', 'Digestive Health')], max_length=2),
        ),
        migrations.AlterField(
            model_name='specialoffer',
            name='category',
            field=models.CharField(choices=[('GH', 'General Health'), ('MH', 'Men Health'), ('AN', 'Antioxidants'), ('HS', 'Herbal, Specialty Supplements'), ('OG', 'Organic'), ('PC', 'Personal Care'), ('IH', 'Immune Health'), ('VM', 'Vitamins&Minerals'), ('SH', 'Sexual health'), ('WH', 'Women health'), ('AV', 'Ayurvedic'), ('DH', 'Digestive Health')], max_length=2),
        ),
    ]