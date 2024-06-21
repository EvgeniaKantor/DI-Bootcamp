import os
from openai import OpenAI


class BackOpenAI:
    requests_restriction = 10
    count_of_requests = 0
    @staticmethod
    def generate_feedbacks(df_feedback):
        feedbacks_without_no_info = df_feedback[df_feedback['Review_Text'] != 'No info'].copy()
        try:
            client = OpenAI(api_key=os.environ['OPENAI_API_KEY'])
            feedback_dict = {index: row['Review_Text'] for index, row in feedbacks_without_no_info.iterrows()}
            for feedback_key, feedback_value in feedback_dict.items():
                BackOpenAI.count_of_requests += 1
                if BackOpenAI.count_of_requests >= BackOpenAI.requests_restriction:
                    break

                # Construct prompt messages for the GPT model
                prompt_for_role_system = "You specialize in offering a unique and friendly service tailored to responding to customer feedback effectively in Russian"
                prompt_for_role_user = (
                    f"I've received the following feedback from a customer about a jacket: '{feedback_value}'. "
                    "Generate a unique and friendly response from the sales manager in Russian."
                )

                # Send prompt messages to the GPT model
                chat_gpt_response = client.chat.completions.create(
                    model="gpt-3.5-turbo",
                    messages=[
                        {"role": "system", "content": prompt_for_role_system},
                        {"role": "user", "content": prompt_for_role_user}
                    ]
                )

                # Extract the content of the response
                response = chat_gpt_response.choices[0].message.content

                # Add the generated response to the DataFrame
                df_feedback.at[feedback_key, 'Generated_Response'] = response

            # Save the DataFrame to an Excel file
            df_feedback.to_excel("generated_feedbacks.xlsx", index=False)

        except Exception as e:
            print(f"An error occurred: {str(e)}")
