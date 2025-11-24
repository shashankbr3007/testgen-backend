import logging
from app.core.config import settings
from openai import OpenAI, APIConnectionError, APIStatusError, RateLimitError
import backoff

logger = logging.getLogger(__name__)
client = OpenAI(api_key=settings.OPENAI_API_KEY)

MAX_RETRIES = 3
BACKOFF_BASE = 2 # exponential backoff base

class TestCaseGenerator:
    @staticmethod
    @backoff.on_exception(
        backoff.expo,
        (RateLimitError, APIConnectionError, APIStatusError),
        max_tries=MAX_RETRIES
    )
    async def generate(payload):
        try:
            prompt = f"""
            Generate 5 functional test cases.
            Requirement Docs: {payload.requirements}
            Customer Personas: {payload.personas}
            Business Process Info: {payload.business_process}
            Journey Info: {payload.customer_journey}
            Website Content: {payload.site_content}

            Output format:
            - Test Name
            - Test Description
            - Steps
            - Expected Outcome
            - Actual Outcome (blank)
            - Step Result (blank)
            """

            response = client.chat.completions.create(
                model=settings.OPENAI_MODEL,
                messages=[
                    {"role": "system", "content": "You generate structured test cases."},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.2,
            )

            raw = response.choices[0].message.content
            logger.info(f"AI Model response received.")
            return raw
        

        except RateLimitError as e:
            logger.error(f"Rate limit exceeded: {e}")
            raise Exception("OpenAI rate limit exceeded. Try again later.")

        except APIConnectionError as e:
            logger.error(f"Connection error: {e}")
            raise Exception("Connection error when calling OpenAI.")

        except APIStatusError as e:
            logger.error(f"API Status error: {e}")
            raise Exception(f"OpenAI error: {e}")

        except Exception as e:
            logger.exception("Unexpected error.")
            raise Exception(f"Unexpected error: {str(e)}")
