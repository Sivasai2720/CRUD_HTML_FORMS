from django.shortcuts import render

# Create your views here.
from app.models import *
def insert_objects_topic(request):
    if request.method=='POST':
        tn=request.POST['tn']
        TO=Topic.objects.get_or_create(topic_name=tn)[0]
        TO.save()
        QLTO=Topic.objects.filter(topic_name='').delete()
        QLTO=Topic.objects.all()
        d={'topics':QLTO}
        return render(request,'display_topic.html',d)
    return render(request,'insert_objects_topic.html')

def insert_objects_webpage(request):
    QLTO=Topic.objects.all()
    d={'topics':QLTO}
    if request.method=='POST':
        tn=request.POST['tn']
        na=request.POST['na']
        ma=request.POST['ma']
        ur=request.POST['ur']
        em=request.POST['em']
        TO=Topic.objects.get(topic_name=tn)
        wo=Webpage.objects.get_or_create(topic_name=TO,name=na,matches_win=ma,url=ur,email=em)[0]
        wo.save()
        QLWO=Webpage.objects.all()
        d1={'webpages':QLWO}
        return render(request,'dispaly_webpages.html',d1)
    return render(request,'insert_objects_webpage.html',d)



#This select_multiple_topic written for drop down method
def select_multiple_topics(request):  #by using drop down we are selecting multiple topic names
    QLTO=Topic.objects.all()
    d={'topics':QLTO}

    if request.method=='POST':
        topiclist=request.POST.getlist('tn')#getlist will used for store the topic_names in the list that u r selected like [cricket,vallyball,raby....],
        QLWO=Webpage.objects.none()#none method --- creates a empty Queryset, like in python sum=0 or L=[],or s='' or add=0

        for i in topiclist:
            QLWO=QLWO|Webpage.objects.filter(topic_name=i)# | pipe that will concating Ex:from topic_name coming cricket that will be in check in webpage if it is there means it will display
            #print(tn) #it will be show on cmd in the form of list -->[cricket,vallyball,raby....]
        d1={'webpages':QLWO}
        return render(request,'dispaly_webpages.html',d1)
    return render(request,'select_multiple_topics.html',d)


#This for checkbox for selecting multiple options in topic_name
def checkbox(request):
    QLTO=Topic.objects.all()
    d={'topics':QLTO}


    return render(request,'checkbox.html',d)
