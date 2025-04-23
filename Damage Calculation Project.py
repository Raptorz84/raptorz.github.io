# Attack boosts skill function
def apply_attack_boost(raw, bonus_raw, attack_boost_level):
# raw: base vale attack value of a given weapon.
# bonus_raw: bonus attack granted from meal buffs,consumables, or armor skills.
# attack_boost_level: skill level of attack boost.
    
    #conditional statement for the different levels of attack boost
    if attack_boost_level == 1:    
        total_raw = raw + 3 # level one give three extra attack
    elif attack_boost_level == 2:
        total_raw = raw + 5 # level two gives 5 extra attack
    elif attack_boost_level == 3:
        total_raw = raw + 7 # level three gives 7 extra attack
    elif attack_boost_level == 4:
        total_raw = raw*1.02 + 8 # level 4 gives a .02% increase in attack and a flat 8 extra attack
    elif attack_boost_level >= 5:
        total_raw = raw*1.04 + 9 # level 5 gives a .04% increase in attack and a flat 9 extra attack
    else:
        total_raw = raw # if no attack boost levels are present then total_raw and raw are the same value

   # this the bonus_raw added to the attack plus the attack boost skill because bonus attack is applied after the attack boost skill
    total_raw = total_raw + bonus_raw
    
    # this function will return the total_raw as the output
    return total_raw

# Critical boost skill function
def apply_critical_boost(critical_boost_level):
    critical_modifier = 1.25 + (critical_boost_level*0.03)
# this function adds the level of the critical boost skill to the base crit modifer of 1.25
# critical_boost_level: the level of the skill
    
    critical_modifier = min(critical_modifier, 1.4) # This is the maximum the critical boost can go up to which is 5 levels.
    critical_modifier = max(critical_modifier, 1.25) # This is the minnimum the critical boost skill can be at which is with 0 levels.
   
    # This function returns the critical modifier with the correct level of crit boost applied to it.
    return critical_modifier
# This calculates the total affinity
def calculate_affinity(weapon_affinity, crit_eye_level, bonus_crit_chance):

# This conditional statement gives the percentage increase in affinity for the coresponding level of crit eye
    if crit_eye_level == 0:
        increase_affinity = 0
    elif crit_eye_level == 1:
        increase_affinity = 4
    elif crit_eye_level == 2:
        increase_affinity = 8
    elif crit_eye_level == 3:
        increase_affinity = 12
    elif crit_eye_level == 4:
        increase_affinity = 16
    elif crit_eye_level >= 5:
        increase_affinity = 20

# This calculates the total percentage of affinity
    affinity = weapon_affinity + bonus_crit_chance + increase_affinity

# This stops the affinity from going above 100%
    affinity = min(affinity, 100)
    
    return affinity

# This gives the affinity percentage
calculate_affinity(weapon_affinity = 5,
                   crit_eye_level = 5,
                   bonus_crit_chance = 70) 
# Bonus crit chance is any additional affinity gained from other skills

# This function gives the effective critical value
def effective_critical_modifier(critical_modifier, affinity):
# affinity: is the chance to land a critical hit

    # crit chance only goes up to 100%
    portion_of_crits = affinity/100 

    # if a crit is not a crit it is not a crit
    portion_of_not_crits = 1-portion_of_crits 
    
    # if it is a crit the damage will be multiplied by the crit_modifier
    damage_from_crits = portion_of_crits*critical_modifier 
    
    # if it is not a crit the damage will remain the same so multiplied by 1
    damage_from_not_crits = portion_of_not_crits*1 

    # The effective critical is the damage we get from crits as well as from not crits
    effective_critical_modifier = damage_from_crits+damage_from_not_crits

    # it returns the effective critical damage
    return effective_critical_modifier

# This function is to apply the sharpness boost to the final attack value
def calculate_sharpness_boost(sharpness_color):

# Conditional statement to apply the correct sharpness raw attack increase
    if sharpness_color == "white":
        sharpness_raw_multiplier = 1.33
    elif sharpness_color == "blue":
        sharpness_raw_multiplier = 1.20
    elif sharpness_color == "green":
        sharpness_raw_multiplier = 1.05
    elif sharpness_color == "yellow":
        sharpness_raw_multiplier = 1.00
    elif sharpness_color == "orange":
        sharpness_raw_multiplier = 0.75
    elif sharpness_color == "red":
        sharpness_raw_multiplier = 0.50
    else:
        sharpness_raw_multiplier = 0

# This returns the sharpness multiplier
    return sharpness_raw_multiplier

# This function puts together all the values to give us our true damage value by combining the previous two functions
def calculate_damage(raw, bonus_raw, weapon_affinity, crit_eye_level, bonus_affinity, attack_boost_level, critical_boost_level, sharpness_color):

    # This is using the total raw function
    total_raw = apply_attack_boost(raw, bonus_raw, attack_boost_level)
    
    # This is using the critical boost skill function
    critical_modifier = apply_critical_boost(critical_boost_level)

    affinity = calculate_affinity(weapon_affinity, crit_eye_level, bonus_affinity)

    # This is using the effective critical function
    calculate_effective_critical_modifier = effective_critical_modifier(critical_modifier, affinity)

    sharpness_raw_multiplier = calculate_sharpness_boost(sharpness_color)
    
    # By combining all of these functions we can get our true damage value
    damage = total_raw * calculate_effective_critical_modifier

    true_damage = damage * sharpness_raw_multiplier
    
    # This returns the true damage value
    return true_damage
    
# This function will compare two differnt attack values to find which combination is better
def find_difference(raw, bonus_raw, weapon_affinity, crit_eye_level, bonus_affinity, 
                    attack_boost_level_a, 
                    critical_boost_level_a,
                    attack_boost_level_b, 
                    critical_boost_level_b,
                    sharpness_color):

    damage_a = calculate_damage(raw, bonus_raw, weapon_affinity, crit_eye_level, bonus_affinity,
                                attack_boost_level_a, critical_boost_level_a, sharpness_color)
    damage_b = calculate_damage(raw, bonus_raw, weapon_affinity, crit_eye_level, bonus_affinity,
                                attack_boost_level_b, critical_boost_level_b, sharpness_color)

    difference_as_percent = (damage_a - damage_b)/damage_a

    return difference_as_percent

# This gives us the damage comparison in percentage format
find_difference(raw = 225,
                bonus_raw = 50,
                weapon_affinity = 5,
                crit_eye_level = 5,
                bonus_affinity = 50,
                attack_boost_level_a = 0,
                critical_boost_level_a = 5,
                attack_boost_level_b = 5,
                critical_boost_level_b = 0,
                sharpness_color = "white")

# Get user input for each parameter
raw = float(input("Enter the weapon's base raw attack value: "))
bonus_raw = float(input("Enter the bonus raw attack (from buffs, armor, etc.): "))
weapon_affinity = float(input("Enter the weapon's base affinity (%): "))
crit_eye_level = int(input("Enter the Critical Eye skill level (0-7): "))
bonus_affinity = float(input("Enter the bonus affinity from skills (%): "))
attack_boost_level = int(input("Enter the Attack Boost skill level (0-7): "))
critical_boost_level = int(input("Enter the Critical Boost skill level (0-5): "))
sharpness_color = input("Enter the weapon's sharpness color (white, blue, green, yellow, orange, red): ").lower()

# Call the calculate_damage function with user inputs
true_damage = calculate_damage(
    raw,
    bonus_raw,
    weapon_affinity,
    crit_eye_level,
    bonus_affinity,
    attack_boost_level,
    critical_boost_level,
    sharpness_color
)

# The 1st variable is the base raw attack the weapon has.
# The 2nd variable is the bonus attack given from armor skills, food buffs, and consumables.
# The 3rd variable is the weapon affinity which is nherint crit chance the weapon has.
# The 4th variable is the level of the crit eye skill.
# The 5th variable is the bonus affinity gained from other armor and weapon skills. 
# The 6th variable is the level of the equipped attack boost skill.
# The 7th variable is the level of the equipped crit boost skill.
# The 8th variable is the color of the sharpness gauge on the weapon. 


print(f"\nEstimated True Damage Output: {true_damage:.2f}")
