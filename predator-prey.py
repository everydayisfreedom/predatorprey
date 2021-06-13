from datetime import datetime
import random as rand
import pygame
import math
import string

BACKGROUND_COLOUR = (27, 27, 27)
SCREEN_WIDTH = SCREEN_HEIGHT = 650
seconds_in_day = 24 * 60 * 60
timetogethungry = 30
straight_angle = 180
PI = math.pi

num = 0
def getid():
	global num
	num += 1
	return num



class Predator():
    def __init__(self):
        self.weight = rand.randint(8, 12)
        self.id = getid()
        self.colour = (rand.randint(200, 250), rand.randint(5, 20), rand.randint(5, 20))   
        self.x_pos = self.y_pos = rand.randrange(self.weight, SCREEN_WIDTH - self.weight)
        self.random_direct = rand.randint(10, 35)
        self.direct = rand.randrange(400)
        self.time = datetime.now()

        self.speed = self.hungry = 1
        self.victim = None
        
        self.ate = False
        
    
    def eat(self, preys):
        if self.hungry >= 50 and self.ate == False:
            for prey in preys:
                dist = ((self.x_pos - prey.x_pos)**2 + (self.y_pos - prey.y_pos)**2) ** 0.5
                if dist < self.weight + prey.weight - 1:
                    prey.life = False
                    self.hungry -= 50
                    self.weight += 1
                    self.colour = (139, 1, 1)
                    print('predator', self.id,'ate a prey')
                    self.ate = True
                    break;

    
    def move(self, preys):
        if not self.victim or not self.victim.life and preys:
            self.victim = rand.choice(preys)

        time1 = datetime.now()
        difference = time1 - self.time
        minsec = divmod(difference.days * seconds_in_day + difference.seconds, 60)
        if minsec[1] == timetogethungry:
            self.hungry = 50
            

        self.x_pos += math.cos(self.direct * (PI / straight_angle)) * self.speed
        self.y_pos += math.sin(self.direct * (PI / straight_angle)) * self.speed
        
        if self.hungry >= 50 and self.ate == False:
        	#if hungry start searching for prey
            self.direct = math.atan2(self.victim.y_pos - self.y_pos, self.victim.x_pos - self.x_pos) * (straight_angle / PI)

        else:
        	#if not move normally
            self.direct = self.direct + rand.randint(-self.random_direct, self.random_direct)

            # go in opposite direct if a wall is hit
            if self.x_pos - self.weight <= 0:
                self.x_pos = self.weight            
                self.direct = self.direct - straight_angle           
            elif self.x_pos + self.weight >= SCREEN_WIDTH:
                self.x_pos = SCREEN_WIDTH - self.weight
                self.direct = self.direct - straight_angle

            if self.y_pos - self.weight <= 0:
                self.y_pos = self.weight
                self.direct = self.direct - straight_angle        
            elif self.y_pos + self.weight >= SCREEN_HEIGHT:
                self.y_pos = SCREEN_HEIGHT - self.weight
                self.direct = self.direct - straight_angle
    

            
    def draw(self, screen):
        pygame.draw.circle(screen, self.colour, (int(self.x_pos), int(self.y_pos)), self.weight)



class Prey():
    def __init__(self):
        self.weight = rand.randint(5, 10)
        self.colour = (rand.randint(0,10), 205, rand.randint(10, 100))
        self.life = True
        
        self.x_pos = self.y_pos = rand.randrange(self.weight, SCREEN_WIDTH - self.weight)
        
        self.direct = rand.randrange(500)
        self.direct_change = rand.randint(5, 25)
       
        self.speed = 1.1
        

    def alert(self, predators):
        if not predators:
        	self.speed = 1.1
        	return

        for predator in predators:
            dist = ((self.x_pos - predator.x_pos) ** 2 + (self.y_pos - predator.y_pos) ** 2) ** 0.5
            if dist < (self.weight + predator.weight)*3:
                self.direct = predator.direct
                self.speed = 5
                break;
            else:
            	self.speed = 1.1
          
    def move(self):
        self.x_pos += math.cos(self.direct * (PI / straight_angle)) * self.speed
        self.y_pos += math.sin(self.direct * (PI / straight_angle)) * self.speed
        
        self.direct = self.direct + rand.randint(-self.direct_change, self.direct_change)
        
        # go in opposite direct if a wall is hit
        if self.x_pos - self.weight <= 0:
            self.x_pos = self.weight            
            self.direct = self.direct - straight_angle           
        elif self.x_pos + self.weight >= SCREEN_WIDTH:
            self.x_pos = SCREEN_WIDTH - self.weight
            self.direct = self.direct - straight_angle

        if self.y_pos - self.weight <= 0:
            self.y_pos = self.weight
            self.direct = self.direct - straight_angle       
        elif self.y_pos + self.weight >= SCREEN_HEIGHT:
            self.y_pos = SCREEN_HEIGHT - self.weight
            self.direct = self.direct - straight_angle
        
    
    def draw(self, screen):
        pygame.draw.polygon(screen, self.colour, [(int(self.x_pos), int(self.y_pos)),(int(self.x_pos)-1, int(self.y_pos)-1), (int(self.x_pos)+3, int(self.y_pos)+3)], self.weight)



def run():
	pygame.init()
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	pygame.display.set_caption('Predators and Prey Simulation')
	start = True

	# N Predator-Agents and 2N Prey-Agents
	predators = [Predator() for pred in range(15)]
	preys = [Prey() for prey in range(2*len(predators))]


	while start:
		screen.fill(BACKGROUND_COLOUR)

		for prey in preys:
			prey.move()
			prey.alert(predators)
			prey.draw(screen)


		for predator in predators:
			predator.move(preys)
			predator.eat(preys)
			predator.draw(screen)

		# delete starved predators and preys that were eaten
		preys = [prey for prey in preys if prey.life]
		pred_bool = [pred.ate for pred in predators]

		if not (False in pred_bool):
			print('The game finishes when each Predator-Agent eats only one Prey-Agent.')
			start = False

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				start = False

		pygame.display.flip()


run()