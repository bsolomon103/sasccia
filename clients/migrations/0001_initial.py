# Generated by Django 3.2.11 on 2022-03-01 15:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AccommodationStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='AssessmentOutcome',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='AssessmentType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='CostFrequency',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='DeliveryMechanism',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Eligibility',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Employment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Ethnicity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Gender',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=6)),
            ],
        ),
        migrations.CreateModel(
            name='HasInformalCarer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='LDAutismExclASHF',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='LDAutismInclASHF',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='LDLearningDisability',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='LDOther',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='MentalHealthDementia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='MentalHealthOther',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='NeuroAcquiredBrain',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='NeuroMotorNeuron',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='NeuroOther',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='NeuroParkinsons',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='NeuroStroke',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='PhysicalAcquiredPhysical',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='PhysicalCancer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='PhysicalCOPD',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='PhysicalHIVAIDS',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='PhysicalOther',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='PrimarySupportReason',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='RequestOutcome',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='RouteOfAccess',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='SensoryHearingImpaired',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='SensoryOther',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='SensoryVisuallyImpaired',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='ServiceComponent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='ServiceProvider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='ServiceType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lasID', models.PositiveIntegerField()),
                ('nhsNumber', models.CharField(max_length=50, null=True)),
                ('firstName', models.CharField(max_length=50, null=True)),
                ('lastName', models.CharField(max_length=50, null=True)),
                ('birthDate', models.DateField(blank=True, null=True)),
                ('deathDate', models.DateField(blank=True, null=True)),
                ('postCode', models.CharField(max_length=50, null=True)),
                ('requestEvent', models.CharField(max_length=7, null=True)),
                ('requestStart', models.DateField(blank=True, null=True)),
                ('requestEnd', models.DateField(blank=True, null=True)),
                ('assessmentEvent', models.CharField(max_length=50, null=True)),
                ('assessmentStart', models.DateField(blank=True, null=True)),
                ('assessmentEnd', models.DateField(blank=True, null=True)),
                ('weeklyVisits', models.FloatField(blank=True, null=True)),
                ('weeklyCost', models.DecimalField(decimal_places=2, max_digits=6, null=True)),
                ('weeklyMins', models.FloatField(blank=True, null=True)),
                ('unitCost', models.DecimalField(decimal_places=2, max_digits=6, null=True)),
                ('weeklyUnits', models.FloatField(blank=True, null=True)),
                ('serviceEvent', models.CharField(max_length=50, null=True)),
                ('serviceStart', models.DateField(blank=True, null=True)),
                ('serviceEnd', models.DateField(blank=True, null=True)),
                ('age', models.PositiveIntegerField(null=True)),
                ('accommodationStatus', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='clients.accommodationstatus')),
                ('assessmentOutcome', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='clients.assessmentoutcome')),
                ('assessmentType', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='clients.assessmenttype')),
                ('brainInjury', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='clients.neuroacquiredbrain')),
                ('cancer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='clients.physicalcancer')),
                ('copd', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='clients.physicalcopd')),
                ('costFrequency', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='clients.costfrequency')),
                ('deliveryMechanism', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='clients.deliverymechanism')),
                ('dementiaMental', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='clients.mentalhealthdementia')),
                ('eligibility', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='clients.eligibility')),
                ('employment', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='clients.employment')),
                ('ethnicity', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='clients.ethnicity')),
                ('gender', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='clients.gender')),
                ('hearingImpaired', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='clients.sensoryhearingimpaired')),
                ('hivAIDS', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='clients.physicalhivaids')),
                ('informalCarer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='clients.hasinformalcarer')),
                ('ldExcl', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='clients.ldautismexclashf')),
                ('ldIncl', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='clients.ldautisminclashf')),
                ('learningDisability', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='clients.ldlearningdisability')),
                ('motorNeuron', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='clients.neuromotorneuron')),
                ('otherLd', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='clients.ldother')),
                ('otherMental', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='clients.mentalhealthother')),
                ('otherNeuro', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='clients.neuroother')),
                ('otherPhysical', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='clients.physicalother')),
                ('otherSensory', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='clients.sensoryother')),
                ('parkinsons', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='clients.neuroparkinsons')),
                ('physical', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='clients.physicalacquiredphysical')),
                ('primarySupportReason', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='clients.primarysupportreason')),
                ('requestOutcome', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='clients.requestoutcome')),
                ('routeOfAccess', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='clients.routeofaccess')),
                ('serviceComponent', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='clients.servicecomponent')),
                ('serviceProvider', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='clients.serviceprovider')),
                ('serviceType', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='clients.servicetype')),
                ('stroke', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='clients.neurostroke')),
                ('visuallyImpaired', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='clients.sensoryvisuallyimpaired')),
            ],
        ),
    ]