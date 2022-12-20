def add_time(startTime, duration, startDay=None):
    days = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
    stHrs = int(startTime.split(':')[0])
    stMin = int((startTime.split(':')[1]).split(' ')[0])
    am_pm1 = (startTime.split(':')[1]).split(' ')[1]
    addHrs = int(duration.split(':')[0])
    addMin = int(duration.split(':')[1])
    #print(stHrs, stMin,addHrs,addMin, am_pm1)
    newMin = stMin+addMin
    ext,ndays = 0,0
    if newMin>=60:
        ext = newMin//60
        newMin = newMin%60
    #print(newMin,ext)
    newHrs  = stHrs+addHrs+ext
    am_pm = am_pm1
    if newHrs>=24:
        ndays+=(newHrs)//24
        newHrs %= 24
    if newHrs>=12:
        am_pm = 'AM' if am_pm1=='PM' else 'PM'
        newHrs=newHrs-12 if newHrs>12 else newHrs
    if am_pm == 'AM' and am_pm1=='PM':
        ndays+=1
    time = str(newHrs)+':'+str(newMin).rjust(2,'0')+' '+am_pm
    if startDay==None:
        if ndays==0:
            return time    
        time+=' (next day)' if ndays==1 else ' (%s days later)'%str(ndays)
    else:
        startDay = (startDay.lower()).capitalize()
        day = days[(days.index(startDay)+ndays)%7]
        time+= ', '+day
        if ndays==0:
            return time
        time+=' (next day)' if ndays==1 else ' (%s days later)'%str(ndays)
    #print(newHrs, am_pm,time, sep='\n')
    return time