def yearsInAList():
    years = range(2020,2025)
    return(years)

def monthsInAList():
    months = range(1,13)
    return(months)

if __name__ == "__main__":
    try:
        yearsForLoop = yearsInAList()
        monthsForLoop = monthsInAList()
        
        for yr in yearsForLoop:
            for mn in monthsForLoop: 
                print(f"{mn} - {yr}")

    except:
        pass
    finally:
        print(f"No I'm Ramona")