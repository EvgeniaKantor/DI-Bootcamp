import os
from openai import OpenAI, OpenAIError

def generate_keywords(database):
    try:
        client = OpenAI(api_key=os.environ['OPENAI_API_KEY'])
        titles_dict = {index: row['Title'] for index, row in database.iterrows()}  # Assuming `database` is defined somewhere

        keyphrase_dict = {}  # Initialize an empty dictionary to store the generated key phrases
        for title_key, title_value in titles_dict.items():
            # Construct prompt messages for the GPT model
            prompt_for_role_system = "You offer a specialized service aimed at finding a two-word main key phrase"
            prompt_for_role_user = (f"I have the following title: '{title_value}'. "
                                    f"Please generate a two-word main key phrase with only two words, "
                                    f"without additional explanations.")

            # Send prompt messages to the GPT model
            chat_gpt_response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": prompt_for_role_system},
                    {"role": "user", "content": prompt_for_role_user}
                ]
            )

            # Extract the content of the response
            response_content = chat_gpt_response.choices[0].message.content

            # Store the generated key phrase along with the corresponding title key in the dictionary
            keyphrase_dict[title_key] = response_content

            # Print the generated dictionary for debugging purposes
        print(keyphrase_dict)
        return keyphrase_dict

    except OpenAIError as e:
        print(f"Error occurred during OpenAI request: {e}")
        return None
    except Exception as e:
        print(f"Error occurred: {e}")
        return None
