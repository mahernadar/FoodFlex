import re

import numpy as np
from rich import inspect

# the following extract the numbers with the units;
# most of the attributes have 2 values (value + % daily value);
# Percent Daily Values are based on a 2,000 calorie diet!
# the parsing includes 1,000 and 1000 parsing
PARSING_ITEMS = {
    "servings": r"(?<=Servings Per Recipe )(\d+(,\d+)*)",
    "calories": r"(?<=Calories )(\d+(,\d+)*)",
    "total_fat": r"(?<=Total Fat )(\d+(,\d+)*g )(\d+(,\d+)*%)",
    "saturated_fat": r"(?<=Saturated Fat )(\d+(,\d+)*g )(\d+(,\d+)*%)",
    "sodium": r"(?<=Sodium )(\d+(,\d+)*mg )(\d+(,\d+)*%)",
    "cholesterol": r"(?<=Cholesterol )(\d+(,\d+)*mg )(\d+(,\d+)*%)",
    "total_carbs": r"(?<=Total Carbohydrate )(\d+(,\d+)*g )(\d+(,\d+)*%)",
    "dietary_fiber": r"(?<=Dietary Fiber )(\d+(,\d+)*g )(\d+(,\d+)*%)",
    "total_sugars": r"(?<=Total Sugars )(\d+(,\d+)*g)",
    "protein": r"(?<=Protein )(\d+(,\d+)*g)",
    "vitamin_c": r"(?<=Vitamin C )(\d+(,\d+)*mg )(\d+(,\d+)*%)",
    "calcium": r"(?<=Calcium )(\d+(,\d+)*mg )(\d+(,\d+)*%)",
    "iron": r"(?<=Iron )(\d+(,\d+)*mg )(\d+(,\d+)*%)",
    "potassium": r"(?<=Potassium )(\d+(,\d+)*mg )(\d+(,\d+)*%)",
}


def nutrition_facts_parser(unstructured_nutrition_facts: str) -> dict:
    """_summary_

    Args:
        unstructured_nutrition_facts (str): _description_

    Returns:
        dict: _description_
    """
    structured_nutrition_dict = {}
    for nutrient, nutrient_regex in PARSING_ITEMS.items():
        match = re.search(nutrient_regex, unstructured_nutrition_facts)
        if match:
            split_match = match.group().strip().split(" ")
            # print(nutrient, split_match)
            if len(split_match) == 1:

                single_split_match = split_match[0].split('g')
                value = single_split_match[0]
                if len(single_split_match) > 1:
                
                    structured_nutrition_dict[f"{nutrient}_g"] = int(
                        value.replace(',', '')
                    )
                else:
                    structured_nutrition_dict[nutrient] = int(
                        value.replace(',', '')
                    )

            # adding the value and percentage daily value (assuming 2k calories):
            elif len(split_match) == 2:
                # separate value from unit:
                (value, _, value_unit) = re.match(
                    r"(\d+(,\d+)*)([a-z]+)", split_match[0], re.I
                ).groups()
                # get percentage value
                prct_daily_value = int(
                    re.match(r"(\d+(,\d+)*)", split_match[1], re.I).groups()[0].replace(',', '')
                )

                # add the nutrient value with its unit to the dict:
                structured_nutrition_dict[f"{nutrient}_{value_unit}"] = int(
                    value.replace(',', '')
                )
                structured_nutrition_dict[
                    f"{nutrient}_prct_daily"
                ] = prct_daily_value

    return structured_nutrition_dict


if __name__ == "__main__":
    # example text obtained via scraping:
    text = "Nutrition Facts\nServings Per Recipe 16\nCalories 80\n% Daily Value *\nTotal Fat 4g 6%\nSaturated Fat 2g 11%\nCholesterol 148mg 49%\nSodium 114mg 5%\nTotal Carbohydrate 2g 1%\nDietary Fiber 0g 1%\nTotal Sugars 1g\nProtein 6g\nVitamin C 6mg 29%\nCalcium 12mg 1%\nIron 2mg 13%\nPotassium 76mg 2%\n* Percent Daily Values are based on a 2,000 calorie diet. Your daily values may be higher or lower depending on your calorie needs.\n** Nutrient information is not available for all ingredients. Amount is based on available nutrient data.\n(-) Information is not currently available for this nutrient. If you are following a medically restrictive diet, please consult your doctor or registered dietitian before preparing this recipe for personal consumption.\nPowered by the ESHA Research Database © 2018, ESHA Research, Inc. All Rights Reserved"

    print(nutrition_facts_parser(unstructured_nutrition_facts=text))
