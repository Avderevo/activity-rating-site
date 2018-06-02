# Generated by Django 2.0.4 on 2018-05-25 15:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Activities',
            fields=[
                ('activityId', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('maxFractionalCadence', models.CharField(default=None, max_length=30, null=True)),
                ('avgGroundContactBalance', models.CharField(default=None, max_length=30, null=True)),
                ('avgStrokeCadence', models.CharField(default=None, max_length=30, null=True)),
                ('steps', models.CharField(default=None, max_length=30, null=True)),
                ('elapsedDuration', models.CharField(default=None, max_length=30, null=True)),
                ('lapCount', models.CharField(default=None, max_length=30, null=True)),
                ('maxElevation', models.CharField(default=None, max_length=30, null=True)),
                ('leftBalance', models.CharField(default=None, max_length=30, null=True)),
                ('minElevation', models.CharField(default=None, max_length=30, null=True)),
                ('timeZoneId', models.CharField(default=None, max_length=20)),
                ('maxSwimCadenceInStrokesPerMinute', models.CharField(default=None, max_length=30, null=True)),
                ('calories', models.CharField(default=None, max_length=30, null=True)),
                ('courseId', models.CharField(default=None, max_length=30, null=True)),
                ('maxStrokeCadence', models.CharField(default=None, max_length=30, null=True)),
                ('numberOfActivityComments', models.CharField(default=None, max_length=30, null=True)),
                ('maxDoubleCadence', models.CharField(default=None, max_length=30, null=True)),
                ('parentId', models.CharField(default=None, max_length=30, null=True)),
                ('distance', models.CharField(default=None, max_length=30, null=True)),
                ('commentedByUser', models.CharField(default=None, max_length=300, null=True)),
                ('activityLikeFullNames', models.CharField(default=None, max_length=100, null=True)),
                ('avgStrokeDistance', models.CharField(default=None, max_length=30, null=True)),
                ('decoDive', models.CharField(default=None, max_length=30, null=True)),
                ('duration', models.CharField(default=None, max_length=50, null=True)),
                ('avgGroundContactTime', models.CharField(default=None, max_length=30, null=True)),
                ('aerobicTrainingEffect', models.CharField(default=None, max_length=30, null=True)),
                ('ownerFullName', models.CharField(default=None, max_length=100, null=True)),
                ('averageSwimCadenceInStrokesPerMinute', models.CharField(default=None, max_length=30, null=True)),
                ('startN2', models.CharField(default=None, max_length=30, null=True)),
                ('startTimeLocal', models.DateTimeField(null=True)),
                ('description', models.CharField(default=None, max_length=30, null=True)),
                ('maxTemperature', models.CharField(default=None, max_length=30, null=True)),
                ('maxVerticalSpeed', models.CharField(default=None, max_length=30, null=True)),
                ('elevationLoss', models.CharField(default=None, max_length=30, null=True)),
                ('endCns', models.CharField(default=None, max_length=100, null=True)),
                ('startCns', models.CharField(default=None, max_length=100, null=True)),
                ('activityName', models.CharField(default=None, max_length=100, null=True)),
                ('likedByUser', models.CharField(default=None, max_length=100, null=True)),
                ('activeLengths', models.CharField(default=None, max_length=100, null=True)),
                ('lactateThresholdSpeed', models.CharField(default=None, max_length=30, null=True)),
                ('maxSpeed', models.CharField(default=None, max_length=30, null=True)),
                ('maxBikingCadenceInRevPerMinute', models.CharField(default=None, max_length=30, null=True)),
                ('trainingStressScore', models.CharField(default=None, max_length=30, null=True)),
                ('strokes', models.CharField(default=None, max_length=100, null=True)),
                ('floorsClimbed', models.CharField(default=None, max_length=100, null=True)),
                ('avgStrideLength', models.CharField(default=None, max_length=100, null=True)),
                ('workoutId', models.CharField(default=None, max_length=30, null=True)),
                ('avgVerticalSpeed', models.CharField(default=None, max_length=30, null=True)),
                ('elevationGain', models.CharField(default=None, max_length=30, null=True)),
                ('maxDepth', models.CharField(default=None, max_length=30, null=True)),
                ('avgLeftBalance', models.CharField(default=None, max_length=30, null=True)),
                ('ownerId', models.CharField(default=None, max_length=30)),
                ('anaerobicTrainingEffect', models.CharField(default=None, max_length=30, null=True)),
                ('movingDuration', models.CharField(default=None, max_length=30, null=True)),
                ('avgFractionalCadence', models.CharField(default=None, max_length=30, null=True)),
                ('floorsDescended', models.CharField(default=None, max_length=100, null=True)),
                ('intensityFactor', models.CharField(default=None, max_length=100, null=True)),
                ('startLatitude', models.CharField(default=None, max_length=30, null=True)),
                ('sportTypeId', models.CharField(default=None, max_length=30, null=True)),
                ('beginTimestamp', models.CharField(default=None, max_length=30, null=True)),
                ('maxPower', models.CharField(default=None, max_length=30, null=True)),
                ('minCda', models.CharField(default=None, max_length=30, null=True)),
                ('averageSpeed', models.CharField(default=None, max_length=30, null=True)),
                ('vO2MaxValue', models.CharField(default=None, max_length=30, null=True)),
                ('averageHR', models.CharField(default=None, max_length=30, null=True)),
                ('endLatitude', models.CharField(default=None, max_length=30, null=True)),
                ('poolLength', models.CharField(default=None, max_length=30, null=True)),
                ('avgDoubleCadence', models.CharField(default=None, max_length=30, null=True)),
                ('lactateThresholdBpm', models.CharField(default=None, max_length=30, null=True)),
                ('avgWindYawAngle', models.CharField(default=None, max_length=30, null=True)),
                ('minTemperature', models.CharField(default=None, max_length=30, null=True)),
                ('deviceId', models.CharField(default=None, max_length=30, null=True)),
                ('activityLikeAuthors', models.CharField(default=None, max_length=100, null=True)),
                ('diveNumber', models.CharField(default=None, max_length=100, null=True)),
                ('averageBikingCadenceInRevPerMinute', models.CharField(default=None, max_length=30, null=True)),
                ('ownerProfilePk', models.CharField(default=None, max_length=30, null=True)),
                ('rightBalance', models.CharField(default=None, max_length=30, null=True)),
                ('normPower', models.CharField(default=None, max_length=30, null=True)),
                ('averageSwolf', models.CharField(default=None, max_length=30, null=True)),
                ('maxCda', models.CharField(default=None, max_length=30, null=True)),
                ('requestorRelationship', models.CharField(default=None, max_length=30, null=True)),
                ('avgVerticalOscillation', models.CharField(default=None, max_length=30, null=True)),
                ('conversationUuid', models.CharField(default=None, max_length=30, null=True)),
                ('conversationPk', models.CharField(default=None, max_length=30, null=True)),
                ('avgWattsPerCda', models.CharField(default=None, max_length=30, null=True)),
                ('surfaceInterval', models.CharField(default=None, max_length=100, null=True)),
                ('locationName', models.CharField(default=None, max_length=200, null=True)),
                ('ownerDisplayName', models.CharField(default=None, max_length=50, null=True)),
                ('ownerProfileImageUrlMedium', models.CharField(default=None, max_length=200, null=True)),
                ('avgStrokes', models.CharField(default=None, max_length=30, null=True)),
                ('numberOfActivityLikes', models.CharField(default=None, max_length=30, null=True)),
                ('endN2', models.CharField(default=None, max_length=30, null=True)),
                ('avgPower', models.CharField(default=None, max_length=30, null=True)),
                ('videoUrl', models.CharField(default=None, max_length=200, null=True)),
                ('maxAirSpeed', models.CharField(default=None, max_length=30, null=True)),
                ('avgAirSpeed', models.CharField(default=None, max_length=30, null=True)),
                ('maxHR', models.CharField(default=None, max_length=30, null=True)),
                ('maxFtp', models.CharField(default=None, max_length=30, null=True)),
                ('averageRunningCadenceInStepsPerMinute', models.CharField(default=None, max_length=30, null=True)),
                ('avgVerticalRatio', models.CharField(default=None, max_length=30, null=True)),
                ('avgCda', models.CharField(default=None, max_length=30, null=True)),
                ('bottomTime', models.CharField(default=None, max_length=30, null=True)),
                ('minStrokes', models.CharField(default=None, max_length=30, null=True)),
                ('endLongitude', models.CharField(default=None, max_length=30, null=True)),
                ('ownerProfileImageUrlLarge', models.CharField(default=None, max_length=200, null=True)),
                ('maxRunningCadenceInStepsPerMinute', models.CharField(default=None, max_length=30, null=True)),
                ('comments', models.CharField(default=None, max_length=200, null=True)),
                ('activityLikeDisplayNames', models.CharField(default=None, max_length=100, null=True)),
                ('minAirSpeed', models.CharField(default=None, max_length=30, null=True)),
                ('activityType', models.CharField(default=None, max_length=30, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('userId', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('displayName', models.CharField(default=None, max_length=40)),
                ('fullName', models.CharField(default=None, max_length=40)),
                ('location', models.CharField(default='', max_length=100, null=True)),
                ('profileImageUrlMedium', models.CharField(default=None, max_length=200, null=True)),
                ('profileImageUrlSmall', models.CharField(default=None, max_length=200, null=True)),
                ('connectionRequestId', models.CharField(default=None, max_length=30)),
            ],
        ),
        migrations.AddField(
            model_name='activities',
            name='userId',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='activrating.Users'),
        ),
    ]
