import tkinter as tk
from tkinter import messagebox

# Define lists of positive and negative words
positive_words = ["happy", "good", "love", "great", "excellent", "amazing", "fantastic", "joy", "positive", "awesome"]
negative_words = ["bad", "sad", "hate", "angry", "terrible", "awful", "poor", "horrible", "disappointed", "negative"]

# Create the main window
root = tk.Tk()
root.title("Social Media Sentiment Analyzer")

# Function to analyze sentiment based on predefined lists of words
def analyze_sentiment():
    # Get the user input from the text box
    user_input = input_text.get("1.0", "end-1c").lower()
    
    if not user_input.strip():
        messagebox.showwarning("Input Error", "Please enter some text.")
        return
    
    # Split the input text into individual words
    words = user_input.split()
    
    # Initialize counts for positive and negative words
    positive_count = 0
    negative_count = 0
    
    # Check each word in the input and count positive/negative words
    for word in words:
        if word in positive_words:
            positive_count += 1
        elif word in negative_words:
            negative_count += 1
    
    # Determine sentiment based on the counts
    if positive_count > negative_count:
        sentiment = "Positive"
        color = "green"
    elif positive_count < negative_count:
        sentiment = "Negative"
        color = "red"
    else:
        sentiment = "Neutral"
        color = "gray"
    
    # Display the result in the result_label
    result_label.config(text=f"Sentiment: {sentiment}", fg=color)

# Create a label and text box for user input
input_label = tk.Label(root, text="Enter Social Media Post:")
input_label.pack(pady=10)

input_text = tk.Text(root, height=10, width=50)
input_text.pack(pady=10)

# Create a button to analyze sentiment
analyze_button = tk.Button(root, text="Analyze Sentiment", command=analyze_sentiment)
analyze_button.pack(pady=10)

# Create a label to display the sentiment result
result_label = tk.Label(root, text="Sentiment: None", font=("Helvetica", 16))
result_label.pack(pady=20)

# Run the Tkinter event loop
root.mainloop()
