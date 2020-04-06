def yearsInAList():
    years = range(2020,2025)
    return(years)

def monthsIndexList():
    monthsIndex = range(0,12)
    return(monthsIndex )
    

if __name__ == "__main__":
    try:
        yearsForLoop = yearsInAList()
        monthIndex = monthsIndexList()

        months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
        
        for yr in yearsForLoop:
            for mn in monthIndex: 
                print(f"{months[mn]} - {yr}")

    except:
        pass
    finally:
        print(f"No I'm Ramona")