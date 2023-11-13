NAME = AutoClick
CC = c++
FLAGS = -Wall -Wextra -Werror
RM = rm -rf
LIB = -lX11 -lXtst

SRC =	souris.cpp \
	Click.cpp \

OBJ = $(SRC:.cpp=.o)

%.o : %.cpp
	$(CC) $(FLAGS) -c $< -o $@

$(NAME) : $(OBJ)
	$(CC) $(FLAGS) $(OBJ) -o $(NAME) $(LIB)

all : $(NAME)

clean : 
	@$(RM) $(OBJ)

fclean : clean
	@$(RM) $(NAME)

re : fclean all