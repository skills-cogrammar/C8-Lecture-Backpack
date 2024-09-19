def analyze_reviews(filename):
    # Check if the file is a .txt file by looking at its extension
    if not filename.endswith('.txt'):
        # If the file is not a .txt file, raise an error
        raise ValueError('Error: Only .txt files are supported.')

    try:
        # Open the specified file in 'read' mode
        with open(filename, 'r') as file:
            # Read all the lines from the file into a list called 'reviews'
            reviews = file.readlines()

            # Check if the file only contains empty lines or no content
            # The strip() function removes any extra spaces or newline characters
            if all(not review.strip() for review in reviews):
                # If all lines are empty, raise an error
                raise Exception('Error: The review file is empty or contains only blank lines.')

            # Remove any empty lines and extra spaces from the reviews
            non_empty_reviews = [review.strip() for review in reviews if review.strip()]

            # Count how many non-empty reviews there are
            num_reviews = len(non_empty_reviews)

            # Count the number of words in each review (splitting by spaces)
            word_counts = [len(review.split()) for review in non_empty_reviews]

            # Calculate the average length of the reviews in words
            # If there are no reviews, the average length will be set to 0
            avg_length = sum(word_counts) / num_reviews if num_reviews > 0 else 0

            # Calculate how many reviews were missing (empty lines in the original file)
            missing_reviews = len(reviews) - num_reviews

        # Open a new file (or create it if it doesn't exist) to write the analysis results
        # 'a+' mode lets us append to the file or create it if it doesn't exist
        with open('review_analysis.txt', 'a+') as output_file:
            # Write the total number of reviews to the file
            output_file.write(f'Total Reviews: {num_reviews}\n')

            # Write the average length of the reviews in words to the file
            output_file.write(f'Average Review Length (in words): {avg_length:.2f}\n')

            # Write how many reviews were missing (empty lines) to the file
            output_file.write(f'Missing Reviews: {missing_reviews}\n')

        # Let the user know the analysis is complete and where the results are stored
        print(f'Review analysis complete. Results written to review_analysis.txt')

    # If the file is not found, print an error message
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")

    # Handle any errors related to the file type
    except ValueError as ve:
        print(ve)

    # Handle any other errors that might occur
    except Exception as e:
        print(e)

    # This block will always run, even if an error happens
    finally:
        # Let the user know that the attempt to analyze the reviews is complete
        print('Review analysis attempt completed.')

# Prompt the user to enter the name of the review file
# It should be "reviews.txt". It must be located exactly where this python file is running from.
filename = input('Enter the review filename (with .txt extension): ')

# Call the analyze_reviews function with the user-provided filename
analyze_reviews(filename)
