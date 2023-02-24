#Index Number: 6929621
#Name: Asafo-Adjei Nana Kwabena Kwarteng
#https://github.com/Aankka

#Question: Car dealership, Toyota car, Benz, Rolls Royce etc, each car has its own sales price, write a code that asks the person buying the car the brand of car that he wants and tells the price of that car
#Over 30 cars minimum

mercedes_benz = {'AMG one':250000,'Actros':455500,'Sprinter': 79000, 'AMG GT': 300000, 'GLS':270000, 'G-Wagen':262000}  #A dictionary of a car brand, its available models and prices
mercedes_benz_list = list(mercedes_benz.keys())  # A list that contains only the keys of the key-value pair

volkswagen = {'T-Roc':110000,'Tiguan':220523, 'Caddy': 90000, 'Multivan':500200, 'Golf': 120540,'Polo':85600}
volkswagen_list = list(volkswagen.keys())

infiniti = {'QX80':818750, 'QX60':554375, 'QX50':465625, 'QX30': 379375, 'Q70': 630000, 'Q60': 516875}
infiniti_list = list(infiniti.keys())

jeep = {'Wrangler':562314, 'Renegade':679002, 'Compass':305234,'Grand Cherokee':743562,'Grand Wagoneer':3110265, 'Commander':542356}
jeep_list = list(jeep.keys())

chevrolet = {'Impala':25300, 'Camaro':428563, 'Corvette':623457, 'Equinox':567890 , 'Silverado':349072 , 'Suburban':823456}
chevrolet_list = list(chevrolet.keys())

rolls_royce = {'Wraith':1000000, 'Cullinan':2500000, 'Phantom':3245678,'Dawn':2314568,'Ghost':3247659,'Phantom Coupe':543218}
rolls_royce_list = list = list(rolls_royce.keys())

print('''Welcome to Nanakwarts delearship, good prices for luxury people\nHere is a list of cars currently available, please type the number that corresponds with the car you want.
 1)Mercedes Benz\n 2)Volkswagen\n 3)Infiniti\n 4)Jeep\n 5)Chevrolet\n 6)Rolls Royce\n''')  #List of available cars
user_preference = input('What car would you like to select from the expansive variety of cars at this dealership? ') #Input for buyer to choose car option


if user_preference == '1':  #If user chooses the option for benz
    benz_pref = input(f'\nThis is a list of the models available for Mercedes Benz, please type the name of the car model whoose price you want to see. {mercedes_benz_list}:\n')
    if benz_pref.lower() == 'g-wagen': #the code recoognizes the input regardless of uppercase or lowercase variations
        print('the price of the car you have chosen is ' + str(mercedes_benz['G-Wagen']) + ' cedis') #Returns the price of the specified model stored in the dictionary, quoted in cedis
    elif benz_pref.lower() == 'amg one':
        print('the price of the car you have chosen is ' + str(mercedes_benz['AMG one']) + ' cedis')
    elif benz_pref.lower() == 'sprinter':
        print('the price of the car you have chosen is ' + str(mercedes_benz['Sprinter']) + ' cedis')
    elif benz_pref.lower() == 'actros':
        print('the price of the car you have chosen is ' + str(mercedes_benz['Actros']) + ' cedis')
    elif benz_pref.lower() == 'amg gt':
        print('the price of the car you have chosen is ' + str(mercedes_benz['AMG GT']) + ' cedis')
    elif benz_pref.lower() == 'gls':
        print('the price of the car you have chosen is ' + str(mercedes_benz['GLS']) + ' cedis')
        
elif user_preference == '2':  #If user chooses the option for Volkswagen
    volkswagen_pref = input(f'\nThis is a list of the models available for Volksvagen, please type the name of the car model whoose price you want to see. {volkswagen_list}:\n')
    if volkswagen_pref.lower() == 't-roc':
        print('the price of the car you have chosen is ' + str(volkswagen['T-Roc']) + ' cedis')
    elif volkswagen_pref.lower() == 'tiguan':
        print('the price of the car you have chosen is ' + str(volkswagen['Tiguan']) + ' cedis')
    elif volkswagen_pref.lower() == 'caddy':
        print('the price of the car you have chosen is ' + str(volkswagen['Caddy']) + ' cedis')
    elif volkswagen_pref.lower() == 'multivan':
        print('the price of the car you have chosen is '+ str(volkswagen['Multivan']) + ' cedis')
    elif volkswagen_pref.lower() == 'golf':
        print('the price of the car you have chosen is ' + str(volkswagen['Golf']) + ' cedis')
    elif volkswagen_pref.lower() == 'polo':
        print('the price of the car you have chosen is ' + str(volkswagen['Polo']) + ' cedis')
    
elif user_preference == '3': #If user chooses option for Infiniti
    infiniti_pref = input(f'\nThis is a list of the models available for Infiniti, please type the name of the car model whoose price you want to see. {infiniti_list}:\n')
    if infiniti_pref.upper() == 'QX80':
        print('the price of the car you have chosen is ' + str(infiniti['QX80']) + ' cedis')
    elif infiniti_pref.upper() == 'QX60':
        print('the price of the car you have chosen is ' + str(infiniti['QX60']) + ' cedis')
    elif infiniti_pref.upper() == 'QX50':
        print('the price of the car you have chosen is ' + str(infiniti['QX50']) + ' cedis')
    elif infiniti_pref.upper() == 'QX30':
        print('the price of the car you have chosen is ' + str(infiniti['QX30']) + ' cedis')
    elif infiniti_pref.upper() == 'Q70':
        print('the price of the car you have chosen is ' + str(infiniti['Q70']) + ' cedis')
    elif infiniti_pref.upper() == 'Q60':
        print('the price of the car you have chosen is ' + str(infiniti['Q60']) + ' cedis')
    
elif user_preference == '4': #If user chooses option for Jeep
    jeep_pref = input(f'\nThis is a list of the models available for Jeep, please type the name of the car model whoose price you want to see. {jeep_list}:\n')
    if jeep_pref.lower() == 'wrangler':
        print('the price of the car you have chosen is ' + str(jeep['Wrangler']) + ' cedis')
    elif jeep_pref.lower() == 'renegade':
        print('the price of the car you have chosen is ' + str(jeep['Renegade']) + ' cedis')
    elif jeep_pref.lower() == 'compass':
        print('the price of the car you have chosen is ' + str(jeep['Compass']) + ' cedis')
    elif jeep_pref.lower() == 'grand cherokee':
        print('the price of the car you have chosen is ' + str(jeep['Grand Cherokee']) + ' cedis')
    elif jeep_pref.lower() == 'grand wagoneer':
        print('the price of the car you have chosen is ' + jeep['Grand Wagoneer'] + ' cedis')
    elif jeep_pref.lower() == 'commander':
        print('the price of the car you have chosen is ' + str(jeep['Commander']) + ' cedis')
    
elif user_preference == '5': #If user chooses option for Chevrolet
    chevrolet_pref = input(f'\nThis is a list of the models available for Chevrolet, please type the name of the car model whoose price you want to see. {chevrolet_list}:\n')
    if chevrolet_pref.lower() == 'impala':
        print('the price of the car you have chosen is ' + str(chevrolet['Impala']) + ' cedis')
    elif chevrolet_pref.lower() == 'camaro':
        print('the price of the car you have chosen is ' + str(chevrolet['Camaro']) + ' cedis')
    elif chevrolet_pref.lower() == 'corvette':
        print('the price of the car you have chosen is ' + str(chevrolet['Corvette']) + ' cedis')
    elif chevrolet_pref.lower() == 'equinox':
        print('the price of the car you have chosen is ' + str(chevrolet['Equinox']) + ' cedis')
    elif chevrolet_pref.lower() == 'silverado':
        print('the price of the car you have chosen is ' + str(chevrolet['Silverado']) + ' cedis')
    elif chevrolet_pref.lower() == 'suburban':
        print('the price of the car you have chosen is ' + str(chevrolet['Suburban']) + ' cedis')
    
elif user_preference == '6':  #If user chooses option for Rolls Royce
    rolls_pref = input(f'\nThis is a list of the models available for Rolls Royce, please type the name of the car model whoose price you want to see. {rolls_royce_list}:\n')
    if rolls_pref.lower() == 'wraith':
        print('the price of the car you have chosen is ' + str(rolls_royce['Wraith']) + ' cedis')
    elif rolls_pref.lower() == 'cullinan':
        print('the price of the car you have chosen is ' + str(rolls_royce['Cullinan']) + ' cedis')
    elif rolls_pref.lower() == 'phantom':
        print('the price of the car you have chosen is ' + str(rolls_royce['Phantom']) + ' cedis')
    elif rolls_pref.lower() == 'dawn':
        print('the price of the car you have chosen is ' + str(rolls_royce['Dawn']) + ' cedis')
    elif rolls_pref.lower() == 'ghost':
        print('the price of the car you have chosen is ' + str(rolls_royce['Ghost']) + ' cedis')
    elif rolls_pref.lower() == 'phantom coupe':
        print('the price of the car you have chosen is ' + str(rolls_royce['Phantom Coupe']) + ' cedis')
        
else:
    print('Your input is invalid') #For any input either than the 1-6 options provided
   
    
    

 

