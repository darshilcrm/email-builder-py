from src.utils.prompt import *

from src.llm.llm import llm , agent , llm_structure


inputs = {"messages": [{"role": "user", "content":"""Generate a fully dynamic email layout for the following details:

Email Type: "Weekly Newsletter"
Purpose: "Share top blog posts and product tips"
Tone: "Casual, helpful" 
Target Audience: "Existing users"
Key Points:
- 3 article teasers (title + 1-sentence summary each)
- 1 upcoming webinar promo with date/time
- CTA: "Read more" for each article

"""}]}

# query = EMAIL_TEMPLATE_PROMPT + """Generate a fully dynamic email layout for the following details:
# Email Type: "Welcome Email" - Purpose: "Welcome new subscribers to our platform" - Tone: "Professional" - Target Audience: "New subscribers" - Key Points: ["Welcome message", "Discount code: WELCOME20", "How to redeem"]

# """

query = EMAIL_TEMPLATE_PROMPT + """

Email Type: "Weekly Newsletter"
Purpose: "Share top blog posts and product tips"
Tone: "Casual, helpful" 
Target Audience: "Existing users"
Key Points:
- 3 article teasers (title + 1-sentence summary each)
- 1 upcoming webinar promo with date/time
- CTA: "Read more" for each article
"""



# response = llm_structure.invoke(query)
response = agent.invoke(inputs)

print(response["messages"][-1])
# json_string = response.model_dump_json(indent=2 , by_alias=True ,exclude_none=True)