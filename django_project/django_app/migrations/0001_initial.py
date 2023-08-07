# Generated by Django 4.2.4 on 2023-08-06 15:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CompanyInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, help_text='Enter name', max_length=100)),
                ('domain_name', models.CharField(blank=True, help_text='Enter domain name', max_length=50)),
                ('industry', models.CharField(blank=True, help_text='Enter indistry', max_length=100)),
                ('c_country', models.CharField(blank=True, help_text='Enter country', max_length=50)),
                ('c_state', models.CharField(blank=True, help_text='Enter state', max_length=50)),
                ('c_city', models.CharField(blank=True, help_text='Enter city', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('date', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='PersonalInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lead_status', models.CharField(choices=[('', 'Lead Status Choice'), ('New', 'New'), ('Open', 'Open'), ('In Progress', 'In Progress'), ('Open Deal', 'Open Deal'), ('Unqualified', 'Unqualified')], default='New', max_length=20)),
                ('life_cycle_stage', models.CharField(choices=[('', 'Life Cycle Stage'), ('Lead', 'Lead'), ('Marketing qualified lead', 'Marketing qualified lead'), ('Sales qualified lead', 'Sales qualified lead'), ('Opportunity', 'Opportunity'), ('Customer', 'Customer'), ('Evangelist', 'Evangelist'), ('Others', 'Others')], default='Lead', max_length=50)),
                ('prefix', models.CharField(blank=True, choices=[('', 'Select Prefix'), ('Mr.', 'Mr.'), ('Mrs.', 'Mrs.'), ('Ms.', 'Ms.'), ('Father', 'Father'), ('Elder', 'Elder'), ('Brother', 'Brother'), ('Sister', 'Sister'), ('Rabbi', 'Rabbi'), ('Rev', 'Rev'), ('Capt.', 'Capt.'), ('Chief', 'Chief'), ('Cmdr.', 'Cmdr.'), ('Lt Col.', 'Lt Col.'), ('Lt.', 'Lt.'), ('Col.', 'Col.'), ('Gen.', 'Gen.'), ('Hon.', 'Hon.'), ('Maj.', 'Maj.'), ('MSgt.', 'MSgt.'), ('Adm.', 'Adm.'), ('Atty.', 'Atty.'), ('Dean', 'Dean'), ('Prof.', 'Prof.'), ('Dr.', 'Dr.'), ('Prince', 'Prince')], default='Mr.', max_length=30)),
                ('first_name', models.CharField(help_text='Enter first name', max_length=30)),
                ('middle_name', models.CharField(blank=True, help_text='Enter middle name', max_length=30)),
                ('last_name', models.CharField(blank=True, help_text='Enter last name', max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='AccountsReceivable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.BigIntegerField(default=0, null=True)),
                ('created_at', models.DateTimeField()),
                ('paid', models.BooleanField(default=False)),
                ('contact', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='django_app.personalinfo')),
                ('invoice', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='django_app.invoice')),
            ],
        ),
        migrations.CreateModel(
            name='AccountsPayable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('outstanding_amount', models.BigIntegerField(default=0, null=True)),
                ('amount_paid', models.BigIntegerField(default=0, null=True)),
                ('payment_status', models.CharField(blank=True, help_text='payment status', max_length=50)),
                ('created_at', models.DateTimeField(blank=True)),
                ('invoice', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='django_app.invoice')),
            ],
        ),
    ]
