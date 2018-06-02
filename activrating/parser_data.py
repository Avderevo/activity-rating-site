#!/usr/bin/env python3


import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Activity_rating_site.settings')
django.setup()

from activrating.models import Users, Activities
from grab import Grab

url_login = 'https://sso.garmin.com/sso/login?service=https%3A%2F%2Fconnect.garmin.com%2Fmodern%2F&webhost=https%3A%2F%2Fconnect.garmin.com&source=https%3A%2F%2Fconnect.garmin.com%2Fru-RU%2Fsignin&redirectAfterAccountLoginUrl=https%3A%2F%2Fconnect.garmin.com%2Fmodern%2F&redirectAfterAccountCreationUrl=https%3A%2F%2Fconnect.garmin.com%2Fmodern%2F&gauthHost=https%3A%2F%2Fsso.garmin.com%2Fsso&locale=en_US&id=gauth-widget&cssUrl=https%3A%2F%2Fstatic.garmincdn.com%2Fcom.garmin.connect%2Fui%2Fcss%2Fgauth-custom-v1.2-min.css&privacyStatementUrl=%2F%2Fconnect.garmin.com%2Fru-RU%2Fprivacy%2F&clientId=GarminConnect&rememberMeShown=true&rememberMeChecked=false&createAccountShown=true&openCreateAccount=false&displayNameShown=false&consumeServiceTicket=false&initialFocus=true&embedWidget=false&generateExtraServiceTicket=false&generateNoServiceTicket=false&globalOptInShown=true&globalOptInChecked=false&mobile=false&connectLegalTerms=true&locationPromptShown=true'
url_activities = 'https://connect.garmin.com/proxy/activitylist-service/activities/'
# лимит загрузок активностей для каждого пользователя
limitt = '?start=1&limit=40'
# Тут должны быть ваши логин и пароль для входа в гармин-аккаунт
user_log = {'username': 'username', 'password': 'password'}
social_url = 'https://connect.garmin.com/modern/proxy/userprofile-service/socialProfile/connections'
cookie_path = 'cookiefile'

Cf = open(cookie_path, 'w')
Cf.close()
g = Grab()


def login_garmin():
    g.setup(url=url_login, post=user_log)
    rec = g.request(cookiefile=cookie_path)
    print(rec.code)


def grab_users():
    users_file = g.go(url=social_url, cookiefile=cookie_path)
    userprof = users_file.json
    userprof = userprof['userConnections']
    for i in range(len(userprof)):
        if Users.objects.filter(userId=userprof[i]['userId']):
            continue
        else:
            Users.objects.create(userId=userprof[i]['userId'],
                              displayName=userprof[i]['displayName'],
                              fullName=userprof[i]['fullName'],
                              location=userprof[i]['location'],
                              profileImageUrlMedium=userprof[i]['profileImageUrlMedium'],
                              profileImageUrlSmall=userprof[i]['profileImageUrlSmall'],
                              connectionRequestId=userprof[i]['connectionRequestId'])


def garb_activiti():
    names = Users.objects.values_list('displayName', flat=True)
    for n in range(len(names)):
        activities=g.go(url=url_activities+names[n]+limitt, cookiefile=cookie_path )
        activities=activities.json
        act = activities["activityList"]
        for i in range(len(act)):
            if Activities.objects.filter(activityId=act[i]['activityId']):
                continue
            else:
                Activities.objects.create(activityId = act[i]['activityId'],
                                          maxFractionalCadence = act[i]['maxFractionalCadence'],
                                          activityType=act[i]['activityType']['typeId'],
                                          avgGroundContactBalance = act[i]['maxFractionalCadence'],
                                          avgStrokeCadence = act[i]['avgStrokeCadence'],
                                          steps = act[i]['steps'],
                                          elapsedDuration = act[i]['elapsedDuration'],
                                          lapCount = act[i]['lapCount'],
                                          maxElevation =act[i]['maxElevation'],
                                          leftBalance = act[i]['leftBalance'],
                                          minElevation = act[i]['minElevation'],
                                          timeZoneId = act[i]['timeZoneId'],
                                          maxSwimCadenceInStrokesPerMinute = act[i]['maxSwimCadenceInStrokesPerMinute'],
                                          calories = act[i]['calories'],
                                          courseId = act[i]['courseId'],
                                          numberOfActivityComments = act[i]['numberOfActivityComments'],
                                          maxDoubleCadence = act[i]['maxDoubleCadence'],
                                          parentId = act[i]['parentId'],
                                          distance = act[i]['distance'],
                                          commentedByUser = act[i]['commentedByUser'],
                                          activityLikeFullNames = act[i]['activityLikeFullNames'],
                                          avgStrokeDistance = act[i]['avgStrokeDistance'],
                                          decoDive = act[i]['decoDive'],
                                          duration = act[i]['duration'],
                                          avgGroundContactTime = act[i]['avgGroundContactTime'],
                                          aerobicTrainingEffect = act[i]['aerobicTrainingEffect'],
                                          ownerFullName = act[i]['ownerFullName'],
                                          averageSwimCadenceInStrokesPerMinute = act[i]['averageSwimCadenceInStrokesPerMinute'],
                                          startN2 = act[i]['startN2'],
                                          startTimeLocal =act[i]['startTimeLocal'],
                                          description = act[i]['description'],
                                          maxTemperature = act[i]['maxTemperature'],
                                          maxVerticalSpeed = act[i]['maxVerticalSpeed'],
                                          elevationLoss = act[i]['elevationLoss'],
                                          endCns = act[i]['endCns'],
                                          startCns = act[i]['startCns'],
                                          activityName = act[i]['activityName'],
                                          likedByUser = act[i]['likedByUser'],
                                          activeLengths = act[i]['activeLengths'],
                                          lactateThresholdSpeed = act[i]['lactateThresholdSpeed'],
                                          maxSpeed = act[i]['maxSpeed'],
                                          maxBikingCadenceInRevPerMinute = act[i]['maxBikingCadenceInRevPerMinute'],
                                          trainingStressScore = act[i]['trainingStressScore'],
                                          strokes =act[i]['strokes'],
                                          floorsClimbed = act[i]['floorsClimbed'],
                                          avgStrideLength = act[i]['avgStrideLength'],
                                          workoutId = act[i]['workoutId'],
                                          avgVerticalSpeed = act[i]['avgVerticalSpeed'],
                                          elevationGain = act[i]['elevationGain'],
                                          maxDepth = act[i]['maxDepth'],
                                          avgLeftBalance = act[i]['avgLeftBalance'],
                                          ownerId = act[i]['ownerId'],
                                          anaerobicTrainingEffect = act[i]['anaerobicTrainingEffect'],
                                          movingDuration = act[i]['movingDuration'],
                                          avgFractionalCadence = act[i]['avgFractionalCadence'],
                                          floorsDescended = act[i]['floorsDescended'],
                                          intensityFactor = act[i]['intensityFactor'],
                                          startLatitude = act[i]['startLatitude'],
                                          sportTypeId = act[i]['sportTypeId'],
                                          beginTimestamp = act[i]['beginTimestamp'],
                                          maxPower = act[i]['maxPower'],
                                          minCda = act[i]['minCda'],
                                          averageSpeed = act[i]['averageSpeed'],
                                          vO2MaxValue = act[i]['vO2MaxValue'],
                                          averageHR = act[i]['averageHR'],
                                          endLatitude = act[i]['endLatitude'],
                                          poolLength = act[i]['poolLength'],
                                          avgDoubleCadence = act[i]['avgDoubleCadence'],
                                          lactateThresholdBpm = act[i]['lactateThresholdBpm'],
                                          avgWindYawAngle = act[i]['avgWindYawAngle'],
                                          minTemperature = act[i]['minTemperature'],
                                          deviceId = act[i]['deviceId'],
                                          activityLikeAuthors = act[i]['activityLikeAuthors'],
                                          diveNumber = act[i]['diveNumber'],
                                          averageBikingCadenceInRevPerMinute = act[i]['averageBikingCadenceInRevPerMinute'],
                                          ownerProfilePk = act[i]['ownerProfilePk'],
                                          rightBalance = act[i]['rightBalance'],
                                          normPower = act[i]['normPower'],
                                          averageSwolf = act[i]['averageSwolf'],
                                          maxCda = act[i]['maxCda'],
                                          requestorRelationship = act[i]['requestorRelationship'],
                                          avgVerticalOscillation = act[i]['avgVerticalOscillation'],
                                          conversationUuid = act[i]['conversationUuid'],
                                          conversationPk = act[i]['conversationPk'],
                                          avgWattsPerCda = act[i]['avgWattsPerCda'],
                                          surfaceInterval = act[i]['surfaceInterval'],
                                          locationName = act[i]['locationName'],
                                          ownerDisplayName = act[i]['ownerDisplayName'],
                                          ownerProfileImageUrlMedium = act[i]['ownerProfileImageUrlMedium'],
                                          avgStrokes = act[i]['avgStrokes'],
                                          numberOfActivityLikes = act[i]['numberOfActivityLikes'],
                                          endN2 = act[i]['endN2'],
                                          avgPower = act[i]['avgPower'],
                                          videoUrl = act[i]['videoUrl'],
                                          maxAirSpeed = act[i]['maxAirSpeed'],
                                          avgAirSpeed = act[i]['avgAirSpeed'],
                                          maxHR = act[i]['maxHR'],
                                          maxFtp = act[i]['maxFtp'],
                                          averageRunningCadenceInStepsPerMinute = act[i]['averageRunningCadenceInStepsPerMinute'],
                                          avgVerticalRatio = act[i]['avgVerticalRatio'],
                                          avgCda = act[i]['avgCda'],
                                          bottomTime = act[i]['bottomTime'],
                                          minStrokes = act[i]['minStrokes'],
                                          endLongitude = act[i]['endLongitude'],
                                          ownerProfileImageUrlLarge = act[i]['ownerProfileImageUrlLarge'],
                                          maxRunningCadenceInStepsPerMinute = act[i]['maxRunningCadenceInStepsPerMinute'],
                                          comments = act[i]['comments'],
                                          activityLikeDisplayNames = act[i]['activityLikeDisplayNames'],
                                          minAirSpeed = act[i]['minAirSpeed'])


if __name__ == '__main__':
    login_garmin()
    grab_users()
    garb_activiti()
