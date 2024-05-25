from neural_structure import Cortical_Column, Neuron 
from directional_arrow import Arrow
import random
import pygame



'''
Road Map

1. Fully implement dendritic & axonal connections. [x]
2. Localizational binding probability of starting dendritic & axonal connections. []
3. Algorithm for pathway atrophy and neurogenesis. [x]
4. Create sensor neuron.
5. Physical neural output reliant on sensor.

'''

if __name__ == "__main__":

    cortical_column = Cortical_Column() # Declares cortical column
    x_depth, y_depth, z_depth = 23, 23, 23 # X, Y, & Z depths.

    for z in range(z_depth):
        for y in range(y_depth):
            for x in range(x_depth):
                cortical_column.add_neuron(x, y, z) # Initializes the cortical column.

    for n in cortical_column.neurons: # Initializes dendrites
        print(n.generation_id, ":", end=" ")
        for number in range(random.randint(1, 6)): # Defines number of generated dendrite 1-6.
            n.add_dendrite(cortical_column.neurons[random.randint(0, len(cortical_column.neurons)-1)]) # Forms a dendrite connection to a random neuron.
            print(n.outgoing_dendrites[number].generation_id, end=" |")
        print()

    for n in cortical_column.neurons: # Initializes axon
        print(n.generation_id, ":", end=" ")
        for number in range(random.randint(1,  6)): # Defines number of generated axons
            n.add_axon(cortical_column.neurons[random.randint(0, len(cortical_column.neurons)-1)]) # Forms a axon connection to a random neuron.
            print(n.outgoing_axon[number].generation_id, end=" |")
        print()


    # pygame setup
    pygame.init()
    window_x = 100 * x_depth
    window_y = 100 * x_depth
    window_size = (window_x, window_y)
    pygame.display.set_caption("Cortical Column")

    window = pygame.display.set_mode(window_size)
    transparent_surface = pygame.Surface(window_size, pygame.SRCALPHA)

    clock = pygame.time.Clock()

    background_color = (0, 0, 20)
    neuron_color = (75, 0, 100)
    dendrite_color = (50, 50, 80, 128)
    axon_color = (80, 0, 50)
    color_shift = 200 // z_depth

    running = True
    angle = 90

    generation_time = 4000
    dial_time = 1000
    lapse_generation = False
    min_list = []

    arrow = Arrow(window)

    # fill the screen with a color to wipe away anything from last frame
    window.fill(background_color)

    AXON_GROWTH = pygame.USEREVENT + 1 # Axon prune and growth event. 
    DIAL_MOVEMENT = pygame.USEREVENT + 2
    pygame.time.set_timer(AXON_GROWTH, generation_time) # Even set to trigger every loop of generation time in ms.
    pygame.time.set_timer(DIAL_MOVEMENT, dial_time)

    while running:
        
        ''' Enables space bar to advance one neural generation at a time. 
        key_pressed = False
        while not key_pressed:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    key_pressed = True  # Exit the inner loop as well
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        key_pressed = True  # Advance to the next frame
        '''

        # Exiting event, for space bar generational advance code snippet must be commented out. 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == AXON_GROWTH: 
                lapse_generation = True
            elif event.type == DIAL_MOVEMENT: 
                print("MOVE")
                
                angle += 1
                print(arrow.degree)

        
        # RENDER YOUR GAME HERE
        window.fill(background_color)
        for n in cortical_column.neurons:
            
            arrow.render(angle) # Renders directional arrow
            


        
            #print(n.position, "|", end=' ')
            for dendrite in n.outgoing_dendrites: # Finds presynaptic neurons through dendrites. 

                if dendrite.fire == True and n.neural_memory == 0: # If presynaptic neuron fire.
                    n.membrane_potential += n.dendrite_power
                    if n.action_potential(): 
                        n.fire = True # Postsynaptic neuron is fired.
                        dendrite.neural_memory = 1 # Presynaptic neuron enter a refractory period.
                        
            if n.fire == False: n.neural_memory = 0 # If neuron has not fired then the refractory period is over. 
        



            # Changes axon branch.
            if lapse_generation: # If AXON_GROWTH event has been triggered.

                min_list.clear()
                #print(len(n.outgoing_axon))
                for post_neuron in n.outgoing_axon: # Finds neuron with least amount of time fired, prunes it, and reconnects to another neuron. 
                    min_list.append(post_neuron.history)
                    n.history = 0
                #print(min_list)    
                min_score = min_list.index(min(min_list)) # Gets the index place of which neuron has the lost history score.
                #print(min_score)
                min_place = n.outgoing_axon.index(n.outgoing_axon[min_score]) # Get the index place in the axon list of the neuron with the lowest history score.
                n.outgoing_axon[min_place] = cortical_column.neurons[random.randint(0, len(cortical_column.neurons)-1)] # Replaces old axon with connection to a random neuron.

                

                



            #print(cortical_column.neurons[0].outgoing_axon)
            #print()



            # If neuron reaches action potential 
            fire = 0
            if n.fire == True: 
                fire = 50
                n.history += 1
            else: fire = 0
            
            pygame.draw.ellipse(window, #Draws neuron
            (50 + color_shift * n.z - fire, fire * 2, 100 + (fire * 2)), # Color Red one layer refractory visual "+ (200 * n.neural_memory)"
            (window_x//4 + n.x * 50 + (n.z * 10), # X position
            window_y//4 + n.y * 50 + (n.z * 10), # Y position
             25, 25)) # Ellipse dimensions
            
            for l in range(len(n.outgoing_dendrites)): # Renders dendrite
                pygame.draw.line(transparent_surface, dendrite_color,
                ((window_x//4) + (n.x * 50 + 12) + (n.z * 10), # X starting (window + x-position + z-offset) ("+ 10" offset so it hits center of the neuron)
                (window_y//4) + (n.y * 50 + 12) + (n.z * 10)), # Y starting (window + y-position + z-offset)
                
                ((window_x//4) + (n.outgoing_dendrites[l].x * 50 + 12) + (n.outgoing_dendrites[l].z * 10), # X end (window + x-pos connected neuron + z-offset)
                (window_x//4) + (n.outgoing_dendrites[l].y * 50 + 12) + (n.outgoing_dendrites[l].z * 10)) # Y end (window + y-pos connected neuron + z-offset)
                , 1) # Line thickness
            
            for a in range(len(n.outgoing_axon)): # Renders axon
                pygame.draw.line(window, axon_color,
                ((window_x//4) + (n.x * 50 + 12) + (n.z * 10), # X starting (window + x-position + z-offset) ("+ 10" offset so it hits center of the neuron)
                (window_y//4) + (n.y * 50 + 12) + (n.z * 10)), # Y starting (window + y-position + z-offset)
                
                ((window_x//4) + (n.outgoing_axon[a].x * 50 + 12) + (n.outgoing_axon[a].z * 10), # X end (window + x-pos connected neuron + z-offset)
                (window_x//4) + (n.outgoing_axon[a].y * 50 + 12) + (n.outgoing_axon[a].z * 10)) # Y end (window + y-pos connected neuron + z-offset)
                , 1) # Line thickness



            if n.fire == True and n.neural_memory == 0: # Regulates neural refractory period
                n.neural_memory = 1 # If neuron has fired it enters the refractory period after render. 
                n.membrane_potential = n.resting_potential # Resets membrane potential to resting potential after neural firing. 
            else: n.fire = False # Resets neurons ability to fire. (Refractory period acts as neurons memory of previous state).

            
            
            for axon in n.outgoing_axon: # Carries firing to post synaptic neuron through the axon. 
                if n.fire:
                    axon.membrane_potential += axon.axon_power
                    if axon.action_potential():
                        axon.fire = True
                        axon.neural_memory = 0

        lapse_generation = False # Ends AXON_GROWTH event 

            
        
            
        # Blit the transparent surface onto the main window surface.
        window.blit(transparent_surface, (0, 0))

        # flip() the display to put your work on screen
        pygame.display.flip()
        clock.tick(5)  # limits FPS

    pygame.quit()


    


