
SCRIPT_START=	EpiReminder.py
SHELL		=	/bin/bash
RM			=	/bin/rm -f
BUILD_DIR	=	build
DIST_DIR	=	dist

all:
			pyinstaller --onefile $(SCRIPT_START)
			cp dist/EpiReminder .

clean:
			$(RM) -r $(DIST_DIR)/*
			$(RM) -r $(BUILD_DIR)/*

fclean:		clean
			$(RM) EpiReminder

test:
			python -m unittest discover

re:			fclean all

.PHONY:		clean fclean re
