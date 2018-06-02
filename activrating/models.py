from django.db import models


from pexpect import searcher_re



class Users(models.Model):
    userId = models.CharField(max_length=20, primary_key=True)
    displayName = models.CharField(max_length=40,default=None)
    fullName = models.CharField(max_length=40,default=None)
    location = models.CharField(max_length=100,default='', null = True)
    profileImageUrlMedium =models.CharField(max_length=200,default=None, null = True)
    profileImageUrlSmall = models.CharField(max_length=200, default=None, null = True)
    connectionRequestId = models.CharField(max_length=30, default=None)
    def __str__(self):
        return  "%s, %s, %s" % (self.displayName, self.location, self.fullName)


class Activities(models.Model):
    activityId = models.CharField(max_length=20, primary_key=True)
    maxFractionalCadence = models.CharField(max_length=30,default=None, null = True)
    avgGroundContactBalance = models.CharField(max_length=30, default=None, null = True)
    avgStrokeCadence = models.CharField(max_length=30, default=None, null = True)
    steps = models.CharField(max_length=30, default=None, null = True)
    elapsedDuration = models.CharField(max_length=30, default=None, null = True)
    lapCount = models.CharField(max_length=30, default=None, null = True)
    maxElevation = models.CharField(max_length=30, default=None, null = True)
    leftBalance = models.CharField(max_length=30, default=None, null = True)
    minElevation = models.CharField(max_length=30, default=None, null = True)
    timeZoneId = models.CharField( max_length=20, default=None )
    maxSwimCadenceInStrokesPerMinute = models.CharField(max_length=30, default=None, null = True)
    calories = models.CharField(max_length=30, default=None, null = True)
    courseId = models.CharField(max_length=30, default=None, null = True)
    maxStrokeCadence = models.CharField(max_length=30,default=None, null = True)
    numberOfActivityComments = models.CharField(max_length=30, default=None, null = True)
    maxDoubleCadence = models.CharField(max_length=30, default=None, null = True)
    parentId = models.CharField(max_length=30, default=None, null = True)
    distance = models.CharField(max_length=30, default=None, null = True)
    commentedByUser = models.CharField(max_length=300, default=None, null = True)
    activityLikeFullNames = models.CharField(max_length=100, default=None, null = True)
    avgStrokeDistance = models.CharField(max_length=30, default=None, null = True)
    decoDive = models.CharField(max_length=30, default=None, null = True)
    duration = models.CharField(max_length=50, default=None, null = True)
    avgGroundContactTime = models.CharField(max_length=30, default=None, null = True)
    aerobicTrainingEffect = models.CharField(max_length=30, default=None, null = True)
    ownerFullName = models.CharField(max_length=100, default=None, null = True)
    averageSwimCadenceInStrokesPerMinute = models.CharField(max_length=30, default=None, null = True)
    startN2 = models.CharField(max_length=30,default=None, null = True)
    startTimeLocal = models.DateTimeField(auto_now=False, auto_now_add=False, null = True)
    description = models.CharField(max_length=30, default=None, null = True)
    maxTemperature = models.CharField(max_length=30, default=None, null = True)
    maxVerticalSpeed = models.CharField(max_length=30, default=None, null = True)
    elevationLoss = models.CharField(max_length=30, default=None, null = True)
    endCns = models.CharField(max_length=100, default=None, null = True)
    startCns = models.CharField(max_length=100, default=None, null = True)
    activityName = models.CharField(max_length=100, default=None, null = True)
    likedByUser = models.CharField(max_length=100, default=None, null = True)
    activeLengths = models.CharField(max_length=100, default=None, null = True)
    lactateThresholdSpeed = models.CharField(max_length=30, default=None, null = True)
    maxSpeed = models.CharField(max_length=30, default=None, null = True)
    maxBikingCadenceInRevPerMinute = models.CharField(max_length=30, default=None, null = True)
    trainingStressScore = models.CharField(max_length=30,default=None, null = True)
    strokes = models.CharField(max_length=100, default=None, null = True)
    floorsClimbed = models.CharField(max_length=100, default=None, null = True)
    avgStrideLength = models.CharField(max_length=100,default=None, null = True )
    workoutId = models.CharField(max_length=30, default=None, null = True)
    avgVerticalSpeed = models.CharField(max_length=30,default=None, null = True)
    elevationGain = models.CharField(max_length=30,default=None, null = True)
    maxDepth = models.CharField(max_length=30,default=None, null = True)
    avgLeftBalance = models.CharField(max_length=30,default=None, null = True)
    userId = models.ForeignKey('Users', on_delete=models.CASCADE, null = True )
    ownerId = models.CharField(max_length=30,default=None)
    anaerobicTrainingEffect = models.CharField(max_length=30,default=None, null = True)
    movingDuration = models.CharField(max_length=30,default=None, null = True)
    avgFractionalCadence = models.CharField(max_length=30, default=None, null = True)
    floorsDescended = models.CharField(max_length=100, default=None, null = True)
    intensityFactor = models.CharField(max_length=100, default=None, null = True)
    startLatitude = models.CharField(max_length=30,default=None, null = True)
    sportTypeId = models.CharField(max_length=30,default=None, null = True)
    beginTimestamp = models.CharField(max_length=30,default=None, null = True)
    maxPower = models.CharField(max_length=30,default=None, null = True)
    minCda = models.CharField(max_length=30,default=None, null = True)
    averageSpeed = models.CharField(max_length=30,default=None, null = True)
    vO2MaxValue = models.CharField(max_length=30,default=None, null = True)
    averageHR = models.CharField(max_length=30,default=None, null = True)
    endLatitude = models.CharField(max_length=30,default=None, null = True)
    poolLength = models.CharField(max_length=30,default=None, null = True)
    avgDoubleCadence = models.CharField(max_length=30,default=None, null = True)
    lactateThresholdBpm = models.CharField(max_length=30,default=None, null = True)
    avgWindYawAngle = models.CharField(max_length=30,default=None, null = True)
    minTemperature = models.CharField(max_length=30,default=None, null = True)
    deviceId = models.CharField(max_length=30,default=None, null = True)
    activityLikeAuthors = models.CharField(max_length=100, default=None, null = True)
    diveNumber = models.CharField(max_length=100, default=None, null = True)
    averageBikingCadenceInRevPerMinute = models.CharField(max_length=30,default=None, null = True)
    ownerProfilePk = models.CharField(max_length=30,default=None, null = True)
    rightBalance = models.CharField(max_length=30,default=None, null = True)
    normPower = models.CharField(max_length=30,default=None, null = True)
    averageSwolf = models.CharField(max_length=30,default=None, null = True)
    maxCda = models.CharField(max_length=30,default=None, null = True)
    requestorRelationship = models.CharField(max_length=30,default=None, null = True)
    avgVerticalOscillation = models.CharField(max_length=30,default=None, null = True)
    conversationUuid = models.CharField(max_length=30,default=None, null = True)
    conversationPk = models.CharField(max_length=30,default=None, null = True)
    avgWattsPerCda = models.CharField(max_length=30,default=None, null = True)
    surfaceInterval = models.CharField(max_length=100, default=None, null = True)
    locationName = models.CharField(max_length=200, default=None, null = True)
    ownerDisplayName = models.CharField(max_length=50, default=None, null = True)
    ownerProfileImageUrlMedium = models.CharField(max_length=200, default=None, null = True)
    avgStrokes = models.CharField(max_length=30,default=None, null = True)
    numberOfActivityLikes = models.CharField(max_length=30,default=None, null = True)
    endN2 = models.CharField(max_length=30,default=None, null = True)
    avgPower = models.CharField(max_length=30,default=None, null = True)
    videoUrl = models.CharField(max_length=200, default=None, null = True)
    maxAirSpeed = models.CharField(max_length=30,default=None, null = True)
    avgAirSpeed = models.CharField(max_length=30,default=None, null = True)
    maxHR = models.CharField(max_length=30,default=None, null = True)
    maxFtp = models.CharField(max_length=30,default=None, null = True)
    averageRunningCadenceInStepsPerMinute = models.CharField(max_length=30,default=None, null = True)
    avgVerticalRatio = models.CharField(max_length=30,default=None, null = True)
    avgCda = models.CharField(max_length=30,default=None, null = True)
    bottomTime = models.CharField(max_length=30,default=None, null = True)
    minStrokes = models.CharField(max_length=30,default=None, null = True)
    endLongitude = models.CharField(max_length=30,default=None, null = True)
    ownerProfileImageUrlLarge = models.CharField(max_length=200, default=None, null = True)
    maxRunningCadenceInStepsPerMinute = models.CharField(max_length=30,default=None, null = True)
    comments = models.CharField(max_length=200, default=None, null = True)
    activityLikeDisplayNames = models.CharField(max_length=100, default=None, null = True)
    minAirSpeed = models.CharField(max_length=30,default=None, null = True)
    activityType = models.CharField(max_length=30,default=None, null = True)
    def __str__(self):
        return "%s, %s, " % (self.ownerFullName, self.distance)

