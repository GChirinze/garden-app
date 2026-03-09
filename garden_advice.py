# Gardening tips app for gardener

def get_season(month):
    # TODO: Create a function to determine season based on month
    # Currently hardcoded - should be improved
    if month in [12, 1, 2]:
        return "Winter"
    elif month in [3, 4, 5]:
        return "Spring"
    elif month in [6, 7, 8]:
        return "Summer"
    elif month in [9, 10, 11]:
        return "Autumn"
    else:
        return "Unknown"

def get_gardening_tips(season):
    # TODO: Replace hardcoded values with a data structure (dictionary)
    # TODO: Add more comprehensive tips for each season
    if season == "Spring":
        return "Plant new seeds, prepare soil, start composting"
    elif season == "Summer":
        return "Water regularly, mulch plants, harvest vegetables"
    elif season == "Autumn":
        return "Clean up leaves, plant bulbs, protect sensitive plants"
    elif season == "Winter":
        return "Plan garden layout, maintain tools, start seeds indoors"
    else:
        return "No tips available for this season"

def main():
    # TODO: Add docstring documentation for this function
    # TODO: Add input validation for month
    month = int(input("Enter the month (1-12): "))
    
    # TODO: Create a function to display tips in a formatted way
    season = get_season(month)
    tips = get_gardening_tips(season)
    
    print(f"\nCurrent season: {season}")
    print(f"Gardening tips: {tips}")
    
    # TODO: Add feature to get tips for multiple months
    # TODO: Add error handling for invalid inputs

if __name__ == "__main__":
    main()



















