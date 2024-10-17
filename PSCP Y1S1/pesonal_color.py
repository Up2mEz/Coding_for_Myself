

import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib.patheffects as pe

def verify_undertone():
    print("Let's determine your skin undertone.")
    print("Answer the following questions:")

    # Ask questions to determine skin undertone
    valid_veins = {"blue", "purple", "green", "both"}
    valid_jewelry = {"silver", "gold", "both"}
    valid_sun = {"burns", "tans"}

    veins = input("1. What color are the veins on your wrist? (blue/purple, green, or both): ").lower()
    while veins not in valid_veins:
        veins = input("Please enter a valid vein color (blue/purple, green, or both): ").lower()

    jewelry = input("2. Which jewelry suits you better? (silver, gold, or both): ").lower()
    while jewelry not in valid_jewelry:
        jewelry = input("Please enter a valid jewelry preference (silver, gold, or both): ").lower()

    sun_reaction = input("3. How does your skin react to the sun? (burns or tans): ").lower()
    while sun_reaction not in valid_sun:
        sun_reaction = input("Please enter a valid sun reaction (burns or tans): ").lower()

    # Determine vein tone, jewelry tone, and sun reaction tone
    vein_tone = "cool" if veins in ["blue", "purple"] else "warm" if veins == "green" else "neutral"
    jew_tone = "cool" if jewelry == "silver" else "warm" if jewelry == "gold" else "neutral"
    sun_tone = "cool" if sun_reaction == "burns" else "warm"

    # Count tones to determine overall undertone
    tone_counts = {"cool": 0, "warm": 0, "neutral": 0}
    tone_counts[vein_tone] += 1
    tone_counts[jew_tone] += 1
    tone_counts[sun_tone] += 1
    
    undertone = max(tone_counts, key=tone_counts.get)
    
    print(f"Your undertone is likely {undertone}.")
    return undertone

def determine_season_by_undertone(undertone):
    # Determine possible seasons based on undertone
    if undertone == "warm":
        possible_seasons = ["Spring", "Autumn"]
    elif undertone == "cool":
        possible_seasons = ["Summer", "Winter"]
    else:  # Neutral undertone
        possible_seasons = ["Spring", "Summer", "Autumn", "Winter"]
    return possible_seasons

def determine_season(face_dimension, eye_color, personality, possible_seasons):
    # Determine season based on face dimension
    face_season = None
    if face_dimension.lower() == "less defined face" and len(possible_seasons) == 2:
        face_season = possible_seasons[0]
    elif face_dimension.lower() == "defined face" and len(possible_seasons) == 2:
        face_season = possible_seasons[1]

    # Determine season based on eye color
    eye_season = None
    if eye_color.lower() == "light brown" and "Spring" in possible_seasons:
        eye_season = "Spring"
    elif eye_color.lower() == "dark brown" and "Autumn" in possible_seasons:
        eye_season = "Autumn"
    elif eye_color.lower() in ["reddish", "dark"] and "Summer" in possible_seasons:
        eye_season = "Summer"
    elif eye_color.lower() == "deep black" and "Winter" in possible_seasons:
        eye_season = "Winter"

    # Determine season based on personality
    personality_season = None
    if personality.lower() == "cheerful" and "Spring" in possible_seasons:
        personality_season = "Spring"
    elif personality.lower() == "mature" and "Autumn" in possible_seasons:
        personality_season = "Autumn"
    elif personality.lower() == "cute" and "Summer" in possible_seasons:
        personality_season = "Summer"
    elif personality.lower() == "confident" and "Winter" in possible_seasons:
        personality_season = "Winter"

    # Combine the results to find the most matching season
    season_counts = {"Spring": 0, "Summer": 0, "Autumn": 0, "Winter": 0}

    if face_season:
        season_counts[face_season] += 1
    if eye_season:
        season_counts[eye_season] += 1
    if personality_season:
        season_counts[personality_season] += 1

    # Check if there are no valid seasons selected
    if all(count == 0 for count in season_counts.values()):
        return "Unable to determine the season. Please check your inputs."

    # Find the season with the highest count
    final_season = max(season_counts, key=season_counts.get)

    return final_season

def recommend_colors(season):
    # Color recommendations for each season with valid CSS names or hex codes
    color_recommendations = {
        "Spring": {
            "overall_look": "Fresh and light",
            "recommended_colors": ["peachpuff", "coral", "#FFFFE0", "mintcream", "lavender"],
            "avoid_colors": ["black", "darkgray", "darkblue"]
        },
        "Summer": {
            "overall_look": "Soft and muted",
            "recommended_colors": ["pink", "lightblue", "thistle", "lightgray", "aqua"],
            "avoid_colors": ["orange", "red", "#A52A2A"] 
        },
        "Autumn": {
            "overall_look": "Rich and earthy",
            "recommended_colors": ["olive", "#FFD700", "#B7410E", "#D2691E", "#C19A6B"],
            "avoid_colors": ["white", "deepskyblue", "#39FF14"]  
        },
        "Winter": {
            "overall_look": "Sharp and contrasting",
            "recommended_colors": ["blue", "green", "fuchsia", "black", "snow"],
            "avoid_colors": ["orange", "#8B4513", "#8B7D6B"]
        }
    }
    # Return the recommendations for the determined season
    return color_recommendations[season]

def display_color_images(color_list, title):
    # Use matplotlib to display color patches
    fig, ax = plt.subplots(figsize=(8, 2))
    plt.title(title)
    ax.axis('off')  # Turn off axis

    # Define the width of each color patch
    width = 1 / len(color_list)

    for i, color in enumerate(color_list):
        try:
            # Create a rectangle patch for each color
            rect = patches.Rectangle((i * width, 0), width, 1, facecolor=color.lower())
            ax.add_patch(rect)
            # Add a label for each color patch
            plt.text(i * width + width / 2, 0.5, color, ha='center', va='center', fontsize=12, color='white'
                     ,path_effects=[pe.withStroke(linewidth=1, foreground="black")])
        except ValueError:
            print(f"Color '{color}' is not recognized. Please use a standard CSS color name or hex code.")

    plt.show()

def main():
    # Step 1: Determine undertone
    undertone = verify_undertone()

    # Step 2: Determine possible seasons based on undertone
    possible_seasons = determine_season_by_undertone(undertone)

    # Step 3: Refine the season by asking additional questions
    face_dimension_input = input("Enter face dimension (Less defined face or Defined face): ")
    eye_color_input = input("Enter eye color (Light brown, Dark brown, Reddish, Dark, or Deep black): ")
    personality_input = input("Enter personality (Cheerful, Mature, Cute, Confident): ")

    # Step 4: Further narrow down the season based on the user's specific traits
    final_season = determine_season(face_dimension_input, eye_color_input, personality_input, possible_seasons)

    # Step 5: Provide color recommendations based on the final season
    color_info = recommend_colors(final_season)
    
    print(f"\nThe season of personal color is: {final_season} ({undertone} undertone).")
    print(f"Overall look for {final_season}: {color_info['overall_look']}")
    print(f"Recommended colors: {', '.join(color_info['recommended_colors'])}")
    print(f"Colors to avoid: {', '.join(color_info['avoid_colors'])}")

    # Step 6: Display images for the recommended and avoid colors
    display_color_images(color_info['recommended_colors'], "Recommended Colors")
    display_color_images(color_info['avoid_colors'], "Colors to Avoid")


#["Spring", "Summer", "Autumn", "Winter"]
final_season = "Spring"
undertone = "cold"
# Step 5: Provide color recommendations based on the final season
color_info = recommend_colors(final_season)

print(f"\nThe season of personal color is: {final_season} ({undertone} undertone).")
print(f"Overall look for {final_season}: {color_info['overall_look']}")
print(f"Recommended colors: {', '.join(color_info['recommended_colors'])}")
print(f"Colors to avoid: {', '.join(color_info['avoid_colors'])}")
# Step 6: Display images for the recommended and avoid colors
display_color_images(color_info['recommended_colors'], "Recommended Colors")
display_color_images(color_info['avoid_colors'], "Colors to Avoid")