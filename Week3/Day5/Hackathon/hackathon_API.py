import os
from openai import OpenAI

client = OpenAI(api_key=os.environ['OPENAI_API_KEY'])


def generate_CV(cv_template_text, job_description, job_title):
    prompt_for_role_system = ("You offer a specialized service aimed at enhancing resumes "
                              "tailored for specific job vacancies")
    prompt_for_role_user = (f"I have the following text template for my CV: {cv_template_text}\n"
                            f"Could you please tailor this CV to align with the job "
                            f"description provided below: {job_description}\n"
                            f"This is for the position of {job_title}.\n")
    # for the old version :
    # chat_gpt_response = openai.Completion.create(
    #     engine="text-davinci-002",
    #     prompt=prompt,
    #     max_tokens=150
    # )
    # for the new version
    chat_gpt_response = client.chat.completions.create(
                        model="gpt-3.5-turbo",
                        messages=[
                         {"role": "system", "content": prompt_for_role_system},
                         {"role": "user", "content": prompt_for_role_user}
                        ]
                        )

    # Extract modified CV from completion response
    #modified_cv = chat_gpt_response.choices[0].text.strip()
    modified_cv = chat_gpt_response.choices[0].message.content
    return modified_cv

def keywords_description(job_description):
    prompt_for_role_system = ("You will be provided with a block of text, and your "
                              "task is to make a short summary")
    prompt_for_role_user = (f"The text is job description: {job_description}"
                            f"the summary should not be more that 20 words")

    chat_gpt_response = client.chat.completions.create(
                        model="gpt-3.5-turbo",
                        messages=[
                         {"role": "system", "content": prompt_for_role_system},
                         {"role": "user", "content": prompt_for_role_user}
                        ]
                        )

    # Extract modified CV from completion response
    # modified_cv = chat_gpt_response.choices[0].text.strip()
    modified_description = chat_gpt_response.choices[0].message.content
    return modified_description