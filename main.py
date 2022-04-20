# this code was created by Valentin POQUET

# import the modules
import pygame as pg
import time
import math
import random
import webbrowser
from PIL import Image as IMG
import sys
#import os

pg.init()
WIN = pg.display.set_mode((0, 0), pg.FULLSCREEN)
#WIN = pg.display.set_mode((1080, 1920))
WIDTH = pg.display.get_surface().get_width()
HEIGHT = pg.display.get_surface().get_height()
if WIDTH < HEIGHT:
    screen_type = "vertical"
    #WIDTH, HEIGHT = HEIGHT, WIDTH
else:
    screen_type = "horizontal"
pg.display.set_caption("Motus")
pygame_icon = pg.image.load('data/icone.png')
pg.display.set_icon(pygame_icon)
WHITE, GREY, BLACK, RED, BACKGROUND_COLOR = (255, 255, 255), (128, 128, 128), (0, 0, 0), (199, 0, 57), (215, 225, 215)

class Image:
    def __init__(self, image, width, height):
        self.image = image
        self.width = width
        self.height = height

    def scale(self):
        self.image = pg.transform.scale(self.image, ((self.width, self.height)))

    def get_scale(self):
        """
        scale the image and return the scale
        """
        self.image = pg.transform.scale(self.image, ((self.width, self.height)))
        return (self.width, self.height)

    def get_image(self):
        """
        return the image
        """
        return self.image

    def set_pos(self, pos):
        self.pos = pos

    def get_pos(self):
        return self.pos

def create_contour_word(current_path_file:str, n_caracteres:int):
    """
    return an image for the word's outline and take a n_caracteres in argument
    """
    # set the size for the images
    image_size = [WIDTH//20, WIDTH//20]

    # get the images
    image_contour_mot_gauche = IMG.open(current_path_file+"contour_mot\\Contour_mot_gauche.png")
    image_contour_mot_droite = IMG.open(current_path_file+"contour_mot\\Contour_mot_droite.png")
    image_contour_mot = IMG.open(current_path_file+"contour_mot\\Contour_mot.png")

    # rezize images
    image_contour_mot_gauche = image_contour_mot_gauche.resize(image_size, IMG.ANTIALIAS)
    image_contour_mot_droite = image_contour_mot_droite.resize(image_size, IMG.ANTIALIAS)
    image_contour_mot = image_contour_mot.resize(image_size, IMG.ANTIALIAS)

    # create a new image
    image_contours_mot = IMG.new('RGBA',(n_caracteres*image_size[0], image_size[1]), (255, 255, 255, 0))

    # merge the images
    for lettre in range(n_caracteres):
        if lettre == 0:
            image_contours_mot.paste(image_contour_mot_gauche, (0,0))
        elif lettre == n_caracteres-1:
            image_contours_mot.paste(image_contour_mot_droite, (image_size[0]*lettre,0))
        else:
            image_contours_mot.paste(image_contour_mot, (image_size[0]*lettre,0))

    # convert the new image into a Surface type for pygame
    mode = image_contours_mot.mode
    size = image_contours_mot.size
    data = image_contours_mot.tobytes()
    image_contours_mot = pg.image.fromstring(data, size, mode)

    return image_contours_mot

def create_background_word(current_path_file:str, n_caracteres:int):
    """
    return an image for the word's background and take a n_caracteres in argument
    """
    # set the size for the images
    image_size = [WIDTH//20, WIDTH//20]

    # get the images
    image_fond_mot_gauche = IMG.open(current_path_file+"fond_mot\\fond_mot_left.png")
    image_fond_mot_droite = IMG.open(current_path_file+"fond_mot\\fond_mot_right.png")
    image_fond_mot = IMG.open(current_path_file+"fond_mot\\fond_mot.png")

    # rezize images
    image_fond_mot_gauche = image_fond_mot_gauche.resize(image_size, IMG.ANTIALIAS)
    image_fond_mot_droite = image_fond_mot_droite.resize(image_size, IMG.ANTIALIAS)
    image_fond_mot = image_fond_mot.resize(image_size, IMG.ANTIALIAS)

    # create a new image
    image_fonds_mot = IMG.new('RGBA',(n_caracteres*image_size[0], image_size[1]), (255, 255, 255, 0))

    # merge the images
    for lettre in range(n_caracteres):
        if lettre == 0:
            image_fonds_mot.paste(image_fond_mot_gauche, (0,0))
        elif lettre == n_caracteres-1:
            image_fonds_mot.paste(image_fond_mot_droite, (image_size[0]*lettre,0))
        else:
            image_fonds_mot.paste(image_fond_mot, (image_size[0]*lettre,0))

    # convert the new image into a Surface type for pygame
    mode = image_fonds_mot.mode
    size = image_fonds_mot.size
    data = image_fonds_mot.tobytes()
    image_fonds_mot = pg.image.fromstring(data, size, mode)

    return image_fonds_mot

def type_interaction(mouse_x:float, mouse_y:float, n_caracteres:int, n_mot:int, game_over:bool) -> str or int or None:
    """
    return the type of button that the player is pushing and return None if he is not pushing any button
    """
    size_buttons = WIDTH//20
    debut_mot = ((WIDTH/2)-(size_buttons)*(n_caracteres/2))//1

    # check if the player is clicking in the exit button
    if math.sqrt((mouse_x-0.03906*WIDTH)**2+(mouse_y-0.06944*HEIGHT)**2) < math.sqrt(WIDTH**2+HEIGHT**2)*0.02269:
        return "exit"

    # check if the player is clicking in the reset button
    elif math.sqrt((mouse_x-0.93750*WIDTH)**2+(mouse_y-0.06944*HEIGHT)**2) < math.sqrt(WIDTH**2+HEIGHT**2)*0.02269:
        return "reset"

    # check if the player is clicking in the searche button
    elif math.sqrt((mouse_x-(debut_mot+(size_buttons*n_caracteres+size_buttons*0.95)//1))**2+(mouse_y-0.542372813559*HEIGHT)**2) < math.sqrt(WIDTH**2+HEIGHT**2)*0.02269 and game_over:
        return "searche"
    # (debut_mot+(size_buttons*n_caracteres), HEIGHT//2)

    # check in which column the player is clicking
    if mouse_x >= WIDTH*0.01302 and not game_over:
        if mouse_x >= WIDTH*0.06510:
            if mouse_x >= WIDTH*0.11718:
                if mouse_x >= WIDTH*0.16927:

                    # buttons in the fourth column
                    if mouse_x <= WIDTH*0.16927+size_buttons:
                        if mouse_y >= HEIGHT*0.25:
                            if mouse_y >= HEIGHT*0.35:
                                if mouse_y >= HEIGHT*0.45:
                                    if mouse_y >= HEIGHT*0.55:
                                        if mouse_y >= HEIGHT*0.65:
                                            if mouse_y >= HEIGHT*0.75:
                                                if mouse_y >= HEIGHT*0.85:
                                                    if mouse_y <= HEIGHT*0.85+size_buttons:
                                                        return "enter"
                                                elif mouse_y <= HEIGHT*0.75+size_buttons:
                                                    return "X_button"
                                            elif mouse_y <= HEIGHT*0.65+size_buttons:
                                                return "T_button"
                                        elif mouse_y <= HEIGHT*0.55+size_buttons:
                                            return "P_button"
                                    elif mouse_y <= HEIGHT*0.45+size_buttons:
                                        return "L_button"
                                elif mouse_y <= HEIGHT*0.35+size_buttons:
                                    return "H_button"
                            elif mouse_y <= HEIGHT*0.25+size_buttons:
                                return "D_button"

                # buttons in the thirst column
                elif mouse_x <= WIDTH*0.11718+size_buttons:
                    if mouse_y >= HEIGHT*0.25:
                        if mouse_y >= HEIGHT*0.35:
                            if mouse_y >= HEIGHT*0.45:
                                if mouse_y >= HEIGHT*0.55:
                                    if mouse_y >= HEIGHT*0.65:
                                        if mouse_y >= HEIGHT*0.75:
                                            if mouse_y >= HEIGHT*0.85:
                                                if mouse_y <= HEIGHT*0.85+size_buttons:
                                                    return "delete"
                                            elif mouse_y <= HEIGHT*0.75+size_buttons:
                                                return "W_button"
                                        elif mouse_y <= HEIGHT*0.65+size_buttons:
                                            return "S_button"
                                    elif mouse_y <= HEIGHT*0.55+size_buttons:
                                        return "O_button"
                                elif mouse_y <= HEIGHT*0.45+size_buttons:
                                    return "K_button"
                            elif mouse_y <= HEIGHT*0.35+size_buttons:
                                return "G_button"
                        elif mouse_y <= HEIGHT*0.25+size_buttons:
                            return "C_button"

            # buttons in the second column
            elif mouse_x <= WIDTH*0.06510+size_buttons:
                if mouse_y >= HEIGHT*0.25:
                    if mouse_y >= HEIGHT*0.35:
                        if mouse_y >= HEIGHT*0.45:
                            if mouse_y >= HEIGHT*0.55:
                                if mouse_y >= HEIGHT*0.65:
                                    if mouse_y >= HEIGHT*0.75:
                                        if mouse_y >= HEIGHT*0.85:
                                            if mouse_y <= HEIGHT*0.85+size_buttons:
                                                return "Z_button"
                                        elif mouse_y <= HEIGHT*0.75+size_buttons:
                                            return "V_button"
                                    elif mouse_y <= HEIGHT*0.65+size_buttons:
                                        return "R_button"
                                elif mouse_y <= HEIGHT*0.55+size_buttons:
                                    return "N_button"
                            elif mouse_y <= HEIGHT*0.45+size_buttons:
                                return "J_button"
                        elif mouse_y <= HEIGHT*0.35+size_buttons:
                            return "F_button"
                    elif mouse_y <= HEIGHT*0.25+size_buttons:
                        return "B_button"

        # buttons in the first column
        elif mouse_x <= WIDTH*0.01302+size_buttons:
            if mouse_y >= HEIGHT*0.25:
                if mouse_y >= HEIGHT*0.35:
                    if mouse_y >= HEIGHT*0.45:
                        if mouse_y >= HEIGHT*0.55:
                            if mouse_y >= HEIGHT*0.65:
                                if mouse_y >= HEIGHT*0.75:
                                    if mouse_y >= HEIGHT*0.85:
                                        if mouse_y <= HEIGHT*0.85+size_buttons:
                                            return "Y_button"
                                    elif mouse_y <= HEIGHT*0.75+size_buttons:
                                        return "U_button"
                                elif mouse_y <= HEIGHT*0.65+size_buttons:
                                    return "Q_button"
                            elif mouse_y <= HEIGHT*0.55+size_buttons:
                                return "M_button"
                        elif mouse_y <= HEIGHT*0.45+size_buttons:
                            return "I_button"
                    elif mouse_y <= HEIGHT*0.35+size_buttons:
                        return "E_button"
                elif mouse_y <= HEIGHT*0.25+size_buttons:
                    return "A_button"

    # check if the player is clicking on a letter to change
    if debut_mot <= mouse_x <= debut_mot+size_buttons*n_caracteres:
        if HEIGHT//4+HEIGHT*((n_mot)/10) <= mouse_y <= HEIGHT*((n_mot+1)/10)+HEIGHT//4:
            return int((mouse_x-debut_mot)//(size_buttons))
            # last method
            #for lettre in range(n_caracteres):
            #    if debut_mot+size_buttons*lettre <= mouse_x <= debut_mot+size_buttons*(lettre+1):
            #        return lettre

    return None

def algo_motus(mot_secret:str, mot_joueur:list, mots_joueur:list, lettres_indice:list):
    """
    exemple:

    pizza	| bon mot
    pazia	| mot joueur

    !i!z!	| bon mot
    !a!i!	| mot joueur

    !!!z!	| bon mot
    !a!!!	| mot joueur

    !!!!!	| bon mot
    !!!!!	| mot joueur
    """
    mots_joueur.append([[char.upper(), 0] for char in mot_joueur])
    mot_secret_temp = [lettre.upper() for lettre in mot_secret]
    mot_joueur_temp = [lettre.upper() for lettre in mot_joueur]

    for lettre in range(len(mot_secret_temp)): # look if a letter is at his right place
        if mot_joueur_temp[lettre] == mot_secret_temp[lettre]:
            mots_joueur[-1][lettre] = [mot_joueur_temp[lettre], 2]
            lettres_indice[lettre] = mot_secret_temp[lettre]
            mot_joueur_temp[lettre] = "!"
            mot_secret_temp[lettre] = "!"

    for lettre in range(len(mot_secret_temp)): # look if a letter is not at his right place
        if mot_joueur_temp[lettre] != "!":
            for lettre_ in range(len(mot_secret_temp)):
                if mot_secret_temp[lettre_] != "!":
                    if mot_joueur_temp[lettre] == mot_secret_temp[lettre_]:
                        mots_joueur[-1][lettre] = [mot_joueur_temp[lettre], 1]
                        mot_joueur_temp[lettre] = "!"
                        mot_secret_temp[lettre_] = "!"
                        break

    return mots_joueur, lettres_indice

def buttons_display(is_first_time:bool, images:dict, button_pressed:str, deactivate_button:dict, letter:str, game_over:bool) -> dict:
    """
    update a button on the screen with a letter like "a" or "v" or "enter"
    """
    # add the button to the screen if the game is over or if it's the first time
    if is_first_time or game_over:
        WIN.blit(images["{}_not_pressed".format(letter)].get_image(), images["{}_not_pressed".format(letter)].get_pos())

    # change the state of the button to pressed if the button pressed matches with the letter in argument
    elif button_pressed == "{}_button".format(letter) or button_pressed == letter:
        pg.draw.rect(WIN, BACKGROUND_COLOR, (images["{}_pressed".format(letter)].get_pos()[0], images["{}_pressed".format(letter)].get_pos()[1], WIDTH//20, WIDTH//20))
        WIN.blit(images["{}_pressed".format(letter)].get_image(), images["{}_pressed".format(letter)].get_pos())

    # change the state of the button to not pressed if the button was pressed
    elif "{}_button".format(letter) in deactivate_button or letter in deactivate_button:
        if "{}_button".format(letter) in deactivate_button:
            deactivate_button.pop("{}_button".format(letter))
        else:
            deactivate_button.pop(letter)
        pg.draw.rect(WIN, BACKGROUND_COLOR, (images["{}_not_pressed".format(letter)].get_pos()[0], images["{}_not_pressed".format(letter)].get_pos()[1], WIDTH//20, WIDTH//20))
        WIN.blit(images["{}_not_pressed".format(letter)].get_image(), images["{}_not_pressed".format(letter)].get_pos())

    return deactivate_button

def is_word_empty(mot_joueur):
    for lettre in mot_joueur:
        if lettre == "":
            return True
    return False

def secret_word_display(mot_secret:str, images:dict, n_caracteres:int, debut_mot:float or int):
    """
    add the secret word on the screen
    """
    # add the background for the secret word
    WIN.blit(images["fond_mot_{}".format(str(n_caracteres))], (debut_mot, HEIGHT//2))

    # add the letters for the secret word
    for lettre in range(len(mot_secret)):
        WIN.blit(images[mot_secret[lettre].upper()].get_image(), (debut_mot+(WIDTH//20*lettre), HEIGHT//2))

def add_rows(essai, n_caracteres, debut_mot):
    """
    add the rows
    """
    for lettre in range(n_caracteres-1):
        pg.draw.line(WIN, BLACK, (debut_mot+(WIDTH//20*(lettre+1)), HEIGHT*(essai/10)+HEIGHT//4), (debut_mot+(WIDTH//20*(lettre+1)), HEIGHT*(essai/10)+HEIGHT//4+WIDTH//20-1))

def update_display(images:dict, n_essais:int, n_caracteres:int, button_pressed:str, mot_joueur:list, mot_secret:str, mots_joueur:list, n_mot:int, game_over:bool, pos_edit_letter:int, is_first_time:bool, deactivate_button:dict, lettres_indice:list, time_playthrough:float, do_once_secret_link) -> bool and dict:
    win_ = 0  # win and not windows
    alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    debut_mot = ((WIDTH/2)-(WIDTH//20)*(n_caracteres/2))//1

    if is_first_time or game_over:
        WIN.fill(BACKGROUND_COLOR)
        WIN.blit(images["motus"].get_image(), (0, 0))

    # add the keyboard
    if is_first_time or button_pressed != None or deactivate_button != {} or game_over:
        for letter in alphabet:
            buttons_display(is_first_time, images, button_pressed, deactivate_button, letter, game_over)
        buttons_display(is_first_time, images, button_pressed, deactivate_button, "delete", game_over)
        buttons_display(is_first_time, images, button_pressed, deactivate_button, "enter", game_over)


    # add the background for the words
    if is_first_time or game_over:
        for essai in range(n_essais):
            WIN.blit(images["fond_mot_{}".format(str(n_caracteres))], (debut_mot, HEIGHT*(essai/10)+HEIGHT//4))
    elif button_pressed != "enter":
        WIN.blit(images["fond_mot_{}".format(str(n_caracteres))], (debut_mot, HEIGHT*(n_mot/10)+HEIGHT//4))

    # add the correction of the word
    if button_pressed == "enter" and not is_word_empty(mot_joueur) and not game_over:
        # add the background for the word
        WIN.blit(images["fond_mot_{}".format(str(n_caracteres))], (debut_mot, HEIGHT*((n_mot-1)/10)+HEIGHT//4))
        for lettre in range(n_caracteres):
            # add the correct box
            if mots_joueur[-1][lettre][1] == 2:
                win_ += 1
                if lettre == 0:
                    WIN.blit(images["fond_bonne_lettre_gauche"].get_image(), (debut_mot+(WIDTH//20*lettre), HEIGHT*((n_mot-1)/10)+HEIGHT//4))
                elif lettre == len(mots_joueur[-1])-1:
                    WIN.blit(images["fond_bonne_lettre_droite"].get_image(), (debut_mot+(WIDTH//20*lettre), HEIGHT*((n_mot-1)/10)+HEIGHT//4))
                else:
                    WIN.blit(images["fond_bonne_lettre"].get_image(), (debut_mot+(WIDTH//20*lettre), HEIGHT*((n_mot-1)/10)+HEIGHT//4))
            # add the correct but not at good place box
            elif mots_joueur[-1][lettre][1] == 1:
                WIN.blit(images["fond_lettre_mauvais_endroit"].get_image(), (debut_mot+(WIDTH//20*lettre), HEIGHT*((n_mot-1)/10)+HEIGHT//4))
            # add the letters
            WIN.blit(images[mots_joueur[-1][lettre][0]].get_image(), (debut_mot+(WIDTH//20*lettre), HEIGHT*((n_mot-1)/10)+HEIGHT//4))
        # add the rows
        add_rows(n_mot-1, n_caracteres, debut_mot)
        # add the outline for the word
        WIN.blit(images["coutour_mot_{}".format(str(n_caracteres))], (debut_mot, HEIGHT*((n_mot-1)/10)+HEIGHT//4))
    elif game_over:
        # I put the code which was the last method but it can be a little buggy, I think ...
        for mot in range(len(mots_joueur)):
            for lettre in range(len(mots_joueur[mot])):
                if mots_joueur[mot][lettre][1] == 2:
                    win_ += 1
                    if lettre == 0:
                        WIN.blit(images["fond_bonne_lettre_gauche"].get_image(), (debut_mot+(WIDTH//20*lettre), HEIGHT*(mot/10)+HEIGHT//4))
                    elif lettre == len(mots_joueur[mot])-1:
                        WIN.blit(images["fond_bonne_lettre_droite"].get_image(), (debut_mot+(WIDTH//20*lettre), HEIGHT*(mot/10)+HEIGHT//4))
                    else:
                        WIN.blit(images["fond_bonne_lettre"].get_image(), (debut_mot+(WIDTH//20*lettre), HEIGHT*(mot/10)+HEIGHT//4))
                elif mots_joueur[mot][lettre][1] == 1:
                    win_ = 0
                    WIN.blit(images["fond_lettre_mauvais_endroit"].get_image(), (debut_mot+(WIDTH//20*lettre), HEIGHT*(mot/10)+HEIGHT//4))
                else:
                    win_ = 0
                if mots_joueur[mot][lettre][0] in images:
                    WIN.blit(images[mots_joueur[mot][lettre][0]].get_image(), (debut_mot+(WIDTH//20*lettre), HEIGHT*(mot/10)+HEIGHT//4))
            if win_ >= n_caracteres:
                break
            else:
                win_ = 0

    # add the letters
    if not (n_mot == n_essais or win_ >= n_caracteres) and button_pressed != "enter":
        for lettre in range(n_caracteres):
            if mot_joueur[lettre] != "":
                WIN.blit(images[mot_joueur[lettre]].get_image(), (debut_mot+(WIDTH//20*lettre), HEIGHT*(n_mot/10)+HEIGHT//4))
    elif not (n_mot == n_essais or win_ >= n_caracteres) and button_pressed == "enter" and not is_word_empty(mot_joueur):
        for lettre in range(n_caracteres):
            if lettres_indice[lettre] != "":
                WIN.blit(images[lettres_indice[lettre]].get_image(), (debut_mot+(WIDTH//20*lettre), HEIGHT*(n_mot/10)+HEIGHT//4))

    #add the rows
    if is_first_time or game_over:
        for essai in range(n_essais):
            add_rows(essai, n_caracteres, debut_mot)
    elif button_pressed != "enter":
        add_rows(n_mot, n_caracteres, debut_mot)

    # add the outline for the words
    if is_first_time or game_over:
        for essai in range(n_essais):
            pg.image
            WIN.blit(images["coutour_mot_{}".format(str(n_caracteres))], (debut_mot, HEIGHT*(essai/10)+HEIGHT//4))
    elif button_pressed != "enter":
        WIN.blit(images["coutour_mot_{}".format(str(n_caracteres))], (debut_mot, HEIGHT*(n_mot/10)+HEIGHT//4))

    # add the selection box
    if not (n_mot == n_essais or win_ >= n_caracteres) and not game_over:
        # make the selection box
        if pos_edit_letter < n_caracteres-1:
            WIN.blit(images["contour_lettre_select"].get_image(), (debut_mot+(WIDTH//20*(pos_edit_letter+1)), HEIGHT*(n_mot/10)+HEIGHT//4))
        else:
            WIN.blit(images["contour_lettre_select"].get_image(), (debut_mot+(WIDTH//20*(n_caracteres-1)), HEIGHT*(n_mot/10)+HEIGHT//4))

    # add the game over screen
    if win_ >= n_caracteres:
        WIN.blit(images["fond_transparent"].get_image(), (0, 0))
        WIN.blit(images["gagne"].get_image(), (0, 0))
        secret_word_display(mot_secret, images, n_caracteres, debut_mot)
        game_over = True
    elif n_mot == n_essais:
        WIN.blit(images["fond_transparent"].get_image(), (0, 0))
        WIN.blit(images["perdu"].get_image(), (0, 0))
        secret_word_display(mot_secret, images, n_caracteres, debut_mot)
        game_over = True

    # add the searche button
    open_link = False
    if button_pressed != "searche" and game_over:
        WIN.blit(images["searche_not_pressed"].get_image(), ((debut_mot+(WIDTH//20*(n_caracteres+0.5)))//1, HEIGHT//2))
    elif game_over:
        WIN.blit(images["searche_pressed"].get_image(), ((debut_mot+(WIDTH//20*(n_caracteres+0.5)))//1, HEIGHT//2))
        open_link = True
    if open_link and game_over:
        url = "https://www.google.com/search?q={}".format(mot_secret)
        webbrowser.open(url, new=0, autoraise=True)

    # setup the chrono   891 716
    if not game_over:
        setup_chrono(images, time_playthrough)
    else: setup_chrono(images, time_playthrough, WIDTH*0.46406, HEIGHT*0.6455)

    # setup the points
    if game_over:
        if mot_secret == "rickroll" and do_once_secret_link:
            do_once_secret_link = False
            webbrowser.open("https://www.youtube.com/watch?v=dQw4w9WgXcQ", new=0, autoraise=True)
            time.sleep(2)
            pg.quit()
            sys.exit()
        setup_points(images, n_essais, n_caracteres, n_mot, lettres_indice, time_playthrough)

    # add the exit button
    if button_pressed != "exit":
        WIN.blit(images["exit_not_pressed"].get_image(), images["exit_not_pressed"].get_pos())
    else:   WIN.blit(images["exit_pressed"].get_image(), images["exit_pressed"].get_pos())

    # add the reset button
    if button_pressed != "reset":
        WIN.blit(images["reset_not_pressed"].get_image(), images["reset_not_pressed"].get_pos())
    else:   WIN.blit(images["reset_pressed"].get_image(), images["reset_pressed"].get_pos())

    # update the screen
    pg.display.update()

    return game_over, deactivate_button, do_once_secret_link

def setup_points(images, n_essais, n_caracteres, n_mot, lettres_indice, time_playthrough):
    """
    setup the points and add it to the screen
    """
    # setup the variables
    scale = images["chrono"].get_scale()[0]*0.75
    point = 0

    # points by number of try
    if not "" in lettres_indice:
        point += (n_essais-n_mot+1)*100

    # point by number of good letters
    for char in lettres_indice:
        if char != "":
            point += 75

    # remove points from the letters that was already there
    if n_caracteres > 7:
        point -= 150
    else: point -= 75

    # points by the time of the game
    if not "" in lettres_indice:
        seconds = 150
        point_time = (seconds-time_playthrough//1)*2
        if point_time < 0: point_time = 0
        point += point_time

    # add the points to the screen
    if point < 0: point = 0
    point_str = str(int(point))
    for n in range(len(point_str)):
        WIN.blit(images[point_str[n]].get_image(), (WIDTH*0.497+scale*int(n), HEIGHT*0.7574))

def setup_chrono(images, time_playthrough, x_pos=-1, y_pos=-1):
    """
    setup the chronometer
    """
    # setup the variables
    if x_pos == -1 and y_pos == -1:
        x_pos = images["chrono"].get_pos()[0]
        y_pos = images["chrono"].get_pos()[1]
    size_numbers = images["chrono"].get_scale()[0]

    # add the image of the chrono
    if x_pos == images["chrono"].get_pos()[0] and y_pos == images["chrono"].get_pos()[1]:
        WIN.blit(images["chrono"].get_image(), images["chrono"].get_pos())
    else:
        WIN.blit(images["chrono"].get_image(), (x_pos+size_numbers*3.85, y_pos*.992))

    # get the minutes and the seconds of the time of the playthrough by using time_playthrough
    minutes = time_playthrough//60
    seconds = time_playthrough//1
    if seconds >= 60:
        seconds %= 60

    # add the minutes of the playthrough time
    WIN.blit(images[str(int(minutes//10))].get_image(), (x_pos+size_numbers, y_pos))
    WIN.blit(images[str(int(minutes%10))].get_image(), (x_pos+size_numbers*1.5, y_pos))

    # add the two dots for the playthrough time
    WIN.blit(images[":"].get_image(), (x_pos+size_numbers*2, y_pos))

    # add the seconds of the playthrough time
    WIN.blit(images[str(int(seconds//10))].get_image(), (x_pos+size_numbers*2.5, y_pos))
    WIN.blit(images[str(int(seconds%10))].get_image(), (x_pos+size_numbers*3, y_pos))

def extract_secret_word(n_caracteres:int, current_path_file:str) -> list:
    """
    return a list with all the words by n_caracteres and uses the .txt file by using the current_path_file
    """
    with open(current_path_file+"mots\\mots_{}_lettres_correct.txt".format(str(n_caracteres)), "r", encoding="UTF-8") as t:
        t_ = t.read()
        mots = []
        do_once = True
        for char in range(len(t_)-1): # -1 because the last character is "|"
            if do_once:
                mots.append("")
                do_once = False
            if t_[char] != "|":
                mots[-1] += t_[char]
            else:
                do_once = True

    return mots

def setup_images(current_path_file:str) -> dict:
    """
    Get the images from their path file and put them into a dict
    """
    size_buttons = WIDTH//20
    size_letters = WIDTH//20
    size_numbers = WIDTH//24

    image_motus = Image(pg.image.load(current_path_file+"MOTUS.png"), WIDTH, HEIGHT)
    image_motus.scale()
    image_fond_bonne_lettre = Image(pg.image.load(current_path_file+"fond_lettre\\fond_bonne_lettre.png"), size_letters, size_letters)
    image_fond_bonne_lettre.scale()
    image_fond_bonne_lettre_gauche = Image(pg.image.load(current_path_file+"fond_lettre\\fond_bonne_lettre_gauche.png"), size_letters, size_letters)
    image_fond_bonne_lettre_gauche.scale()
    image_fond_bonne_lettre_droite = Image(pg.image.load(current_path_file+"fond_lettre\\fond_bonne_lettre_droite.png"), size_letters, size_letters)
    image_fond_bonne_lettre_droite.scale()
    image_fond_lettre_mauvais_endroit = Image(pg.image.load(current_path_file+"fond_lettre\\fond_lettre_mauvais_endroit.png"), size_letters, size_letters)
    image_fond_lettre_mauvais_endroit.scale()
    image_fond_gagne = Image(pg.image.load(current_path_file+"image_gagne.png"), WIDTH, HEIGHT)
    image_fond_gagne.scale()
    image_fond_perdu = Image(pg.image.load(current_path_file+"image_perdu.png"), WIDTH, HEIGHT)
    image_fond_perdu.scale()
    image_fond_transparent = Image(pg.image.load(current_path_file+"fond_transparent.png"), WIDTH, HEIGHT)
    image_fond_transparent.scale()
    image_Contour_lettre_select = Image(pg.image.load(current_path_file+"Contour_lettre_select.png"), size_letters, size_letters)
    image_Contour_lettre_select.scale()
    image_chrono = Image(pg.image.load(current_path_file+"Chrono.png"), size_numbers, size_numbers)
    image_chrono.scale()
    image_chrono.set_pos((WIDTH*0.743, HEIGHT*0.04166))

    image_delete_not_pressed = Image(pg.image.load(current_path_file+"other_buttons\\delete_not_pressed.png"), WIDTH//20, WIDTH//20)
    image_delete_not_pressed.scale()
    image_delete_not_pressed.set_pos((WIDTH*0.11718, HEIGHT*0.85))
    image_delete_pressed = Image(pg.image.load(current_path_file+"other_buttons\\delete_pressed.png"), WIDTH//20, WIDTH//20)
    image_delete_pressed.scale()
    image_delete_pressed.set_pos(image_delete_not_pressed.get_pos())
    image_exit_not_pressed = Image(pg.image.load(current_path_file+"other_buttons\\exit_not_pressed.png"), WIDTH//20, WIDTH//20)
    image_exit_not_pressed.scale()
    image_exit_not_pressed.set_pos((0.03906*WIDTH-(math.sqrt(WIDTH**2+HEIGHT**2)*0.02269), (0.06944*HEIGHT)//2))
    image_exit_pressed = Image(pg.image.load(current_path_file+"other_buttons\\exit_pressed.png"), WIDTH//20, WIDTH//20)
    image_exit_pressed.scale()
    image_exit_pressed.set_pos(image_exit_not_pressed.get_pos())
    image_enter_not_pressed = Image(pg.image.load(current_path_file+"other_buttons\\ok_not_pressed.png"), WIDTH//20, WIDTH//20)
    image_enter_not_pressed.scale()
    image_enter_not_pressed.set_pos((WIDTH*0.16927, HEIGHT*0.85))
    image_enter_pressed = Image(pg.image.load(current_path_file+"other_buttons\\ok_pressed.png"), WIDTH//20, WIDTH//20)
    image_enter_pressed.scale()
    image_enter_pressed.set_pos(image_enter_not_pressed.get_pos())
    image_reset_not_pressed = Image(pg.image.load(current_path_file+"other_buttons\\reset_not_pressed.png"), WIDTH//20, WIDTH//20)
    image_reset_not_pressed.scale()
    image_reset_not_pressed.set_pos((0.93750*WIDTH-(math.sqrt(WIDTH**2+HEIGHT**2)*0.02269), (0.06944*HEIGHT)//2))
    image_reset_pressed = Image(pg.image.load(current_path_file+"other_buttons\\reset_pressed.png"), WIDTH//20, WIDTH//20)
    image_reset_pressed.scale()
    image_reset_pressed.set_pos(image_reset_not_pressed.get_pos())
    image_searche_not_pressed = Image(pg.image.load(current_path_file+"other_buttons\\searche_not_pressed.png"), WIDTH//20, WIDTH//20)
    image_searche_not_pressed.scale()
    image_searche_pressed = Image(pg.image.load(current_path_file+"other_buttons\\searche_pressed.png"), WIDTH//20, WIDTH//20)
    image_searche_pressed.scale()

    # setup the images of the not pressed buttons
    image_A_not_pressed = Image(pg.image.load(current_path_file+"not_pressed\\A_not_pressed.png"), size_buttons, size_buttons)
    image_A_not_pressed.scale()
    image_A_not_pressed.set_pos((WIDTH*0.01302, HEIGHT*0.25))
    image_B_not_pressed = Image(pg.image.load(current_path_file+"not_pressed\\B_not_pressed.png"), size_buttons, size_buttons)
    image_B_not_pressed.scale()
    image_B_not_pressed.set_pos((WIDTH*0.06510, HEIGHT*0.25))
    image_C_not_pressed = Image(pg.image.load(current_path_file+"not_pressed\\C_not_pressed.png"), size_buttons, size_buttons)
    image_C_not_pressed.scale()
    image_C_not_pressed.set_pos((WIDTH*0.11718, HEIGHT*0.25))
    image_D_not_pressed = Image(pg.image.load(current_path_file+"not_pressed\\D_not_pressed.png"), size_buttons, size_buttons)
    image_D_not_pressed.scale()
    image_D_not_pressed.set_pos((WIDTH*0.16927, HEIGHT*0.25))
    image_E_not_pressed = Image(pg.image.load(current_path_file+"not_pressed\\E_not_pressed.png"), size_buttons, size_buttons)
    image_E_not_pressed.scale()
    image_E_not_pressed.set_pos((WIDTH*0.01302, HEIGHT*0.35))
    image_F_not_pressed = Image(pg.image.load(current_path_file+"not_pressed\\F_not_pressed.png"), size_buttons, size_buttons)
    image_F_not_pressed.scale()
    image_F_not_pressed.set_pos((WIDTH*0.06510, HEIGHT*0.35))
    image_G_not_pressed = Image(pg.image.load(current_path_file+"not_pressed\\G_not_pressed.png"), size_buttons, size_buttons)
    image_G_not_pressed.scale()
    image_G_not_pressed.set_pos((WIDTH*0.11718, HEIGHT*0.35))
    image_H_not_pressed = Image(pg.image.load(current_path_file+"not_pressed\\H_not_pressed.png"), size_buttons, size_buttons)
    image_H_not_pressed.scale()
    image_H_not_pressed.set_pos((WIDTH*0.16927, HEIGHT*0.35))
    image_I_not_pressed = Image(pg.image.load(current_path_file+"not_pressed\\I_not_pressed.png"), size_buttons, size_buttons)
    image_I_not_pressed.scale()
    image_I_not_pressed.set_pos((WIDTH*0.01302, HEIGHT*0.45))
    image_J_not_pressed = Image(pg.image.load(current_path_file+"not_pressed\\J_not_pressed.png"), size_buttons, size_buttons)
    image_J_not_pressed.scale()
    image_J_not_pressed.set_pos((WIDTH*0.06510, HEIGHT*0.45))
    image_K_not_pressed = Image(pg.image.load(current_path_file+"not_pressed\\K_not_pressed.png"), size_buttons, size_buttons)
    image_K_not_pressed.scale()
    image_K_not_pressed.set_pos((WIDTH*0.11718, HEIGHT*0.45))
    image_L_not_pressed = Image(pg.image.load(current_path_file+"not_pressed\\L_not_pressed.png"), size_buttons, size_buttons)
    image_L_not_pressed.scale()
    image_L_not_pressed.set_pos((WIDTH*0.16927, HEIGHT*0.45))
    image_M_not_pressed = Image(pg.image.load(current_path_file+"not_pressed\\M_not_pressed.png"), size_buttons, size_buttons)
    image_M_not_pressed.scale()
    image_M_not_pressed.set_pos((WIDTH*0.01302, HEIGHT*0.55))
    image_N_not_pressed = Image(pg.image.load(current_path_file+"not_pressed\\N_not_pressed.png"), size_buttons, size_buttons)
    image_N_not_pressed.scale()
    image_N_not_pressed.set_pos((WIDTH*0.06510, HEIGHT*0.55))
    image_O_not_pressed = Image(pg.image.load(current_path_file+"not_pressed\\O_not_pressed.png"), size_buttons, size_buttons)
    image_O_not_pressed.scale()
    image_O_not_pressed.set_pos((WIDTH*0.11718, HEIGHT*0.55))
    image_P_not_pressed = Image(pg.image.load(current_path_file+"not_pressed\\P_not_pressed.png"), size_buttons, size_buttons)
    image_P_not_pressed.scale()
    image_P_not_pressed.set_pos((WIDTH*0.16927, HEIGHT*0.55))
    image_Q_not_pressed = Image(pg.image.load(current_path_file+"not_pressed\\Q_not_pressed.png"), size_buttons, size_buttons)
    image_Q_not_pressed.scale()
    image_Q_not_pressed.set_pos((WIDTH*0.01302, HEIGHT*0.65))
    image_R_not_pressed = Image(pg.image.load(current_path_file+"not_pressed\\R_not_pressed.png"), size_buttons, size_buttons)
    image_R_not_pressed.scale()
    image_R_not_pressed.set_pos((WIDTH*0.06510, HEIGHT*0.65))
    image_S_not_pressed = Image(pg.image.load(current_path_file+"not_pressed\\S_not_pressed.png"), size_buttons, size_buttons)
    image_S_not_pressed.scale()
    image_S_not_pressed.set_pos((WIDTH*0.11718, HEIGHT*0.65))
    image_T_not_pressed = Image(pg.image.load(current_path_file+"not_pressed\\T_not_pressed.png"), size_buttons, size_buttons)
    image_T_not_pressed.scale()
    image_T_not_pressed.set_pos((WIDTH*0.16927, HEIGHT*0.65))
    image_U_not_pressed = Image(pg.image.load(current_path_file+"not_pressed\\U_not_pressed.png"), size_buttons, size_buttons)
    image_U_not_pressed.scale()
    image_U_not_pressed.set_pos((WIDTH*0.01302, HEIGHT*0.75))
    image_V_not_pressed = Image(pg.image.load(current_path_file+"not_pressed\\V_not_pressed.png"), size_buttons, size_buttons)
    image_V_not_pressed.scale()
    image_V_not_pressed.set_pos((WIDTH*0.06510, HEIGHT*0.75))
    image_W_not_pressed = Image(pg.image.load(current_path_file+"not_pressed\\W_not_pressed.png"), size_buttons, size_buttons)
    image_W_not_pressed.scale()
    image_W_not_pressed.set_pos((WIDTH*0.11718, HEIGHT*0.75))
    image_X_not_pressed = Image(pg.image.load(current_path_file+"not_pressed\\X_not_pressed.png"), size_buttons, size_buttons)
    image_X_not_pressed.scale()
    image_X_not_pressed.set_pos((WIDTH*0.16927, HEIGHT*0.75))
    image_Y_not_pressed = Image(pg.image.load(current_path_file+"not_pressed\\Y_not_pressed.png"), size_buttons, size_buttons)
    image_Y_not_pressed.scale()
    image_Y_not_pressed.set_pos((WIDTH*0.01302, HEIGHT*0.85))
    image_Z_not_pressed = Image(pg.image.load(current_path_file+"not_pressed\\Z_not_pressed.png"), size_buttons, size_buttons)
    image_Z_not_pressed.scale()
    image_Z_not_pressed.set_pos((WIDTH*0.06510, HEIGHT*0.85))

    image_A_pressed = Image(pg.image.load(current_path_file+"pressed\\A_pressed.png"), size_buttons, size_buttons)
    image_A_pressed.scale()
    image_A_pressed.set_pos(image_A_not_pressed.get_pos())
    image_B_pressed = Image(pg.image.load(current_path_file+"pressed\\B_pressed.png"), size_buttons, size_buttons)
    image_B_pressed.scale()
    image_B_pressed.set_pos(image_B_not_pressed.get_pos())
    image_C_pressed = Image(pg.image.load(current_path_file+"pressed\\C_pressed.png"), size_buttons, size_buttons)
    image_C_pressed.scale()
    image_C_pressed.set_pos(image_C_not_pressed.get_pos())
    image_D_pressed = Image(pg.image.load(current_path_file+"pressed\\D_pressed.png"), size_buttons, size_buttons)
    image_D_pressed.scale()
    image_D_pressed.set_pos(image_D_not_pressed.get_pos())
    image_E_pressed = Image(pg.image.load(current_path_file+"pressed\\E_pressed.png"), size_buttons, size_buttons)
    image_E_pressed.scale()
    image_E_pressed.set_pos(image_E_not_pressed.get_pos())
    image_F_pressed = Image(pg.image.load(current_path_file+"pressed\\F_pressed.png"), size_buttons, size_buttons)
    image_F_pressed.scale()
    image_F_pressed.set_pos(image_F_not_pressed.get_pos())
    image_G_pressed = Image(pg.image.load(current_path_file+"pressed\\G_pressed.png"), size_buttons, size_buttons)
    image_G_pressed.scale()
    image_G_pressed.set_pos(image_G_not_pressed.get_pos())
    image_H_pressed = Image(pg.image.load(current_path_file+"pressed\\H_pressed.png"), size_buttons, size_buttons)
    image_H_pressed.scale()
    image_H_pressed.set_pos(image_H_not_pressed.get_pos())
    image_I_pressed = Image(pg.image.load(current_path_file+"pressed\\I_pressed.png"), size_buttons, size_buttons)
    image_I_pressed.scale()
    image_I_pressed.set_pos(image_I_not_pressed.get_pos())
    image_J_pressed = Image(pg.image.load(current_path_file+"pressed\\J_pressed.png"), size_buttons, size_buttons)
    image_J_pressed.scale()
    image_J_pressed.set_pos(image_J_not_pressed.get_pos())
    image_K_pressed = Image(pg.image.load(current_path_file+"pressed\\K_pressed.png"), size_buttons, size_buttons)
    image_K_pressed.scale()
    image_K_pressed.set_pos(image_K_not_pressed.get_pos())
    image_L_pressed = Image(pg.image.load(current_path_file+"pressed\\L_pressed.png"), size_buttons, size_buttons)
    image_L_pressed.scale()
    image_L_pressed.set_pos(image_L_not_pressed.get_pos())
    image_M_pressed = Image(pg.image.load(current_path_file+"pressed\\M_pressed.png"), size_buttons, size_buttons)
    image_M_pressed.scale()
    image_M_pressed.set_pos(image_M_not_pressed.get_pos())
    image_N_pressed = Image(pg.image.load(current_path_file+"pressed\\N_pressed.png"), size_buttons, size_buttons)
    image_N_pressed.scale()
    image_N_pressed.set_pos(image_N_not_pressed.get_pos())
    image_O_pressed = Image(pg.image.load(current_path_file+"pressed\\O_pressed.png"), size_buttons, size_buttons)
    image_O_pressed.scale()
    image_O_pressed.set_pos(image_O_not_pressed.get_pos())
    image_P_pressed = Image(pg.image.load(current_path_file+"pressed\\P_pressed.png"), size_buttons, size_buttons)
    image_P_pressed.scale()
    image_P_pressed.set_pos(image_P_not_pressed.get_pos())
    image_Q_pressed = Image(pg.image.load(current_path_file+"pressed\\Q_pressed.png"), size_buttons, size_buttons)
    image_Q_pressed.scale()
    image_Q_pressed.set_pos(image_Q_not_pressed.get_pos())
    image_R_pressed = Image(pg.image.load(current_path_file+"pressed\\R_pressed.png"), size_buttons, size_buttons)
    image_R_pressed.scale()
    image_R_pressed.set_pos(image_R_not_pressed.get_pos())
    image_S_pressed = Image(pg.image.load(current_path_file+"pressed\\S_pressed.png"), size_buttons, size_buttons)
    image_S_pressed.scale()
    image_S_pressed.set_pos(image_S_not_pressed.get_pos())
    image_T_pressed = Image(pg.image.load(current_path_file+"pressed\\T_pressed.png"), size_buttons, size_buttons)
    image_T_pressed.scale()
    image_T_pressed.set_pos(image_T_not_pressed.get_pos())
    image_U_pressed = Image(pg.image.load(current_path_file+"pressed\\U_pressed.png"), size_buttons, size_buttons)
    image_U_pressed.scale()
    image_U_pressed.set_pos(image_U_not_pressed.get_pos())
    image_V_pressed = Image(pg.image.load(current_path_file+"pressed\\V_pressed.png"), size_buttons, size_buttons)
    image_V_pressed.scale()
    image_V_pressed.set_pos(image_V_not_pressed.get_pos())
    image_W_pressed = Image(pg.image.load(current_path_file+"pressed\\W_pressed.png"), size_buttons, size_buttons)
    image_W_pressed.scale()
    image_W_pressed.set_pos(image_W_not_pressed.get_pos())
    image_X_pressed = Image(pg.image.load(current_path_file+"pressed\\X_pressed.png"), size_buttons, size_buttons)
    image_X_pressed.scale()
    image_X_pressed.set_pos(image_X_not_pressed.get_pos())
    image_Y_pressed = Image(pg.image.load(current_path_file+"pressed\\Y_pressed.png"), size_buttons, size_buttons)
    image_Y_pressed.scale()
    image_Y_pressed.set_pos(image_Y_not_pressed.get_pos())
    image_Z_pressed = Image(pg.image.load(current_path_file+"pressed\\Z_pressed.png"), size_buttons, size_buttons)
    image_Z_pressed.scale()
    image_Z_pressed.set_pos(image_Z_not_pressed.get_pos())

    image_A = Image(pg.image.load(current_path_file+"letters\\A.png"), size_letters, size_letters)
    image_A.scale()
    image_B = Image(pg.image.load(current_path_file+"letters\\B.png"), size_letters, size_letters)
    image_B.scale()
    image_C = Image(pg.image.load(current_path_file+"letters\\C.png"), size_letters, size_letters)
    image_C.scale()
    image_D = Image(pg.image.load(current_path_file+"letters\\D.png"), size_letters, size_letters)
    image_D.scale()
    image_E = Image(pg.image.load(current_path_file+"letters\\E.png"), size_letters, size_letters)
    image_E.scale()
    image_F = Image(pg.image.load(current_path_file+"letters\\F.png"), size_letters, size_letters)
    image_F.scale()
    image_G = Image(pg.image.load(current_path_file+"letters\\G.png"), size_letters, size_letters)
    image_G.scale()
    image_H = Image(pg.image.load(current_path_file+"letters\\H.png"), size_letters, size_letters)
    image_H.scale()
    image_I = Image(pg.image.load(current_path_file+"letters\\I.png"), size_letters, size_letters)
    image_I.scale()
    image_J = Image(pg.image.load(current_path_file+"letters\\J.png"), size_letters, size_letters)
    image_J.scale()
    image_K = Image(pg.image.load(current_path_file+"letters\\K.png"), size_letters, size_letters)
    image_K.scale()
    image_L = Image(pg.image.load(current_path_file+"letters\\L.png"), size_letters, size_letters)
    image_L.scale()
    image_M = Image(pg.image.load(current_path_file+"letters\\M.png"), size_letters, size_letters)
    image_M.scale()
    image_N = Image(pg.image.load(current_path_file+"letters\\N.png"), size_letters, size_letters)
    image_N.scale()
    image_O = Image(pg.image.load(current_path_file+"letters\\O.png"), size_letters, size_letters)
    image_O.scale()
    image_P = Image(pg.image.load(current_path_file+"letters\\P.png"), size_letters, size_letters)
    image_P.scale()
    image_Q = Image(pg.image.load(current_path_file+"letters\\Q.png"), size_letters, size_letters)
    image_Q.scale()
    image_R = Image(pg.image.load(current_path_file+"letters\\R.png"), size_letters, size_letters)
    image_R.scale()
    image_S = Image(pg.image.load(current_path_file+"letters\\S.png"), size_letters, size_letters)
    image_S.scale()
    image_T = Image(pg.image.load(current_path_file+"letters\\T.png"), size_letters, size_letters)
    image_T.scale()
    image_U = Image(pg.image.load(current_path_file+"letters\\U.png"), size_letters, size_letters)
    image_U.scale()
    image_V = Image(pg.image.load(current_path_file+"letters\\V.png"), size_letters, size_letters)
    image_V.scale()
    image_W = Image(pg.image.load(current_path_file+"letters\\W.png"), size_letters, size_letters)
    image_W.scale()
    image_X = Image(pg.image.load(current_path_file+"letters\\X.png"), size_letters, size_letters)
    image_X.scale()
    image_Y = Image(pg.image.load(current_path_file+"letters\\Y.png"), size_letters, size_letters)
    image_Y.scale()
    image_Z = Image(pg.image.load(current_path_file+"letters\\Z.png"), size_letters, size_letters)
    image_Z.scale()

    # setup the images of the numbers
    image_zero = Image(pg.image.load(current_path_file+"Numbers\\zero.png"), size_numbers, size_numbers)
    image_zero.scale()
    image_one = Image(pg.image.load(current_path_file+"Numbers\\one.png"), size_numbers, size_numbers)
    image_one.scale()
    image_two = Image(pg.image.load(current_path_file+"Numbers\\two.png"), size_numbers, size_numbers)
    image_two.scale()
    image_three = Image(pg.image.load(current_path_file+"Numbers\\three.png"), size_numbers, size_numbers)
    image_three.scale()
    image_four = Image(pg.image.load(current_path_file+"Numbers\\four.png"), size_numbers, size_numbers)
    image_four.scale()
    image_five = Image(pg.image.load(current_path_file+"Numbers\\five.png"), size_numbers, size_numbers)
    image_five.scale()
    image_six = Image(pg.image.load(current_path_file+"Numbers\\six.png"), size_numbers, size_numbers)
    image_six.scale()
    image_seven = Image(pg.image.load(current_path_file+"Numbers\\seven.png"), size_numbers, size_numbers)
    image_seven.scale()
    image_eight = Image(pg.image.load(current_path_file+"Numbers\\eight.png"), size_numbers, size_numbers)
    image_eight.scale()
    image_nine = Image(pg.image.load(current_path_file+"Numbers\\nine.png"), size_numbers, size_numbers)
    image_nine.scale()
    image_two_dots = Image(pg.image.load(current_path_file+"Numbers\\two_dots.png"), size_numbers, size_numbers)
    image_two_dots.scale()

    # add the images in a dict named images
    images = {"motus": image_motus, "fond_bonne_lettre": image_fond_bonne_lettre, "fond_bonne_lettre_gauche": image_fond_bonne_lettre_gauche, "fond_bonne_lettre_droite": image_fond_bonne_lettre_droite, "fond_lettre_mauvais_endroit": image_fond_lettre_mauvais_endroit, "gagne": image_fond_gagne, "perdu": image_fond_perdu, "delete_not_pressed": image_delete_not_pressed, "delete_pressed": image_delete_pressed, "exit_not_pressed": image_exit_not_pressed, "exit_pressed": image_exit_pressed, "enter_not_pressed": image_enter_not_pressed, "enter_pressed": image_enter_pressed, "reset_not_pressed": image_reset_not_pressed, "reset_pressed": image_reset_pressed, "contour_lettre_select": image_Contour_lettre_select,"searche_not_pressed": image_searche_not_pressed, "searche_pressed": image_searche_pressed, "fond_transparent": image_fond_transparent, "chrono": image_chrono,
    "A_not_pressed": image_A_not_pressed, "B_not_pressed": image_B_not_pressed, "C_not_pressed": image_C_not_pressed, "D_not_pressed": image_D_not_pressed, "E_not_pressed": image_E_not_pressed, "F_not_pressed": image_F_not_pressed, "G_not_pressed": image_G_not_pressed, "H_not_pressed": image_H_not_pressed, "I_not_pressed": image_I_not_pressed, "J_not_pressed": image_J_not_pressed, "K_not_pressed": image_K_not_pressed, "L_not_pressed": image_L_not_pressed, "M_not_pressed": image_M_not_pressed, "N_not_pressed": image_N_not_pressed, "O_not_pressed": image_O_not_pressed, "P_not_pressed": image_P_not_pressed, "Q_not_pressed": image_Q_not_pressed, "R_not_pressed": image_R_not_pressed, "S_not_pressed": image_S_not_pressed, "T_not_pressed": image_T_not_pressed, "U_not_pressed": image_U_not_pressed, "V_not_pressed": image_V_not_pressed, "W_not_pressed": image_W_not_pressed, "X_not_pressed": image_X_not_pressed, "Y_not_pressed": image_Y_not_pressed, "Z_not_pressed": image_Z_not_pressed,
    "A_pressed": image_A_pressed, "B_pressed": image_B_pressed, "C_pressed": image_C_pressed, "D_pressed": image_D_pressed, "E_pressed": image_E_pressed, "F_pressed": image_F_pressed, "G_pressed": image_G_pressed, "H_pressed": image_H_pressed, "I_pressed": image_I_pressed, "J_pressed": image_J_pressed, "K_pressed": image_K_pressed, "L_pressed": image_L_pressed, "M_pressed": image_M_pressed, "N_pressed": image_N_pressed, "O_pressed": image_O_pressed, "P_pressed": image_P_pressed, "Q_pressed": image_Q_pressed, "R_pressed": image_R_pressed, "S_pressed": image_S_pressed, "T_pressed": image_T_pressed, "U_pressed": image_U_pressed, "V_pressed": image_V_pressed, "W_pressed": image_W_pressed, "X_pressed": image_X_pressed, "Y_pressed": image_Y_pressed, "Z_pressed": image_Z_pressed,
    "A": image_A, "B": image_B, "C": image_C, "D": image_D, "E": image_E, "F": image_F, "G": image_G, "H": image_H, "I": image_I, "J": image_J, "K": image_K, "L": image_L, "M": image_M, "N": image_N, "O": image_O, "P": image_P, "Q": image_Q, "R": image_R, "S": image_S, "T": image_T, "U": image_U, "V": image_V, "W": image_W, "X": image_X, "Y": image_Y, "Z": image_Z,
    "0": image_zero, "1": image_one, "2": image_two, "3": image_three, "4": image_four, "5": image_five, "6": image_six, "7": image_seven, "8": image_eight, "9": image_nine, ":": image_two_dots
    }

    # create the words' outline and put them into a dict named images
    for n_char in range(5, 11):
        images["coutour_mot_{}".format(str(n_char))] = create_contour_word(current_path_file, n_char)

    # create the words' background and put them into a dict named images
    for n_char in range(5, 11):
        images["fond_mot_{}".format(str(n_char))] = create_background_word(current_path_file, n_char)

    return images

def main(fps, n_essais):
    # get the path of the file
    ##current_path_file = __file__
    ##current_path_file_temp = ""
    ##for char in range(len(current_path_file)-7): # -7 because "main.py" is 7 characteres
    ##    current_path_file_temp += current_path_file[char]
    ##current_path_file = current_path_file_temp+"data\\"
    current_path_file = "data\\"

    # setup the images
    images = setup_images(current_path_file)

    # setup the dictionary
    dictonary = {}
    for n_letters in range(5, 11):
        dictonary["{}_letters".format(n_letters)] = extract_secret_word(n_letters, current_path_file)

    # setup the secret word
    n_caracteres = random.randint(5, 10)
    length_dict_words = len(dictonary["{}_letters".format(n_caracteres)])
    mot_secret = dictonary["{}_letters".format(n_caracteres)] [random.randint(0, length_dict_words-1)]

    frame = 0
    pause = False
    time_start_frame = 0
    time_end_frame = 0
    did_click_left = False
    button_pressed = None
    remove_button = False
    do_once_remove_button = False
    start_frame_remove_button = 0
    mots_joueur = [] # ex = [[a, 1], [r, 2], [e, 0] ...]    0 = mauvais    1 = mauvaise place   2 = bonne place
    lettres_indice = ["" for char in range(n_caracteres)]
    lettres_indice[0] = mot_secret[0].upper()
    if n_caracteres > 7:
        n_random = random.randint(2, 3)
        lettres_indice[n_random] = mot_secret[n_random].upper()
    mot_joueur = lettres_indice[:]
    alphabet = ["A_button", "B_button", "C_button", "D_button", "E_button", "F_button", "G_button", "H_button", "I_button", "J_button", "K_button", "L_button", "M_button", "N_button", "O_button", "P_button", "Q_button", "R_button", "S_button", "T_button", "U_button", "V_button", "W_button", "X_button", "Y_button", "Z_button"]
    n_mot = 0
    game_over = False
    pos_edit_letter = 0
    counter_frame_click_left_mouse = 0
    counter_frame_keyboard = 0
    letter_keyboard = ""
    mouse_x, mouse_y = 0, 0
    run = True
    is_first_time = True
    deactivate_button = {}
    time_playthrough = 0
    last_time_playthrough = 0
    time_start_game = time.time()

    do_once_secret_link = True
    game_over, deactivate_button, do_once_secret_link = update_display(images, n_essais, n_caracteres, button_pressed, mot_joueur, mot_secret, mots_joueur, n_mot, game_over, pos_edit_letter, is_first_time, deactivate_button, lettres_indice, time_playthrough, do_once_secret_link)
    is_first_time = False

    # boucle principale
    while run:
        if not pause:
            time_start_frame = time.time()
            frame += 1

        # actions with the keyboard
        if letter_keyboard != "":
            # allow the player to delete a letter of the word by pressing the delete key
            if letter_keyboard == "delete" and not game_over:
                if pos_edit_letter < n_caracteres-1:
                    mot_joueur[pos_edit_letter+1] = ""
                elif pos_edit_letter >= n_caracteres-1:
                    mot_joueur[pos_edit_letter] = ""
                    pos_edit_letter -= 1
                if pos_edit_letter > -1:
                    pos_edit_letter -= 1

            # allow the player to verify the word with the enter key
            elif letter_keyboard == "enter" and not is_word_empty(mot_joueur) and n_mot < n_essais and not game_over:
                n_mot += 1
                button_pressed = "enter"
                mots_joueur, lettres_indice = algo_motus(mot_secret, mot_joueur, mots_joueur, lettres_indice)
                pos_edit_letter = -1
                for lettre in range(len(lettres_indice)):
                    if lettres_indice[lettre] == "":
                        pos_edit_letter = lettre-1
                        break
                game_over, deactivate_button, do_once_secret_link = update_display(images, n_essais, n_caracteres, button_pressed, mot_joueur, mot_secret, mots_joueur, n_mot, game_over, pos_edit_letter, is_first_time, deactivate_button, lettres_indice, time_playthrough, do_once_secret_link)
                deactivate_button[button_pressed] = True
                remove_button = True
                mot_joueur = lettres_indice[:]

            # allow the player to move the position of the pos_edit_letter with the right or left key
            elif letter_keyboard == "left" and pos_edit_letter > -1:
                pos_edit_letter -= 1
            elif letter_keyboard == "right" and pos_edit_letter < n_caracteres-2:
                pos_edit_letter += 1

            # allow the player to write with keyboard
            elif letter_keyboard in [word[0] for word in alphabet]:
                if n_mot < n_essais and not game_over and pos_edit_letter < n_caracteres:
                    if pos_edit_letter+1 < n_caracteres:
                        pos_edit_letter += 1
                    mot_joueur[pos_edit_letter] = letter_keyboard
                    if pos_edit_letter+2 > n_caracteres:
                        pos_edit_letter -= 1

            letter_keyboard = ""
            game_over, deactivate_button, do_once_secret_link = update_display(images, n_essais, n_caracteres, button_pressed, mot_joueur, mot_secret, mots_joueur, n_mot, game_over, pos_edit_letter, is_first_time, deactivate_button, lettres_indice, time_playthrough, do_once_secret_link)
            button_pressed = None

        # actions with the left mouse button
        if did_click_left and not pause and frame >= counter_frame_click_left_mouse and letter_keyboard == "":
            # DEBUG
            # print(mouse_x, mouse_y)

            button_pressed = type_interaction(mouse_x, mouse_y, n_caracteres, n_mot, game_over)
            if button_pressed != None:
                remove_button = True
                do_once_remove_button = False
                deactivate_button[button_pressed] = True

                # allow the player to write a letter for the word by clicking on one of the screen's button (which got a letter on it)
                if button_pressed in alphabet and n_mot < n_essais and not game_over and pos_edit_letter < n_caracteres:
                    if pos_edit_letter+1 < n_caracteres:
                        pos_edit_letter += 1
                    mot_joueur[pos_edit_letter] = button_pressed[0] # [0] because we want the first letter (ex: button_pressed = "A_button")
                    if pos_edit_letter+2 > n_caracteres:
                        pos_edit_letter -= 1

                # allow the player to verify the word by clicking on the screen's enter button (the green one)
                elif button_pressed == "enter" and not is_word_empty(mot_joueur) and n_mot < n_essais and not game_over:
                    n_mot += 1
                    mots_joueur, lettres_indice = algo_motus(mot_secret, mot_joueur, mots_joueur, lettres_indice)
                    pos_edit_letter = -1
                    for lettre in range(len(lettres_indice)):
                        if lettres_indice[lettre] == "":
                            pos_edit_letter = lettre-1
                            break
                    game_over, deactivate_button, do_once_secret_link = update_display(images, n_essais, n_caracteres, button_pressed, mot_joueur, mot_secret, mots_joueur, n_mot, game_over, pos_edit_letter, is_first_time, deactivate_button, lettres_indice, time_playthrough, do_once_secret_link)
                    mot_joueur = lettres_indice[:]

                # delete the letter in the selection box and move back the selection box by 1 if the player click on the delete button
                elif button_pressed == "delete" and not game_over:
                    if pos_edit_letter < n_caracteres-1:
                        #if mot_joueur[pos_edit_letter+1] == "": # delete the letter of the box-1 if the box is empty
                        #    mot_joueur[pos_edit_letter] = ""
                        #else:
                        mot_joueur[pos_edit_letter+1] = ""
                    elif pos_edit_letter >= n_caracteres-1:
                        mot_joueur[pos_edit_letter] = ""
                        pos_edit_letter -= 1

                    if pos_edit_letter > -1:
                        pos_edit_letter -= 1

                # quit the game if the player click on the exit button
                elif button_pressed == "exit":
                    run = False

                # create a new word if the player click on the reset button
                elif button_pressed == "reset":

                    # setup the secret word
                    n_caracteres = random.randint(5, 10)
                    length_dict_words = len(dictonary["{}_letters".format(n_caracteres)])
                    mot_secret = dictonary["{}_letters".format(n_caracteres)] [random.randint(0, length_dict_words-1)]

                    # setup the clue letters
                    lettres_indice = ["" for char in range(n_caracteres)]
                    lettres_indice[0] = mot_secret[0].upper()
                    if n_caracteres > 7:
                        n_random = random.randint(2, 3)
                        lettres_indice[n_random] = mot_secret[n_random].upper()
                    mot_joueur = lettres_indice[:]

                    # resetup the variables
                    mots_joueur = []
                    game_over = False
                    n_mot = 0
                    pos_edit_letter = 0
                    is_first_time = True
                    time_playthrough = 0
                    last_time_playthrough = 0
                    time_start_game = time.time()
                    do_once_secret_link = True

                # change the location of the selection box
                elif type(button_pressed) == int:
                    pos_edit_letter = button_pressed-1

                game_over, deactivate_button, do_once_secret_link = update_display(images, n_essais, n_caracteres, button_pressed, mot_joueur, mot_secret, mots_joueur, n_mot, game_over, pos_edit_letter, is_first_time, deactivate_button, lettres_indice, time_playthrough, do_once_secret_link)
                button_pressed = None
                if is_first_time:
                    is_first_time = False
            did_click_left = False

        if remove_button and not pause:
            if not do_once_remove_button:
                start_frame_remove_button = frame
                do_once_remove_button = True
            if frame-start_frame_remove_button > 3:
                button_pressed = None
                remove_button = False
                game_over, deactivate_button, do_once_secret_link = update_display(images, n_essais, n_caracteres, button_pressed, mot_joueur, mot_secret, mots_joueur, n_mot, game_over, pos_edit_letter, is_first_time, deactivate_button, lettres_indice, time_playthrough, do_once_secret_link)

        for event in pg.event.get():

            if event.type == pg.QUIT or pg.key.get_pressed()[pg.K_ESCAPE]:
                run = False

            elif pg.mouse.get_pressed()[0]:
                mouse_x, mouse_y = pg.mouse.get_pos()
                did_click_left = True
                if counter_frame_click_left_mouse < frame:
                    counter_frame_click_left_mouse = frame+3

            elif event.type == pg.KEYDOWN:
                # take the input of the letters of the player's keyboard
                if event.key == pg.K_a: letter_keyboard = "A"
                elif event.key == pg.K_b: letter_keyboard = "B"
                elif event.key == pg.K_c: letter_keyboard = "C"
                elif event.key == pg.K_d: letter_keyboard = "D"
                elif event.key == pg.K_e: letter_keyboard = "E"
                elif event.key == pg.K_f: letter_keyboard = "F"
                elif event.key == pg.K_g: letter_keyboard = "G"
                elif event.key == pg.K_h: letter_keyboard = "H"
                elif event.key == pg.K_i: letter_keyboard = "I"
                elif event.key == pg.K_j: letter_keyboard = "J"
                elif event.key == pg.K_k: letter_keyboard = "K"
                elif event.key == pg.K_l: letter_keyboard = "L"
                elif event.key == pg.K_m: letter_keyboard = "M"
                elif event.key == pg.K_n: letter_keyboard = "N"
                elif event.key == pg.K_o: letter_keyboard = "O"
                elif event.key == pg.K_p: letter_keyboard = "P"
                elif event.key == pg.K_q: letter_keyboard = "Q"
                elif event.key == pg.K_r: letter_keyboard = "R"
                elif event.key == pg.K_s: letter_keyboard = "S"
                elif event.key == pg.K_t: letter_keyboard = "T"
                elif event.key == pg.K_u: letter_keyboard = "U"
                elif event.key == pg.K_v: letter_keyboard = "V"
                elif event.key == pg.K_w: letter_keyboard = "W"
                elif event.key == pg.K_x: letter_keyboard = "X"
                elif event.key == pg.K_y: letter_keyboard = "Y"
                elif event.key == pg.K_z: letter_keyboard = "Z"
                elif event.key == pg.K_RETURN or event.key == pg.K_KP_ENTER: letter_keyboard = "enter"
                elif event.key == 8: letter_keyboard = "delete"
                elif event.key == pg.K_LEFT: letter_keyboard = "left"
                elif event.key == pg.K_RIGHT: letter_keyboard = "right"

        #if not pause:
        time_end_frame = time.time()
        if time_end_frame - time_start_frame < 1/fps:
            pause = True
        else:
            pause = False
            WIDTH = pg.display.get_surface().get_width()
            HEIGHT = pg.display.get_surface().get_height()
            if WIDTH < HEIGHT:
                screen_type = "vertical"
                #WIDTH, HEIGHT = HEIGHT, WIDTH
            else:
                screen_type = "horizontal"

        # setup the chrono
        if not game_over:
            time_playthrough = time.time()-time_start_game
            if int(last_time_playthrough)<int(time_playthrough):
                last_time_playthrough = time_playthrough
                pg.draw.rect(WIN, BACKGROUND_COLOR, (images["chrono"].get_pos()[0], images["chrono"].get_pos()[1], images["chrono"].get_scale()[0]*4, images["chrono"].get_scale()[0]))
                setup_chrono(images, time_playthrough)
                # update the screen for the chrono
                pg.display.update()
        # update_display(images, n_essais, n_caracteres, button_pressed)
    pg.quit()
    sys.exit()

fps = 30
n_essais = 7
main(fps, n_essais)

"""
BUG:
- Aucun (pour le moment ...)

ajout:
- Aucun (pour le moment ...)
"""