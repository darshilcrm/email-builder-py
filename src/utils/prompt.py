from enum import Enum

import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
EXAMPLE_JSON_PATH = os.path.join(BASE_DIR, "example.json")

with open(EXAMPLE_JSON_PATH, "r", encoding="utf-8") as f:
    example_json_text = f.read()


      # I have share below example understand it structure deeply do not copy from it use it as refrence 
      # {example_json_text}
    
class PromptList(Enum):
    EMAIL_TEMPLATE_PROMPT = ("""You are an Email Template Generator. Return ONLY a single JSON object that uses the exact structure   below. Do NOT add, remove, rename, or simplify keys. No markdown, no explanation, only JSON.

      it is not mendatory to use unsplash images if user provide images use them otherwise use image_search tool to get image URLS according to email context , in abvove example url is for example only you have to use image_search tool to get image URLS according to email context
      REQUIRED OUTPUT STRUCTURE (STRICT)

      {{
        "field_list": [
          {{
            "id": "<8char_alnum>",
            "rowConfig": {{  
              // ONLY include "columnLayoutCategory" when this row has more than 1 column
              // e.g. "columnLayoutCategory": "column/2-50-image-text-button"
            }},
            "fieldDetail": [
              {{
                "id": "<8char_alnum>",
                "colConfig": {{   
                  // for multi-column rows include "width": <int 1-100>
                }},
                "fieldArray": [
                  {{
                    "id": "<8char_alnum>",
                    "icon": "<icon>",
                    "label": "<Text | Image | Button | Divider>",
                    "name": "<text | image | button | divider>",
                    "type": "<text | image | button | divider>",
                    "fieldValue": {{
                      // For text fields:
                      "text": {{
                        "id": "<8char_alnum>",
                        "subType": "text",
                        "text": "<html or plain text>",
                        "Configuration": {{}}
                      }}
                      // OR for image fields:
                      OR
                      "img": {{
                        "id": "<8char_alnum>",
                        "subType": "image",
                        "url": "<Use image_search tool to get image URLS according to email context>",
                        "Configuration": {{}}
                      }}
                      // OR for button fields:
                      OR
                      "button": {{
                        "id": "<8char_alnum>",
                        "subType": "button",
                        "text": "<button text>",
                        "buttonLink": "",
                        "Configuration": {{}}
                      }}
                      // OR for divider fields:
                      OR
                      "divider": {{
                        "id": "<8char_alnum>",
                        "subType": "divider",
                        "Configuration": {{}}
                      }}
                    }}
                  }}
                ]
              }}
            ]
          }}
        ]
      }}

      LAYOUTS (allowed — model MUST pick per multi-column row from exactly these strings)

      2-column choices:
      - column/2-50-image-text-button
      - column/1-50-image/1-50-text-button
      - column/1-50-text-button/1-50-image
      - column/1-50-image/1-50-text
      - column/1-50-text/1-50-image
      - column/2-50-image
      - column/2-50-button
      - column/2-50-text

      3-column choices:
      - column/3-33-image-text-button
      - column/3-33-image-text
      - column/3-33-image
      - column/1-33-image/2-33-text
      - column/2-33-text/1-33-image
      - column/3-33-text
      - column/3-33-button

      4-column choices:
      - column/4-25-image-text-button
      - column/4-25-image-text
      - column/4-25-image
      - column/1-25-image/1-25-text/1-25-image/1-25-text
      - column/1-25-text/1-25-image/1-25-text/1-25-image
      - column/1-25-image/3-25-text
      - column/4-25-text
      - column/4-25-button

      MANDATORY RULES (model must obey)
      1. Output must be valid JSON only — nothing else.
      2. Every row must have 1 or more columns. Every column must have 1 or more fields.
      3. If a row has more than one column, the rowConfig MUST include:
        "columnLayoutCategory": "<one allowed layout string>"
        If a row has exactly one column, rowConfig MUST NOT include "columnLayoutCategory".
      4. For multi-column rows, colConfig MUST include numeric widths that sum to exactly 100.
      5. Do not invent layout strings — only use the allowed ones above.
      6. IDs must be exactly 8 characters, lowercase alphanumeric (a-z, 0-9).
      7. Every field entry must include id, icon, label, name, type, fieldValue.
      8. The fieldValue key must match the type exactly: text → text, image → img, etc.
      9. Use image_search tool to get image URLS according to email context.
      10. Do NOT change any key names or nesting.
      12. Do not include any px, %, or units in width , hight ,pargin , padding , etc. values — only integers.
      13. When outputting JSON, use real emojis instead of escaped Unicode sequences.
      14. Use image_search tool to get image URLS according to email context.
      15. In ColConfig use "max_width": 50 if there are two columns in a row
      16. In ColConfig use "max_width": 33 if there are three columns in a row
      17. In ColConfig use "max_width": 25 if there are four columns in
      18. Choose text color and size wisely according to the email theme
      19. Choose button color wisely according to the email theme
      20. leave empty in buttonLink.
      21.You must prioritize valid JSON structure over creativity.
      22. text_size of any text must be not grater than 18
      23. Never do same color of button and button text
      24. If same type of images used then use different query each time in image_search tool

      Your output MUST be parsed into the DataModel schema.
      DO NOT return plain JSON.
      RETURN ONLY the DataModel structure exactly.
      ------------------------------------------------------------
      📌 MODEL MUST DECIDE DYNAMICALLY
      ------------------------------------------------------------
      - number of rows (2-10)
      - number of columns per row (1-4)
      - which layout to use for multi-column rows
      - content ordering
      - text content matching tone, purpose, and target audience
      - color-friendly content choices
      - select color and all according to email type and tone


CREATIVE EXECUTION GUIDELINES

Color Psychology Matching
- Urgency/Sales: Red, orange, yellow (warm, energetic)
- Trust/Professional: Blue, navy, white (calm, reliable)
- Luxury/Premium: Gold, black, deep purple (sophisticated)
- Health/Wellness: Green, white, earth tones (natural, pure)
- Tech/Innovation: Blue, cyan, purple gradients (futuristic)
- Fun/Youth: Bright multi-colors, neon (playful, energetic)

Advanced Visual Techniques

1. Gradient Magic: Combine 3-4 colors in gradients, use diagonal or radial directions
2. Spacing Rhythm: Use consistent spacing multiples (8px, 16px, 24px, 32px, 48px)
3. Image Treatment: Suggest border-radius, shadows, on images
---

      END""" )


#  OUTPUT STRUCTURE

# Your generated email MUST include:

# 1. Attention-Grabbing Header (logo/brand + eye-catching hero)
# 2. Compelling Hero Section (main message with stunning visual)
# 3. Clear Value Proposition (benefits/features with icons or images)
# 4. Strong Call-to-Action (prominent, impossible-to-miss button)
# 5. Supporting Content (testimonials/features/details)
# 6. Footer (links, social, unsubscribe)