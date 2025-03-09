import streamlit as st

# Title
st.markdown("### Text Analyzer created by Usama")
st.markdown("---")

# User Input
paragraph = st.text_area("Enter a paragraph:", height=150)

if paragraph:  # Ensuring input is not empty
    # Word and Character Count
    words = paragraph.split()
    total_words = len(words)
    total_chars = len(paragraph)

    # Vowel Count
    vowels = "aeiouAEIOU"
    vowel_count = sum(1 for char in paragraph if char in vowels)

    # Search and Replace
    search_word = st.text_input("Enter a word to search for:")
    replace_word = st.text_input("Enter a word to replace it with:")

    if search_word and replace_word:
        modified_paragraph = paragraph.replace(search_word, replace_word)
    else:
        modified_paragraph = paragraph

    # Uppercase & Lowercase Conversion
    uppercase_paragraph = paragraph.upper()
    lowercase_paragraph = paragraph.lower()

    # Operators - Checking if "Python" exists
    contains_python = "Python" in paragraph

    # Average Word Length Calculation
    average_word_length = total_chars / total_words if total_words > 0 else 0

    # Display Results
    st.markdown(f"**Original Paragraph:**\n\n{paragraph}")

    st.markdown(f"**Total Words:** {total_words}")
    st.markdown(f"**Total Characters:** {total_chars}")
    st.markdown(f"**Number of Vowels:** {vowel_count}")

    st.markdown(f"**Does the paragraph contain the word 'Python'?** {'Yes' if contains_python else 'No'}")

    if search_word and replace_word:
        st.markdown(f"**Modified Paragraph:**\n\n{modified_paragraph}")

    st.markdown(f"**Paragraph in Uppercase:**\n\n{uppercase_paragraph}")
    st.markdown(f"**Paragraph in Lowercase:**\n\n{lowercase_paragraph}")

    st.markdown(f"**Average Word Length:** {round(average_word_length, 2)}")

else:
    st.warning("Please enter a paragraph to analyze.")

