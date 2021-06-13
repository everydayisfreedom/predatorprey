++++++
Requirements:

python 3.9.4
pygame

++++++
Specifications:

The simulation has N Predator-Agents and 2xN Prey-Agents: 15 predators for 30 preys that start in random locations.
The program tracks the speed, and distance between the predator and the prey.
Predators:
  • The predators are red in color, and in the shape of circles.
  • The predators hunt to eat only when they are hungry:
    o At the beginning of the game after the 30 second mark, and every 30 seconds afterwards. 
  • When they are not hungry, they move normally.• They only have one speed.
  • When they eat: they turn into a darker shade of red, and gain weight.
  
Preys:
• The preys are green, and in the shape of polygons.
• The preys enter alert mode when they cross paths with a predator:
o They speed up and go into the opposite direction.
• The preys exit alert mode when they are away from the predators and uses normal speed.
The code:
  • Two classes:
    o Predator:
      ▪ Attributes:
        • Weight
        • Color
        • X position, Y position
        • Time
        • Random direction
        • Direction
        • Speed
        • Victim: the targeted prey that the predator will be chasing
        • Boolean ate: to check if the predator has eaten yet or not.
        • ID: unique ID to keep track of the predator.
      ▪ Behavior:
        • Eat
        • Move
        • Draw
    o Prey:
      ▪ Attributes:
        • Weight
        • Color
        • X position, Y position
        • Life: To check if it was eaten or not, if yes then it should be deleted.
        • Direction
        • Change of direction.
        • Speed
      ▪ Behavior:
        • Alert:
          o Speed up.
          o Run away from the predator.
        • Move
        • Draw
        
The simulation:
• The simulation outputs which predator ate a prey.
• The simulation finishes when each predator has eaten only one prey.
