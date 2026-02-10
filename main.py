# attempt 2 of council's program

# import modules
import pygame
import csv
import time
import pandas as pd
from tkinter import Tk, filedialog
import os
import sys


def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS  # PyInstaller sets this at runtime
    except AttributeError:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


# initiate pygame
pygame.init()

# create window
screen = pygame.display.set_mode((1200, 700), pygame.RESIZABLE)
icon = pygame.image.load(resource_path('icon.png'))
pygame.display.set_icon(icon)
pygame.display.set_caption("Pay Cheque")


def search(number):
    # make the number a string
    number = str(number)
    # create option list
    options = [1, 2, 3, 4]
    # create option variable
    option_count = 5
    read = False
    count_num = -2

    # open the payment file
    with open(file_path) as file_1:
        file_reader_1 = csv.reader(file_1, delimiter=',')
        # skip the first row, read every other row
        for row_1 in file_reader_1:
            count_num += 1
            if not read:
                read = True
            else:
                if number == row_1[0].replace(".0", "") or number == row_1[1].replace(".0", ""):
                    # get student's name
                    name = str(row_1[3]) + " " + str(row_1[2])
                    # name checks
                    if len(name) > 50:
                        name = name[0:47] + "..."
                    # get the student's grade
                    grade_1 = row_1[4].replace(".0", "")
                    # get options
                    for opt in options:
                        opt = opt - 1
                        options[opt] = row_1[option_count]
                        option_count += 1

                    if row_1[9] != "":
                        time_last_scanned = row_1[10]
                        return ["repeat", name, options, grade_1, time_last_scanned]

                    # update to be scanned and time
                    edits_1 = pd.read_csv(file_path)
                    edits_1.loc[count_num, "Checked In"] = "x"

                    scan_time = time.localtime()
                    scan_time = time.strftime("%I:%M:%S %p", scan_time)
                    edits_1.loc[count_num, "Time"] = scan_time
                    edits_1.to_csv(file_path, index=False)

                    file_1.close()
                    return ["paid", name, options, grade_1, num]

                else:
                    pass

        return ["no"]


def name_search(person):
    # splice into first / last
    person = person.split()

    if len(person) != 2:
        return ["no"]

    # create option list
    options = [1, 2, 3, 4]
    # create option variable
    option_count = 5
    read = False
    count_num = -2

    # open the payment file
    with open(file_path) as file_1:
        file_reader_1 = csv.reader(file_1, delimiter=',')
        # skip the first row, read every other row
        for row_1 in file_reader_1:
            count_num += 1
            if not read:
                read = True
            else:
                if person[0].lower() == row_1[3].lower() and person[1].lower() == row_1[2].lower():
                    # get student_ID
                    stu_ID = row_1[0].replace(".0", "")
                    # make name variable
                    name = person[0].capitalize() + " " + person[1].capitalize()
                    # get the student's grade
                    grade_1 = row_1[4].replace(".0", "")
                    # get options
                    for opt in options:
                        opt = opt - 1
                        options[opt] = row_1[option_count]
                        option_count += 1

                    if row_1[9] != "":
                        time_last_scanned = row_1[10]
                        return ["repeat", name, options, grade_1, time_last_scanned, stu_ID]

                    # update to be scanned
                    # update to be scanned and time
                    edits_1 = pd.read_csv(file_path)
                    edits_1.loc[count_num, "Checked In"] = "x"

                    scan_time = time.localtime()
                    scan_time = time.strftime("%I:%M:%S %p", scan_time)
                    edits_1.loc[count_num, "Time"] = scan_time
                    edits_1.to_csv(file_path, index=False)

                    file_1.close()
                    return ["paid", name, options, grade_1, num, stu_ID]

                else:
                    pass

        return ["no"]


def file_examiner(f, cell):
    counter_1 = 0
    with open(f) as file:
        file_reader = csv.reader(file, delimiter=',')
        for row in file_reader:
            if not row[cell] == "":
                counter_1 += 1
        file.close()

    return counter_1


def resize(new_size):
    global height
    global width
    global fontL
    global fontM
    global fontS
    global fonts
    global screen
    global search_icon
    global search_icon_rect
    global number_icon
    global top_rect
    global bottom_rect
    global reset_text
    global reset_text_rect
    global num
    global num_rect
    global file_name
    global file_name_text
    global file_name_text_rect

    width, height = new_size
    if width < 400:
        width = 400
    if height < 300:
        height = 300

    # resize fonts
    scale_w = width / 1200
    scale_h = height / 700
    scale = min(scale_w, scale_h)
    fontL = pygame.font.Font(resource_path('times.ttf'), int(120 * scale))
    fontM = pygame.font.Font(resource_path('times.ttf'), int(60 * scale))
    fontS = pygame.font.Font(resource_path('times.ttf'), int(45 * scale))
    fonts = pygame.font.Font(resource_path('times.ttf'), int(30 * scale))

    # resize graphics
    search_icon = pygame.image.load(resource_path('search.png')).convert_alpha()
    search_icon = pygame.transform.scale(search_icon, (int(40 * scale), int(40 * scale)))
    search_icon_rect = search_icon.get_rect()
    search_icon_rect.topright = (width, 0)
    number_icon = pygame.image.load(resource_path('number.png')).convert_alpha()
    number_icon = pygame.transform.scale(number_icon, (int(40 * scale), (int(40 * scale))))

    # resize rectangles
    top_rect = (-5, -3, width + 10, int(48 * scale))
    bottom_rect = (-5, height - int(48 * scale), width + 10, int(48 * scale))
    num = fontM.render("1234567890", True, black)
    num_rect = num.get_rect()

    reset_text = fonts.render("RESET", True, light_gray)
    reset_text_rect = reset_text.get_rect()
    reset_text_rect.midtop = (width / 2, int(6 * scale))

    file_name_text = fonts.render(file_name, True, light_gray)
    file_name_text_rect = file_name_text.get_rect()
    file_name_text_rect.midbottom = (width / 2, height - int(6 * scale))

    # display file name
    pygame.draw.rect(screen, gray, file_name_text_rect, 0, 3)
    screen.blit(file_name_text, file_name_text_rect)

    # resize screen
    screen = pygame.display.set_mode((width, height), pygame.RESIZABLE)


def file_select(current_path):

    try:
        global file_name
        global file_name_text
        global file_name_text_rect
        global total_list
        global total_scanned

        # ask for file

        # Hide the root Tk window
        Tk().withdraw()

        file_path_1 = filedialog.askopenfilename(
            title="Select CSV file",
            filetypes=[("CSV files", "*.csv")]
        )

        if file_path_1:
            do_1 = True
        else:
            do_1 = False

        # create file text
        file_name = os.path.basename(file_path_1).strip(".csv")
        if len(file_name) > 25:
            file_name = file_name[:25]
        else:
            file_name = file_name

        file_name_text = fonts.render(file_name, True, light_gray)
        file_name_text_rect = file_name_text.get_rect()
        file_name_text_rect.midbottom = (600, 694)

        total_scanned = file_examiner(file_path_1, 9) - 1
        total_list = file_examiner(file_path_1, 1) - 1

        return do_1, file_path_1

    except FileNotFoundError:
        file_path_1 = current_path

        if file_path_1:
            do_1 = True
        else:
            do_1 = False

        # create file text
        file_name = os.path.basename(file_path_1).strip(".csv")
        if len(file_name) > 25:
            file_name = file_name[:25]
        else:
            file_name = file_name

        file_name_text = fonts.render(file_name, True, light_gray)
        file_name_text_rect = file_name_text.get_rect()
        file_name_text_rect.midbottom = (600, 694)

        if file_path_1 != "":
            total_scanned = file_examiner(file_path_1, 9) - 1
            total_list = file_examiner(file_path_1, 1) - 1

        return do_1, file_path_1


# colour and text vals
black = (0, 0, 0)
gray = (56, 63, 65)
light_gray = (167, 169, 171)
med_gray = (128, 124, 124)
fontL = pygame.font.Font(resource_path('times.ttf'), 120)
fontM = pygame.font.Font(resource_path('times.ttf'), 60)
fontS = pygame.font.Font(resource_path('times.ttf'), 45)
fonts = pygame.font.Font(resource_path('times.ttf'), 30)

# create graphics
search_icon = pygame.image.load(resource_path('search.png')).convert_alpha()
search_icon = pygame.transform.scale(search_icon, (40, 40))
search_icon_rect = search_icon.get_rect()
search_icon_rect.topright = (1200, 0)

number_icon = pygame.image.load(resource_path('number.png')).convert_alpha()
number_icon = pygame.transform.scale(number_icon, (40, 40))

reset_text = fonts.render("RESET", True, light_gray)
reset_text_rect = reset_text.get_rect()
reset_text_rect.midtop = (600, 6)

file_name_text = fonts.render("file_name", True, light_gray)
file_name_text_rect = file_name_text.get_rect()
file_name_text_rect.midbottom = (600, 694)

top_rect = (-5, -3, 1210, 48)
bottom_rect = (-5, 655, 1210, 48)
num = fontM.render("1234567890", True, black)
num_rect = num.get_rect()

file_name = ""
try:
    do, file_path = file_select("")
except TypeError:
    do = False

# start loop
student_ID = ""
student_name = ""
carry_over = ""
student = ""
keys_pressed = 0
options_count = 0
options_dict = {}
width = 1200
height = 700
possible_delete = False
exemption = False
do_last = False
cheat_mode = False
caps = False
full_delete = False
if do:
    total_scanned = file_examiner(file_path, 9) - 1
    total_list = file_examiner(file_path, 1) - 1

counter = -2

search_number = True
search_name = False
display_results = False
reset = False

while do:

    while search_number:

        screen_size = screen.get_size()

        if keys_pressed == 9:
            # reset remaining variables
            student_ID = "" + carry_over
            options_count = 0
            if carry_over == "":
                keys_pressed = 0
            else:
                keys_pressed = 1
            carry_over = ""

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                do = False
                search_number = False
            if event.type == pygame.VIDEORESIZE:
                resize(event.size)
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = event.pos
                if search_icon_rect.collidepoint(pos):
                    # reset remaining variables
                    student_ID = ""
                    student_name = ""
                    keys_pressed = 0
                    # transfer
                    search_name = True
                    search_number = False

                if reset_text_rect.collidepoint(pos):
                    reset = True
                    search_number = False

                if file_name_text_rect.collidepoint(pos):
                    file_select(file_path)
                    last_student = ""
                    student_ID = ""
                    student_name = ""
                    keys_pressed = 0

            if event.type == pygame.KEYDOWN:
                # student ID
                if keys_pressed < 9:
                    key = pygame.key.name(event.key)
                    if key.isnumeric() and len(key) == 1:
                        student_ID += key
                        keys_pressed += 1
                    if event.key == pygame.K_BACKSPACE:
                        if student_ID != "":
                            keys_pressed -= 1
                            student_ID = student_ID[:-1]

        # make screen white
        screen.fill((255, 255, 255))
        # border
        pygame.draw.rect(screen, light_gray, top_rect)
        pygame.draw.rect(screen, gray, top_rect, 2, 3)
        pygame.draw.rect(screen, light_gray, bottom_rect)
        pygame.draw.rect(screen, gray, bottom_rect, 2, 3)

        # display reset
        pygame.draw.rect(screen, gray, reset_text_rect, 0, 3)
        screen.blit(reset_text, reset_text_rect)

        # display file name
        pygame.draw.rect(screen, gray, file_name_text_rect, 0, 3)
        screen.blit(file_name_text, file_name_text_rect)

        screen.blit(search_icon, search_icon_rect)

        if 0 < keys_pressed < 9:
            # display enter box
            num_rect.center = (width / 2, height / 3)
            pygame.draw.rect(screen, light_gray, num_rect)
            pygame.draw.rect(screen, med_gray, num_rect, 2, 3)

            # display student ID
            text = fontM.render(student_ID, True, black)
            text_rect = text.get_rect()
            text_rect.center = (width / 2, height / 3)
            screen.blit(text, text_rect)

        # if there is a complete student ID
        if keys_pressed == 9:
            # run results
            results = search(student_ID)
            display_results = True
            search_number = False

        if keys_pressed == 0:
            # display prompt text
            text = fontM.render("Enter a Student ID", True, med_gray)
            text_rect = text.get_rect()
            text_rect.center = (width / 2, height / 3)
            screen.blit(text, text_rect)

        pygame.display.update()

    while search_name:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                do = False
                search_name = False
            if event.type == pygame.VIDEORESIZE:
                resize(event.size)
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = event.pos
                if search_icon_rect.collidepoint(pos):
                    # reset remaining variables
                    student_name = ""
                    student_ID = ""
                    keys_pressed = 0
                    # transfer
                    search_number = True
                    search_name = False

                if reset_text_rect.collidepoint(pos):
                    reset = True
                    search_name = False

                if file_name_text_rect.collidepoint(pos):
                    file_select(file_path)
                    last_student = ""
                    student_ID = ""
                    student_name = ""

            if event.type == pygame.KEYDOWN:
                key = pygame.key.name(event.key)
                if key == "left shift":
                    caps = True
                if key.isalpha() and len(key) == 1:
                    if not caps:
                        student_name += key
                    else:
                        student_name += key.capitalize()
                elif key == "space":
                    student_name += " "
                elif key == "dash":
                    student_name += "-"
                elif key == "'":
                    student_name += "'"

                if event.key == pygame.K_BACKSPACE:
                    if student_name != "":
                        student_name = student_name[:-1]
                        if full_delete:
                            student_name = ""

                if event.key == pygame.K_RETURN:
                    results = name_search(student_name)
                    display_results = True
                    search_name = False
                if event.key == pygame.K_LCTRL:
                    full_delete = True

            if event.type == pygame.KEYUP:
                key = pygame.key.name(event.key)
                if key == "left shift":
                    caps = False
                if event.key == pygame.K_LCTRL or pygame.KMOD_META:
                    full_delete = False

        # make screen white
        screen.fill((255, 255, 255))
        # border
        pygame.draw.rect(screen, light_gray, top_rect)
        pygame.draw.rect(screen, gray, top_rect, 2, 3)
        pygame.draw.rect(screen, light_gray, bottom_rect)
        pygame.draw.rect(screen, gray, bottom_rect, 2, 3)

        # display reset
        pygame.draw.rect(screen, gray, reset_text_rect, 0, 3)
        screen.blit(reset_text, reset_text_rect)

        # display file name
        pygame.draw.rect(screen, gray, file_name_text_rect, 0, 3)
        screen.blit(file_name_text, file_name_text_rect)

        screen.blit(number_icon, search_icon_rect)

        if student_name != "":
            # display name
            if len(student_name) < 40:
                text = fontM.render(student_name, True, black)
                text_rect = text.get_rect()
                text_rect.center = (width / 2, height / 3)
                screen.blit(text, text_rect)
            elif 40 <= len(student_name) < 70:
                text = fonts.render(student_name, True, black)
                text_rect = text.get_rect()
                text_rect.center = (width / 2, height / 3)
                screen.blit(text, text_rect)
            else:
                text = fonts.render("..." + student_name[len(student_name) - 67:], True, black)
                text_rect = text.get_rect()
                text_rect.center = (width / 2, height / 3)
                screen.blit(text, text_rect)

            # display instructions
            return_text = fonts.render("Press Return to Search", True, med_gray)
            return_text_rect = return_text.get_rect()
            return_text_rect.center = (width / 2, height / 2)
            screen.blit(return_text, return_text_rect)

        else:
            # display prompt text
            text = fontM.render("Enter a Student Name", True, med_gray)
            text_rect = text.get_rect()
            text_rect.center = (width / 2, height / 3)
            screen.blit(text, text_rect)

        pygame.display.update()

    while display_results:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                display_results = False
                search_number = False
                search_name = False
                do = False
            if event.type == pygame.VIDEORESIZE:
                resize(event.size)
            if event.type == pygame.KEYDOWN:
                if student != "" and len(results) > 1:
                    last_student = results[1]
                    do_last = True
                counter = -2
                options_count = 0
                options_dict = {}
                key = pygame.key.name(event.key)
                if key.isnumeric():
                    carry_over += key
                if len(results) == 6:
                    search_name = True
                    student_name = ""
                    student_ID = ""
                else:
                    search_number = True
                    student_ID = ""
                    student_name = ""
                results = []
                display_results = False

        if results:
            # fill screen with coulour
            status = results[0]
            if status == "paid":
                screen.fill((73, 209, 109))
            elif status == "repeat":
                screen.fill((247, 247, 84))
            elif status == "no":
                screen.fill((240, 40, 34))

            # border
            pygame.draw.rect(screen, light_gray, top_rect)
            pygame.draw.rect(screen, gray, top_rect, 2, 3)
            pygame.draw.rect(screen, light_gray, bottom_rect)
            pygame.draw.rect(screen, gray, bottom_rect, 2, 3)

            # if they have paid
            if results[0] == "paid":

                counter += 1

                # safety check to not duplicate this call
                if counter == 0:
                    # increase number of people scanned
                    total_scanned += 1

            elif results[0] == "repeat":
                # display last scan
                last_scan_text = fonts.render(results[4], True, black)
                last_scan_text_rect = last_scan_text.get_rect()
                last_scan_text_rect.bottomleft = 5, height - 5
                screen.blit(last_scan_text, last_scan_text_rect)

            # if they haven't paid
            elif results[0] == "no":
                # display student ID
                # display student name
                if student_ID != "":
                    poor_ID = fontL.render(student_ID, True, black)
                elif student_name != "":
                    poor_ID = fontL.render(student_name, True, black)
                if student_name != "" or student_ID != "":
                    poor_ID_rect = poor_ID.get_rect()
                    poor_ID_rect.center = (width / 2, height / 5)
                    screen.blit(poor_ID, poor_ID_rect)

            # print last person to scan
            if do_last:
                if len(last_student) > 25:
                    last_student = last_student[:22] + "..."
                # display last scanned
                last_student_text = fonts.render(last_student, True, black)
                last_scanned_rect = last_student_text.get_rect()
                last_scanned_rect.topleft = (2, reset_text_rect[1])
                screen.blit(last_student_text, last_scanned_rect)

            if results[0] == "paid" or results[0] == "repeat":
                # display student name
                if len(results[1]) < 30:
                    student = fontL.render(results[1], True, black)
                else:
                    student = fontS.render(results[1], True, black)
                student_rect = student.get_rect()
                student_rect.center = (width / 2, height / 6)
                screen.blit(student, student_rect)

                # display student grade
                grade_text = fonts.render("Grade " + results[3], True, black)
                grade_text_rect = grade_text.get_rect()
                grade_text_rect.midtop = (width / 2, 4)
                screen.blit(grade_text, grade_text_rect)

                # display enter box
                num_rect.center = (width / 2, height / 3)
                pygame.draw.rect(screen, light_gray, num_rect)
                pygame.draw.rect(screen, med_gray, num_rect, 2, 3)
                # display student ID
                # display student ID
                if len(results) == 6:
                    student_ID = results[5]
                text = fontM.render(student_ID, True, black)
                text_rect = text.get_rect()
                text_rect.center = (width / 2, height / 3)
                screen.blit(text, text_rect)

                # display options
                for i in results[2]:
                    options_count += 1
                    if i != "":
                        options_text = fontS.render("- " + i, True, black)
                        options_text_rect = options_text.get_rect()
                        options_text_rect.center = (width / 2, (height / 2.5 + (options_count * (height / 12))))
                        options_dict["Option" + str(options_count)] = [options_text, options_text_rect]
                        if options_count == 4:
                            options_count = 0

                for item in options_dict:
                    screen.blit(options_dict[item][0], options_dict[item][1])

            # display number scanned
            scanned = fonts.render((str(total_scanned) + "/" + str(total_list)), True, black)
            scanned_rect = scanned.get_rect()
            scanned_rect.bottomright = (width - 5, height - 5)
            screen.blit(scanned, scanned_rect)

            pygame.display.update()

    while reset:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                do = False
                search_number = False
                search_name = False
                display_results = False
                reset = False
            if event.type == pygame.VIDEORESIZE:
                resize(event.size)
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = event.pos
                if confirm_text_rect.collidepoint(pos):
                    # change all values in scanned column to blank
                    delete = pd.read_csv(file_path)
                    delete["Checked In"] = delete["Checked In"].replace({"x": ""})
                    delete["Time"] = ""
                    delete.to_csv(file_path, index=False)
                    # reset total scanned and last scanned
                    total_scanned = 0
                    last_student = ""
                    # start loop
                    student_ID = ""
                    student_name = ""
                    carry_over = ""
                    student = ""
                    keys_pressed = 0
                    options_count = 0
                    options_dict = {}
                    possible_delete = False
                    exemption = False
                    do_last = False
                    cheat_mode = False
                    caps = False
                    full_delete = False
                    counter = -2
                    search_number = True
                    search_name = False
                    display_results = False
                    reset = False

                if reset_text_rect.collidepoint(pos):
                    if student_name != "":
                        search_name = True
                        reset = False
                    else:
                        search_number = True
                        reset = False

        # make screen light red
        screen.fill((217, 76, 76))
        # border
        pygame.draw.rect(screen, light_gray, top_rect)
        pygame.draw.rect(screen, gray, top_rect, 2, 3)
        pygame.draw.rect(screen, light_gray, bottom_rect)
        pygame.draw.rect(screen, gray, bottom_rect, 2, 3)

        # click to confirm
        confirm_text = fontM.render("Click to Confirm", True, black)
        confirm_text_rect = confirm_text.get_rect()
        confirm_text_rect.center = (width / 2, height / 2)
        screen.blit(confirm_text, confirm_text_rect)

        # display back
        back_text = fonts.render("BACK", True, black)
        screen.blit(back_text, reset_text_rect)

        pygame.display.update()
