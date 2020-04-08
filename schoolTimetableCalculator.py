import calendar
from datetime import datetime

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
        
        termTwoStartStr = '2020-04-15'
        termTwoEndStr = '2020-07-03'
        termThreeStartStr = '2020-07-20'
        termThreeEndStr = '2020-09-25'
        termFourStartStr = '2020-10-12'
        termFourEndStr ='2020-12-04'

        termTwoStartDate = datetime.strptime(termTwoStartStr, '%Y-%m-%d')
        termTwoEndDate = datetime.strptime(termTwoEndStr, '%Y-%m-%d')
        termThreeStartDate = datetime.strptime(termThreeStartStr, '%Y-%m-%d')
        termThreeEndDate = datetime.strptime(termThreeEndStr, '%Y-%m-%d')
        termFourStartDate = datetime.strptime(termFourStartStr, '%Y-%m-%d')
        termFourEndDate = datetime.strptime(termFourEndStr, '%Y-%m-%d')

        

        for yr in yearsForLoop:
            for mn in monthIndex: 
                weekList = [calendar.monthcalendar(yr,mn+1)]
                for dayList in weekList:
                    for week in dayList:
                        for seperateDay in week:
                            if seperateDay != 0:
                                theGeneratedDate = datetime.strptime(f"{seperateDay} - {mn+1} - {yr}", '%d - %m - %Y')
                                if ( (theGeneratedDate >= termTwoStartDate and theGeneratedDate <= termTwoEndDate) or 
                                     (theGeneratedDate >= termThreeStartDate and theGeneratedDate <= termThreeEndDate) or 
                                     (theGeneratedDate >= termFourStartDate and theGeneratedDate <= termFourEndDate)):
                                    print(f"{seperateDay} - {months[mn]} - {yr}")


    except Exception as e:
        print(f"Something went wrong, specifically ", e)
    finally:
        print(f"No I'm Ramona")