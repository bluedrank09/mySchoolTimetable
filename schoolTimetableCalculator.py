import calendar
from datetime import datetime
from datetime import timedelta

def yearsInAList():
    years = range(2020,2021)
    return(years)

def monthsIndexList():
    monthsIndex = range(0,12)
    return(monthsIndex)
    

if __name__ == "__main__":
    try:
        yearsForLoop = yearsInAList()
        monthIndex = monthsIndexList()

        months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
        
        termStartAndEndDates = ['02-01','04-04','04-15','07-03','07-20','09-25','10-12','12-04']
        
        termDates=[]
        for date in termStartAndEndDates: 
            tempDates=datetime.strptime(date,'%m-%d')
            termDates.append(tempDates)
        print(f"{termDates}")

       

        for yr in yearsForLoop:
            for mn in monthIndex: 
                weekList = [calendar.monthcalendar(yr,mn+1)]
                for dayList in weekList:
                    for week in dayList:
                        for seperateDay in week:
                            if seperateDay != 0:
                                theGeneratedDate = datetime.strptime(f"{mn+1}-{seperateDay}", '%m-%d')
                                if theGeneratedDate >=termDates[4] and theGeneratedDate <= termDates[5]:
                                    print(f"{seperateDay} - {months[mn]} - {yr}")


    except Exception as e:
        print(f"Something went wrong, specifically ", e)
    finally:
        print(f"No I'm Ramona")