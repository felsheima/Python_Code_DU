def view_movies(movies):
    #Displays all the movies within the selection
    print('\n------All Movies--------')
    #Cycles through each movie and shows the movie, rating, and genre
    for i, movie in enumerate(movies, 1):
        print(f'{i}, {movie[0]} - Rating {movie[1]} - Genre: {movie[2]} ') 

def add_movie(movies):
    #Adds a movie to the list
    print('\n-------Adding a Movie-------')
    title = input('\nEnter a new movie title: ')
    rating = input('\nPlease enter a rating of the movie (1-10): ')
    genre = input('\nPlease enter a genre: ')
    #Adds the movie the user inputed above to the end of the list
    movies.append([title, rating, genre])
    return f'\n{title} has been successfully added!' 
    
def update_rating(movies):
    #Updates a rating of a selected movie
    print('\n--------New rating for selected movie--------')
    #First print all movies so user knows what is available
    for i, movie in enumerate(movies, 1):
        print(f'{i}, {movie[0]}, - Rating {movie[1]} - Genre: {movie[2]} ')
        
    #Get the movie the user chooses to update the rating
    selection = input(f'\nPlease select the movie from the list you would like to update the rating of: ')
    new_rating = int(input('\nPlease enter the new rating you wish to add to the selected movie (1-10): '))

    for movie in movies:
        if movie[0].lower() == selection.lower():   
            #Save old rating and update
            old_rating = movie[1]
            movie[1] = new_rating
            return f'\n{movie[0]} rating updated from {old_rating} to {new_rating}!' 

    #If the movie that is selected is not found, print error message
    return f'\nSorry {movie} was not in the list '
    
def remove_movie(movies):
    #Removing a movie from the list
    print('\n-------Removing a selected movie--------')
    #First print all movies so user knows what is available
    for i, movie in enumerate(movies, 1):
        print(f'{i}, {movie[0]}, - Rating {movie[1]} - Genre: {movie[2]} ')

    selection = input(f'\nPlease select a movie you would like to remove from the existing list: ')
        
    #Get the movie the user chooses to remove
    for movie in movies:
        if movie[0].lower() == selection.lower():
            movies.remove(movie)
            return f'\n{selection} was removed from the list'
    #If the movie the user selected is not found within the list, print this error message
    return f'\nSorry, {selection} was not found in the movie list '

def average_rating(movies):
    #Shows the average rating of all the movies within the list
    print(f'\n---------Average Rating-----------')

    #Create an empty list to store ratins
    ratings = []

    #List of all ratings
    for movie in movies:
        ratings.append(float(movie[1]))

    if ratings: #Checks list is not empty
        #Finds the average of all the ratings within the list
        avg = sum(ratings) / len(ratings)
        print(f'\nThe average rating of all the movies in the list is {avg:.2f}')
    else:
        #If no movies exist within the list then an error message occurs 
        print('No movies exist to calculate the average') 
    
def recommend_by_genre(movies, genre):
    #Recommends a movie by its genre
    print(f'\n---------Movie recommendation by genre----------')
    #Create an empty recommendations list to store recommendations found
    recommendations = []
    #Loop through movies based on specific genre and add them to the recommendations list
    for movie in movies:
        if movie[2].lower() == genre.lower():
            recommendations.append(movie)

    #Show the movies within the recommendation list
    if recommendations:
        for movie in recommendations:
            print(f'\n {movie[0]} Rating: {movie[1]}')
    #Print error message if no movies are found within the selected genre
    else:
        print(f'\nSorry no movies found in the genre {genre}')
    
def recommend_top3(movies):
    #Reccomends top 3 movies based on highest ratings
    print(f'\n-------------Top 3 Movies---------------')
    #Sort and find the top 3 rated movies: reference: 
    sorted_movies = sorted(movies, key=lambda x: x[1], reverse=True)

    #Take the top 3
    top_3 = sorted_movies[:3]
    
    for movie in top_3:
        print(f'{movie[0]} (Rating: {movie[1]}, Genre: {movie[2]}') 

def movie_menu():
    #Main menu function for the movie management system 
    
    movies = [
    ["Inception", 9.0, "Sci-Fi"],
    ["The Matrix", 8.7, "Sci-Fi"],
    ["La La Land", 8.3, "Musical"],
    ["Interstellar", 9.2, "Sci-Fi"],
    ["Coco", 8.5, "Animation"],
    ["The Dark Knight", 9.0, "Action"],
    ["Titanic", 7.9, "Romance"],
    ["Avatar", 7.8, "Sci-Fi"],
    ["The Lion King", 8.8, "Animation"],
    ["Joker", 8.5, "Drama"],
    ["Forrest Gump", 8.9, "Drama"],
    ["Parasite", 8.6, "Thriller"],
    ["Gladiator", 8.5, "Action"],
    ["The Godfather", 9.2, "Crime"],
    ["Toy Story", 8.3, "Animation"],
    ["The Shawshank Redemption", 9.3, "Drama"],
    ["Spider-Man: Into the Spider-Verse", 8.4, "Animation"],
    ["Frozen", 7.4, "Animation"],
    ["Black Panther", 8.1, "Action"],
    ["Up", 8.2, "Animation"]
    ]
    
    while True:
        print('\nMovie Menu:')
        print('\n1. View all movies')
        print('\n2. Add a new movie')
        print('\n3. Upate a movie rating')
        print('\n4. Remove a movie')
        print('\n5. Show average rating')
        print('\n6. Reccomend a movie by genre')
        print('\n7. Reccomend top 3 highest-rated movies')
        print('\n8. Exit')

        option = input('\nEnter your option (1-8): ')

        if option == '1':
            view_movies(movies)
        elif option == '2':
            print(add_movie(movies))
        elif option == '3':
            print(update_rating(movies))
        elif option == '4':
            print(remove_movie(movies))
        elif option == '5':
            average_rating(movies)
        elif option == '6':
            genre = input('Please enter a genre you are looking for in a movie: ')
            recommend_by_genre(movies, genre)
        elif option == '7':
            recommend_top3(movies)
        elif option == '8':
            print('Goodbye!')
            break
        else:
            print('That is not a correct option to choose from....TRY AGAIN') 


if __name__ == '__main__':
    movie_menu()

#Output of running some of this program
# Movie Menu:

# 1. View all movies

# 2. Add a new movie

# 3. Upate a movie rating

# 4. Remove a movie

# 5. Show average rating

# 6. Reccomend a movie by genre

# 7. Reccomend top 3 highest-rated movies

# 8. Exit

# Enter your option (1-8): 1

# ------All Movies--------
# 1, Inception - Rating 9.0 - Genre: Sci-Fi 
# 2, The Matrix - Rating 8.7 - Genre: Sci-Fi 
# 3, La La Land - Rating 8.3 - Genre: Musical 
# 4, Interstellar - Rating 9.2 - Genre: Sci-Fi 
# 5, Coco - Rating 8.5 - Genre: Animation 
# 6, The Dark Knight - Rating 9.0 - Genre: Action 
# 7, Titanic - Rating 7.9 - Genre: Romance 
# 8, Avatar - Rating 7.8 - Genre: Sci-Fi 
# 9, The Lion King - Rating 8.8 - Genre: Animation 
# 10, Joker - Rating 8.5 - Genre: Drama 
# 11, Forrest Gump - Rating 8.9 - Genre: Drama 
# 12, Parasite - Rating 8.6 - Genre: Thriller 
# 13, Gladiator - Rating 8.5 - Genre: Action 
# 14, The Godfather - Rating 9.2 - Genre: Crime 
# 15, Toy Story - Rating 8.3 - Genre: Animation 
# 16, The Shawshank Redemption - Rating 9.3 - Genre: Drama 
# 17, Spider-Man: Into the Spider-Verse - Rating 8.4 - Genre: Animation 
# 18, Frozen - Rating 7.4 - Genre: Animation 
# 19, Black Panther - Rating 8.1 - Genre: Action 
# 20, Up - Rating 8.2 - Genre: Animation 

# Movie Menu:

# 1. View all movies

# 2. Add a new movie

# 3. Upate a movie rating

# 4. Remove a movie

# 5. Show average rating

# 6. Reccomend a movie by genre

# 7. Reccomend top 3 highest-rated movies

# 8. Exit

# Enter your option (1-8): 2

# -------Adding a Movie-------

# Enter a new movie title: Yankee

# Please enter a rating of the movie (1-10): 8

# Please enter a genre: Comedy

# Yankee has been successfully added!
