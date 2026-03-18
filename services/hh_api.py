import httpx 
import asyncio 


async def get_vacancies(query: str):
    url = "https://api.hh.ru/vacancies"

    params = { 
        "text": query,
        "per_page": 5,     
        "schedule": "remote",  
        "order_by": "publication_time",
        "only_with_salary": True,
        "experience": "between1And3",
    }


    async with httpx.AsyncClient() as client:
        response = await client.get(url, params=params)

        data = response.json()

        return data['items']
    

def format_vacancies(vacancies):

    text = ""

    for job in vacancies:

        title = job['name']
        company = job['employer']['name']
        url = job['alternate_url']

        text += (
            f"💼 {title}\n"
            f"🏢 {company}\n"
            f"🔗 {url}\n\n"
        )

    return text
