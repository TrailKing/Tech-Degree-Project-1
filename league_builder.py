if __name__ == "__main__":
    import csv
    #define objects needed in program
    team1 = []
    team2 = []
    team3 = []
    soccer_experience = list([])
    soccer_inexperience = list([])
    
    #create function that populates teams with experienced players
    def populate_experience():
        counter = 0
        while counter < experience:
            team1.append(soccer_experience[counter])
            team2.append(soccer_experience[counter+1])
            team3.append(soccer_experience[counter+2])
            counter += 3
    #create function that populates teams with unexperienced players
    def populate_not_experienced():
        counter = 0
        while counter < not_experience:
            team1.append(soccer_inexperience[counter])
            team2.append(soccer_inexperience[counter+1])
            team3.append(soccer_inexperience[counter+2])
            counter += 3
    #create function that uses results of populated teams and writes out the league roster        
    def write_league_rosters():
        with open('teams.txt','a') as csvfile:
            field_keys = ['Name','Height (inches)','Soccer Experience','Guardian Name(s)']
            team1writer = csv.DictWriter(csvfile,field_keys,delimiter=',')
            csvfile.write("Sharks\n")
            team1writer.writerows(team1)
 
            team2writer = csv.DictWriter(csvfile,field_keys,delimiter=',')
            csvfile.write("Dragons\n")
            team2writer.writerows(team2)
            
            team3writer = csv.DictWriter(csvfile,field_keys,delimiter=',')
            csvfile.write("Raptors\n")
            team3writer.writerows(team3)
    #import the csv file and finds experienced and unexperienced players lists that will be used by the functions    
    with open('soccer_players.csv', newline='') as csvfile:
        soccer_reader = csv.DictReader(csvfile, delimiter=",")
        rows = list(soccer_reader)
        for row in rows:
            if ((row['Soccer Experience'])) == 'YES':
                soccer_experience.append(row)
            else:
                soccer_inexperience.append(row)
    experience = len(soccer_experience)
    not_experience = len(soccer_inexperience)
    
    #call functions
    populate_experience()
    populate_not_experienced()
    write_league_rosters()
    
    
        
    

    
#create a function that adds equal number of experienced players to each team
#create a function that adds equal number of inexperienced players to each team

                




