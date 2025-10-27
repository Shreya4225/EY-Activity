from transformers import pipeline

# Load a sentiment-analysis pipeline
classifier = pipeline("sentiment-analysis")

# Example text
#text = "I absolutely love this product! It's fantastic."
text= "I don't like your product"

# Run classification
result = classifier(text)

# Print result
print(f"Label: {result[0]['label']}, Confidence: {result[0]['score']:.2f}")